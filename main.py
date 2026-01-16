from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load('trained_model.pkl')

class PredictRequest(BaseModel):
    Partner: str
    Dependents: str
    Service1: str
    Service2: str
    Security: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    Charges: float
    Demand: int

class_mapping = {0: 'Alpha', 1: 'Betha'}

label_encoders = {
    'Partner': {'No': 0, 'Yes': 1},
    'Dependents': {'No': 0, 'Yes': 1},
    'Service1': {'No': 0, 'Yes': 1},
    'Service2': {'No': 0, 'Yes': 1},
    'Security': {'No': 0, 'Yes': 1, 'No internet service': 2},
    'OnlineBackup': {'No': 0, 'Yes': 1, 'No internet service': 2},
    'DeviceProtection': {'No': 0, 'Yes': 1, 'No internet service': 2},
    'TechSupport': {'No': 0, 'Yes': 1, 'No internet service': 2},
    'Contract': {'Month-to-month': 0, 'One year': 1, 'Two year': 2},
    'PaperlessBilling': {'No': 0, 'Yes': 1},
    'PaymentMethod': {'Electronic check': 0, 'Mailed check': 1, 'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3},
}

scaler = joblib.load('scaler.pkl') 

@app.post("/predict/")
def predict(request: PredictRequest):
    input_data = pd.DataFrame([request.dict()])

    for column, mapping in label_encoders.items():
        if column in input_data.columns:
            input_data[column] = input_data[column].map(mapping)

    input_data[['Charges']] = scaler.transform(input_data[['Charges']])

    prediction = model.predict(input_data)
    
    predicted_class = class_mapping[prediction[0]]

    return {"prediction": predicted_class}
 