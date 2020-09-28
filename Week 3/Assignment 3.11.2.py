coordinates = [(135, 100), (90, 100), (45,100), (90, 141.2), (144.7, 173.7), (215.3, 141.2), (270, 100)]



import turtle
paper = turtle.Screen()

House = turtle.Turtle()

for angle, steps in coordinates:
    turtle.left(angle)
    turtle.forward(steps)

paper.exitonclick()
