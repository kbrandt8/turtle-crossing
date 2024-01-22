import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.onkey(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car_manager.release_the_cars()
    car_manager.start_move()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 250:
        player.start_pos()
        car_manager.move_inc()
        scoreboard.level_up()

    screen.update()
screen.exitonclick()
