black = [0, 1]
brown = [1, 10]
red = [2, 100]
orange = [3, 1000]
yellow = [4, 10000]
green = [5, 100000]
blue = [6, 1000000]
violet = [7, 10000000]
grey = [8, 100000000]
white = [9, 1000000000]

a = input("1: ")
b = input("2: ")
c = input("3: ")

d = 0
e = 0
f = 0
while 1:
    if a == 'black':
        d = black[0]
        break
    elif a == 'brown':
        d = brown[0]
        break
    elif a == 'red':
        d = red[0]
        break
    elif a == 'orange':
        d = orange[0]
        break
    elif a == 'yellow':
        d = yellow[0]
        break
    elif a == 'green':
        d = green[0]
        break
    elif a == 'blue':
        d = blue[0]
        break
    elif a == 'violet':
        d = violet[0]
        break
    elif a == 'grey':
        d = grey[0]
        break
    else:
        d = white[0]
        break
while 1:
    if b == 'black':
        e = black[0]
        break
    elif b == 'brown':
        e = brown[0]
        break
    elif b == 'red':
        e = red[0]
        break
    elif b == 'orange':
        e = orange[0]
        break
    elif b == 'yellow':
        e = yellow[0]
        break
    elif b == 'green':
        e = green[0]
        break
    elif b == 'blue':
        e = blue[0]
        break
    elif b == 'violet':
        e = violet[0]
        break
    elif b == 'grey':
        e = grey[0]
        break
    else:
        e = white[0]
        break
while 1:
    if c == 'black':
        f = black[1]
        break
    elif c == 'brown':
        f = brown[1]
        break
    elif c == 'red':
        f = red[1]
        break
    elif c == 'orange':
        f = orange[1]
        break
    elif c == 'yellow':
        f = yellow[1]
        break
    elif c == 'green':
        f = green[1]
        break
    elif c == 'blue':
        f = blue[1]
        break
    elif c == 'violet':
        f = violet[1]
        break
    elif c == 'grey':
        f = grey[1]
        break
    else:
        f = white[1]
        break
print(d * (f * 10) + e * f)