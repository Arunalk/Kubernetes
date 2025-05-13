from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.title("PING PONG GAME")
screen.setup(800,600)
screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
score = ScoreBoard()


screen.listen()
screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down,"Down")
screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down,"s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    '''
    Detects the collission of the up and down wall
    '''    

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    '''
    Detect the collission between the paddle
    '''

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    '''
    Detect when ball moves beyond the ball
    '''

    '''
    if right padddle misses
    '''
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    '''
    if right padddle misses
    '''

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick()