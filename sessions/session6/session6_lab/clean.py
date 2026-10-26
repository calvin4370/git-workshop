"""Clean the visit data."""
from config import MUSEUMS


def clean_visits(visits):
    """Drop incomplete rows, and keep only the museums listed in MUSEUMS.

    Args:
        visits (pd.DataFrame): The raw visit data.

    Returns:
        pd.DataFrame: The cleaned visit data.
    """
    visits = visits.dropna()
    visits = visits.astype({"visits": int})
    visits = visits[visits["museum"].isin(MUSEUMS)]
    return visits
