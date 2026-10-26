# Minion Visitorship Pipeline

Analyses visits to NHB's museums by minions.

## How to run

From the root of the `minions-visitorship` repo:

```
python -m venv .venv
source .venv/bin/activate
pip install -r session6_lab/requirements.txt
python session6_lab/main.py
```

## Pipeline

1. `load.py`: loads the visit data from `data/sample_visits.csv`
2. `clean.py`: drops incomplete rows, and keeps only the museums in `MUSEUMS`
3. `analysis.py`: calculates the summaries
4. `report.py`: prints the summaries, and saves the charts to `output/`

## Configuration

All settings are in `config.py`:

- `DATA_PATH`: path to the visit data
- `OUTPUT_DIR`: where charts are saved. Can be overridden with an `OUTPUT_DIR` variable in a `.env` file
- `MUSEUMS`: the museums to include in the analysis

## Features

- Total visits by museum, printed and saved as a bar chart
