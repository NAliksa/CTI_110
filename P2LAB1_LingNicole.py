# Nicole Ling
# 02/25/2025
# P2LAB1
# Display how to write code that performs mathematical calculations and displays information to users
import math

# Get formula information
radius = float(input("Enter the radius: "))
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius**2
print()

#Display results
print("What is the radius of the circle?", radius)
print()
print(f"The diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circumference: .2f}")
print()
print(f"The area of the circle is {area: .3f}")
