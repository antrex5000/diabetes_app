from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from schema.user_input import InputData
from model.predict import predict_output, MODEL_VERSION
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/")
def home():
    print("Welcome!")
    print("Test yourself and get well.")

@app.get("/health")
def health_care():
    return {
        "status": "Ok",
        "version": MODEL_VERSION
    }

@app.post("/predict")
def predict(data: InputData):
    features = np.array([
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]).reshape(1, -1)


    pred = predict_output(features)

    try:
        if pred == 1:
            result = "The patient has Diabetes"
        else:
            result = "The patient does not have Diabetes"
        
        return JSONResponse(status_code=200, content={"prediction": result})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))

