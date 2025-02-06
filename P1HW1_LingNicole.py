# Nicole Ling
# February 6, 2025
# P1HW1
# Using Python's input and print functions, create a program that shows outputs

# Get data from user for exponents
print()
print("-" * 5, "Calculating Exponents", "-" * 5)
print()
first_number = int(input("Enter an integer as the base value: "))
second_number = int(input("Enter an integer as the exponent: "))
results1 = (first_number**second_number)
print()
print(first_number, "raised to the power of", second_number, "is", results1, "!!!")
print()

# Get data from user for addition and subtraction
print("-" * 5, "Addition and Subtraction", "-" * 5)
print()
first_number1 = int(input("Enter a starting integer: "))
second_number2 = int(input("Enter an integer to add: "))
third_number = int(input("Enter an integer to subtract: "))
results2 = (first_number1 + second_number2 - third_number)
print()
print(first_number1, "+", second_number2, "-", third_number, "is equal to", results2)

