from fastapi import APIRouter, UploadFile
import pandas as pd
from services.gemini_utils import detect_anomalies_description

router = APIRouter()

@router.post("/anomaly")
def anomaly(file: UploadFile):
    df = pd.read_csv(file.file)
    summary = df.describe().to_string()
    anomalies = detect_anomalies_description(summary)
    return {"anomalies": anomalies}
