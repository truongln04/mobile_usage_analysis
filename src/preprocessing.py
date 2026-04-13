import pandas as pd

def clean_data(df):
    # Giữ lại các cột cần thiết
    df = df[[
        'user_id',
        'date',
        'app_name',
        'category',
        'screen_time_min',
        'launches',
        'interactions',
        'is_productive'
    ]]

    # Xóa trùng
    df = df.drop_duplicates()

    # Xóa thiếu dữ liệu quan trọng
    df = df.dropna()

    # Convert date
    df['date'] = pd.to_datetime(df['date'])

    return df


def feature_engineering(df):
    df['weekday'] = df['date'].dt.day_name()
    df['month'] = df['date'].dt.month

    return df