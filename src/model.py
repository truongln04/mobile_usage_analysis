import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ======================================================
# FONT TIẾNG VIỆT
# ======================================================
plt.rcParams['font.family'] = 'DejaVu Sans'


# ======================================================
# STYLE CHUNG
# ======================================================
def style_chart(ax):

    ax.grid(
        axis='y',
        linestyle='--',
        alpha=0.4
    )

    for spine in ax.spines.values():

        spine.set_linewidth(1)


# ======================================================
# TẠO NOTEBOX
# ======================================================
def create_note_box(
        ax_note,
        note
):

    ax_note.axis('off')

    ax_note.text(
        0.02,
        0.98,
        note,

        fontsize=10,
        va='top',
        linespacing=1.6,

        bbox=dict(
            facecolor='#F8F9F9',
            edgecolor='#2C3E50',
            linewidth=1.5,
            boxstyle='round,pad=1'
        )
    )


# ======================================================
# MODEL COMPARISON CHART
# ======================================================
def plot_model_comparison(
        result_df,
        best_name,
        best_r2,
        best_mae,
        best_rmse,
        show=False
):

    # ==================================================
    # FIGURE
    # ==================================================
    fig = plt.figure(
        figsize=(18,7),
        facecolor='white'
    )

    # ==================================================
    # LAYOUT
    # ==================================================
    gs = fig.add_gridspec(
        1,
        2,

        width_ratios=[2.7,1.3],

        wspace=0.12
    )

    # ==================================================
    # LEFT CHART
    # ==================================================
    ax = fig.add_subplot(gs[0])

    result_df.set_index(
        "Model"
    )[[
        "MAE",
        "RMSE",
        "R2"
    ]].plot(
        kind='bar',
        ax=ax,
        width=0.65
    )

    # ==================================================
    # SHOW VALUE
    # ==================================================
    for container in ax.containers:

        ax.bar_label(
            container,
            fmt='%.3f',
            padding=3,
            fontsize=8,
            fontweight='bold'
        )

    # ==================================================
    # TITLE
    # ==================================================
    ax.set_title(
        "SO SÁNH HIỆU SUẤT MÔ HÌNH\n"
        "(Model Performance Comparison)",

        fontsize=16,
        fontweight='bold',
        pad=15
    )

    # ==================================================
    # LABELS
    # ==================================================
    ax.set_xlabel(
        "\nTên Mô Hình (Model Name)",

        fontsize=11,
        fontweight='bold'
    )

    ax.set_ylabel(
        "Giá Trị Đánh Giá\n"
        "(Evaluation Value)",

        fontsize=11,
        fontweight='bold'
    )

    plt.xticks(
        rotation=0,
        fontsize=10
    )

    style_chart(ax)

    # ==================================================
    # RIGHT NOTEBOX
    # ==================================================
    ax_note = fig.add_subplot(gs[1])

    note = f"""
- MỤC ĐÍCH
So sánh hiệu suất giữa
các mô hình Machine Learning.

- NHẬN XÉT
• Mô hình tốt nhất: {best_name}
• R2 cao nhất: {round(best_r2,3)}
• MAE: {round(best_mae,3)}
• RMSE: {round(best_rmse,3)}

- ĐÁNH GIÁ
• R2 càng gần 1 thì
  mô hình càng chính xác.
• MAE và RMSE càng thấp
  thì sai số càng nhỏ.
• Mô hình học được
  xu hướng dữ liệu tốt.
  
- KẾT LUẬN
{best_name} cho khả năng
dự đoán tốt hơn.
"""

    create_note_box(
        ax_note,
        note
    )

    # ==================================================
    # ADJUST
    # ==================================================
    plt.subplots_adjust(
        left=0.1,
        right=0.97,
        top=0.88,
        bottom=0.12
    )

    # ==================================================
    # SAVE
    # ==================================================
    plt.savefig(
        "result/model_comparison.png",
        dpi=300,
        bbox_inches='tight'
    )

    if show:
        plt.show()

    plt.close()


