Angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

import turtle
paper = turtle.Screen()

Donatello = turtle.Turtle()

for i in Angles:
    Donatello.right(i)
    Donatello.forward(100)

paper.exitonclick()
