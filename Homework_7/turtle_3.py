import turtle

circle = turtle.Turtle()
circle.shape('turtle')

for i in range(6):
    circle.left(60)
    for j in range(1):
        circle.pendown()
        circle.circle(50)
circle.exitonclick()