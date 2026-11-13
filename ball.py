from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.choice([45, 135, 225, 315]))
        self.move_speed = 10

    def move(self):
        self.forward(self.move_speed)

    def bounce_y(self):
        self.setheading(360 - self.heading())

    def bounce_x(self):
        self.setheading(180 - self.heading())

    def reset_position(self):
        self.goto(0, 0)
        
        self.setheading(random.choice([45, 135, 225, 315]))

    def increase_speed(self):
        self.move_speed += 0.5
