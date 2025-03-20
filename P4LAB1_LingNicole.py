# Nicole Ling
# P4LAB1
# March 20, 2025
# Write a turtle graphics program that draws a triangle and a square using loops

import turtle

# Create drawing window
win = turtle.Screen()
# Create turtle object
slick = turtle.Turtle()

# Set some attributes
slick.pensize(5)
slick.pencolor("light pink")
slick.shape("arrow")
win.bgcolor("black")

#TEST
# slick.forward(60)

# For loop to draw triangle
for i in (1,2,3):
    slick.forward(150)
    slick.left(120)

# While loop to draw a square
side_num =0

while side_num <= 3:
    slick.forward(150)
    slick.right(90)
    side_num += 1














# Keep windown open
win.mainloop()