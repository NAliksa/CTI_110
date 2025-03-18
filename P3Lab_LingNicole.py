# Nicole Ling
# P3LAB
# 03/18/2025
# 

# Get the amount of money from user as float
amount = float(input(f"Enter the amount of money as a float: $"))

# Convert amount into an integer
amount = int(round(amount * 100, 2))

if amount <=0:
    print("No change")

# Determine num_dollars in amount
num_dollars = amount // 100
# Subtract num_dollars from amount
amount = amount - (num_dollars * 100)


# Determine num_quarters in amount
num_quarters = amount // 25
# Subtract num_quarters from amount
amount = amount - (num_quarters * 25)


# Determine num_dimes in amount
num_dimes = amount // 10
# Subtract num_dimes from amount
amount = amount - (num_dimes * 10)


# Determine num_nickels in amount
num_nickels = amount // 5
# Subtract num_nickels from amount
amount = amount - (num_nickels * 5)

# Determine num_pennies in amount
num_pennies = amount // 1

if num_dollars >= 1:

    if num_dollars == 1:
        print("1 Dollar")
    else:
        print(num_dollars, "Dollars")

if num_quarters >= 1:

    if num_quarters == 1:
        print("1 Quarter")
    else:
        print(num_quarters, "Quarters")

if num_dimes >= 1:

    if num_dimes == 1:
        print("1 Dime")
    else:
        print(num_dimes, "Dimes")

if num_nickels >= 1:

    if num_nickels == 1:
        print("1 Nickel")
    else:
        print(num_nickels, "Nickels")

if num_pennies >= 1:

    if num_pennies == 1:
        print("1 Penny")
    else:
        print(num_pennies, "Pennies")