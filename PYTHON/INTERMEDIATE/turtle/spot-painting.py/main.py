import colorgram
from turtle import Turtle, Screen
import random

def extract_color():
    '''
    Extract colors
    '''
    colors = colorgram.extract('./spot-image.png', 10)
    print(colors)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)
        rgb_colors.append(new_color)
    print(rgb_colors)

color_list = [(43, 17, 11), (157, 69, 45), (15, 15, 31), (29, 13, 19), (124, 38, 26), (31, 35, 135)]
t1 = Turtle()
s1 = Screen()
s1.colormode(255)
t1.setheading(225)
t1.penup()
t1.hideturtle()
t1.forward(300)
number_of_dots = 100
for i in range(1, number_of_dots + 1):
    t1.setheading(0)
    t1.dot(20, random.choice(color_list))
    t1.forward(50)
    if i % 10 == 0: 
        t1.setheading(90)
        t1.forward(50)
        t1.setheading(180)
        t1.forward(500)

s1.exitonclick()