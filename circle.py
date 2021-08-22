import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.width(1)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# for _ in range(59):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.left(6)
#     tim.circle(100)
def draw_spirograph(shift_amount):
    for _ in range(int(360 / shift_amount)):
        tim.color(random_color())
        tim.circle(100)
        tim.left(shift_amount)
        tim.circle

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()