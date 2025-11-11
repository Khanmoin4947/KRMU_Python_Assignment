# Author: Moin Khan
# Reg no. :2501730052
# Course: Ai/ML
# Title: Analyzing and Reporting Student Grades

import statistics

def display_welcome_message():
    """Display welcome message and main menu"""
    print("\n" + "="*60)
    print("          WELCOME TO GRADEBOOK ANALYZER")
    print("="*60)
    print("\nThis program helps teachers analyze student performance")
    print("after class tests by computing statistics, grades, and summaries.")
    print("\n" + "="*60)
    print("MAIN MENU")
    print("="*60)
    print("1. Input Student Data")
    print("2. Analyze and Display Results")
    print("3. Exit")
    print("="*60 + "\n")



def input_student_data():
    """
    Ask user for number of students and collect name and marks for each.
    Returns dictionary with student names as keys and marks as values.
    """
    marks = {}
    
    try:
        num_students = int(input("Enter the number of students in the class: "))
        
        if num_students <= 0:
            print("Error: Number of students must be greater than 0!")
            return None
        
        print(f"\nEnter data for {num_students} student(s):\n")
        
        for i in range(num_students):
            print(f"--- Student {i+1} ---")
            name = input("Enter student name: ").strip()
            
            if not name:
                print("Error: Name cannot be empty!")
                return None
            
            try:
                mark = float(input(f"Enter marks for {name}: "))
                
                if mark < 0 or mark > 100:
                    print("Error: Marks must be between 0 and 100!")
                    return None
                
                marks[name] = mark
            except ValueError:
                print("Error: Marks must be a valid number!")
                return None
            
            print()
        
        return marks
    
    except ValueError:
        print("Error: Number of students must be a valid integer!")
        return None


def calculate_average(marks_dict):
    """Calculate and return average of all marks"""
    if not marks_dict:
        return 0
    return sum(marks_dict.values()) / len(marks_dict)


def calculate_median(marks_dict):
    """Calculate and return median of all marks"""
    if not marks_dict:
        return 0
    marks_list = list(marks_dict.values())
    return statistics.median(marks_list)


def find_max_score(marks_dict):
    """Find and return maximum score"""
    if not marks_dict:
        return 0
    return max(marks_dict.values())


def find_min_score(marks_dict):
    """Find and return minimum score"""
    if not marks_dict:
        return 0
    return min(marks_dict.values())


def display_statistics(marks_dict):
    """Display all statistical analysis"""
    print("\n" + "="*60)
    print("STATISTICAL ANALYSIS")
    print("="*60)
    
    average = calculate_average(marks_dict)
    median = calculate_median(marks_dict)
    max_score = find_max_score(marks_dict)
    min_score = find_min_score(marks_dict)
    
    print(f"Average Score:  {average:.2f}")
    print(f"Median Score:   {median:.2f}")
    print(f"Maximum Score:  {max_score:.2f}")
    print(f"Minimum Score:  {min_score:.2f}")
    print("="*60 + "\n")


def assign_grade(marks):
    """
    Assign grade based on marks using if-elif-else logic.
    A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60
    """
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def calculate_grades(marks_dict):
    """
    Create and return dictionary with student names and their grades.
    """
    grades = {name: assign_grade(mark) for name, mark in marks_dict.items()}
    return grades


def display_grade_distribution(grades):
    """Display count of students per grade category"""
    grade_count = {}
    
    for grade in ["A", "B", "C", "D", "F"]:
        count = list(grades.values()).count(grade)
        grade_count[grade] = count
    
    print("\n" + "="*60)
    print("GRADE DISTRIBUTION")
    print("="*60)
    
    for grade in ["A", "B", "C", "D", "F"]:
        print(f"Grade {grade}: {grade_count[grade]} student(s)")
    
    print("="*60 + "\n")



def filter_pass_fail_students(marks_dict):
    """
    Use list comprehensions to separate passed and failed students.
    Pass: marks >= 40
    Fail: marks < 40
    """
    passed_students = [name for name, m in marks_dict.items() if m >= 40]
    failed_students = [name for name, m in marks_dict.items() if m < 40]
    
    return passed_students, failed_students


def display_pass_fail_summary(marks_dict):
    """Display pass/fail students and their counts"""
    passed, failed = filter_pass_fail_students(marks_dict)
    
    print("\n" + "="*60)
    print("PASS/FAIL SUMMARY")
    print("="*60)
    
    print(f"\nPassed Students ({len(passed)}):")
    if passed:
        for name in passed:
            print(f"  • {name}: {marks_dict[name]:.1f}")
    else:
        print("  None")
    
    print(f"\nFailed Students ({len(failed)}):")
    if failed:
        for name in failed:
            print(f"  • {name}: {marks_dict[name]:.1f}")
    else:
        print("  None")
    
    print("="*60 + "\n")

def display_results_table(marks_dict, grades):
    """Display formatted results table with Name, Marks, and Grade"""
    print("\n" + "="*60)
    print("RESULTS TABLE")
    print("="*60)
    
    print(f"\n{'Name':<20} {'Marks':<12} {'Grade':<8}")
    print("-" * 60)
    
    for name, mark in marks_dict.items():
        grade = grades[name]
        print(f"{name:<20} {mark:<12.2f} {grade:<8}")
    
    print("="*60 + "\n")


def analyze_gradebook(marks_dict):
    """Main analysis function that displays all reports"""
    
    grades = calculate_grades(marks_dict)

    display_statistics(marks_dict)
    display_grade_distribution(grades)
    display_pass_fail_summary(marks_dict)
    display_results_table(marks_dict, grades)


def main():
    """Main function with user loop for re-running analysis"""
    display_welcome_message()
    
    marks_dict = None
    
    while True:
        if marks_dict is None:
            marks_dict = input_student_data()
            
            if marks_dict is None:
                print("\nData entry failed. Please try again.\n")
                continue
            analyze_gradebook(marks_dict)
       
        print("\nWhat would you like to do?")
        print("1. Enter new student data")
        print("2. Display current analysis again")
        print("3. Exit program")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            marks_dict = None
            print()
        elif choice == "2":
            if marks_dict:
                analyze_gradebook(marks_dict)
            else:
                print("\nNo data available. Please enter student data first.\n")
        elif choice == "3":
            print("\n" + "="*60)
            print("Thank you for using GradeBook Analyzer!")
            print("Happy coding and stay curious!")
            print("="*60 + "\n")
            break
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.\n")



if __name__ == "__main__":
    main()
