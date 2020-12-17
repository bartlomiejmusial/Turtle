from turtle import *

# DRAW SQUARE
# tim = Turtle()
# tim.shape("turtle")
# tim.color("DeepPink")
# for side in range(4):
#     tim.forward(200)
#     tim.right(90)

color('MidnightBlue', 'gold1')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
