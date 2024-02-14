# This program allows users to draw free sketches using turtle
# Documentation: https://docs.python.org/3/library/turtle.html#turtle.textinput

from turtle import Turtle, Screen

# Create a turtle and a screen
tim = Turtle()
screen = Screen()

# Define functions to control the turtle movements
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def clock_wise():
    tim.right(10)
    tim.forward(10)

def anti_clock_wise():
    tim.left(10)
    tim.forward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Listen for key events
screen.listen()

# Associate key presses with corresponding actions
screen.onkey(move_backward, 's')
screen.onkey(move_forward, 'w')
screen.onkey(clock_wise, 'd')
screen.onkey(anti_clock_wise, 'a')
screen.onkey(clear, 'c')

# Close the program when the screen is clicked
screen.exitonclick()