"""
Machine learning model definitions.

Models implemented:
- Logistic Regression
- Random Forest
- XGBoost
"""

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


def get_logistic_regression():
    """
    Returns Logistic Regression baseline model.
    """

    return LogisticRegression(
        max_iter=1000,
        random_state=42
    )


def get_random_forest():
    """
    Returns Random Forest classifier.
    """

    return RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )


def get_xgboost():
    """
    Returns XGBoost classifier.
    """

    return XGBClassifier(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=5,
        random_state=42,
        eval_metric="logloss"
    )


def get_all_models():
    """
    Returns all models in dictionary format.
    """

    models = {

        "Logistic Regression":
            get_logistic_regression(),

        "Random Forest":
            get_random_forest(),

        "XGBoost":
            get_xgboost()
    }

    return models
