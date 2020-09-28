import turtle

paper = turtle.Screen()
donut = turtle.Turtle()

colors = ['yellow', 'hotpink', 'hotpink', 'hotpink', 'yellow', 'yellow']

donut.pensize(3)
donut.speed(100000)

# make a pink donut
for i in range(36):
    donut.left(10)
    donut.penup()
    donut.forward(10)
    donut.pendown()
    for element in range(12):
        donut.color(colors[element % len(colors)])
        donut.forward(50)
        donut.left(30)
        print(element + 5)


donut.penup()
donut.left(90)
donut.forward(60)
donut.left(90)
donut.forward(5)

donut.speed(1)

# add chocolate
donut.shape("square")
donut.shapesize(0.25, 1)
donut.color('brown')

for i in range(12):
    donut.right(30)
    donut.forward(100)
    donut.stamp()
    donut.backward(100)

donut.undo()

paper.exitonclick()
