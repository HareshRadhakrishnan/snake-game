from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
LEFT = 0
UP = 90
RIGHT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            self.segments.append(tim)
    def add_seg(self):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        self.segments.append(tim)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,0)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            Position_x = self.segments[seg - 1].xcor()
            Position_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(Position_x, Position_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    def down(self):
        if self.segments[0].heading() != UP:
             self.segments[0].setheading(DOWN)