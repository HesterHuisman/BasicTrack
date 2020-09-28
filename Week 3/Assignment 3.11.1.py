import turtle
paper = turtle.Screen()
paper.bgcolor("lightgreen")

Clock = turtle.Turtle()
Clock.shape("turtle")
Clock.color("blue")
Clock.stamp()
Clock.penup()

for i in range(12):
    Clock.right(30)
    Clock.forward(200)
    Clock.stamp()
    Clock.backward(200)

Clock.shape("square")
Clock.shapesize(0.25, 1)

for i in range(12):
    Clock.right(30)
    Clock.forward(160)
    Clock.stamp()
    Clock.backward(160)

Clock.hideturtle()

paper.exitonclick()
