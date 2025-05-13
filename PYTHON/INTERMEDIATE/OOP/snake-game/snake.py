from turtle import Turtle 
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.all_turtles = []
        self.createsnake()
        self.head = self.all_turtles[0]
        
    def createsnake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
    
    def add_segment(self, pos):
        t1 = Turtle(shape='square')
        t1.color('white')
        t1.penup()
        t1.goto(pos)
        self.all_turtles.append(t1)

    def extend(self):
        self.add_segment(pos = self.all_turtles[-1].position())

    def move(self):
        for seg in range(len(self.all_turtles) - 1,0,-1):
            new_x = self.all_turtles[seg - 1].xcor()
            new_y = self.all_turtles[seg - 1].ycor()
            self.all_turtles[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.all_turtles[0].clear()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)