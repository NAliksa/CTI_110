# Nicole Ling
# February 11, 2025
# P1HW2
# Create a program that does some basic math on numbers that are entered.


print("This program calculates and displays travel expenses")
print()
budget = int(input("Enter Budget: "))
print()
location = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
results = budget - gas - hotel - food
print()
print("-" * 10, "Travel Expenses", "-" * 10)
print("Location: ", location)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:", hotel)
print("Food:", food)
print()
print("Remaining Balance:", results)