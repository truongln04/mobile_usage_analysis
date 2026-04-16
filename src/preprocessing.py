import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
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
    df = df.drop_duplicates()
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df['weekday'] = df['date'].dt.day_name()
    df['month'] = df['date'].dt.month
    return df
