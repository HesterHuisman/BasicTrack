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

tess_size = 0

for i in range(5):
    tess_size = tess_size + 20
    draw_square(tess, tess_size)
    tess.penup()
    tess.forward(tess_size + 10)
    tess.right(90)
    tess.forward(10)
    tess.right(180)
    tess.pendown()


paper.mainloop()
