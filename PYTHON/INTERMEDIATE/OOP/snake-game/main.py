from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake and prey')
screen.tracer(0) 

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    '''
    Collission with the food
    '''
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.total_score()

    '''
    Detect collission with Wall
    '''
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_on = False

    '''
    Detect collission with Tail
    '''
    for seg in snake.all_turtles[1:]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            game_on = False

screen.exitonclick()