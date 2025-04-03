# Nicole Ling
# 04/03/2026
# P5LAB
# Use loops, functions and module import to assignments

import random


def disperse_change(amount):


    # Convert amount into an integer

    amount = int(round(amount * 100, 2))
    if amount ==0:
    
        print("No change due")

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

"""
random_owed = random code
user_amount_paid = float(input)
change_owed = (user_amount_paid - random_owed) 

    def disperse_change(change_owed):
"""

def main():
    random_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${random_owed:.2f}")
    user_amt_paid = float(input("How much cash will you put into self-checkout? $"))
    change_owed = user_amt_paid - random_owed
    print(f"Change owed: ${change_owed:.2f}")
    print()

    # Call the function to show the coins
    disperse_change(change_owed)

# Call the main
if __name__ == "__main__":
    main()