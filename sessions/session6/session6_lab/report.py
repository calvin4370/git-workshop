"""Print and plot the results."""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

from config import OUTPUT_DIR


def print_summary(by_museum):
    """Print the total visits for each museum.

    Args:
        by_museum (pd.Series): Total visits, indexed by museum.
    """
    print("Total visits by museum")
    print(by_museum.to_string())


def plot_visits_by_museum(by_museum):
    """Save a bar chart of the total visits for each museum.

    Args:
        by_museum (pd.Series): Total visits, indexed by museum.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ax = sns.barplot(x=by_museum.index, y=by_museum.values)
    ax.set_title("Total visits by museum")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "visits_by_museum.png"))
    plt.close()