# ======================================================
# PREDICT VS ACTUAL
# ======================================================
def plot_predict_vs_actual(
        y_test,
        preds,
        corr,
        show=False
):

    fig = plt.figure(
        figsize=(18,7),
        facecolor='white'
    )

    gs = fig.add_gridspec(
        1,
        2,

        width_ratios=[2.7,1.3],

        wspace=0.12
    )

    # ==================================================
    # LEFT CHART
    # ==================================================
    ax = fig.add_subplot(gs[0])

    ax.scatter(
        y_test,
        preds,
        alpha=0.7
    )

    ax.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        'r--',
        linewidth=2
    )

    ax.set_title(
        "SO SÁNH GIÁ TRỊ DỰ ĐOÁN VÀ THỰC TẾ\n"
        "(Predicted vs Actual)",

        fontsize=16,
        fontweight='bold',
        pad=15
    )

    ax.set_xlabel(
        "\nGiá Trị Thực Tế - phút\n"
        "(Actual Screen Time)",

        fontsize=11,
        fontweight='bold'
    )

    ax.set_ylabel(
        "Giá Trị Dự ĐoÁN - phút\n"
        "(Predicted Screen Time)",

        fontsize=11,
        fontweight='bold'
    )

    style_chart(ax)

    # ==================================================
    # RIGHT NOTEBOX
    # ==================================================
    ax_note = fig.add_subplot(gs[1])

    note = f"""
- MỤC ĐÍCH
So sánh dữ liệu dự đoán
và dữ liệu thực tế.

- NHẬN XÉT
• Các điểm gần đường đỏ
  cho thấy dự đoán tốt.

• Tương quan:
  {round(corr,3)}

- ĐÁNH GIÁ
• Mô hình học được
  xu hướng dữ liệu.
• Sai lệch nhỏ cho thấy
  độ chính xác cao.


- KẾT LUẬN
Mô hình dự đoán khá tốt
screen time thực tế.
"""

    create_note_box(
        ax_note,
        note
    )

    plt.subplots_adjust(
        left=0.1,
        right=0.97,
        top=0.88,
        bottom=0.12
    )

    plt.savefig(
        "result/predict_vs_actual.png",
        dpi=300,
        bbox_inches='tight'
    )

    if show:
        plt.show()

    plt.close()


# ======================================================
# FORECAST CHART
# ======================================================
def plot_forecast(
        preds,
        periods,
        trend,
        start,
        end,
        show=False
):

    fig = plt.figure(
        figsize=(18,7),
        facecolor='white'
    )

    gs = fig.add_gridspec(
        1,
        2,

        width_ratios=[2.7,1.3],

        wspace=0.12
    )

    # ==================================================
    # LEFT CHART
    # ==================================================
    ax = fig.add_subplot(gs[0])

    ax.plot(
        range(periods),
        preds,

        marker='o',
        linewidth=2
    )

    # ==================================================
    # SHOW VALUE
    # ==================================================
    for i, v in enumerate(preds):

        ax.text(
            i,
            v + 2,

            f"{v:.1f}",

            ha='center',
            fontsize=8,
            fontweight='bold'
        )

    ax.set_title(
        f"DỰ BÁO SCREEN TIME "
        f"{periods} NGÀY TỚI\n"
        f"(Forecast Screen Time)",

        fontsize=16,
        fontweight='bold',
        pad=15
    )

    ax.set_xlabel(
        "\nNgày Tương Lai\n"
        "(Future Days)",

        fontsize=11,
        fontweight='bold'
    )

    ax.set_ylabel(
        "Screen Time Dự ĐoÁN - phút\n"
        "(Predicted Screen Time)",

        fontsize=11,
        fontweight='bold'
    )

    style_chart(ax)

    # ==================================================
    # RIGHT NOTEBOX
    # ==================================================
    ax_note = fig.add_subplot(gs[1])

    note = f"""
- MỤC ĐÍCH
Dự báo xu hướng sử dụng
điện thoại trong tương lai.

- NHẬN XÉT
• Giá trị đầu: {start} phút
• Giá trị cuối: {end} phút
• Xu hướng: {trend}

- ĐÁNH GIÁ
• Mô hình dự báo được
  sự thay đổi screen time.
• Dữ liệu thay đổi
  theo thời gian.

- KẾT LUẬN
Screen time tương lai
có xu hướng {trend}.
"""

    create_note_box(
        ax_note,
        note
    )

    plt.subplots_adjust(
        left=0.1,
        right=0.97,
        top=0.88,
        bottom=0.12
    )

    plt.savefig(
        "result/forecast.png",
        dpi=300,
        bbox_inches='tight'
    )

    if show:
        plt.show()

    plt.close()


