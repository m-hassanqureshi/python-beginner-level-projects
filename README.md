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
from email_validation_system import email_validation_system

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
# Project No.3 : QR Code Generation Project

This Python project focuses on QR code generation using the `qrcode` library, providing both a simple QR code creation and a more advanced option with customizable features.
### Author

Muhammad Hassan Qureshi

Code Link : [QR Code Generator](https://github.com/m-hassanqureshi/python-beginner-level-projects/blob/main/qr-code-generator.py)


## Overview

The project consists of two main parts:

### 1. Simple QR Code Creation

In this part of the project, a basic QR code is generated with the URL "https://github.com/m-hassanqureshi". The resulting image is saved as "simple.png".

### 2. Advance QR Code Creation
The project also explores advanced QR code generation with specific options. Here, the script configures the QR code to have a version of 1, use H error correction, set a box size of 10, and include a border of size 1. The data for the QR code remains the same as in the simple example ("https://github.com/m-hassanqureshi"). The resulting QR code is generated, and additional styling is applied, such as a green fill color and a white background. The final image is saved as "advanced_qr.png".

# Project No.4 : Password Generator

This Python script generates a random password using a combination of uppercase and lowercase letters, digits, and special characters.

## Overview

The Random Password Generator is a simple Python script designed to create secure and random passwords. It utilizes a mix of uppercase and lowercase letters, digits, and special characters to enhance the strength of the generated password.

Code Link : [Password Generator](https://github.com/m-hassanqureshi/python-beginner-level-projects/blob/main/password-generator.py)

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
  ```
      python generate_password.py
   ```

2.Enter the Desired Length:

- When prompted, enter the desired length for the generated password.

3.View the Generated Password:

- The script will generate a random password based on your specified length.
The generated password will be displayed in the console.

4.Customization (Optional):

- You can customize the script to suit your password requirements by modifying the character sets and length within the script itself.

Feel free to use and adapt this script for your password generation needs. Adjust the length and character sets as necessary.

# Project No.4 : Employee Management System

## Description
This project is an Employee Management System implemented in Python using SQLite as the database backend. It allows users to manage departments, employees, and salary grades through a command-line interface.

## Features
- Add, search, delete, list, and edit departments
- Add, search, delete, list, and edit employees
- Order employees by employee number
- Add, search, delete, list, and edit salary grades
 ### Author : Hassan Qureshi
 ---------

  Code link : [Employ Management System](https://github.com/m-hassanqureshi/python-beginner-level-projects/blob/main/employ_management_system.py)


