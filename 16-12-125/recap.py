# Grade Calculator & Menu System
score = int(input("Enter your score (0-100): "))

# CONDITIONAL STATEMENTS (if, elif, else)
if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# NESTED CONDITIONALS
if grade in ["A+", "A"]:
    if score >= 95:
        print("Excellent! Top performer!")
    else:
        print("Great job!")
else:
    print("Keep studying!")

# LOOP STATEMENTS with CONTROLS
print("\n=== Improvement Menu ===")
options = ["1. Retry score", "2. View tips", "3. Exit"]

while True:  # WHILE LOOP
    # FOR LOOP to display menu
    for option in options:
        print(option)
    
    choice = input("Enter choice (1-3): ")
    
    # CONTROL STATEMENTS inside loop
    if choice == "1":
        new_score = int(input("Enter new score: "))
        if new_score > score:
            print("Improved!")
            score = new_score
        continue  # Skip to next iteration (back to menu)
    
    elif choice == "2":
        tips = ["Study daily", "Practice problems", "Ask doubts"]
        for i, tip in enumerate(tips, 1):
            print(f"{i}. {tip}")
        input("Press Enter to continue...")
        pass  # Placeholder 
    
    elif choice == "3":
        print("Thank you! Goodbye.")
        break  # Exit the loop completely
    
    else:
        print("Invalid choice!")
        continue  # Skip rest and show menu again