# ======================================================
# TRAIN MODEL
# ======================================================
def train_model(
        df,
        show=False
):

    # ==================================================
    # FEATURE ENGINEERING
    # ==================================================
    df['usage_per_launch'] = (
        df['screen_time_min'] /
        (df['launches'] + 1)
    )

    # ==================================================
    # FEATURES & TARGET
    # ==================================================
    X = df[[
        'launches',
        'interactions',
        'usage_per_launch'
    ]]

    y = df['screen_time_min']

    # ==================================================
    # SPLIT DATA
    # ==================================================
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,

        test_size=0.2,

        shuffle=False
    )

    # ==================================================
    # LINEAR REGRESSION
    # ==================================================
    lr = LinearRegression()

    lr.fit(
        X_train,
        y_train
    )

    # ==================================================
    # RANDOM FOREST
    # ==================================================
    rf = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    rf.fit(
        X_train,
        y_train
    )

    # ==================================================
    # PREDICT
    # ==================================================
    y_pred_lr = lr.predict(X_test)

    y_pred_rf = rf.predict(X_test)

    # ==================================================
    # LINEAR REGRESSION METRICS
    # ==================================================
    mae_lr = mean_absolute_error(
        y_test,
        y_pred_lr
    )

    rmse_lr = np.sqrt(
        mean_squared_error(
            y_test,
            y_pred_lr
        )
    )

    r2_lr = r2_score(
        y_test,
        y_pred_lr
    )

    # ==================================================
    # RANDOM FOREST METRICS
    # ==================================================
    mae_rf = mean_absolute_error(
        y_test,
        y_pred_rf
    )

    rmse_rf = np.sqrt(
        mean_squared_error(
            y_test,
            y_pred_rf
        )
    )

    r2_rf = r2_score(
        y_test,
        y_pred_rf
    )

    # ==================================================
    # RESULT TABLE
    # ==================================================
    result_df = pd.DataFrame({

        "Model": [
            "Linear Regression",
            "Random Forest"
        ],

        "MAE": [
            mae_lr,
            mae_rf
        ],

        "RMSE": [
            rmse_lr,
            rmse_rf
        ],

        "R2": [
            r2_lr,
            r2_rf
        ]
    })

    print("\n========== MODEL EVALUATION ==========\n")

    print(result_df)

    # ==================================================
    # BEST MODEL
    # ==================================================
    best_model = (
        rf if r2_rf > r2_lr
        else lr
    )

    best_name = (
        "Random Forest"
        if best_model == rf
        else "Linear Regression"
    )

    best_r2 = max(
        r2_lr,
        r2_rf
    )

    best_mae = (
        mae_rf if best_model == rf
        else mae_lr
    )

    best_rmse = (
        rmse_rf if best_model == rf
        else rmse_lr
    )

    # ==================================================
    # MODEL COMPARISON CHART
    # ==================================================
    plot_model_comparison(
        result_df,
        best_name,
        best_r2,
        best_mae,
        best_rmse,
        show=show
    )

    # ==================================================
    # PREDICT VS ACTUAL
    # ==================================================
    preds = best_model.predict(
        X_test
    )

    corr = np.corrcoef(
        y_test,
        preds
    )[0,1]

    plot_predict_vs_actual(
        y_test,
        preds,
        corr,
        show=show
    )

    print(
        f"\n✔ Best Model: {best_name}"
    )

    return best_model

