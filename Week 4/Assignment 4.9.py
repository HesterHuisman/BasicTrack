import turtle


def draw_star(animal):
    for i in range(5):
        animal.forward(100)
        animal.right(144)


paper = turtle.Screen()
paper.bgcolor("black")

tess = turtle.Turtle()
tess.color("yellow")
tess.pensize(3)

draw_star(tess)

paper.exitonclick()
