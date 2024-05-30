from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score_Board
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake game")
screen.tracer(0)
score_board = Score_Board()
score_board.show_score()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Left")
screen.onkey(snake.left, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        score_board.refresh_score()
        snake.add_seg()
        food.re_feed()
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        score_board.reset()
        snake.reset()
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            snake.reset()
            score_board.reset()

screen.exitonclick()
