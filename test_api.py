import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_health_check():
    print("--- Kiểm tra trạng thái hệ thống (/health) ---")
    response = requests.get(f"{BASE_URL}/health")
    if response.status_code == 200:
        print("Thành công:", response.json())
    else:
        print("Thất bại:", response.status_code)
    print("-" * 40)

def test_prediction(text_to_test):
    print(f"--- Đang kiểm tra dự đoán với văn bản: '{text_to_test}' ---")
    payload = {"text": text_to_test}
    
    try:
        response = requests.post(f"{BASE_URL}/predict", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            print("Kết quả trả về từ API:")
            print(json.dumps(result, indent=4))
        else:
            print(f"Lỗi API (Mã lỗi {response.status_code}):", response.text)
            
    except requests.exceptions.ConnectionError:
        print("Lỗi: Không thể kết nối đến Server!")

if __name__ == "__main__":
    test_health_check()
    
    test_sentences = [
        "I am so happy!",
        "I feel lonely today.",
        "I am very angry!"
    ]
    
    for sentence in test_sentences:
        test_prediction(sentence)