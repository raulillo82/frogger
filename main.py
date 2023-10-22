import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #Create a new car every few steps
    cars.add_car()
    #Move all cars
    cars.move()
    #Detect collision and abort the game
    for car in cars.cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            score.game_over()
    #Detect the top edge
    if turtle.detect_finish_line():
        turtle.reset_position()
        #Increase level
        score.increase_score()
        #Increase cars speed
        cars.increase_speed()


screen.exitonclick()
