# 📱 Mobile Usage Analysis  
> Phân tích thói quen sử dụng điện thoại của người dùng  

---

## 📌 Giới thiệu (Introduction)

Dự án này nhằm phân tích **thói quen sử dụng điện thoại của người dùng** dựa trên dữ liệu screen time.  
Mục tiêu là hiểu rõ hành vi sử dụng ứng dụng và xây dựng mô hình dự đoán thời gian sử dụng.

---

## 🎯 Mục tiêu (Objectives)

- 📊 Phân tích dữ liệu sử dụng điện thoại
- 🧹 Làm sạch dữ liệu (Data Cleaning)
- 📈 Trực quan hóa dữ liệu (Visualization)
- 🤖 Xây dựng mô hình dự đoán (Machine Learning)
- 🔍 Rút ra insight hành vi người dùng

---

## 📂 Dataset

- 📁 Nguồn: Kaggle  
- 📊 Các thuộc tính chính:
  - `user_id` – ID người dùng  
  - `date` – ngày sử dụng  
  - `app_name` – tên ứng dụng  
  - `category` – loại ứng dụng  
  - `screen_time_min` – thời gian sử dụng (phút)  
  - `launches` – số lần mở app  
  - `interactions` – số tương tác  
  - `is_productive` – app hữu ích (1) / không (0)  

---

## ⚙️ Công nghệ sử dụng (Tech Stack)

- 🐍 Python  
- 📊 Pandas  
- 🔢 NumPy  
- 📈 Matplotlib  
- 🎨 Seaborn  
- 🤖 Scikit-learn  

---

## 📁 Cấu trúc dự án

mobile_usage_analysis/
│
├── data/                  # Dataset
├── result/                # Output (biểu đồ, file CSV)
│
├── src/
│   ├── data_loader.py     # Load dữ liệu
│   ├── preprocessing.py   # Làm sạch + feature
│   ├── eda.py             # Phân tích dữ liệu
│   ├── visualization.py   # Vẽ biểu đồ
│   └── model.py           # Machine Learning
│
├── main.py                # File chạy chính
├── README.md

---

## ▶️ Cách chạy dự án

### 1️⃣ Cài thư viện

pip install pandas numpy matplotlib seaborn scikit-learn

### 2️⃣ Chạy chương trình

python main.py

---

## 📊 Kết quả (Results)

### 📌 Visualization

- 📊 Top ứng dụng sử dụng nhiều nhất  
- 🥧 Phân bố theo category  
- 📈 Xu hướng sử dụng theo thời gian  
- 📅 Sử dụng theo ngày trong tuần  
- 📦 Phân bố dữ liệu (Boxplot)  
- ⚖️ So sánh app hữu ích và không hữu ích  

---

### 🤖 Machine Learning

Sử dụng 2 mô hình:

- 🔹 Linear Regression  
- 🔹 Random Forest  

### 📊 Chỉ số đánh giá:

- MAE (Mean Absolute Error)  
- RMSE (Root Mean Squared Error)  
- R² Score  

---

## 📉 Biểu đồ mô hình

- 📊 So sánh hiệu suất model  
- 📍 Dự đoán vs thực tế  
- 📉 Phân bố sai số  

---

## 🔍 Insight (Kết luận)

- 📱 Người dùng tập trung vào một số ứng dụng chính  
- 🎮 Ứng dụng giải trí chiếm phần lớn thời gian  
- 📅 Có sự khác biệt rõ theo ngày trong tuần  
- 🤖 Random Forest cho kết quả dự đoán tốt hơn Linear Regression  

---

## ⚠️ Hạn chế (Limitations)

- Dataset còn nhỏ  
- Chưa có nhiều đặc trưng nâng cao  
- Chưa áp dụng mô hình Deep Learning  

---

## 🚀 Hướng phát triển (Future Work)

- 🔍 Thêm nhiều feature hơn  
- ⏳ Áp dụng phân tích chuỗi thời gian (Time Series)  
- 🤖 Nâng cấp model (XGBoost, LSTM)  
- 📊 Xây dựng dashboard trực quan  

---

## 👨‍💻 Tác giả

- ✍️ Sinh viên: Lưu Nguyên Trường  
- 🎓 Môn học: Phân tích dữ liệu Python  
