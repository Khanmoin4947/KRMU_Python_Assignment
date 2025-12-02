# KRMU_Python_Assignment

> University Python coursework and capstone project by **Moin Khan**

This repository contains lab assignments and a capstone project for the course *Programming for Problem Solving using Python*. Each assignment demonstrates core Python concepts and small projects; the capstone is a larger, structured project.

---

## Repository structure (actual)

```
KRMU_Python_Assignment/
├── Assignment-1/
│   └── Calorie-intake-tracker.py
├── Assignment-2/
│   └── Grade-book-analyzer.py
├── Assignment-3/
│   ├── cli/
│   ├── data/
│   ├── library_manager/
│   ├── tests/
│   ├── library.log
│   └── README.md
├── Assignment-4/
│   ├── plots/
│   ├── weather_data_visualizer.py
│   ├── weather_dataset.csv
│   └── requirements.txt
├── Capston-Project/
│   ├── energy_dashboard/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── .gitignore
└── README.md   <-- (this file)
```

---

## Short description of each assignment

### Assignment 1 — Calorie Intake Tracker
`Calorie-intake-tracker.py`  
A small script to track daily calorie intake — practice with user input, conditionals, and basic file I/O (if used). Good for learning core control flow and simple data storage.

### Assignment 2 — Grade Book Analyzer
`Grade-book-analyzer.py`  
Analyzes student marks and provides statistics — practice with lists, loops, functions, use of the `statistics` module, and basic reporting.

### Assignment 3 — Library Manager (package-style)
Folder structure:
- `cli/` — command-line interface utilities  
- `data/` — sample data files  
- `library_manager/` — package modules for library management logic  
- `tests/` — unit tests  
- `library.log` — runtime / example log file  

### Assignment 4 — Weather Data Visualizer
- `weather_data_visualizer.py` — script to load and visualize weather dataset  
- `weather_dataset.csv` — sample dataset used by the script  
- `plots/` — generated plot images  
- `requirements.txt` — Python dependencies  

### Capstone Project — Campus Energy Dashboard
Located in `Capston-Project/`:
- `energy_dashboard/` — project package  
- `main.py` — entry point  
- `requirements.txt` — dependencies  
- `README.md` — detailed description  

---

## How to run the examples

1. Clone the repository:
```bash
git clone https://github.com/Khanmoin4947/KRMU_Python_Assignment.git
cd KRMU_Python_Assignment
```

2. Run Assignment 1 or 2:
```bash
python Assignment-1/Calorie-intake-tracker.py
python Assignment-2/Grade-book-analyzer.py
```

3. Run Assignment 4:
```bash
cd Assignment-4
pip install -r requirements.txt
python weather_data_visualizer.py
```

4. Run Capstone:
```bash
cd Capston-Project
pip install -r requirements.txt
python main.py
```

---

## Tech / libraries used
- Python 3.x  
- pandas  
- matplotlib  
- unittest / pytest  
- Other libs listed in requirements.txt

---

## Contact
Moin Khan — GitHub: **@Khanmoin4947**
