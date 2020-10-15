import turtle


def draw_square_4(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)
    animal.right(90)


paper = turtle.Screen()
paper.bgcolor("lightgreen")


tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

for j in range(5):
    for i in range(4):
        draw_square_4(tess, 100)
    tess.right(72)

paper.exitonclick()
