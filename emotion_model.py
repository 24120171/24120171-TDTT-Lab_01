import torch
from omegaconf import OmegaConf
from transformers import BertTokenizer, BertForSequenceClassification

class EmotionClassification:
    def __init__(self, config_path):
        self.config = OmegaConf.load(config_path)
        self.tokenizer = BertTokenizer.from_pretrained(self.config.model_path)
        self.model = BertForSequenceClassification.from_pretrained(self.config.model_path)
        self.model.eval()

    def __call__(self, message: str):
        inputs = self.tokenizer(message, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            logits = self.model(**inputs).logits
        
        predicted_class_id = logits.argmax().item()
        label = self.model.config.id2label[predicted_class_id]
        score = torch.softmax(logits, dim=1)[0][predicted_class_id].item()
        return {"label": label, "score": round(score, 4)}