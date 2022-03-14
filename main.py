from turtle import Screen, Turtle
import random

# screen setups
screen = Screen()
screen.setup(width=500, height=400)

# ask user to guess the winner
user_guess = screen.textinput(title="Turtle Race", prompt="Who do you think will win the race? Enter a color: ")

# turtle characteristics
colors = ["red", "blue", "green", "yellow", "orange", "purple"]

# create turtles
turtles = {}
for color in colors:
    turtles[color] = Turtle("turtle")


# move turtle to edge of screen
def move_turtle(all_turtles, y):
    for key, value in all_turtles.items():
        value.color(key)
        value.penup()
        value.goto(x=-230, y=y)
        y += 50


race_is_on = True


# let the race begin
def race(all_turtles, current_state):
    while current_state:
        for key, turtle in all_turtles.items():
            if turtle.xcor() > 230:
                current_state = False
                if turtle.pencolor() == user_guess:
                    print(f"Congratulations! You won the game. The winning color is {turtle.pencolor()}")
                else:
                    print(f"You lost the game :(. The winning color is {turtle.pencolor()}")
            turtle.forward(random.randint(0, 10))


move_turtle(turtles, -100)
race(turtles, race_is_on)

# exit game
screen.exitonclick()
