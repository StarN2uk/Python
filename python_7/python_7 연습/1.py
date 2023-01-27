import random
m = int(input('1 : 가위, 2 : 보, 3 : 바위'))
r = random.randint(1, 3)
if r == 1:
    print('Com(1) : User(%d)'% m)
    if m == 1:
        print('비겼다')
    elif m == 2:
        print('졌다')
    else:
        print('이겼다')
elif r == 2:
    print('Com(2) : User(%d)'% m)
    if m == 1:
        print('이겼다')
    elif m == 2:
        print('비겼다')
    else:
        print('졌다')
else:
    print('Com(3) : User(%d)'% m)
    if m == 1:
        print('졌다')
    elif m == 2:
        print('이겼다')
    else:
        print('비겼다')