from turtle import Turtle, Screen, colormode
from random import randint, choice

tim = Turtle()
tim.shape("turtle")
colormode(255)

#RANDOK COLOR
def rgb():
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    tim.pencolor((R, G, B))
    tim.speed(10)
    tim.pensize(10)


def turn():
    tim.forward(30)
    t = [0, 90, 180, 270]
    tim.right(choice(t))


#RANDOM TURTLE WALK
def random_walk():
    rgb()
    turn()


for _ in range(500):
    random_walk()


screen = Screen()
screen.exitonclick() 
