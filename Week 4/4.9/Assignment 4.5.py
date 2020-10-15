import turtle


def spiral(animal, size):
    for i in range(62):
        size = size + 5
        animal.backward(size)
        animal.right(90)


paper = turtle.Screen()
paper.bgcolor("lightgreen")


tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)


spiral(tess, 0)

tess.penup()
tess.right(180)
tess.forward(600)
tess.right(90)
tess.forward(130)
tess.pendown()

def turn_spiral(animal, size):
    for i in range(60):
        size = size + 5
        animal.backward(size)
        animal.right(92)

turn_spiral(tess, 0)


paper.exitonclick()
