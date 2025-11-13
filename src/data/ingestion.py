import pandas as pd
import os

def load_raw_data():
    # Example: load CSV from data/raw
    file_path = os.path.join("data", "raw", "sample_data.csv")
    df = pd.read_csv(file_path)
    print("Raw data loaded:", df.shape)
    return df

def save_processed_data(df):
    processed_path = os.path.join("data", "processed", "processed_data.csv")
    df.to_csv(processed_path, index=False)
    print("Processed data saved:", processed_path)
