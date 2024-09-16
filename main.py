from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.07)

    snake.snake_move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        score.update_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_reset()
        snake.reset_snake()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_reset()
            snake.reset_snake()

screen.exitonclick()


