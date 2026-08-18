"""
Data preprocessing utilities

Financial Risk Prediction Project
"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



def load_data(path):
    """
    Load financial dataset.

    Parameters:
        path (str): Dataset location

    Returns:
        pandas DataFrame
    """

    return pd.read_csv(path)



def check_missing_values(df):
    """
    Check missing values in dataset.

    Returns:
        Missing value count
    """

    return df.isnull().sum()



def separate_features_target(df, target_column="Bankrupt?"):
    """
    Separate independent variables and target variable.
    """

    X = df.drop(
        target_column,
        axis=1
    )

    y = df[target_column]

    return X, y



def split_data(
    X,
    y,
    test_size=0.2,
    random_state=42
):
    """
    Split dataset into training and testing sets.
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )



def scale_features(
    X_train,
    X_test
):
    """
    Standardize numerical features.

    Returns:
        Scaled training data,
        scaled testing data,
        scaler object
    """

    scaler = StandardScaler()


    X_train_scaled = scaler.fit_transform(
        X_train
    )

    X_test_scaled = scaler.transform(
        X_test
    )


    return (
        X_train_scaled,
        X_test_scaled,
        scaler
    )
