Prediction pipeline for corporate bankruptcy risk.

Loads trained machine learning models and generates
bankruptcy risk predictions.

import joblib
import pandas as pd


def load_models():

    rf_model = joblib.load(
        "models/random_forest.pkl"
    )

    xgb_model = joblib.load(
        "models/xgboost.pkl"
    )

    scaler = joblib.load(
        "models/scaler.pkl"
    )

    return rf_model, xgb_model, scaler


def predict_risk(data):

    """
    Predict bankruptcy risk using XGBoost model.
    
    Input:
    Financial indicators dataframe
    
    Output:
    Bankruptcy prediction probability
    """

    _, xgb_model, scaler = load_models()

    data_scaled = scaler.transform(data)

    prediction = xgb_model.predict(data_scaled)

    probability = xgb_model.predict_proba(
        data_scaled
    )[:,1]

    return prediction, probability
