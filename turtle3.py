from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()
tim.shape("turtle")
colormode(255)

def rgb():
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    tim.pencolor(R, G, B)


# TURTLE DRAWING SHAPES WITH RANDOM GENERATED RGB COLORS
for shape in range(3, 11):
    rgb()
    tim.forward(100)
    for side in range(shape - 1):
        tim.right(360/shape)
        tim.forward(100)
    tim.right(360 / shape)



screen = Screen() 
screen.exitonclick() 
