def analyze_data(df):
    print("\n===== THỐNG KÊ =====")
    print(df.describe())

    print("\n===== TOP APP =====")
    print(df.groupby('app_name')['screen_time_min']
          .sum().sort_values(ascending=False).head())

    print("\n===== CATEGORY =====")
    print(df.groupby('category')['screen_time_min'].sum())

    print("\n===== TRUNG BÌNH =====")
    print(df['screen_time_min'].mean())