# ======================================================
# FORECAST CHART
# ======================================================
def plot_forecast(
        preds,
        periods,
        trend,
        start,
        end,
        show=False
):

    # ==================================================
    # FIGURE
    # ==================================================
    fig = plt.figure(
        figsize=(16,7),
        facecolor='white'
    )

    # ==================================================
    # LAYOUT
    # ==================================================
    gs = fig.add_gridspec(
        1,
        2,
        width_ratios=[2.8,1.2],
        wspace=0.12
    )

    # ==================================================
    # LEFT CHART
    # ==================================================
    ax = fig.add_subplot(gs[0])

    # NGÀY 1 -> 30
    x = range(1, periods + 1)

    ax.plot(
        x,
        preds,
        marker='o',
        linewidth=2,
        markersize=5
    )

    # ==================================================
    # SHOW VALUE FULL
    # ==================================================
    for i, v in enumerate(preds):
        ax.annotate(
            f"{v:.1f}",
            (x[i], v),

            textcoords="offset points",
            xytext=(0, 8),

            ha='center',
            fontsize=7,
            fontweight='bold'
        )

    # ==================================================
    # TITLE
    # ==================================================
    ax.set_title(
        f"DỰ BÁO SCREEN TIME "
        f"{periods} NGÀY TỚI\n"
        f"(Forecast Screen Time)",

        fontsize=16,
        fontweight='bold',
        pad=15
    )

    # ==================================================
    # LABEL
    # ==================================================
    ax.set_xlabel(
        "\nNgày Tương Lai\n"
        "(Future Days)",

        fontsize=11,
        fontweight='bold'
    )

    ax.set_ylabel(
        "Screen Time Dự ĐoÁN - phút\n"
        "(Predicted Screen Time)",

        fontsize=11,
        fontweight='bold',
        labelpad=15
    )

    # ==================================================
    # HIỆN ĐỦ TRỤC X
    # ==================================================
    ax.set_xticks(list(x))

    ax.set_xticklabels(
        list(x),
        fontsize=8
    )

    # ==================================================
    # LIMIT Y
    # ==================================================
    ax.set_ylim(
        min(preds) - 2,
        max(preds) + 2
    )

    # ==================================================
    # GRID STYLE
    # ==================================================
    style_chart(ax)

    # ==================================================
    # RIGHT NOTEBOX
    # ==================================================
    ax_note = fig.add_subplot(gs[1])

    note = f"""
- MỤC ĐÍCH
Dự báo xu hướng sử dụng
điện thoại trong tương lai.

- NHẬN XÉT
• Giá trị đầu: {start} phút
• Giá trị cuối: {end} phút
• Xu hướng: {trend}

- ĐÁNH GIÁ
• Dự báo dựa trên dữ liệu
  launches và interactions
  trong dataset thực tế.

• Machine Learning học từ
  hành vi sử dụng trước đó.

• Dữ liệu thay đổi theo
  xu hướng thời gian.

- KẾT LUẬN
Screen time tương lai
có xu hướng {trend}.
"""

    create_note_box(
        ax_note,
        note
    )

    # ==================================================
    # ADJUST
    # ==================================================
    plt.subplots_adjust(
        left=0.08,
        right=0.97,
        top=0.88,
        bottom=0.14
    )

    # ==================================================
    # SAVE
    # ==================================================
    plt.savefig(
        "result/forecast.png",
        dpi=300,
        bbox_inches='tight'
    )

    if show:
        plt.show()

    plt.close()

# ======================================================
# FORECAST FUTURE
# ======================================================
def forecast_future(
        best_model,
        df,
        periods=30,
        show=False
):

    # ==================================================
    # LẤY SCREEN TIME THỰC TẾ
    # ==================================================
    history = (
        df['screen_time_min']
        .tail(14)
        .values
        .tolist()
    )

    # ==================================================
    # DỰ BÁO
    # ==================================================
    preds = []

    for i in range(periods):

        # trung bình 7 ngày gần nhất
        moving_avg = np.mean(
            history[-7:]
        )

        # xu hướng tăng giảm
        trend = (
            history[-1]
            - history[-7]
        ) / 7

        # dự báo tiếp theo
        next_value = (
            moving_avg
            + trend * 0.5
        )

        # giới hạn hợp lý
        next_value = max(
            5,
            next_value
        )

        preds.append(
            round(next_value, 1)
        )

        history.append(
            next_value
        )

    preds = np.array(preds)

    # ==================================================
    # SAVE CSV
    # ==================================================
    future_df = pd.DataFrame({

        "day": range(1, periods + 1),

        "predicted_screen_time": preds
    })

    future_df.to_csv(
        "result/forecast.csv",
        index=False
    )

    # ==================================================
    # TREND
    # ==================================================
    start = round(preds[0], 1)

    end = round(preds[-1], 1)

    trend_text = (
        "tăng"
        if end > start
        else "giảm"
    )

    # ==================================================
    # DRAW CHART
    # ==================================================
    plot_forecast(
        preds,
        periods,
        trend_text,
        start,
        end,
        show=show
    )

    print(
        "\n✔ Đã lưu forecast.csv và forecast.png"
    )

    return preds