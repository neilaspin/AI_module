
# import turtle
# import random
#
# x = turtle.Turtle()
# x.speed(100)
# turtle.bgcolor("black")
# turtle.colormode(255)
# turtle.hideturtle()
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# for y in range(24000000):
#     x.color(random_color())
#     x.circle(y)
#     x.left(5)
# turtle(done)

import turtle
import random

x = turtle.Turtle()
x.speed(100)
turtle.bgcolor("black")
turtle.colormode(255)
turtle.hideturtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for y in range(240000000):
    x.color(random_color())
    x.circle(y)
    x.left(5)
turtle(done)

