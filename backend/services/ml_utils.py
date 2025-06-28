from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_kpi(df):
    X = np.arange(len(df)).reshape(-1, 1)
    y = df.iloc[:, 1].values
    model = LinearRegression().fit(X, y)
    prediction = model.predict([[len(df)]])
    return prediction.tolist()

def detect_anomalies(df):
    values = df.iloc[:, 1]
    mean, std = values.mean(), values.std()
    threshold = 2
    anomalies = df[abs(values - mean) > threshold * std]
    return anomalies.to_dict(orient="records")