import turtle
import random
import numpy as np

# def straight(t):
#     print("straight")
#     t.forward(10)
#
#     return t
#
# def left(t):
#     print("left")
#     t.left(90)
#     t.forward(10)
#
#     return t
#
# def right(t):
#     print("right")
#     t.right(90)
#     t.forward(10)
#
#     return t
#
# #Functions
# def go_up(t, existing_point):
#     print("up")
#     [x, y] = t.pos()
#     if [x, y + 10] in existing_point:
#         print("skip")
#     else:
#         t.sety(y + 10)
#         existing_point += [[t.xcor(), t.ycor()]]
#
#     return existing_point
#
#
# def go_down(t, existing_point):
#     print("down")
#     [x, y] = t.pos()
#     if [x, y - 10] in existing_point:
#         print("skip")
#     else:
#         t.sety(y - 10)
#         existing_point += [[t.xcor(), t.ycor()]]
#
#     return existing_point
#
#
# def go_left(t, existing_point):
#     print("left")
#     [x, y] = t.pos()
#     if [x - 10, y] in existing_point:
#         print("skip")
#     else:
#         t.setx(x - 10)
#         existing_point += [[t.xcor(), t.ycor()]]
#
#     return existing_point
#
#
# def go_right(t, existing_point):
#     print("right")
#     [x, y] = t.pos()
#     if [x + 10, y] in existing_point:
#         print("skip")
#     else:
#         t.setx(x + 10)
#         existing_point += [[t.xcor(), t.ycor()]]
#
#     return existing_point


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
    while len(existing_point) < 1000:
        i = random.choice(range(4))
        a, b = 0, 0
        if i == 0:
            b = 10
        elif i == 1:
            b = -10
        elif i == 2:
            a = -10
        elif i == 3:
            a = 10

        if all([point in existing_point for point in get_adjacent_point(step_size)]):
            t.penup()
            [x, y] = t.pos()
            a, b = random.randint(-10, 10), random.randint(1, 10)
            t.goto(a*10, b*10)
            t.pendown()
            existing_point += [[t.xcor(), t.ycor()]]
        else:
            existing_point = step_once(t, a, b, existing_point)

    # for r in range(1000):
    #     i = random.choice(range(3))
    #     if i == 0:
    #         straight(t)
    #     elif i == 1:
    #         left(t)
    #     elif i == 2:
    #         right(t)
