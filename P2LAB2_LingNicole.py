# Nicole Ling
# 02/25/2025
# P2LAB2
# Write code using a dictionary to store user input and displays output to user

# Dictionaries
cars = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}

# Get keys from dictionary
cars_keys = cars.keys()

print(cars_keys)
print(*cars_keys, sep = ", ")
print()

# Get a car from user
car_name = input("Enter a car: ")
print()

# Get mpg for the given car
car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon.")
print()

# Get number of miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}?"))
print()

# Calculate gallons of gas needed to drive the specified car
gallons_needed = miles_driven/car_mpg


# Display results
print(f"{gallons_needed: .2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles.")


