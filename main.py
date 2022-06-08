import turtle
import random


def step_once(t, a, b, existing_point):
    print("right")
    [x, y] = t.pos()
    if [x + a, y + b] in existing_point:
        print("skip")
    else:
        t.setx(x + a)
        t.sety(y + b)
        existing_point += [[t.xcor(), t.ycor()]]

    return existing_point


def get_adjacent_point(step_size):
    adj_points = []
    [x, y] = t.pos()
    for step in [-step_size, step_size]:
        adj_points += [[x + step, y]]
        adj_points += [[x, y + step]]
    return adj_points


if __name__ == '__main__':
    t = turtle.Turtle()

    step_size = 10
    existing_point = [[t.xcor(), t.ycor()]]
    while len(existing_point) < 10000:
        i = random.choice(range(4))
        a, b = 0, 0
        if i == 0:
            b = step_size
        elif i == 1:
            b = -step_size
        elif i == 2:
            a = -step_size
        elif i == 3:
            a = step_size

        if all([point in existing_point for point in get_adjacent_point(step_size)]):
            t.penup()
            [x, y] = t.pos()
            a, b = random.randint(-10, 10), random.randint(-10, 10)
            t.goto(a*step_size, b*step_size)
            t.pendown()
            existing_point += [[t.xcor(), t.ycor()]]
        else:
            existing_point = step_once(t, a, b, existing_point)
    t.penup()
    print("Enjoy art!")
