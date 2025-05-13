from turtle import Turtle, Screen
import random

s1 = Screen()
s1.setup(width=1000, height=700)
is_raceon = False
colors = ['blue','green','purple','grey','brown','red']
user_bet = s1.textinput(title='Turtle Race', prompt='Who do you think will win?Enter a color!!')
y_positions = [-70,-40,-10,20,50,80]

all_turtles = []
'''
Creating Turtles
and to go to position think of this as x,y coordinates. If width is 1000 divide it by half.Similarly to width
'''
for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-450, y=y_positions[turtle_index]) 
    all_turtles.append(new_turtle)

if user_bet:
    is_raceon = True

while is_raceon:
    for turtle in all_turtles:
        if turtle.xcor() > 470:
            is_raceon = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You have won. The winner is {winning_color}!!")
            else:
                print(f"sorry you've lost. The winner is {winning_color}")
            break
        random_distance = random.randint(1,10)
        turtle.forward(random_distance)

s1.exitonclick()