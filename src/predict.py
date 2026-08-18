"""
Prediction pipeline for corporate bankruptcy risk.

Loads trained machine learning models and generates
financial distress predictions.
"""


import joblib
import pandas as pd

from src.config import MODEL_DIR



def load_models():

    """
    Load trained models and scaler.
    """

    rf_model = joblib.load(
        f"{MODEL_DIR}/random_forest.pkl"
    )

    xgb_model = joblib.load(
        f"{MODEL_DIR}/xgboost.pkl"
    )

    scaler = joblib.load(
        f"{MODEL_DIR}/scaler.pkl"
    )


    return (
        rf_model,
        xgb_model,
        scaler
    )



def predict_risk(data):

    """
    Predict corporate bankruptcy risk.

    Parameters:
        data:
            Financial indicators dataframe

    Returns:
        Prediction label
        Risk probability
    """


    if not isinstance(data, pd.DataFrame):

        raise TypeError(
            "Input must be a pandas DataFrame"
        )


    _, xgb_model, scaler = load_models()


    data_scaled = scaler.transform(
        data
    )


    prediction = xgb_model.predict(
        data_scaled
    )


    probability = xgb_model.predict_proba(
        data_scaled
    )[:,1]


    risk_level = [
        "Healthy Company"
        if value == 0
        else "Financial Distress Risk"
        for value in prediction
    ]


    results = pd.DataFrame({

        "Prediction":
            risk_level,

        "Risk Probability":
            probability

    })


    return results
