from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from emotion_model import EmotionClassification

app = FastAPI()

# Khởi tạo mô hình một lần khi chạy server
model_service = EmotionClassification(config_path="config.yaml")

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "API nhận diện cảm xúc văn bản tiếng Anh - Lab01"}

@app.get("/health")
def health():
    return {"status": "healthy", "model": "bert-base-uncased-emotion"}

@app.post("/predict")
async def predict(data: TextInput):
    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Văn bản không được để trống")
    try:
        return model_service(data.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))