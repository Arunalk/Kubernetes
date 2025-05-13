from turtle import Turtle, Screen

t1 = Turtle()
t1.shape('circle')
t1.color('aquamarine4', 'pink')
for i in range(4):
    t1.forward(100)
    t1.right(90)
screen = Screen()
screen.exitonclick()