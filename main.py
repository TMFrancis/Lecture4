# Lecture 4
# September 1, 2021
# Turtle library

import turtle

turtle.color("black", "red")
turtle.begin_fill()             #start process
turtle.circle(75)               #
turtle.end_fill()


def draw_square(t, sz):
    for i in range(6):
        t.forward(sz)
        t.left(60)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()
draw_square(alex, 100)
wn.mainloop()


