# =========================================================
# FILE: visualization.py
# =========================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

os.makedirs("result", exist_ok=True)

# =========================================================
# FONT
# =========================================================
plt.rcParams['font.family'] = 'DejaVu Sans'


# =========================================================
# SAVE FIGURE
# =========================================================
def _save_and_show(fig, path, show=False):

    fig.savefig(
        path,
        dpi=300,
        bbox_inches='tight'
    )

    if show:
        plt.show()

    plt.close(fig)


# =========================================================
# STYLE CHART
# =========================================================
def style_chart(ax):

    ax.grid(
        axis='y',
        linestyle='--',
        alpha=0.4
    )

    for spine in ax.spines.values():
        spine.set_linewidth(1)


# =========================================================
# NOTE BOX
# =========================================================
def create_note_box(ax_note, note):

    ax_note.axis('off')

    ax_note.text(
        0.02,
        0.98,
        note,

        fontsize=9,
        va='top',
        linespacing=1.5,

        bbox=dict(
            facecolor='#F8F9F9',
            edgecolor='#2C3E50',
            linewidth=1.3,
            boxstyle='round,pad=0.8'
        )
    )


# =========================================================
# CREATE LAYOUT
# =========================================================
def create_layout():

    fig = plt.figure(
        figsize=(14,6),
        facecolor='white'
    )

    gs = fig.add_gridspec(
        1,
        2,

        width_ratios=[3.2,1],

        wspace=0.12
    )

    ax = fig.add_subplot(gs[0])

    ax_note = fig.add_subplot(gs[1])

    return fig, ax, ax_note


