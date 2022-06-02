from turtle import Turtle
from score_board import ScoreBoard
from food import Food

class Snake:
    def __init__(self):
        self.snake=[]
        self.snake_length=0
        for x in range(3):  
            self.snake.append(Turtle(shape="square"))            
            self.snake[x].penup()
            self.snake[x].color("green")
            self.snake[x].setposition(-20 * self.snake_length,0)
            self.snake_length += 1
        self.snake[1].color("white")
        self.new_position=0
        self.snake_head = self.snake[0]
    
    def _has_snake_collided_with_left_right_walls(self, width, height):
        if self.snake[0].position()[0] >= 285 or self.snake[0].position()[0] <= -285:
            print("collision happened with left right walls")
            return True            
        else:
            return False

    def _has_snake_collided_with_top_bottom_walls(self, width, height):
        if self.snake[0].position()[1] >= 285 or self.snake[0].position()[1] <= -285:
            print("collision happened with top down walls")
            return True
        else:
            return False

    def _add_new_tail(self, snake_tail_coordinates):
        self.snake.append(Turtle(shape="square"))
        
        self.snake_length += 1
        self.snake[self.snake_length - 1].penup()
        if self.snake_length%2 != 0:
            self.snake[self.snake_length - 1].color("green")
        else:
            self.snake[self.snake_length - 1].color("white")

        self.snake[self.snake_length - 1].setposition(snake_tail_coordinates)
        #self.snake[self.snake_length - 1].color('blue')    

    def _move_snake_head_ahead(self):
        self.snake_head.forward(20)
        self.snake_head.setposition(round(self.snake_head.position()[0]), round(self.snake_head.position()[1]))
        
    def _has_snake_eaten_food(self, food):        
        return food.is_visible and self.snake_head.distance(food) < 15

    def _expand_snake(self):
        self._add_new_tail(self.new_position)
    #================================================== Public ===========================================
    def has_snake_collided_with_body(self):
        for snake_body_part in self.snake:
            if snake_body_part != self.snake_head and self.snake_head.distance(snake_body_part)<10:
            #self.snake_head.position() == snake_body_part.position():
                print("snake collided with body")
                return True
        return False

    def has_snake_collided_with_walls(self, width, height):        
        is_right_left_wall_collision = self._has_snake_collided_with_left_right_walls(width, height)
        is_top_bottom_wall_collision = self._has_snake_collided_with_top_bottom_walls(width, height)
        return is_right_left_wall_collision or is_top_bottom_wall_collision

    def move_snake_forward(self, food, score_board):        
        for snake_body_part in self.snake:
            if snake_body_part == self.snake_head:
                self.new_position = snake_body_part.position()
                self._move_snake_head_ahead()
            else:
                old_position = snake_body_part.position()
                snake_body_part.setposition(self.new_position)
                self.new_position = old_position
        
        if self._has_snake_eaten_food(food):
            food.hide_food()
            score_board.update_score()
            self._expand_snake()
    #================================================ Events ==============================================
    def turn_right(self):
        print("Entered right function")
        if self.snake[0].heading()==90 or self.snake[0].heading()==270:
            self.snake[0].setheading(0)
    
    def turn_left(self):
        print("Entered left function")
        if self.snake[0].heading()==90 or self.snake[0].heading()==270:
            self.snake[0].setheading(180)

    def turn_up(self):
        print("Entered up function")
        if self.snake[0].heading()==0 or self.snake[0].heading()==180:
            self.snake[0].setheading(90)

    def turn_down(self):
        print("Entered down function")
        if self.snake[0].heading()==0 or self.snake[0].heading()==180:
            self.snake[0].setheading(270)