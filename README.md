1.Thông tin sinh viên
    Họ và tên: Nguyễn Khánh Đăng
    Mã số sinh viên: 24120171
    Lớp: 24CTT3
    Khoa: Công nghệ Thông tin - ĐH Khoa học Tự nhiên TP.HCM
2.Giới thiệu mô hình
    Tên mô hình: bert-base-uncased-emotion
    Liên kết mô hình: bhadresh-savani/bert-base-uncased-emotion
3.Chức năng hệ thống: 
    Phân loại văn bản vào 6 nhãn cảm xúc: sadness, joy, love, anger, fear, surprise.
4.Hướng dẫn cài đặt thư viện.
    pip install -r requirements.txt
5.Hướng dẫn chạy chương trình.
    Lệnh để bật Server API: python -m uvicorn main:app --reload
6.Hướng dẫn gọi API và ví dụ request/response.
    Truy cập http://127.0.0.1:8000/ hoặc sử dụng test_api.py
    Request:
        {"text": "I am so happy to see the result!"}
    Response (JSON):
        {
          "input_text": "I am so happy to see the result!",
          "prediction": {
              "label": "joy",
              "score": 0.9982
          }
        }