import turtle as T
import random

t = T.Turtle()
t.speed(100)

colors = ["blue", "red", "green", "yellow", "black"]

def draw_tree(x):
    if(x<10):
        return
    else:
        t.color(random.choice(colors))
        t.forward(x)
        t.left(30)
        draw_tree(3.1*x/4)
        t.right(60)
        draw_tree(3.1*x/4)
        t.left(30)
        t.backward(x)


for x in range(4):
    draw_tree(110)
    t.right(90)