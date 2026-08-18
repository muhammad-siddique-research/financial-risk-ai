"""
Financial Risk Prediction Pipeline

Author:
Muhammad Siddique

Purpose:
End-to-end training pipeline for corporate bankruptcy prediction
using econometric and machine learning approaches.
"""

import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier


# Paths

DATA_PATH = "data/processed/financial_data_cleaned.csv"

MODEL_PATH = "models"

os.makedirs(MODEL_PATH, exist_ok=True)


# Load Data

print("Loading dataset...")

df = pd.read_csv(DATA_PATH)


# Separate features and target

X = df.drop("Bankrupt?", axis=1)

y = df["Bankrupt?"]


# Train-test split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Scaling

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)



# Models

models = {

    "logistic_regression":
    LogisticRegression(max_iter=1000),

    "random_forest":
    RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ),

    "xgboost":
    XGBClassifier(
        random_state=42,
        eval_metric="logloss"
    )
}



# Training

for name, model in models.items():

    print(f"Training {name}...")

    model.fit(
        X_train_scaled,
        y_train
    )

    joblib.dump(
        model,
        f"{MODEL_PATH}/{name}.pkl"
    )


# Save scaler

joblib.dump(
    scaler,
    f"{MODEL_PATH}/scaler.pkl"
)


print("Training completed successfully.")
