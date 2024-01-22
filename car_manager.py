import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

        self.all_cars = []
        self.move = STARTING_MOVE_DISTANCE

    def release_the_cars(self):
        create_car = True if random.randint(1, 6) == 1 else False
        if create_car:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(None, 2)
            y_cord = random.randint(-250, 250)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, y_cord)
            self.all_cars.append(new_car)

    def start_move(self):
        for car in self.all_cars:
            car.forward(self.move)

    def move_inc(self):
        self.move += MOVE_INCREMENT
