Angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

import turtle
paper = turtle.Screen()

Donatello = turtle.Turtle()

for i in Angles:
    Donatello.right(i)
    Donatello.forward(100)

current_angle = 0
for i in Angles:
    current_angle = int(current_angle + i)

paper.exitonclick()

print(current_angle % 360)

