from fastapi import FastAPI
<<<<<<< HEAD
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
=======
from model.predict import predict_output, MODEL_VERSION
from schema.user_input import InputData


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
>>>>>>> d05802a (diabetes Prediction)

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

<<<<<<< HEAD
    pred = int(model.predict(features)[0])
    if pred == 1:
        return "The patient has Diabetes"
    else:
        return "The patient does not have Diabetes"
=======
    pred = predict_output(features)

    try:
        if pred == 1:
            result = "The patient has Diabetes"
        else:
            result = "The patient does not have Diabetes"
        
        return JSONResponse(statue_code=200, content={"prediction": result})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))

    
>>>>>>> d05802a (diabetes Prediction)
