from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def train_model(df):
    print("\n===== TRAIN MODEL =====")

    # ==============================
    # 1. FEATURE ENGINEERING
    # ==============================
    df['usage_per_launch'] = df['screen_time_min'] / (df['launches'] + 1)

    # ==============================
    # 2. CHỌN FEATURE
    # ==============================
    X = df[['launches', 'interactions', 'usage_per_launch']]
    y = df['screen_time_min']

    # ==============================
    # 3. SPLIT DATA
    # ==============================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    results = []

    # ==============================
    # 4. LINEAR REGRESSION
    # ==============================
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)

    y_pred_lr = lr_model.predict(X_test)

    mae_lr = mean_absolute_error(y_test, y_pred_lr)
    rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))
    r2_lr = r2_score(y_test, y_pred_lr)

    print("\n--- Linear Regression ---")
    print("MAE:", mae_lr)
    print("RMSE:", rmse_lr)
    print("R2:", r2_lr)

    results.append(["Linear Regression", mae_lr, rmse_lr, r2_lr])

    # ==============================
    # 5. RANDOM FOREST
    # ==============================
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    y_pred_rf = rf_model.predict(X_test)

    mae_rf = mean_absolute_error(y_test, y_pred_rf)
    rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
    r2_rf = r2_score(y_test, y_pred_rf)

    print("\n--- Random Forest ---")
    print("MAE:", mae_rf)
    print("RMSE:", rmse_rf)
    print("R2:", r2_rf)

    results.append(["Random Forest", mae_rf, rmse_rf, r2_rf])

    # ==============================
    # 6. SO SÁNH MODEL
    # ==============================
    result_df = pd.DataFrame(results, columns=["Model", "MAE", "RMSE", "R2"])
    print("\n===== SO SÁNH MODEL =====")
    print(result_df)

    result_df.to_csv("result/model_comparison.csv", index=False)

    # ==============================
    # 7. BIỂU ĐỒ SO SÁNH MODEL
    # ==============================
    ax = result_df.set_index("Model")[["MAE", "RMSE", "R2"]].plot(
        kind='bar', figsize=(8, 5)
    )

    plt.title("So sánh hiệu suất các mô hình dự đoán", fontsize=14)
    plt.xlabel("Mô hình Machine Learning", fontsize=12)
    plt.ylabel("Giá trị chỉ số đánh giá", fontsize=12)

    plt.legend(title="Chỉ số", loc="upper right")
    plt.xticks(rotation=0)

    for container in ax.containers:
        ax.bar_label(container, fmt='%.2f')

    # 👉 chú thích ngoài
    ax.text(
        1.02, 0.5,
        "Ghi chú:\n- MAE, RMSE càng thấp càng tốt\n- R2 càng gần 1 càng tốt",
        transform=ax.transAxes,
        fontsize=9,
        verticalalignment='center',
        bbox=dict(facecolor='white', alpha=0.8)
    )

    plt.tight_layout()
    plt.savefig("result/model_comparison.png", bbox_inches='tight')
    plt.show()

    # ==============================
    # 8. CHỌN MODEL TỐT NHẤT
    # ==============================
    if r2_rf > r2_lr:
        best_model = rf_model
        y_pred_best = y_pred_rf
        print("\n Chọn Random Forest là model tốt nhất")
    else:
        best_model = lr_model
        y_pred_best = y_pred_lr
        print("\n Chọn Linear Regression là model tốt nhất")

    # ==============================
    # 9. BIỂU ĐỒ DỰ ĐOÁN vs THỰC TẾ
    # ==============================
    plt.figure(figsize=(7, 5))

    plt.scatter(y_test, y_pred_best, alpha=0.6, label="Dữ liệu dự đoán")

    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        'r--',
        label="Đường lý tưởng (y=x)"
    )

    plt.title("So sánh giá trị dự đoán và thực tế", fontsize=14)
    plt.xlabel("Giá trị thực tế (phút)", fontsize=12)
    plt.ylabel("Giá trị dự đoán (phút)", fontsize=12)

    plt.legend()
    plt.grid(True)

    # 👉 chú thích góc dưới
    plt.gca().text(
        0.02, 0.02,
        "Điểm càng gần đường đỏ → dự đoán càng chính xác",
        transform=plt.gca().transAxes,
        fontsize=9,
        bbox=dict(facecolor='white', alpha=0.8)
    )

    plt.tight_layout()
    plt.savefig("result/predict_vs_actual.png", bbox_inches='tight')
    plt.show()

    # ==============================
    # 10. BIỂU ĐỒ SAI SỐ
    # ==============================
    error = y_test - y_pred_best

    plt.figure(figsize=(7, 5))
    plt.hist(error, bins=20)

    plt.title("Phân bố sai số của mô hình", fontsize=14)
    plt.xlabel("Sai số (Actual - Predicted)", fontsize=12)
    plt.ylabel("Tần suất", fontsize=12)

    plt.grid(True)

    # 👉 chú thích bên phải
    plt.gca().text(
        1.02, 0.5,
        "Ghi chú:\n- Sai số gần 0 → dự đoán tốt\n- Phân bố đều → mô hình ổn định",
        transform=plt.gca().transAxes,
        fontsize=9,
        verticalalignment='center',
        bbox=dict(facecolor='white', alpha=0.8)
    )

    plt.tight_layout()
    plt.savefig("result/error_distribution.png", bbox_inches='tight')
    plt.show()

    # ==============================
    # 11. LƯU KẾT QUẢ
    # ==============================
    final_result = pd.DataFrame({
        'Actual': y_test,
        'Predicted': y_pred_best
    })

    final_result.to_csv("result/predictions.csv", index=False)

    print("\n✔ Đã lưu toàn bộ kết quả vào thư mục result/")

    return best_model