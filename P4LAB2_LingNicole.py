# Nicole Ling
# P4LAB2
# March 20, 2025
# Write code that displays information to users using nested loops

# pseudocode
"""
run_again = "yes"
while run_again != "no":
    integer = int(input("Enter an integer: "))
    if integer >= 0:
        for i in range (1,13):
            print(f"{integer} * {i} = {integer * i}")
    else:
        print("This program does not handle negative numbers")
run_again = input(...)
print("Okay, bye bye!")

"""

# Create a variable to control the loop 
run_again = "yes"

# Create while loop to control the main logic
while run_again != "no":
    integer = int(input("Enter an integer: "))
    if integer >= 0:
        for i in range (1,13):
            print(f"{integer} * {i} = {integer * i}")
    else:
        print("Sorry, this program does not handle negative numbers")
    
    run_again = input("Would you like to run the program again? ")

# While loop ends here
print("Okay, bye bye!")