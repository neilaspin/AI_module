import colorgram
import random
import turtle as t
from turtle import *

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)

colors = colorgram.extract('image.jpg', 40)

# print(len(colors))
rgb_colors = []
color_to_use = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

for color in rgb_colors:
    color_to_use.append(color)


# color_to_use = [(227, 238, 247), (235, 247, 242), (238, 224, 81), (205, 4, 74), (199, 164, 8), (238, 48, 132),
#                 (206, 75, 12), (109, 180, 219), (218, 161, 104), (235, 224, 4), (28, 190, 109), (11, 24, 64),
#                 (20, 107, 176), (15, 28, 178), (218, 133, 179), (7, 186, 216), (228, 167, 200), (211, 24, 151),
#                 (120, 191, 159), (7, 50, 26), (60, 21, 7), (125, 219, 234), (32, 136, 71), (192, 13, 4), (108, 88, 215),
#                 (141, 217, 202), (238, 63, 35), (69, 10, 27), (9, 98, 51), (168, 185, 229), (253, 5, 42),
#                 (238, 169, 156), (6, 86, 103), (27, 36, 245), (64, 99, 8), (253, 8, 5), (1, 245, 237)]

# def draw_circle():
#     tim.color(random.choice(color_to_use))
#     tim.dot(20)
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()
#     tim.dot()
#     # tim.up()
#     # tim.back(500)


# def move():

number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_to_use))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
