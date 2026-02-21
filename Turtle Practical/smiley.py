import turtle

pen = turtle.Turtle()
pen.speed(5)

# Face
pen.circle(100)

# Left eye
pen.penup()
pen.goto(-35, 120)
pen.pendown()
pen.circle(10)

# Right eye
pen.penup()
pen.goto(35, 120)
pen.pendown()
pen.circle(10)

# Smile
pen.penup()
pen.goto(-40, 80)
pen.setheading(-60)
pen.pendown()
pen.circle(50, 120)

turtle.done()
