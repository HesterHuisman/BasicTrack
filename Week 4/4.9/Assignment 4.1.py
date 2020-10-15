import turtle


def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)


paper = turtle.Screen()
paper.bgcolor("lightgreen")

tess = turtle.Turtle()


tess.color("hotpink")
tess.pensize(3)

for i in range(5):
    draw_square(tess, 20)
    tess.penup()
    tess.forward(40)
    tess.pendown()


paper.mainloop()
