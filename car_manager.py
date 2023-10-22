from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        if randint(1, 6) == 1:
            car = Turtle()
            car.pu()
            car.shape("square")
            car.color(choice(COLORS))
            car.setheading(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto((300, randint(-250, 250)))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -330:
                self.cars.remove(car)
                car.clear()

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
