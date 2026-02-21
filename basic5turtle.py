import turtle

pen = turtle.Turtle()  ## To create turtle object

# To draw a square
for i in range(4):
    pen.forward(100) # move forward
    pen.right(90) # Turn right

## Change colour
pen.color("red")
pen.circle(50) #To draw a circle

turtle.done()

