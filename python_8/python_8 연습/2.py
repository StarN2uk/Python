from random import *
import turtle
t = turtle.Turtle()
t.pendown()
t.shape('turtle')
t.write('0')
t.goto(150, 0)
t.write('150')
t.goto(300, 0)
t.color('sky blue')
t.begin_fill()
t.forward(75)
t.setheading(90)
t.forward(75)
t.setheading(180)
t.forward(75)
t.setheading(270)
t.forward(75)
t.end_fill()
t.penup()
t.goto(375, 75)
t.pendown()
t.color('blue')
t.begin_fill()
t.setheading(120)
t.forward(75)
t.setheading(240)
t.forward(75)
t.end_fill()
t.penup()
t.goto(300, 0)
t.write('400')
t.home()
list = ["flower", "fruit", "animal"]
flower = ["rose", "lily", "sunflower", "iris", "clover", "daisy", "lilac", "mint", "ivy"]
fruit = ["apple", "banana", "strawberry", "watermelon", "mandarin", "peach", "grapes", "orange", "pear", "kiwi"]
animal = ["bear", "rabbit", "cat", "dog", "monkey", "fox", "wolf", "lion", "tiger", "mouse"]
score = 0
n = randint(5, 10)
for i in range(n):
    k = choice(list)
    if k == 'flower':
        m = choice(flower)
        word = turtle.textinput("flower", "%s(%d/%d)" % (m, i + 1, n))
        if word == m:
            score += 1
    elif k == 'fruit':
        s = choice(fruit)
        word = turtle.textinput("fruit", "%s(%d/%d)" % (s, i + 1, n))
        if word == s:
            score += 1
    else:
        z = choice(animal)
        word = turtle.textinput("animal", "%s(%d/%d)" % (z, i + 1, n))
        if word == z:
            score += 1
rate = score / n * 100
t.penup()
t.goto(0, -50)
t.write("%d/%d번 성공!" %(score, n), True, font = ("Arial", 15, "bold"))
t.penup()
t.goto(0, -100)
t.pendown()
t.write("정확도: %.1f%%" % (rate), True, font = ("Arial", 15, "bold"))
if rate == 100:
    t.penup()
    t.goto(300 / 100 * rate, 0)
    t.write("집에 데려다줘서 고마워!!", False, "center", font = ("Arial", 15, "bold"))
    t.left(60)
    t.right(360)
    t.left(300)
    t.right(360)
elif rate >= 80:
    t.penup()
    t.goto(300 / 100 * rate, 0)
    t.write("집이 코앞인데!! 한 번만 더 시도해줘!", False, "center", font = ("Arial", 15, "normal"))
elif rate >= 50:
    t.penup()
    t.goto(300 / 100 * rate, 0)
    t.write("집에 가고 싶어!!! ㅠ0ㅠ ", False, "center", font = ("Arial", 15, "normal"))
else:
    t.penup()
    t.goto(300 / 100 * rate, 0)
    t.write("거북이가 쓰러졌어요 ㅠ_ㅠ", False, "center", font = ("Arial", 15, "normal"))
turtle.done()