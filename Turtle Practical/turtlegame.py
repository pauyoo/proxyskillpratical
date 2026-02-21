import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Turtle Click Game")
screen.bgcolor("white")

# Player turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.speed(0)
pen.penup()

# Target turtle
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)

# Score display
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(-200, 200)

score = 0

def update_score():
    score_pen.clear()
    score_pen.write(f"Score: {score}", font=("Arial", 16, "bold"))

update_score()

def move_target():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    target.goto(x, y)

move_target()

# Single click handler (IMPORTANT FIX)
def handle_click(x, y):
    global score

    pen.goto(x, y)

    # Check distance to target
    if pen.distance(target) < 20:
        score += 1
        update_score()
        move_target()

screen.onclick(handle_click)

turtle.done()
