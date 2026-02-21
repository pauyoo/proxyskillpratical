import turtle

pen = turtle.Turtle()
pen.speed(10)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(36):
    pen.color(colors[i % 6])
    for j in range(4):
        pen.forward(100)
        pen.right(90)
    pen.right(10)

turtle.done()

