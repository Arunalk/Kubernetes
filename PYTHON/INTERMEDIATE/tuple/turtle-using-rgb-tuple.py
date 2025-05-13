from turtle import Turtle, Screen
import random

angles = [0, 90, 180, 270]
t1 = Turtle()
s1 = Screen()
s1.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

t1.speed("fastest")
t1.pensize(5)
for _ in range(200):
    t1.pencolor(random_color())
    t1.right(random.choice(angles))
    t1.forward(10)

s1.exitonclick()