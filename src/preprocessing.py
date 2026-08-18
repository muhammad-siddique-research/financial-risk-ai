"""
Data preprocessing utilities
Financial Risk Prediction Project
"""

import pandas as pd
import numpy as np


def load_data(path):
    """
    Load financial dataset.
    """
    return pd.read_csv(path)

def check_missing_values(df):
    """
    Check missing values in dataset.
    """
    return df.isnull().sum()
