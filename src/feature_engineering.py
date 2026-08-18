"""
Feature engineering utilities for financial risk modeling.

Includes:
- Feature selection
- Feature transformation
- Dataset preparation
"""


import pandas as pd



def remove_low_variance_features(
    X,
    threshold=0.0
):
    """
    Remove features with zero or very low variance.

    Parameters:
        X : pandas DataFrame
        threshold : variance threshold

    Returns:
        Reduced feature dataframe
    """

    variance = X.var()

    selected_features = variance[
        variance > threshold
    ].index

    return X[selected_features]



def select_features(
    X,
    selected_columns=None
):
    """
    Select important financial indicators.

    Parameters:
        X : dataframe
        selected_columns : list of feature names

    Returns:
        Selected dataframe
    """

    if selected_columns is None:
        return X

    return X[selected_columns]



def transform_features(X):
    """
    Apply feature transformations.

    Currently preserves dataset structure.

    Additional transformations such as:
    - log transformation
    - ratio creation
    - normalization
    can be added here.
    """

    X_transformed = X.copy()

    return X_transformed



def prepare_features(X):
    """
    Complete feature engineering pipeline.

    Steps:
    1. Remove low variance features
    2. Apply transformations
    3. Return processed features
    """

    X = remove_low_variance_features(
        X
    )

    X = transform_features(
        X
    )

    return X
