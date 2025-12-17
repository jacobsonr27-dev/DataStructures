import turtle
# You can name your turtle whatever you like
# by replacing yertle with another name everywhere in the program.
# Command-F (find and replace) is helpful for that
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("green")
screen.title("Image Turtle Example")

image = "drake.gif"
screen.register_shape(image)

yertle = turtle.Turtle()
yertle.getscreen().setup(1000, 800)
yertle.speed(3) # This number can be anywhere between 1 and 10
yertle.shape(image)
yertle.up()


image2 = "stefon.gif"
screen.register_shape(image2)

yertle2 = turtle.Turtle()
yertle2.getscreen().setup(1000, 800)
yertle2.speed(3) # This number can be anywhere between 1 and 10
yertle2.shape(image2)
yertle2.up()
yertle2.setposition(0,400)
image3 = "treyveyon.gif"
screen.register_shape(image3)

yertle3 = turtle.Turtle()
yertle3.getscreen().setup(1000, 1000)
yertle3.speed(3) # This number can be anywhere between 1 and 10
yertle3.shape(image3)
yertle3.up()
yertle3.setposition(-400,0)

image4 = "tom.gif"
screen.register_shape(image4)

yertle4 = turtle.Turtle()
yertle4.getscreen().setup(1000, 1000)
yertle4.speed(3) # This number can be anywhere between 1 and 10
yertle4.shape(image4)
yertle4.up()
yertle4.setposition(-800,0)

yertle4.setposition(-100,0)

yertle4.setposition(-800,0)



turtle.done()
yertle.setposition(0,0)

yertle.down()
yertle.goto()