#              TITLE:    Report Card Generator(RCG)
#### Video Demo: https://youtu.be/rJj5skwcmUI

#### Description:
The Report Card Generator(RCG) is a Python program that allows users to input their marks for various subjects and generates a report card with their performance accordingly. It prompts the user to enter their name, symbol number, and marks for each subject, ensuring that the marks are within the valid range of(0-100). The program then calculates the percentage and GPA based on the entered marks and displays the report card of the given individual with colorful formatting indicating green color as pass and red as failed.

## Files:
- **project.py**: This file contains the main functionality of the Report Card Generator. It includes the `main` function, which handles user input, calculates percentage and GPA, and generates the report card. Additionally, it contains helper functions for calculating percentage, GPA, and formatting the report card.
- **test_project.py**: This file contains test functions for the `calculate_percentage` and `calculate_gpa` functions in `project.py`. These tests ensure the accuracy of the calculation functions.
- **requirements.txt**: This file lists the required pip-installable libraries for the project. Since no external libraries are required, the file is empty.

## Design Choices:
- **Colorful Output**: To enhance readability and user experience, the program uses ANSI escape codes to print colorful text in the terminal. Different colors are used for headers, subject names, marks, percentage, GPA, and result (pass/fail).
- **Input Validation**: User input for marks is validated to ensure it falls within the valid range (0-100). If the user enters invalid input (non-numeric or out-of-range), they are prompted to enter the marks again.
- **Result Determination**: The program determines the overall result (pass/fail) based on the marks entered.Here,I have considered cut-off marking to be 30.Thereore, If any subject has a score below 30, the overall result is marked as fail; otherwise, it's marked as pass.

## Notes:
- Ensure that the terminal supports ANSI escape codes for colorful output.
- This project does not require any external libraries beyond Python's standard library.

Please Do Feel FREE!! to explore the code and experiment with different inputs to generate custom report cards of your OWN!

THANKYOU & NAMASTE.
# BY:
# NAME: SAUMYATA NEPAL
# GitHub: saumyata818
# edX Username: kookiee_18
# Date: 05/18/2024
