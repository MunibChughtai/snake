from turtle import Turtle #, Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")        
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.xposition = 0
        self.yposition = 0     
        self.hide_food()

    def hide_food(self):
        self.is_visible = False
        self.hideturtle()

    def randomly_show_food(self):
        if not self.is_visible and random.choice(["show","not show"]) == "show":
            self._randomly_place_food()

    def _randomly_place_food(self):        
        # self.xposition=random.choice(self.coordinate_set)
        # self.yposition=random.choice(self.coordinate_set)
        self.xposition=random.randint(-280, 280)
        self.yposition=random.randint(-280, 280)
        self.setposition(self.xposition, self.yposition)
        self.showturtle()
        self.is_visible = True
