def create_features(df):
    # Example: add a new feature
    if 'value' in df.columns:
        df['value_squared'] = df['value'] ** 2
    print("Features created")
    return df
