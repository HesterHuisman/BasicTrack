import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(5):
    leonardo.left(10)
    leonardo.penup()
    leonardo.forward(10)
    leonardo.pendown()
    for element in range(12):
        leonardo.color(colors[element % len(colors)])
        leonardo.forward(50)
        leonardo.left(30)
        print(element + 5)

paper.exitonclick()