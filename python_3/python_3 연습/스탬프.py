import turtle
t = turtle.Turtle()
t.shape = ("turtle")
stmp1 = t.stamp()
t.circle(100, 90)
stmp2 = t.stamp()
t.circle(100, 90)
stmp3 = t.stamp()
t.circle(100, 90)
stmp4 = t.stamp()
t.circle(100, 90)
t.clearstamp(stmp2)
t.clearstamp(stmp4)
t.done()
