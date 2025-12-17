import turtle

# Set up the screen
screen = turtle.Screen()

# 1. Register the image file (must be a .gif)
image = "drake.gif"
screen.register_shape(image)

# 2. Assign the image to the turtle
t = turtle.Turtle()
t.shape(image)

# Test movement
t.forward(100)

screen.mainloop()
