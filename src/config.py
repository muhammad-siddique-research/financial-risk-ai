"""
Project configuration settings
"""

import os


# Random seed for reproducibility
RANDOM_STATE = 42


# Data paths

DATA_PATH = "data/processed/financial_data_cleaned.csv"


# Output directories

MODEL_DIR = "models"
RESULTS_DIR = "results"
FIGURES_DIR = "figures"


# Create directories automatically

for directory in [
    MODEL_DIR,
    RESULTS_DIR,
    FIGURES_DIR
]:
    os.makedirs(directory, exist_ok=True)
