from turtle import Turtle, Screen

t1 = Turtle()
t2 = Turtle()
s1 = Screen()

def move_forward():
    t1.forward(50)

def move_backwards():
    t1.backward(50)

def turn_left():
    new_heading = t1.heading() + 10
    t1.setheading(new_heading)

def turn_right():
    new_heading = t1.heading() - 10
    t1.setheading(new_heading)

def clear():
    t1.clear()
    t1.penup()
    t1.home()
    t1.pendown()

s1.listen()
s1.onkey(move_backwards, "Down")
s1.onkey(turn_left, "Left")
s1.onkey(turn_right, "Right")
s1.onkey(move_forward, "Up")
s1.onkey(clear, "c")
s1.exitonclick()