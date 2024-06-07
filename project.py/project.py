import os

# Define ANSI escape codes for colors
YELLOW = '\033[93m'
GREEN = '\033[92m'
BLUE = '\033[94m'
WHITE = '\033[97m'
CYAN = '\033[96m'
RED = '\033[91m'
RESET = '\033[0m'

def main():
    # Prompt the user to enter their name and symbol number
    name = input("Enter your name: ")
    symbol_no = input("Enter your symbol number: ")

    # Prompt the user to enter marks for each subject
    subject_marks = {}
    subjects = ['Mathematics', 'Science', 'English', 'Computer', 'Literature']  # Example subjects
    for subject in subjects:
        while True:
            try:
                marks = float(input(f"Enter marks for {subject} (0-100): "))
                if marks < 0 or marks > 100:
                    print("Marks should be between 0 and 100. Please try again.")
                else:
                    subject_marks[subject] = marks
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    # Calculate percentage
    percentage = calculate_percentage(subject_marks)

    # Calculate GPA
    gpa = calculate_gpa(percentage)

    # Determine result
    result = "Pass" if all(mark > 30 for mark in subject_marks.values()) else "Fail"

    # Generate and display report card
    generate_report_card(name, symbol_no, subject_marks, percentage, gpa, result)

def calculate_percentage(subject_marks):
    total_marks = sum(subject_marks.values())
    total_subjects = len(subject_marks)
    return (total_marks / (total_subjects * 100)) * 100

def calculate_gpa(percentage):
    if percentage >= 90:
        return 4.0
    elif percentage >= 80:
        return 3.5
    elif percentage >= 70:
        return 3.0
    elif percentage >= 60:
        return 2.5
    elif percentage >= 50:
        return 2.0
    elif percentage >= 40:
        return 1.5
    else:
        return 0.0

def generate_report_card(name, symbol_no, subject_marks, percentage, gpa, result):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

    # Print report card header
    print(f"{YELLOW}+-------------------------------+{RESET}")
    print(f"{YELLOW}|       REPORT CARD             |{RESET}")
    print(f"{YELLOW}+-------------------------------+{RESET}")
    print(f"{CYAN}| Name: {name:<24}|{RESET}")
    print(f"{CYAN}| Symbol No: {symbol_no:<16}   |{RESET}")
    print(f"{YELLOW}+-------------------------------+{RESET}")
    print(f"{GREEN}|  Subjects        |    Marks   |{RESET}")
    print(f"{BLUE}+------------------+-------------+{RESET}")

    # Print subject marks
    for subject, marks in subject_marks.items():
        subject_color = RED if marks < 30 else WHITE
        print(f"{subject_color}| {subject:<16} | {marks:<9}  |{RESET}")

    # Print percentage and GPA
    print(f"{BLUE}+------------------+-------------+{RESET}")
    print(f"{CYAN}| Percentage       | {percentage:.2f}%     |{RESET}")
    print(f"{CYAN}| GPA              | {gpa:.2f}       |{RESET}")
    print(f"{YELLOW}+-------------------------------+{RESET}")

    # Print result
    result_color = GREEN if result == "Pass" else RED
    print(f"{result_color}Result: {result}{RESET}")

if __name__ == "__main__":
    main()
