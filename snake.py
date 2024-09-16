from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle()
        t.penup()
        t.shape("square")
        t.color("white")
        t.setposition(position)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def snake_move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_location = self.segments[i - 1].position()
            self.segments[i].goto(new_location)

        self.head.forward(20)

    def reset_snake(self):
        for seg in self.segments:
            seg.setposition(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


