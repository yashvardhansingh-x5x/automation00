import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_model():
    df = pd.read_csv(os.path.join("data", "processed", "processed_data.csv"))
    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    model_path = os.path.join("src", "models", "model.pkl")
    joblib.dump(model, model_path)
    print("Model trained and saved:", model_path)

if __name__ == "__main__":
    train_model()
