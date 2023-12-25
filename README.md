# Python Beginner Level Projects

This repository contains my python beginner level projects from basic to slightly advance version .Here is complete info of all the projects and I will be furthur adding projects here .


## Project No 1: Email Validation System

### Overview

Email Validation System is a basic email validation script implemented in Python without using external modules. The script checks various criteria to determine the validity of an email address. If the provided email is invalid, it returns a message indicating what aspects need correction for a valid email.

**Author: Muhammad Hassan Qureshi**

**Code Link :** [Email Validation System](https://github.com/m-hassanqureshi/python-beginner-level-projects/blob/main/email-validation-system.py)
### Features

- Length requirement check
- First character is a letter
- Single '@' symbol requirement
- Valid domain extension (e.g., '.com')
- Presence of '.', '_', and '-' characters
- Consecutive or non-consecutive occurrences of '-', '_', and '.' characters
- No space, uppercase letters, or special characters allowed

### Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/m-hassanqureshi/python-beginner-level-projects.git
    cd python-beginner-level-projects
    ```

2. **Run the Script:**
    ```bash
    python email-validation-system.py
    ```

3. **Enter your email address when prompted.**

4. **View the validation result.**

### Code Explanation

The `email_validation_system` function in the script performs a series of checks to determine the validity of an email address. It returns specific error messages if any of the criteria are not met. If all checks pass, it indicates that the email is valid.

### Example

```python
from email_validation_system.py import email_validation_system

# Getting user input
email_input = input("Enter your Email: ")

# Validating the email
result = email_validation_system(email_input)

# Displaying the results
print(result)
```

# Project No.2: Student Marks Analyzer

## Overview

The Student Marks Analyzer is a Python program designed to take input for student marks, analyze pass/fail status, calculate the average, and provide additional information based on the entered data.

### Author

Muhammad Hassan Qureshi

Code Link : [Student Marks Analyzer](https://github.com/m-hassanqureshi/python-beginner-level-projects/blob/main/student_marks_analyzer.py)

## Features

- Input validation for positive integers and percentages
- Marks entry for multiple students
- Counting and displaying the number of passing and failing students
- Calculation of average marks
- Displaying marks above and below the average

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/m-hassanquresi/python-beginner-level-projects.git
    python-beginner-level-projects
    ```

2. **Run the Script:**
    ```bash
    python student_marks_analyzer.py
    ```

3. **Enter the number of students and passing marks percentage when prompted.**

4. **Input the marks for each student as requested.**

5. **View the analysis results.**

## Code Explanation

The program consists of several functions that perform the following tasks:

- **`validate_input`**: Validates user input for positive integers within a specified range.
- **`input_student_marks`**: Takes input for the marks of each student based on the number of students.
- **`count_pass_fail`**: Counts the number of passing and failing students.
- **`calculate_average`**: Calculates the average marks.
- **`print_marks_above_average`**: Displays marks above the calculated average.
- **`print_marks_below_average`**: Displays marks below the calculated average.
- **`analyze_pass_fail`**: Analyzes pass/fail status, calculates the average, and prints the results.

## Example

```python
from student_marks_analyzer import main

# Run the program
main()
```

