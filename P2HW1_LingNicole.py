# Nicole Ling
# 02/27/2025
# P2HW1
# Edit and enhance existing programs


print("This program calculates and displays travel expenses")
print()
budget = int(input("Enter budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()
print("-"* 12, "Travel Expenses", "-" * 12)
print("Location:", "  "*5, destination)
print(f'Initial Budget:      ${budget:,.2f}')
print(f'Fuel:                ${gas:.2f}')
print(f'Accomodation:        ${hotel:.2f}')
print(f'Food:                ${food:.2f}')
print("-"*45)
print()
print(f'Remaining Balance:   ${budget - gas - hotel - food:.2f}')