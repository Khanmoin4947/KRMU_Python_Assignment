# 🍽️ Daily Calorie Tracker

**Student Name:** Moin Khan 
**Roll Number:** 2501730052
**Course:** Python Programming - Assignment 1

---

## 📖 Overview

The **Daily Calorie Tracker** is a Python command-line application that helps users monitor their daily calorie intake. Users can record multiple meals with their calorie values, and the program calculates total and average calories, compares them with a daily limit, and optionally saves a session report.

---

## ✨ Features

- ➕ **Add Multiple Meals:** Enter meal names and calorie values interactively
- 📊 **Automatic Calculations:** Computes total and average calorie intake
- ⚖️ **Limit Comparison:** Compares total calories with user-defined daily limit
- 🎨 **Colored Output:** Beautiful formatted table with ANSI color codes
- 💾 **Save Reports:** Export session data to `calorie_log.txt`
- 📅 **Date Tracking:** Automatically records date and time

---

## 🚀 How to Run

1. **Navigate to the project directory:**
   ```bash
   cd ASSIGNMENT-1/daily_calorie_tracker
   ```

2. **Run the program:**
   ```bash
   python tracker.py
   ```

3. **Follow the prompts:**
   - Enter number of meals
   - Set your daily calorie limit
   - Input meal details (format: `meal name, calories`)
   - Choose whether to save the report

---

## 📋 Usage Example

```text
How many meals do you want to add: 3
Enter your daily calorie limit: 2000

Enter meal name and calories separated by a comma: Breakfast, 350
Enter meal name and calories separated by a comma: Lunch, 450
Enter meal name and calories separated by a comma: Dinner, 650

S NO MEAL NAME           CALORIES
--------------------------------------------------
1    BREAKFAST           350.0
2    LUNCH               450.0
3    DINNER              650.0
--------------------------------------------------
Total Calories Consumed : 1450.0

Average Calories per Meal : 483.33

YOU ARE WITHIN YOUR DAILY CALORIE LIMIT.

Do you want to save this session report? (yes/no): yes
Session report saved successfully as 'calorie_log.txt'
```

---

## 📂 Output File Format

When saved, the report (`calorie_log.txt`) contains:

```text
===== DAILY CALORIE TRACKER REPORT =====
NAME: FARHAN HUSSAIN
ROLL NUMBER: 2501730002
DATE: 2025-12-03 ...

S NO MEAL NAME           CALORIES
----------------------------------------
1    BREAKFAST           350.0
2    LUNCH               450.0
3    DINNER              650.0
----------------------------------------
Total Calories Consumed: 1450.0
Average Calories per Meal: 483.33
Daily Calorie Limit: 2000.0
STATUS: You are within your daily calorie limit.
```

---

## 🧠 Python Concepts Demonstrated

- **Input/Output:** `input()` function for user interaction
- **Data Structures:** Lists for storing meals and calories
- **Control Flow:** `while` loops for iteration, `if-else` for comparisons
- **String Operations:** `split()`, `strip()`, `upper()` for data processing
- **File Handling:** Writing reports using `open()` and `write()`
- **Formatting:** F-strings with alignment and precision formatting
- **Built-in Functions:** `sum()`, `len()` for calculations
- **DateTime Module:** `datetime.now()` for timestamps
- **ANSI Codes:** Terminal color formatting

---

## 📦 File Structure

```
daily_calorie_tracker/
├── tracker.py           # Main application
├── calorie_log.txt      # Generated report (after saving)
└── README.md            # This file
```

---

## 🔧 Requirements

- **Python 3.x** or higher
- No external dependencies required
- Works on Windows, macOS, and Linux terminals

**Optional:** For better color support on Windows, install `colorama`:
```bash
pip install colorama
```

---

## 📝 Notes

- Meal names are automatically converted to uppercase
- Calorie values must be numeric (integers or decimals)
- Input format: `meal_name, calories` (comma-separated)
- Extra spaces are automatically trimmed
- Daily limit can be any positive number

---

## 👨‍💻 Author

**Farhan Hussain**  
Roll Number: 2501730002  
B.Tech CSE (AI & ML)  
K.R. Mangalam University

---

## 📄 License

This project is created for educational purposes as part of Python Programming coursework.
