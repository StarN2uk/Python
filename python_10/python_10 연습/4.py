from random import *
s = [1, 2, 3, 4]
count = 0
for i in range(5):
    s[0] = randint(0, 1)
    s[1] = randint(0, 1)
    s[2] = randint(0, 1)
    s[3] = randint(0, 1)
    print(s[0], s[1], s[2], s[3])
    if s[0] == 1:
        count += 1
    if s[1] == 1:
        count += 1
    if s[2] == 1:
        count += 1
    if s[3] == 1:
        count += 1
    if count == 4:
        print('모')
    elif count == 3:
        print('도')
    elif count == 2:
        print('개')
    elif count == 1:
        print('걸')
    else:
        print('윷')
    count = 0