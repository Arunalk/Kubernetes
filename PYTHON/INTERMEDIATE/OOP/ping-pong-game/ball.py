from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.penup()

    def move_ball(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    '''
    Bounce when got in contact with up and down wall
    '''
    def bounce_y(self):
        self.y_move *= -1

    '''
    Bounce when got in contact with the paddle
    '''
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    '''
    Reset to original position when ball goes beyond the wall
    '''

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
