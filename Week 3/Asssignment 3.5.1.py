import turtle

paper = turtle.Screen()
Raphael = turtle.Turtle()

# triangle
for element in range(3):
    Raphael.forward(100)
    Raphael.left(120)

# square
for element in range(4):
    Raphael.forward(100)
    Raphael.left(90)

# hexagon
for element in range(6):
    Raphael.forward(100)
    Raphael.left(60)

# octagon
for element in range(8):
    Raphael.forward(100)
    Raphael.left(45)

paper.exitonclick()

