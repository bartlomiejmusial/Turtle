from turtle import Turtle, Screen


# DRAW SQUARE
tim = Turtle()
tim.shape("turtle")
tim.color("DeepPink")
for side in range(4):
    tim.forward(200)
    tim.right(90)

    
screen = Screen() 
screen.exitonclick()
