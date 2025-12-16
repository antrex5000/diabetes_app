import numpy as np
import pickle

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f) 

MODEL_VERSION = 1.0

def predict_output(features):

    pred = int(model.predict(features)[0])

    return pred