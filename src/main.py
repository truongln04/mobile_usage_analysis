import time
import os
from src.data_loader import load_data
from src.preprocessing import clean_data, feature_engineering
from src.eda import analyze_data
from src.model import train_model, forecast_future
from src.visualization import generate_report

os.makedirs("result", exist_ok=True)

def main():
    print("===== START PROJECT =====")
    start = time.time()

    # 1. Thu thập dữ liệu
    df = load_data()

    # 2. Tiền xử lý dữ liệu
    df = clean_data(df)
    df = feature_engineering(df)
    df.to_csv("result/clean_data.csv", index=False)
    print("✔ Cleaned data saved")

    # 3. Phân tích dữ liệu (EDA)
    analyze_data(df, show=False)
    print("✔ EDA completed")

    # 4. Trực quan hóa dữ liệu + sơ đồ pipeline
    generate_report(df, show=True)
    print("✔ Visualization completed")

    # # 5. Huấn luyện mô hình
    best_model = train_model(df, show=True)

    # 6. Dự báo xu hướng
    preds = forecast_future(
        best_model,
        df,
        periods=30,
        show=True
    )
    print("✔ Forecast completed, first 5 predictions:", preds[:5])

    end = time.time()
    print("===== DONE in", round(end-start,2), "s =====")

if __name__ == "__main__":
    main()
