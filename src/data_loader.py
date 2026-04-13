import kagglehub
import pandas as pd
import os

def load_data():
    path = kagglehub.dataset_download(
        "khushikyad001/screen-time-and-app-usage-dataset-iosandroid"
    )

    files = os.listdir(path)
    csv_file = [f for f in files if f.endswith('.csv')][0]

    df = pd.read_csv(os.path.join(path, csv_file))
    print("Loaded data shape:", df.shape)

    return df