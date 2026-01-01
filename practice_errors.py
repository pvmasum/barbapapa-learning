# practice_errors.py
# -------------------
# Demonstrates basic error handling using try/except in Python

try:
    # Get user input and convert to integer
    number = int(input("Enter your number: "))

    # Perform a calculation that may fail
    result = 10 / number
    print("Result:", result)

except ValueError:
    # Handles non-numeric input
    print("Error: Input must be an integer.")

except ZeroDivisionError:
    # Handles division by zero
    print("Error: Division by zero is not allowed.")

except Exception as error:
    # Catches any unexpected errors
    print("Unexpected error:", error)