from fastapi import APIRouter, UploadFile
import pandas as pd
import numpy as np
from utils.alerts import trigger_alert

router = APIRouter()

# -----------------------------
# Z-Score Anomaly Detection
# -----------------------------
def detect_anomalies(df, threshold=3):
    anomaly_report = []

    numeric_columns = df.select_dtypes(include=[np.number]).columns

    for col in numeric_columns:
        mean = df[col].mean()
        std = df[col].std()

        if std == 0:
            continue

        z_scores = (df[col] - mean) / std
        outliers = df[np.abs(z_scores) > threshold]

        if not outliers.empty:
            for value in outliers[col].values:
                anomaly_report.append({
                    "column": col,
                    "value": float(value),
                    "mean": float(mean),
                    "std": float(std)
                })

                # Trigger real-time alert
                trigger_alert(col, value)

    return anomaly_report


# -----------------------------
# API Endpoint
# -----------------------------
@router.post("/anomaly")
def anomaly(file: UploadFile):
    df = pd.read_csv(file.file)

    anomalies = detect_anomalies(df)

    if anomalies:
        return {
            "status": "Anomaly Detected",
            "alert": True,
            "anomalies": anomalies
        }
    else:
        return {
            "status": "No Anomaly Detected",
            "alert": False,
            "anomalies": []
        }