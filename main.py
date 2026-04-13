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
# from src.visualization import *
def main():
    print("=== START PROJECT ===")

    # 1. Load
    df = load_data()

    # 2. Clean
    df = clean_data(df)

    # 3. Feature
    df = feature_engineering(df)

    # 4. EDA
    analyze_data(df)

    # 5. Visualization
    plot_top_apps(df)
    plot_category(df)
    plot_trend(df)
    plot_weekday(df)
    plot_box(df)
    #
    plot_productive(df)

    # 6. Model
    train_model(df)

    print("=== DONE ===")

if __name__ == "__main__":
    main()