def create_student_record(name, grades): 
    """Create a student record with calculated statistics.""" 
    return { 
        "name": name, 
        "grades": grades, 
        "average": sum(grades) / len(grades), 
        "highest": max(grades), 
        "lowest": min(grades) 
    } 
 
def calculate_letter_grade(average): 
    """Convert numeric average to letter grade.""" 
    if average >= 90: 
        return "A" 
    elif average >= 80: 
        return "B" 
    elif average >= 70: 
        return "C" 
    elif average >= 60: 
        return "D" 
    else: 
        return "F" 
    
def analyze_class_performance(students): 
    """Analyze overall class performance.""" 
    if not students: 
        return {} 
     
    all_averages = [student["average"] for student in students] 
     
    return { 
        "class_average": sum(all_averages) / len(all_averages), 
        "highest_average": max(all_averages), 
        "lowest_average": min(all_averages), 
        "total_students": len(students) 
    } 
 
def get_students_by_grade(students, letter_grade): 
    """Filter students by letter grade.""" 
    return [s for s in students if calculate_letter_grade(s["average"]) == 
letter_grade] 
 
def main(): 
    # Sample data 
    students = [] 
     
    # Get student data 
    while True: 
        name = input("Enter student name (or 'done' to finish): ") 
        if name.lower() == 'done': 
            break 
         
        print(f"Enter grades for {name} (enter 'done' when finished):") 
        grades = [] 
        while True: 
            grade_input = input("Enter grade: ") 
            if grade_input.lower() == 'done': 
                break 
            try: 
                grade = float(grade_input) 
                if 0 <= grade <= 100: 
                    grades.append(grade) 
                else: 
                    print("Grade must be between 0 and 100") 
            except ValueError: 
                print("Please enter a valid number") 
         
        if grades: 
            student_record = create_student_record(name, grades)
            student_record["letter_grade"] = calculate_letter_grade(student_record["average"]) 
            students.append(student_record) 
     
    # Display results 
    if students: 
        print("\n" + "="*60) 
        print("STUDENT PERFORMANCE REPORT") 
        print("="*60) 
         
        # Individual student reports 
        for student in students: 
            print(f"\nStudent: {student['name']}") 
            print(f"Grades: {student['grades']}") 
            print(f"Average: {student['average']:.1f}") 
            print(f"Letter Grade: {student['letter_grade']}") 
         
        # Class statistics 
        class_stats = analyze_class_performance(students) 
        print(f"\n{'='*30}") 
        print("CLASS STATISTICS") 
        print(f"{'='*30}") 
        print(f"Total Students: {class_stats['total_students']}") 
        print(f"Class Average: {class_stats['class_average']:.1f}") 
        print(f"Highest Average: {class_stats['highest_average']:.1f}") 
        print(f"Lowest Average: {class_stats['lowest_average']:.1f}") 
         
        # Grade distribution 
        print(f"\nGRADE DISTRIBUTION:") 
        for grade in ["A", "B", "C", "D", "F"]: 
            count = len(get_students_by_grade(students, grade)) 
            print(f"Grade {grade}: {count} students") 
 
if __name__ == "__main__": 
    main()