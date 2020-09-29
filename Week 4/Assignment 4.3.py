import turtle


def draw_poly(t, n, sz):
    for _ in range(n):
        t.forward(sz)
        angle = 360/n
        t.left(angle)


paper = turtle.Screen()
paper.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)


draw_poly(tess, 8, 50)

paper.mainloop()
