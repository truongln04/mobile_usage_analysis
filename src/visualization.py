import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 1. TOP APP
# ==============================
def plot_top_apps(df):
    top = df.groupby('app_name')['screen_time_min'].sum().sort_values(ascending=False).head(10)

    ax = top.plot(kind='bar', figsize=(8,5), label='Screen Time')

    plt.title("Top 10 Most Used Apps (Top 10 ứng dụng dùng nhiều nhất)")
    plt.xlabel("App Name (Tên ứng dụng)")
    plt.ylabel("Total Screen Time (Tổng thời gian - phút)")
    plt.legend()

    plt.xticks(rotation=45)

    # Hiển thị số
    for container in ax.containers:
        ax.bar_label(container, fmt='%.0f')

    # chú thích ngoài
    ax.text(1.02, 0.5,
            "Higher bar → more usage\n(Cột cao → dùng nhiều)",
            transform=ax.transAxes,
            fontsize=9,
            bbox=dict(facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.savefig("result/top_apps.png", bbox_inches='tight')
    plt.show()


# ==============================
# 2. CATEGORY
# ==============================
def plot_category(df):
    cat = df.groupby('category')['screen_time_min'].sum()

    plt.figure(figsize=(6,6))
    plt.pie(cat, labels=cat.index, autopct='%1.1f%%')

    plt.title("Usage Distribution by Category\n(Phân bố theo loại ứng dụng)")
    plt.legend(title="Category")

    plt.savefig("result/category.png", bbox_inches='tight')
    plt.show()


# ==============================
# 3. TREND
# ==============================
def plot_trend(df):
    daily = df.groupby('date')['screen_time_min'].sum()

    plt.figure(figsize=(8,5))
    plt.plot(daily, marker='o', label='Screen Time')

    plt.title("Usage Trend Over Time\n(Xu hướng sử dụng theo thời gian)")
    plt.xlabel("Date (Ngày)")
    plt.ylabel("Screen Time (phút)")
    plt.legend()
    plt.grid(True)

    plt.text(0.02, 0.9,
             "Trend shows increase/decrease\n(Xu hướng tăng/giảm)",
             transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', alpha=0.8))

    plt.savefig("result/trend.png", bbox_inches='tight')
    plt.show()


# ==============================
# 4. WEEKDAY
# ==============================
def plot_weekday(df):
    weekday = df.groupby('weekday')['screen_time_min'].mean()

    ax = weekday.plot(kind='bar', figsize=(8,5), label='Average Usage')

    plt.title("Average Usage by Weekday\n(Thời gian trung bình theo ngày)")
    plt.xlabel("Weekday (Ngày trong tuần)")
    plt.ylabel("Average Screen Time (phút)")
    plt.legend()

    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f')

    ax.text(1.02, 0.5,
            "Higher → more usage\n(Cao hơn → dùng nhiều)",
            transform=ax.transAxes,
            fontsize=9,
            bbox=dict(facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.savefig("result/weekday.png", bbox_inches='tight')
    plt.show()


# ==============================
# 5. BOXPLOT
# ==============================
def plot_box(df):
    plt.figure(figsize=(7,4))
    sns.boxplot(x=df['screen_time_min'])

    plt.title("Distribution of Screen Time\n(Phân bố thời gian sử dụng)")
    plt.xlabel("Screen Time (phút)")

    plt.text(0.7, 0.8,
             "Outliers = unusual usage\n(Giá trị bất thường)",
             transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', alpha=0.8))

    plt.savefig("result/boxplot.png", bbox_inches='tight')
    plt.show()


# ==============================
# 6. PRODUCTIVE
# ==============================
def plot_productive(df):
    prod = df.groupby('is_productive')['screen_time_min'].sum()

    ax = prod.plot(kind='bar', figsize=(7,5), label='Screen Time')

    plt.title("Productive vs Non-Productive Apps\n(App hữu ích vs không hữu ích)")
    plt.xlabel("App Type (Loại ứng dụng)")
    plt.ylabel("Total Time (phút)")

    plt.xticks([0,1], ['Non-Productive\n(Không hữu ích)', 'Productive\n(Hữu ích)'], rotation=0)
    plt.legend()

    for container in ax.containers:
        ax.bar_label(container, fmt='%.0f')

    ax.text(1.02, 0.5,
            "Compare study vs entertainment\n(So sánh học tập & giải trí)",
            transform=ax.transAxes,
            fontsize=9,
            bbox=dict(facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.savefig("result/productive.png", bbox_inches='tight')
    plt.show()