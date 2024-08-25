from turtle import Turtle
import random

COLORS = ["blue", "red", "cyan", "green", "yellow", "brown", "pink", "purple", "orange"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # From 20x20 to 10x10
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
