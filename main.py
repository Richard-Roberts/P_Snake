import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake 👌")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300:
        score.reset()
        snake.reset()

    if snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        score.reset()
        snake.reset()


    snake_body = snake.segments[1:]

    for segment in snake_body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()

screen.exitonclick()
