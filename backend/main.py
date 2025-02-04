from fastapi import FastAPI, UploadFile, File
import pandas as pd
import uvicorn
from model import train_model, predict

app = FastAPI()

@app.post('/upload/')
async def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    model, accuracy = train_model(df)
    return {"message": "Model trained", "accuracy": accuracy}

@app.post('/predict/')
async def make_prediction(data: dict):
    prediction = predict(data)
    return {"fraud": prediction}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)