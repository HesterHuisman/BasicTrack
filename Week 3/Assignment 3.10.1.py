import turtle
paper = turtle.Screen()

Star = turtle.Turtle()

for i in range(5):
    Star.forward(200)
    Star.left(216)

Star.hideturtle()

paper.exitonclick()
