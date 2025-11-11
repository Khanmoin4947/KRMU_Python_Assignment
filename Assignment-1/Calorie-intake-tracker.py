# Author: Moin Khan
# Reg no. :2501730052
# Course: Ai/ML
# Title: Analyzing and Reporting Student Grades# Task 1: Welcome Message

print("Welcome to Daily Calorie Tracker!")
print("This tool helps you record your meals, calculate total calories compare with your daily limit, and optionally save your session")


meals = []
calories = []

num_meals = int(input("How many meals did you have today? "))
for i in range(num_meals):
    print(f"\nEnter details for meal {i + 1}:")
    meal_name = str(input("Meal name: "))
    calorie_amount = float(input("Calories (in kcal): "))
    meals.append(meal_name)
    calories.append(calorie_amount)

total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))


if total_calories > daily_limit:
    status_message = " You have exceeded your daily calorie limit!"
else:
    status_message = " You are within your daily calorie limit."


print("\n----------- DAILY SUMMARY REPORT -----------\n")
print("Meal Name            Calories")
print("--------------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]}              {calories[i]}")

print("--------------------------------------------")
print(f"Total:               {total_calories}")
print(f"Average:             {average_calories}")
print(f"Status:              {status_message}")
print("--------------------------------------------")