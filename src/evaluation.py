"""
Model evaluation utilities.

Provides:
- Classification metrics
- ROC-AUC evaluation
- Confusion matrix generation
- Performance reporting
"""


import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)


def evaluate_model(model, X_test, y_test):
    """
    Evaluate machine learning model performance.

    Returns:
        Dictionary containing evaluation metrics
    """

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]


    results = {

        "Accuracy":
            accuracy_score(
                y_test,
                predictions
            ),

        "Precision":
            precision_score(
                y_test,
                predictions
            ),

        "Recall":
            recall_score(
                y_test,
                predictions
            ),

        "F1 Score":
            f1_score(
                y_test,
                predictions
            ),

        "ROC-AUC":
            roc_auc_score(
                y_test,
                probabilities
            )
    }


    return results



def get_confusion_matrix(model, X_test, y_test):
    """
    Generate confusion matrix.
    """

    predictions = model.predict(X_test)

    return confusion_matrix(
        y_test,
        predictions
    )



def classification_report_df(model, X_test, y_test):
    """
    Return classification report as dataframe.
    """

    predictions = model.predict(X_test)

    report = classification_report(
        y_test,
        predictions,
        output_dict=True
    )

    return pd.DataFrame(report).transpose()
