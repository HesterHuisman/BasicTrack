import turtle

colors = ['yellow', 'hotpink', 'hotpink', 'hotpink', 'yellow', 'yellow']


def draw_donut(animal):
    """
    Draw a square
    :param animal: This should be the Turtle drawing the square
    :return: nothing
    """
    for i in range(36):
        animal.left(10)
        animal.penup()
        animal.forward(10)
        animal.pendown()
        for element in range(12):
            animal.color(colors[element % len(colors)])
            animal.forward(50)
            animal.left(30)
    animal.penup()
    animal.left(90)
    animal.forward(60)
    animal.left(90)
    animal.forward(5)
    animal.shape("square")
    animal.shapesize(0.25, 1)
    animal.color('brown')
    for i in range(12):
        animal.right(30)
        animal.forward(100)
        animal.stamp()
        animal.backward(100)
    animal.undo()


screen = turtle.Screen()
screen.bgcolor("turquoise")
donut = turtle.Turtle()

donut.pensize(3)

draw_donut(donut)


screen.exitonclick()
