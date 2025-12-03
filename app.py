from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f) 

app = FastAPI()

class InputData(BaseModel):
    Pregnancies: conint(gt=0) 
    Glucose: confloat(gt=0)
    BloodPressure: confloat(gt=0)
    SkinThickness: confloat(gt=0)
    Insulin: confloat(gt=0)
    BMI: confloat(gt=0)
    DiabetesPedigreeFunction: confloat(gt=0)
    Age: conint(gt=0)

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

    pred = int(model.predict(features)[0])
    if pred == 1:
        return "The patient has Diabetes"
    else:
        return "The patient does not have Diabetes"