"""Summarise the visit data."""


def visits_by_museum(visits):
    """Total visits for each museum, highest first.

    Args:
        visits (pd.DataFrame): The cleaned visit data.

    Returns:
        pd.Series: Total visits, indexed by museum.
    """
    return visits.groupby("museum")["visits"].sum().sort_values(ascending=False)
