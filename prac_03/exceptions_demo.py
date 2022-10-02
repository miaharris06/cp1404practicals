"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A: When a non-integer is inputted by the user
2. When will a ZeroDivisionError occur?
A: When a user enters 0 for the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
A:
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")