from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="SmartPredict API")

model = joblib.load("src/models/model.pkl")

@app.get("/")
def root():
    return {"message": "SmartPredict API Running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": prediction.tolist()}
