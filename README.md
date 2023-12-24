# Python Beginner Level Projects

This repository contains my python beginner level projects from basic to slightly advance version .Here is complete info of all the projects and I will be furthur adding projects here .

# Python Beginners Projects

## Project: Email Validation System

### Overview

Email Validation System is a basic email validation script implemented in Python without using external modules. The script checks various criteria to determine the validity of an email address. If the provided email is invalid, it returns a message indicating what aspects need correction for a valid email.

**Author: Muhammad Hassan Qureshi**

**Code Link :** [Email Verification System](https://github.com/m-hassanqureshi/python-beginner-level-projects/blob/main/email-validation-system.py)
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


