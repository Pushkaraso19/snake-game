from turtle import Turtle

MOVE_DISTANCE = 20
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
        """creates the snake"""
        x = 20
        y = 0
        for i in range(3):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape("square")
            new_segment.fillcolor("white")
            new_segment.pencolor("white")
            x -= 20
            new_segment.goto(x, y)
            self.segments.append(new_segment)

    def add_segment(self, position):
        """after successful consumption of food adds a segment to the snake"""
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.fillcolor("white")
        new_segment.pencolor("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """increases the length of the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """moves the snake in forward direction by 20 pixels"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def go_up(self):
        """turns the snake to upwards direction"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        """turns the snake to downwards direction"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_right(self):
        """turns the snake to right direction"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_left(self):
        """turns the snake to left direction"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
