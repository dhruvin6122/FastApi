# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="🏠 House Price Prediction API", version="1.0")

# load model (correct path)
model = joblib.load("model/house_price_model.pkl")

# request schema
class HouseFeatures(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    parking: int

@app.get("/")
def home():
    return {"message": "Welcome to House Price Prediction API"}

@app.post("/predict")
def predict_price(data: HouseFeatures):
    features = np.array([[data.area, data.bedrooms, data.bathrooms, data.stories, data.parking]])
    prediction = model.predict(features)[0]
    return {
        "predicted_price": round(float(prediction), 2),
        "details": data.model_dump()
    }