# =========================================================
# 1. TOP APPS
# =========================================================
def plot_top_apps(df, show=False):

    top = (
        df.groupby('app_name')['screen_time_min']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax, ax_note = create_layout()

    sns.barplot(
        x=top.index,
        y=top.values,
        ax=ax
    )

    ax.set_title(
        "TOP 10 ỨNG DỤNG ĐƯỢC SỬ DỤNG NHIỀU NHẤT",
        fontsize=15,
        fontweight='bold',
        pad=15
    )

    ax.set_xlabel(
        "Tên Ứng Dụng",
        fontsize=11,
        fontweight='bold'
    )

    ax.set_ylabel(
        "Screen Time - phút",
        fontsize=11,
        fontweight='bold'
    )

    plt.xticks(
        rotation=15,
        fontsize=9
    )

    for i, v in enumerate(top.values):

        ax.text(
            i,
            v + 3,
            f"{v:.1f}",
            ha='center',
            fontsize=8,
            fontweight='bold'
        )

    style_chart(ax)

    top_app = top.idxmax()

    note = f"""
- MỤC ĐÍCH
Phân tích ứng dụng
được sử dụng nhiều nhất.

- NHẬN XÉT
• App cao nhất:
  {top_app}

• Một vài app chiếm
  phần lớn screen time.

- ĐÁNH GIÁ
• Người dùng tập trung
  vào nhóm app phổ biến.

- KẾT LUẬN
Ứng dụng phổ biến ảnh hưởng
mạnh đến thói quen sử dụng.
"""

    create_note_box(
        ax_note,
        note
    )

    plt.subplots_adjust(
        left=0.08,
        right=0.97,
        top=0.88,
        bottom=0.14
    )

    _save_and_show(
        fig,
        "result/top_apps.png",
        show
    )

    return {
        "figure":"result/top_apps.png"
    }


# =========================================================
# 2. CATEGORY
# =========================================================
def plot_category(df, show=False):

    cat = (
        df.groupby('category')['screen_time_min']
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax, ax_note = create_layout()

    ax.pie(
        cat.values,
        labels=cat.index,
        autopct='%1.1f%%',
        startangle=140
    )

    ax.set_title(
        "PHÂN BỐ SCREEN TIME THEO DANH MỤC",
        fontsize=15,
        fontweight='bold',
        pad=15
    )

    top_cat = cat.idxmax()

    note = f"""
- MỤC ĐÍCH
Phân tích nhóm ứng dụng
được sử dụng nhiều nhất.

- NHẬN XÉT
• Danh mục lớn nhất:
  {top_cat}

- ĐÁNH GIÁ
• Người dùng ưu tiên
  một số nhóm ứng dụng.

- KẾT LUẬN
Hành vi sử dụng tập trung
vào danh mục phổ biến.
"""

    create_note_box(
        ax_note,
        note
    )

    _save_and_show(
        fig,
        "result/category.png",
        show
    )

    return {
        "figure":"result/category.png"
    }


# =========================================================
# 3. TREND
# =========================================================
def plot_trend(df, show=False):

    df2 = df.copy()

    df2['date'] = pd.to_datetime(df2['date'])

    daily = (
        df2.groupby('date')['screen_time_min']
        .sum()
        .sort_index()
    )

    rolling = daily.rolling(7).mean()

    fig, ax, ax_note = create_layout()

    ax.plot(
        daily.index,
        daily.values,
        label='Daily'
    )

    ax.plot(
        rolling.index,
        rolling.values,
        color='red',
        linewidth=2,
        label='7-Day Average'
    )

    ax.legend()

    ax.set_title(
        "XU HƯỚNG SỬ DỤNG ĐIỆN THOẠI",
        fontsize=15,
        fontweight='bold',
        pad=15
    )

    ax.set_xlabel(
        "Ngày",
        fontsize=11,
        fontweight='bold'
    )

    ax.set_ylabel(
        "Screen Time - phút",
        fontsize=11,
        fontweight='bold'
    )

    style_chart(ax)

    trend = (
        "tăng"
        if rolling.iloc[-1] > rolling.iloc[0]
        else "giảm"
    )

    note = f"""
- MỤC ĐÍCH
Theo dõi xu hướng
sử dụng theo thời gian.

- NHẬN XÉT
• Xu hướng hiện tại:
  {trend}

• Dữ liệu biến động
  theo từng ngày.

- ĐÁNH GIÁ
• Có sự thay đổi hành vi
  sử dụng điện thoại.

- KẾT LUẬN
Screen time đang {trend}.
"""

    create_note_box(
        ax_note,
        note
    )

    _save_and_show(
        fig,
        "result/trend.png",
        show
    )

    return {
        "figure":"result/trend.png"
    }


# =========================================================
# 4. WEEKDAY
# =========================================================
def plot_weekday(df, show=False):

    # =====================================================
    # THỨ TỰ THỨ TRONG TUẦN
    # =====================================================
    weekday_order = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]

    # =====================================================
    # GROUP DATA
    # =====================================================
    weekday = (
        df.groupby('weekday')['screen_time_min']
        .mean()
        .reindex(weekday_order)
    )

    # =====================================================
    # CREATE LAYOUT
    # =====================================================
    fig, ax, ax_note = create_layout()

    # =====================================================
    # BARPLOT
    # =====================================================
    sns.barplot(
        x=weekday.index,
        y=weekday.values,
        ax=ax
    )

    # =====================================================
    # TITLE
    # =====================================================
    ax.set_title(
        "SCREEN TIME THEO THỨ",
        fontsize=15,
        fontweight='bold',
        pad=15
    )

    # =====================================================
    # LABELS
    # =====================================================
    ax.set_xlabel(
        "Ngày Trong Tuần",
        fontsize=11,
        fontweight='bold'
    )

    ax.set_ylabel(
        "Screen Time Trung Bình",
        fontsize=11,
        fontweight='bold',
        labelpad=15
    )

    # =====================================================
    # HIỂN THỊ GIÁ TRỊ
    # =====================================================
    for i, v in enumerate(weekday.values):

        ax.text(
            i,
            v + 2,
            f"{v:.1f}",
            ha='center',
            fontsize=8,
            fontweight='bold'
        )

    # =====================================================
    # STYLE
    # =====================================================
    style_chart(ax)

    # =====================================================
    # NGÀY CAO NHẤT
    # =====================================================
    best_day = weekday.idxmax()

    # =====================================================
    # NOTEBOX
    # =====================================================
    note = f"""
- MỤC ĐÍCH
Phân tích thời gian dùng
theo từng ngày trong tuần.

- NHẬN XÉT
• Ngày cao nhất: {best_day}

- ĐÁNH GIÁ
• Hành vi sử dụng khác nhau
  giữa các ngày.

• Có ngày sử dụng điện thoại
  cao hơn rõ rệt.

- KẾT LUẬN
Người dùng không sử dụng
điện thoại đồng đều mỗi ngày.
"""

    create_note_box(
        ax_note,
        note
    )

    # =====================================================
    # SAVE
    # =====================================================
    _save_and_show(
        fig,
        "result/weekday.png",
        show
    )

    return {
        "figure":"result/weekday.png"
    }
# =========================================================
# 5. BOXPLOT
# =========================================================
def plot_box(df, show=False):

    fig, ax, ax_note = create_layout()

    sns.boxplot(
        x=df['screen_time_min'],
        ax=ax
    )

    ax.set_title(
        "PHÂN BỐ SCREEN TIME",
        fontsize=15,
        fontweight='bold',
        pad=15
    )

    ax.set_xlabel(
        "Screen Time - phút",
        fontsize=11,
        fontweight='bold'
    )

    style_chart(ax)

    note = """
- MỤC ĐÍCH
Phân tích phân bố dữ liệu.

- NHẬN XÉT
• Có nhiều điểm ngoại lệ.

• Dữ liệu phân bố rộng.

- ĐÁNH GIÁ
• Thời gian sử dụng
  không đồng đều.

- KẾT LUẬN
Người dùng có sự khác biệt
lớn về screen time.
"""

    create_note_box(
        ax_note,
        note
    )

    _save_and_show(
        fig,
        "result/boxplot.png",
        show
    )

    return {
        "figure":"result/boxplot.png"
    }


# =========================================================
# 6. PRODUCTIVE APPS
# =========================================================
def plot_productive(df, show=False):

    prod = (
        df.groupby('is_productive')['screen_time_min']
        .sum()
    )

    fig, ax, ax_note = create_layout()

    sns.barplot(
        x=prod.index.astype(str),
        y=prod.values,
        ax=ax
    )

    ax.set_title(
        "APP HỌC TẬP VÀ GIẢI TRÍ",
        fontsize=15,
        fontweight='bold',
        pad=15
    )

    ax.set_xlabel(
        "Loại Ứng Dụng",
        fontsize=11,
        fontweight='bold'
    )

    ax.set_ylabel(
        "Tổng Screen Time",
        fontsize=11,
        fontweight='bold'
    )

    for i, v in enumerate(prod.values):

        ax.text(
            i,
            v + 5,
            f"{v:.1f}",
            ha='center',
            fontsize=8,
            fontweight='bold'
        )

    style_chart(ax)

    note = """
- MỤC ĐÍCH
So sánh app học tập
và giải trí.

- NHẬN XÉT
• Một nhóm app chiếm
  nhiều thời gian hơn.

- ĐÁNH GIÁ
• Người dùng thiên về
  một loại ứng dụng.

- KẾT LUẬN
Có sự khác biệt rõ ràng
giữa học và giải trí.
"""

    create_note_box(
        ax_note,
        note
    )

    _save_and_show(
        fig,
        "result/productive.png",
        show
    )

    return {
        "figure":"result/productive.png"
    }
# =========================================================
# 5. BOXPLOT
# =========================================================
def plot_box(df, show=False):

    fig = plt.figure(
        figsize=(16,6),
        facecolor='white'
    )

    gs = fig.add_gridspec(
        1,
        2,
        width_ratios=[2.8,1.2],
        wspace=0.08
    )

    # =====================================================
    # LEFT CHART
    # =====================================================
    ax = fig.add_subplot(gs[0])

    sns.boxplot(
        x=df['screen_time_min'],
        ax=ax
    )

    ax.set_title(
        "PHÂN BỐ SCREEN TIME\n"
        "(Screen Time Distribution)",
        fontsize=16,
        fontweight='bold',
        pad=15
    )

    ax.set_xlabel(
        "Screen Time - phút",
        fontsize=12,
        fontweight='bold',
        labelpad=12
    )

    ax.grid(
        linestyle='--',
        alpha=0.3
    )

    # =====================================================
    # RIGHT NOTEBOX
    # =====================================================
    ax_note = fig.add_subplot(gs[1])

    note = """
- MỤC ĐÍCH
Phân tích phân bố dữ liệu
screen time của người dùng.

- NHẬN XÉT
• Xuất hiện nhiều điểm
  ngoại lệ trên biểu đồ.

• Dữ liệu phân bố chưa đều.

- ĐÁNH GIÁ
• Người dùng có mức sử dụng
  điện thoại khác nhau.

• Có người dùng rất ít,
  có người dùng rất nhiều.

- KẾT LUẬN
Screen time biến động lớn
giữa các người dùng.
"""

    create_note_box(
        ax_note,
        note
    )

    plt.subplots_adjust(
        left=0.08,
        right=0.97,
        top=0.88,
        bottom=0.15
    )

    _save_and_show(
        fig,
        "result/boxplot.png",
        show
    )

    return {
        "figure":"result/boxplot.png"
    }


# =========================================================
# 6. PRODUCTIVE
# =========================================================
def plot_productive(df, show=False):

    prod = (
        df.groupby('is_productive')['screen_time_min']
        .sum()
    )

    fig = plt.figure(
        figsize=(16,7),
        facecolor='white'
    )

    gs = fig.add_gridspec(
        1,
        2,
        width_ratios=[2.8,1.2],
        wspace=0.08
    )

    # =====================================================
    # LEFT CHART
    # =====================================================
    ax = fig.add_subplot(gs[0])

    sns.barplot(
        x=prod.index.astype(str),
        y=prod.values,
        ax=ax
    )

    ax.set_title(
        "ỨNG DỤNG HỌC TẬP VÀ GIẢI TRÍ\n"
        "(Productive vs Non-Productive Apps)",
        fontsize=16,
        fontweight='bold',
        pad=15
    )

    ax.set_xlabel(
        "Loại Ứng Dụng",
        fontsize=12,
        fontweight='bold',
        labelpad=10
    )

    ax.set_ylabel(
        "Tổng Screen Time - phút",
        fontsize=12,
        fontweight='bold',
        labelpad=12
    )

    for i, v in enumerate(prod.values):

        ax.text(
            i,
            v + 5,
            f"{v:.1f}",
            ha='center',
            fontsize=9,
            fontweight='bold'
        )

    ax.grid(
        axis='y',
        linestyle='--',
        alpha=0.3
    )

    # =====================================================
    # RIGHT NOTEBOX
    # =====================================================
    ax_note = fig.add_subplot(gs[1])

    note = """
- MỤC ĐÍCH
So sánh thời gian sử dụng
giữa app học tập và giải trí.

- NHẬN XÉT
• Một nhóm ứng dụng chiếm
  phần lớn screen time.

• Người dùng thiên về
  một loại app chính.

- ĐÁNH GIÁ
• Có sự chênh lệch rõ ràng
  giữa hai nhóm ứng dụng.

- KẾT LUẬN
Hành vi sử dụng điện thoại
phụ thuộc vào mục đích dùng.
"""

    create_note_box(
        ax_note,
        note
    )

    plt.subplots_adjust(
        left=0.08,
        right=0.97,
        top=0.88,
        bottom=0.15
    )

    _save_and_show(
        fig,
        "result/productive.png",
        show
    )

    return {
        "figure":"result/productive.png"
    }


# =========================================================
# 7. HEATMAP
# =========================================================
def plot_corr_heatmap(df, show=False):

    corr = df[
        ['launches', 'interactions', 'screen_time_min']
    ].corr()

    fig = plt.figure(
        figsize=(16,7),
        facecolor='white'
    )

    gs = fig.add_gridspec(
        1,
        2,
        width_ratios=[2.4,1.3],
        wspace=0.08
    )

    # =====================================================
    # LEFT CHART
    # =====================================================
    ax = fig.add_subplot(gs[0])

    sns.heatmap(
        corr,
        annot=True,
        cmap="vlag",
        ax=ax
    )

    ax.set_title(
        "BẢN ĐỒ NHIỆT TƯƠNG QUAN\n"
        "(Correlation Heatmap)",
        fontsize=16,
        fontweight='bold',
        pad=15
    )

    # =====================================================
    # RIGHT NOTEBOX
    # =====================================================
    ax_note = fig.add_subplot(gs[1])

    note = """
- MỤC ĐÍCH
Phân tích mức độ tương quan
giữa các biến dữ liệu.

- NHẬN XÉT
• Giá trị gần 1:
  tương quan mạnh.

• Giá trị gần 0:
  tương quan yếu.

- ĐÁNH GIÁ
• interactions và launches
  ảnh hưởng đến screen time.

• Các biến phù hợp cho ML.

- KẾT LUẬN
Dữ liệu có mối liên hệ tốt
để xây dựng mô hình dự đoán.
"""

    create_note_box(
        ax_note,
        note
    )

    plt.subplots_adjust(
        left=0.08,
        right=0.97,
        top=0.88,
        bottom=0.12
    )

    _save_and_show(
        fig,
        "result/corr_heatmap.png",
        show
    )

    return {
        "figure":"result/corr_heatmap.png"
    }


# =========================================================
# 8. SCATTER PLOT
# =========================================================
def plot_scatter_interactions(df, show=False):

    fig = plt.figure(
        figsize=(16,7),
        facecolor='white'
    )

    gs = fig.add_gridspec(
        1,
        2,
        width_ratios=[2.8,1.2],
        wspace=0.08
    )

    # =====================================================
    # LEFT CHART
    # =====================================================
    ax = fig.add_subplot(gs[0])

    sns.scatterplot(
        x='interactions',
        y='screen_time_min',
        data=df,
        ax=ax
    )

    sns.regplot(
        x='interactions',
        y='screen_time_min',
        data=df,
        scatter=False,
        color='red',
        ax=ax
    )

    ax.set_title(
        "MỐI QUAN HỆ GIỮA TƯƠNG TÁC VÀ SCREEN TIME\n"
        "(Interactions vs Screen Time)",
        fontsize=16,
        fontweight='bold',
        pad=15
    )

    ax.set_xlabel(
        "Số Lần Tương Tác",
        fontsize=12,
        fontweight='bold',
        labelpad=10
    )

    ax.set_ylabel(
        "Screen Time - phút",
        fontsize=12,
        fontweight='bold',
        labelpad=15
    )

    ax.grid(
        linestyle='--',
        alpha=0.3
    )

    # =====================================================
    # RIGHT NOTEBOX
    # =====================================================
    ax_note = fig.add_subplot(gs[1])

    note = """
- MỤC ĐÍCH
Phân tích mối quan hệ giữa
interactions và screen time.

- NHẬN XÉT
• Các điểm dữ liệu tăng dần
  theo chiều đi lên.

• Đường hồi quy cho thấy
  xu hướng tương quan dương.

- ĐÁNH GIÁ
• interactions tăng thì
  screen time cũng tăng.

• Hai biến liên hệ khá mạnh.

- KẾT LUẬN
interactions là biến quan trọng
trong dự đoán screen time.
"""

    create_note_box(
        ax_note,
        note
    )

    plt.subplots_adjust(
        left=0.08,
        right=0.97,
        top=0.88,
        bottom=0.14
    )

    _save_and_show(
        fig,
        "result/scatter_interactions.png",
        show
    )

    return {
        "figure":"result/scatter_interactions.png"
    }
# =========================================================
# 9. PIPELINE
# =========================================================
def plot_pipeline_with_conclusion(show=False):

    steps = [

        "Thu thập dữ liệu\n(Data Collection)",

        "Tiền xử lý\n(Preprocessing)",

        "EDA\n(Exploratory Analysis)",

        "Visualization\n(Trực quan hóa)",

        "Training\n(Huấn luyện)",

        "Evaluation\n(Đánh giá)",

        "Forecast\n(Dự báo)"
    ]

    fig = plt.figure(
        figsize=(18,6),
        facecolor='white'
    )

    gs = fig.add_gridspec(
        1,
        2,
        width_ratios=[3,1.2],
        wspace=0.08
    )

    # =====================================================
    # LEFT PIPELINE
    # =====================================================
    ax = fig.add_subplot(gs[0])

    ax.axis("off")

    for i, step in enumerate(steps):

        x = i * 2

        box = mpatches.FancyBboxPatch(

            (x,1.5),

            1.7,
            0.8,

            boxstyle="round,pad=0.3",

            facecolor="#AED6F1",
            edgecolor="#1F618D",
            linewidth=2
        )

        ax.add_patch(box)

        ax.text(
            x + 0.85,
            1.9,
            step,

            ha='center',
            va='center',

            fontsize=9,
            fontweight='bold'
        )

        # =================================================
        # ARROW
        # =================================================
        if i < len(steps)-1:

            ax.annotate(
                "",

                xy=(x+1.7,1.9),
                xytext=(x+2,1.9),

                arrowprops=dict(
                    arrowstyle="->",
                    linewidth=2,
                    color="black"
                )
            )

    ax.set_xlim(-0.5, 14)
    ax.set_ylim(0.8, 3)

    ax.set_title(
        "QUY TRÌNH PHÂN TÍCH DỮ LIỆU\n"
        "(Data Analysis Pipeline)",

        fontsize=16,
        fontweight='bold',
        pad=15
    )

    # =====================================================
    # RIGHT NOTEBOX
    # =====================================================
    ax_note = fig.add_subplot(gs[1])

    note = """
- MỤC ĐÍCH
Mô tả toàn bộ quy trình
phân tích dữ liệu.

- NHẬN XÉT
• Dữ liệu đi qua nhiều bước:
  xử lý → phân tích → ML.

• Các bước liên kết chặt chẽ
  với nhau.

- ĐÁNH GIÁ
• Pipeline rõ ràng giúp
  hệ thống dễ mở rộng.

• Quy trình hỗ trợ tốt
  cho dự báo dữ liệu.

- KẾT LUẬN
Hệ thống hoàn chỉnh từ
xử lý dữ liệu đến dự báo.
"""

    create_note_box(
        ax_note,
        note
    )

    plt.subplots_adjust(
        left=0.04,
        right=0.97,
        top=0.88,
        bottom=0.12
    )

    _save_and_show(
        fig,
        "result/pipeline.png",
        show
    )

    return {
        "figure":"result/pipeline.png"
    }


# =========================================================
# 10. GENERATE REPORT
# =========================================================
def generate_report(df, show=False):

    report = {}

    # =====================================================
    # TOP APPS
    # =====================================================
    report['top_apps'] = plot_top_apps(
        df,
        show=show
    )

    # =====================================================
    # CATEGORY
    # =====================================================
    report['category'] = plot_category(
        df,
        show=show
    )

    # =====================================================
    # TREND
    # =====================================================
    report['trend'] = plot_trend(
        df,
        show=show
    )

    # =====================================================
    # WEEKDAY
    # =====================================================
    report['weekday'] = plot_weekday(
        df,
        show=show
    )

    # =====================================================
    # BOXPLOT
    # =====================================================
    report['boxplot'] = plot_box(
        df,
        show=show
    )

    # =====================================================
    # PRODUCTIVE
    # =====================================================
    report['productive'] = plot_productive(
        df,
        show=show
    )

    # =====================================================
    # HEATMAP
    # =====================================================
    report['corr_heatmap'] = plot_corr_heatmap(
        df,
        show=show
    )

    # =====================================================
    # SCATTER
    # =====================================================
    report['scatter'] = plot_scatter_interactions(
        df,
        show=show
    )

    # =====================================================
    # PIPELINE
    # =====================================================
    report['pipeline'] = plot_pipeline_with_conclusion(
        show=show
    )

    print(
        "\n✔ ĐÃ TẠO TOÀN BỘ BIỂU ĐỒ THÀNH CÔNG"
    )

    return report