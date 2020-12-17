from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()
tim.shape("turtle")
colormode(255)


def rand_rgb():
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    tim.pencolor((R, G, B))
    tim.speed(50)

# TURTLE DRAWS SPIROGRAPH WITH RANDOM GENERATED RGB COLORS
for _ in range(0, 72):
    rand_rgb()
    tim.circle(100)
    tim.right(5)


screen = Screen() 
screen.exitonclick() 
