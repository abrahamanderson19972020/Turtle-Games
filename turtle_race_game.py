from turtle import Turtle, Screen
import random


colors =["red", "yellow", "green", "brown", "purple", "blue","orange"]
y_coordinates = [-150, -100, -50, 0 , 50, 100, 150]
screen = Screen()
screen.setup(width=500, height=500)
user_input = screen.textinput(title="Make Your Bet>>>", prompt="Which Turtle Win the Race>>>Choose a Color:")

turtles = list()
for i in range(7):
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(colors[i])
    my_turtle.penup()
    my_turtle.goto(x=-240, y=y_coordinates[i])
    turtles.append(my_turtle)


if user_input:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"Congratulations. The {winning_color} turtle is the winner of the race...")
            else:
                print(f"You have lost the race. The {winning_color} turtle is the winner of the race...")
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)
screen.exitonclick()




