'''This is a basic email validation system without using any module which takes email as a input and return it as valid or in case 
of invalid email it will return message for what should be correct for correct version of email.
Regards:Muhammad Hassan'''
def email_validation_system(email):
    # Initialize check
    contains_space, contains_uppercase, contains_special_char = False, False, False

    # Checking length requirement
    if len(email) < 6:
        return "Invalid Email: Too short"
    if len(email) > 320:
        return "Invalid Email: Exceeds length limit"

    # Checking if the first character is a letter
    if not email[0].isalpha():
        return "Invalid Email: Must start with a letter"

    # Checking for a single '@' symbol
    if email.count("@") != 1 or "@" not in email:
        return "Invalid Email: Must contain a single '@' symbol"

    # Checking for a valid domain extension (e.g., '.com')
    if email[-4] != "." and email[-3] != ".":
        return "Invalid Email: Invalid domain extension"

    # Counting the occurrences of '.' in the email
    dot_count = email.count(".")
    # Checking dot numbers 
    if dot_count > 2 or email.endswith("."):
        return "Invalid Email: Too many '.' characters or '.' at the end"
    # Checking if '_' is present, the count of '.' should be 1
    if "_" in email and dot_count != 1:
        return "Invalid Email: Invalid combination of '_' and '.'"
    if "-" in email and dot_count != 1:
        return "Invalid Email: Invalid combination of '-' and '.'"

    # Checking for consecutive or non-consecutive '-' '_' and '.' characters
    if "-_" in email or "--" in email or "__" in email or ".-" in email or "._" in email or "-." in email or "_." in email:
        return "Invalid Email: '-' and '_' and '.' should not come together"

    # Iterating through each character in the email to check conditions
    for char in email:
        if char.isspace():
            contains_space = True
        elif char.isalpha():
            if char.isupper():
                contains_uppercase = True
        elif char.isdigit():
            continue
        elif char in ["_", ".", "@","-"]:
            continue
        else:
            contains_special_char = True

    # Checking for space, uppercase, or special character issues
    if contains_space:
        return "Invalid Email: Contains space character"
    elif contains_uppercase:
        return "Invalid Email: Contains uppercase letter"
    elif contains_special_char:
        return "Invalid Email: Contains special character"

    # If all checks pass, the email is valid
    return "Valid Email"

def main():
    # Getting user input
    email_input = input("Enter your Email: ")

    # Validating the email
    result = email_validation_system(email_input)

    # Displaying the results
    print(result)

if __name__ == "__main__":
    main()
