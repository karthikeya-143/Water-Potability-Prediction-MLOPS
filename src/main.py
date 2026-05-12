from fastapi import FastAPI
import pickle
import pandas as pd
import uvicorn
from src.data_model import Water

app = FastAPI(
    title="Water Potability Prediction API",
    description="API for predicting water potability based on various features."
)

# load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def index():
    return {"message": "Welcome to the Water Potability Prediction API!"}

@app.post("/predict")
def model_predict(data: Water):
    sample=pd.DataFrame(
        {
            "ph":[data.ph],
            "Hardness":[data.Hardness],
            "Solids":[data.Solids],
            "Chloramines":[data.Chloramines],
            "Sulfate":[data.Sulfate],
            "Conductivity":[data.Conductivity],
            "Organic_carbon":[data.Organic_carbon],
            "Trihalomethanes":[data.Trihalomethanes],
            "Turbidity":[data.Turbidity]
        }
    )
    predicted_value=model.predict(sample)
    if predicted_value==1:
        return "The water is potable."
    else:        
        return "The water is not potable."

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)