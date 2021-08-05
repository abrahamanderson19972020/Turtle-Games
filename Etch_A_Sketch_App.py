from turtle import Turtle, Screen


my_turtle = Turtle()
screen = Screen()


def move_forwards():
    my_turtle.forward(10)


def move_backwards():
    my_turtle.backward(10)


def move_counter_clockwise():
    new_position = my_turtle.heading() + 10
    my_turtle.setheading(new_position)


def move_clockwise():
    new_position = my_turtle.heading() - 10
    my_turtle.setheading(new_position)


def clear_drawing():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


def main():
    screen.listen()
    screen.onkey(key="W", fun=move_forwards)
    screen.onkey(key="S", fun=move_backwards)
    screen.onkey(key="D", fun=move_clockwise)
    screen.onkey(key="A", fun=move_counter_clockwise)
    screen.onkey(key="C", fun=clear_drawing)
    screen.exitonclick()


if __name__ == "__main__":
    main()