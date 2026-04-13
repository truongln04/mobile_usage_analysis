# 📱 Mobile Usage Analysis  
> Phân tích thói quen sử dụng điện thoại của người dùng  

🔗 GitHub Repository: https://github.com/truongln04/mobile_usage_analysis.git  

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

- 📁 Nguồn: Kaggle: https://www.kaggle.com/datasets/khushikyad001/screen-time-and-app-usage-dataset-iosandroid
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

~~~bash
mobile_usage_analysis/
│
├── data/                  # Dataset (file CSV)
├── result/                # Output (biểu đồ, file CSV)
│
├── src/
│   ├── data_loader.py     # Load dữ liệu
│   ├── preprocessing.py   # Làm sạch + feature engineering
│   ├── eda.py             # Phân tích dữ liệu
│   ├── visualization.py   # Vẽ biểu đồ
│   └── model.py           # Machine Learning
│
├── main.py                # File chạy chính
├── README.md
~~~

---

## ▶️ Cài đặt (Installation)

### 1️⃣ Clone project

~~~bash
git clone https://github.com/truongln04/mobile_usage_analysis.git
cd mobile_usage_analysis
~~~

---

### 2️⃣ Tạo môi trường ảo

~~~bash
python -m venv venv
~~~

👉 Kích hoạt:

- Windows:
~~~bash
venv\Scripts\activate
~~~

- Mac/Linux:
~~~bash
source venv/bin/activate
~~~

---

### 3️⃣ Cài đặt thư viện

~~~bash
pip install pandas numpy matplotlib seaborn scikit-learn
~~~

---

## ▶️ Chạy chương trình

~~~bash
python main.py
~~~

---

## 📊 Kết quả (Results)

Sau khi chạy, kết quả nằm trong thư mục `result/`:

- 📊 top_apps.png  
- 🥧 category.png  
- 📈 trend.png  
- 📅 weekday.png  
- 📦 boxplot.png  
- ⚖️ productive.png  
- 🤖 model_comparison.png  
- 📍 predict_vs_actual.png  
- 📉 error_distribution.png  
- 📄 predictions.csv  

---

## 🤖 Mô hình sử dụng

- 🔹 Linear Regression  
- 🔹 Random Forest  

### 📊 Đánh giá:

- MAE  
- RMSE  
- R² Score  

---

## 🔍 Insight

- 📱 Người dùng tập trung vào một số ứng dụng chính  
- 🎮 App giải trí chiếm nhiều thời gian  
- 📅 Có khác biệt theo ngày  
- 🤖 Random Forest tốt hơn  

---

## ⚠️ Hạn chế

- Dataset nhỏ  
- Ít feature  
- Chưa dùng Deep Learning  

---

## 🚀 Hướng phát triển

- 🔍 Thêm feature  
- ⏳ Time Series  
- 🤖 XGBoost / LSTM  
- 📊 Dashboard  

---

## 👨‍💻 Tác giả

- ✍️ **Lưu Nguyên Trường**  
- 🎓 Phân tích dữ liệu Python  
