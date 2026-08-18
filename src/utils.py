"""
Utility functions for financial risk prediction pipeline
"""


import os


def create_directory(path):
    """
    Create directory if it does not exist.
    """

    os.makedirs(
        path,
        exist_ok=True
    )


def save_message(message):
    """
    Standardized pipeline logging.
    """

    print("=" * 60)
    print(message)
    print("=" * 60)
