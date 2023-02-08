import turtle
import random

i = 1
t = turtle.Turtle('turtle')
while i <= 30:
    dist = random.randint(1, 100)
    ang = random.randint(-180, 180)
    t.forward(dist)
    t.right(ang)
    i += 1