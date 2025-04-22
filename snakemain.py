import sys
import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("#2F2F2F")
screen.title("SNAKE GAME")

game_on = False

def play_game():
    screen.clear()
    screen.bgcolor("#2F2F2F")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = ScoreBoard()

    screen.listen()
    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_down, "Down")
    screen.onkey(snake.go_left, "Left")
    screen.onkey(snake.go_right, "Right")
    screen.onkey(start, "Escape")

    global game_on
    game_on = True

    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            # if the snake hits food the food is placed on other location
            food.refresh()
            snake.extend()
            score.increase_score()

        score.check_highscore()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
            # if the snake hits border then game ends
            score.reset()
            score.game_over()
            start()

        for seg in snake.segments[1:]:
            # if the snake has touched its own tail then the game ends
            if snake.head.distance(seg) < 10:
                score.reset()
                score.game_over()
                start()


def start():
    global game_on
    game_on = False
    inp = turtle.numinput("New Game", "\n1.Play New Game\n2.Reset Highscore\n3.Exit\nEnter Your Choice", minval=1, maxval=3)
    if inp == 1:
        play_game()
    elif inp == 2:
        with open("score_record.txt", mode="w") as data:
            data.write(f"0")
        start()
    else:
        sys.exit()
start()
