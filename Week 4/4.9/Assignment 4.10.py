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

for _ in range(5):
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()
    draw_star(tess)


# if not pickup
#for _ in range(5):
    #tess.forward(350)
    #tess.right(144)
    #draw_star(tess)

paper.exitonclick()
