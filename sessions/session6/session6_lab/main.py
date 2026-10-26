"""Run the minion visitorship pipeline: load, clean, analyse, then report."""
from analysis import visits_by_museum
from clean import clean_visits
from config import DATA_PATH
from load import load_visits
from report import plot_visits_by_museum, print_summary


def main():
    visits = load_visits(DATA_PATH)
    visits = clean_visits(visits)

    by_museum = visits_by_museum(visits)

    print_summary(by_museum)
    plot_visits_by_museum(by_museum)


if __name__ == "__main__":
    main()
