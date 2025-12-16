from pydantic import BaseModel, conint, confloat

class InputData(BaseModel):
    Pregnancies: conint(gt=0) 
    Glucose: confloat(gt=0)
    BloodPressure: confloat(gt=0)
    SkinThickness: confloat(gt=0)
    Insulin: confloat(gt=0)
    BMI: confloat(gt=0)
    DiabetesPedigreeFunction: confloat(gt=0)
    Age: conint(gt=0)