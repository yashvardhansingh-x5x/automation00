import pandas as pd

def preprocess(df):
    # Simple preprocessing example
    df = df.dropna()
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype('category').cat.codes
    print("Data preprocessed:", df.shape)
    return df
