import random
from data import colors, angles
from turtle import Turtle, Screen

t1 = Turtle()
s1 = Screen()
t1.speed("fastest")
t1.pensize(10)
for _ in range(200):
    t1.color(random.choice(colors))
    t1.setheading(random.choice(angles))
    t1.forward(15)

s1.exitonclick()