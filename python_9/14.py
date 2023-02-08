from random import *
a = randint(1, 100)
s = 0
while 1:
    s = int(input())
    if s < a:
        print("UP")
    elif s > a:
        print("DOWN")
    elif s == a:
        print("You are correct!!")
        break