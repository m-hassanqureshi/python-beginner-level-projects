def validate_input(value, min_value, max_value, error_message):
    try:
        value = int(value)
        if not (min_value <= value <= max_value):
            raise ValueError(error_message)
        return value


    except ValueError as e:
        print(f"Invalid input: {e}")
        exit(1)

def input_student_marks(num_students):
    marks = [None] * num_students

    for i in range(num_students):
        j = i + 1
        try:
            marks[i] = validate_input(
                input(f"Enter marks of Student No. {j}:"),
                0,
                100,
                "Marks should be between 0 and 100."
            )
        except SystemExit:
            exit(1)

    return marks

def count_pass_fail(marks, passing_mark):
    pass_count = 0

    fail_count = 0

    for mark in marks:
        if mark >= passing_mark:
            pass_count += 1
        else:
            fail_count += 1

    return pass_count, fail_count

def calculate_average(marks):
    if not marks:
        return 0  # Avoid division by zero error

    total_marks = sum(marks)
    average = total_marks / len(marks)
    return average

def print_marks_above_average(marks, average):
    print("Marks Above Average are:")
    for mark in marks:
        if mark > average:
            print(mark, end=", ")
    print("\n")

def print_marks_below_average(marks, average):
    print(f"Students who are below the average marks ({average}) are given below:\n")
    print("Marks", " ", "Status")
    print("-------------------")

    for mark in marks:
        if mark < average:
            print(mark, "    ", "Below Average")

def analyze_pass_fail(marks, passing_mark):
    pass_count, fail_count = count_pass_fail(marks, passing_mark)
    average_marks = calculate_average(marks)

    print("\n\nStudents who have secured {0} percent marks or more are given below:\n".format(passing_mark))
    print("Marks", " ", "Status")
    print("-------------------")

    for mark in marks:
        if mark >= passing_mark:
            print(mark, "    ", "Pass")

    print("\nNumber of students who passed:", pass_count)

    print("The average marks of pass students is: {0}\n".format(average_marks))

    print_marks_above_average(marks, average_marks)

    print_marks_below_average(marks, average_marks)

    print("\nNumber of students who failed:", fail_count)

def main():
    num_students = validate_input(input("Enter Number of Students in your class:"), 1, float('inf'), "Number of students should be a positive integer.")
    
    passing_mark = validate_input(input("Enter passing marks percentage out of 100:"), 0, 100, "Passing percentage should be between 0 and 100.")
    
    marks = input_student_marks(num_students)

    analyze_pass_fail(marks, passing_mark)

if __name__ == "__main__":
    main()
