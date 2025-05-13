from turtle import Turtle, Screen
import random

t1 = Turtle()
s1 = Screen()
s1.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

t1.speed('fastest')
def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        t1.pencolor(random_color())
        t1.circle(100)
        t1.setheading(t1.heading() + size_of_gap) # can use t1.left(5) too

draw_spirograph(1)


s1.exitonclick()