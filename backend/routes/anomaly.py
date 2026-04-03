from fastapi import APIRouter, UploadFile
import pandas as pd
import numpy as np
from utils.alerts import trigger_alert

router = APIRouter()

# -----------------------------
# Z-Score Anomaly Detection
# -----------------------------
def detect_anomalies(df):
    anomaly_report = []

    numeric_columns = df.select_dtypes(include=[np.number]).columns

    for col in numeric_columns:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]

        if not outliers.empty:
            for value in outliers[col].values:
                anomaly_report.append({
                    "column": col,
                    "value": float(value),
                    "lower_bound": float(lower_bound),
                    "upper_bound": float(upper_bound)
                })

                # Trigger alert
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