import turtle
import random
from datetime import datetime as dt

from PIL import ImageGrab
import win32gui


def step_once(t, a, b, existing_point):
    [x, y] = t.pos()
    if [x + a, y + b] not in existing_point:
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


def random_shift(step_size, shift):
    a, b = random.randint(-shift, shift), random.randint(-shift, shift)
    return a * step_size, b * step_size


def save_as_png(t, fileName):
    ts = t.getscreen()
    canvas_id = ts.getcanvas().winfo_id()  # get the handle of the canvas
    rect = win32gui.GetWindowRect(canvas_id)  # get the coordinate of the canvas
    img = ImageGrab.grab(rect)
    img.save("Patterns/" + fileName + '.png', 'png')


if __name__ == '__main__':
    t = turtle.Turtle()

    step_size = 10
    shift = step_size
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

            x_new, y_new = random_shift(step_size, shift)
            points_checked = 0
            while [x_new, y_new] in existing_point:
                x_new, y_new = random_shift(step_size, shift)
                points_checked += 1
                if points_checked > shift * 10:
                    print("shift")
                    shift += int(step_size/2)

            t.goto(x_new, y_new)
            t.pendown()
            existing_point += [[t.xcor(), t.ycor()]]
        else:
            existing_point = step_once(t, a, b, existing_point)
    t.hideturtle()
    save_as_png(t, "Walk" + dt.now().strftime("%d%m%Y%H%M%S"))
    print("Enjoy art!")
