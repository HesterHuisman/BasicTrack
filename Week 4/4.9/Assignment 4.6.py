import turtle


def draw_poly(t, n, sz):
    for _ in range(n):
        t.forward(sz)
        angle = 360/n
        t.left(angle)


def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)


paper = turtle.Screen()

tess = turtle.Turtle()

draw_equitriangle(tess, 100)

paper.exitonclick()
