Drunk_Pirate = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

import turtle
paper = turtle.Screen()

Pirate = turtle.Turtle()

for angle, steps in Drunk_Pirate:
    Pirate.left(angle)
    Pirate.forward(steps)

paper.exitonclick()
