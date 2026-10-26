"""Load the raw visit data."""
import pandas as pd


def load_visits(path):
    """Load the visit data from a CSV file.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: One row per visit record.
    """
    return pd.read_csv(path, parse_dates=["date"])
