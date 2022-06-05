from turtle import Screen, write
from snake import Snake
from food import Food
import time
from score_board import ScoreBoard
# from PIL import Image

def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=590)
    
    screen.bgpic('bg1.gif')
    #screen.bgpic('snake_bg.gif')
    
    screen.title("My Snake Game")
    screen.bgcolor("black")
    screen.tracer(0)
    return screen

def close_screen_on_click(screen):
    screen.exitonclick()

def register_screen_events(screen, snake):
    screen.listen()            
    screen.onkey(fun=snake.turn_right, key="Right")
    screen.onkey(fun=snake.turn_left, key="Left")
    screen.onkey(fun=snake.turn_up, key="Up")
    screen.onkey(fun=snake.turn_down, key="Down")

def start_game():
    screen = setup_screen()
    food = Food()
    snake = Snake()
    score_board = ScoreBoard()

    screen.update()
    register_screen_events(screen, snake)
    continue_playing = True
    
    while continue_playing:
        snake.move_snake_forward(food, score_board)
        #print(snake.snake[0].position())
        screen.update()
        if snake.has_snake_collided_with_walls(300, 300):
            continue_playing = False
            score_board.game_over()
        if snake.has_snake_collided_with_body():
            continue_playing = False
            score_board.game_over()
        time.sleep(0.15)        
        food.randomly_show_food()
        #print(f"food: {food.xposition}, {food.yposition}")
    close_screen_on_click(screen)

start_game()