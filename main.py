import time
import pandas as pd

from src.data_loader import load_data
from src.preprocessing import clean_data, feature_engineering
from src.eda import analyze_data
from src.visualization import (
    plot_top_apps,
    plot_category,
    plot_trend,
    plot_weekday,
    plot_box,
    plot_productive
)
from src.model import train_model


def main():
    print("===== 🚀 START PROJECT =====")
    start_time = time.time()

    try:
        # ================= 1. LOAD =================
        df = load_data()
        print(f"✔ Loaded data: {df.shape}")

        # ================= 2. CLEAN =================
        df = clean_data(df)
        df = df.copy()
        print(f"✔ Cleaned data: {df.shape}")

        # ================= 3. FEATURE =================
        df = feature_engineering(df)
        print("✔ Feature engineering done")

        # ================= 4. SAVE CLEAN DATA =================
        df.to_csv("result/clean_data.csv", index=False, encoding="utf-8-sig")
        print("✔ Saved clean_data.csv")

        # ================= 5. EDA =================
        analyze_data(df)
        print("✔ EDA completed")

        # ================= 6. VISUALIZATION =================
        plot_top_apps(df)
        plot_category(df)
        plot_trend(df)
        plot_weekday(df)
        plot_box(df)
        plot_productive(df)
        print("✔ All charts saved")

        # ================= 7. MODEL =================
        train_model(df)
        print("✔ Model training completed")

    except Exception as e:
        print("❌ ERROR:", e)

    end_time = time.time()
    print(f"===== ✅ DONE in {round(end_time - start_time, 2)}s =====")


if __name__ == "__main__":
    main()