"""Settings for the minion visitorship pipeline."""
import os

from dotenv import load_dotenv

load_dotenv()

DATA_PATH = "session6_lab/data/sample_visits.csv"
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "session6_lab/output")

MUSEUMS = [
    "National Museum of Singapore",
    "Asian Civilisations Museum",
]
