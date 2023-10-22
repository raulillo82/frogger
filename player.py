from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.reset_position()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def detect_finish_line(self):
        is_finish_line = False
        if self.ycor() > FINISH_LINE_Y:
            is_finish_line = True
        return is_finish_line

