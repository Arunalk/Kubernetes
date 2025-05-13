import turtle
import tkinter as TK
'''
Creating an object => module.ClassName
'''
new_object = turtle.Turtle() 
print(new_object)

'''
Another way of using Turtle Class --> https://docs.python.org/3/library/turtle.html#turtle.shape
'''
from turtle import Turtle, Screen

turtle_screen = Turtle()
screen = Screen()
print(turtle_screen)
turtle_screen.shape("turtle")
turtle_screen.color("coral")
turtle_screen.forward(100)
screen.exitonclick()