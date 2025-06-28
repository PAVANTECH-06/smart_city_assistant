from fastapi import APIRouter, UploadFile
import pandas as pd
from services.gemini_utils import forecast_kpi_description

router = APIRouter()

@router.post("/forecast")
def forecast(file: UploadFile):
    df = pd.read_csv(file.file)
    summary = df.describe().to_string()
    prediction = forecast_kpi_description(summary)
    return {"forecast": prediction}
