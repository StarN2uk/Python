import turtle
t = turtle.Turtle()
list = [-150, 0, 150, -80, 80]
t.penup()
t.goto(list[0], 10)
t.pendown()
t.color("blue")
t.circle(75)
t.penup()
t.goto(list[1], 10)
t.pendown()
t.color("black")
t.circle(75)
t.penup()
t.goto(list[2], 10)
t.pendown()
t.color("red")
t.circle(75)
t.penup()
t.goto(list[3], -80)
t.pendown()
t.color("yellow")
t.circle(75)
t.penup()
t.goto(list[4], -80)
t.pendown()
t.color("green")
t.circle(75)
turtle.done()