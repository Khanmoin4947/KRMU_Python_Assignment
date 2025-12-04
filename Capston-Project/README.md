# Campus Energy Dashboard – Moin Khan

This project is a capstone assignment for **Programming for Problem Solving using Python**.  
It analyses campus electricity usage from multiple buildings and presents insights through
aggregations and visualizations.

## Objectives


## Project Structure

```text
project/
├─ data/                     # Raw CSV files (input)
├─ output/                   # Cleaned CSVs, summary.txt, dashboard.png
├─ energy_dashboard/         # Python package with modules
│  ├─ ingestion.py
│  ├─ aggregation.py
│  ├─ models.py
│  ├─ visualization.py
│  └─ persistence.py
├─ main.py                   # Orchestrates all tasks
├─ requirements.txt
└─ README.md

````markdown
# Campus Energy Dashboard – Moin Khan

This project is a capstone assignment for **Programming for Problem Solving using Python**.  
It analyses campus electricity usage from multiple buildings and presents insights through
aggregations and visualizations.

## Objectives

- Read and validate multiple CSV files with monthly electricity data.
- Use Pandas to combine and clean the data.
- Compute daily and weekly energy consumption.
- Design object-oriented models (`Building`, `MeterReading`, `BuildingManager`).
- Build a multi-chart dashboard using Matplotlib.
- Export cleaned datasets, building-wise summaries, and an executive text summary.

## Project Structure

```text
project/
├─ data/                     # Raw CSV files (input)
├─ output/                   # Cleaned CSVs, summary.txt, dashboard.png
├─ energy_dashboard/         # Python package with modules
│  ├─ ingestion.py
│  ├─ aggregation.py
│  ├─ models.py
│  ├─ visualization.py
│  └─ persistence.py
├─ main.py                   # Orchestrates all tasks
├─ requirements.txt
└─ README.md

````

## Installation & Run

Prerequisites: Python 3.10+ and `pip`.

1. Install dependencies:

```powershell
pip install -r requirements.txt
```

2. Place your building CSV files in the `data/` folder. Each CSV should contain at least:
- `timestamp` (ISO datetime string)
- `kwh` (numeric)

Optionally include `building` or the filename will be used as building name.

3. Run the project:

```powershell
python main.py
```

Outputs are written to the `output/` folder: `cleaned_energy_data.csv`, `building_summary.csv`, `summary.txt`, and `dashboard.png`.
