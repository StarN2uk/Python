import random
pscore = 0
cscore = 0
player = set(['가위', '바위', '보'])
print(player)
r = input('내고 싶은 카드는?')
player.remove(r)
s = random.randint(1, 3)
if s == 1:
    print('컴퓨터는 가위를 냈습니다')
    if r == '가위':
        print('비겼습니다')
    elif r == '바위':
        print('이겼습니다')
        pscore = pscore + 1
    else:
        print('졌습니다')
        cscore = cscore + 1
elif s == 2:
    print('컴퓨터는 바위를 냈습니다')
    if r == '가위':
        print('졌습니다')
        cscore = cscore + 1
    elif r == '바위':
        print('비겼습니다')
    else:
        print('이겼습니다')
        pscore = pscore + 1
else:
    print('컴퓨터는 보를 냈습니다.')
    if r == '가위':
        print('이겼습니다')
        pscore = pscore + 1
    elif r == '바위':
        print('졌습니다')
        cscore = cscore + 1
    else:
        print('비겼습니다')
print(player)
r = input('내고 싶은 카드는?')
player.remove(r)
s = random.randint(1, 3)
if s == 1:
    print('컴퓨터는 가위를 냈습니다')
    if r == '가위':
        print('비겼습니다')
    elif r == '바위':
        print('이겼습니다')
        pscore = pscore + 1
    else:
        print('졌습니다')
        cscore = cscore + 1
elif s == 2:
    print('컴퓨터는 바위를 냈습니다')
    if r == '가위':
        print('졌습니다')
        cscore = cscore + 1
    elif r == '바위':
        print('비겼습니다')
    else:
        print('이겼습니다')
        pscore = pscore + 1
else:
    print('컴퓨터는 보를 냈습니다.')
    if r == '가위':
        print('이겼습니다')
        pscore = pscore + 1
    elif r == '바위':
        print('졌습니다')
        cscore = cscore + 1
    else:
        print('비겼습니다')
print(player)
r = input('내고 싶은 카드는?')
player.remove(r)
s = random.randint(1, 3)
if s == 1:
    print('컴퓨터는 가위를 냈습니다')
    if r == '가위':
        print('비겼습니다')
    elif r == '바위':
        print('이겼습니다')
        pscore = pscore + 1
    else:
        print('졌습니다')
        cscore = cscore + 1
elif s == 2:
    print('컴퓨터는 바위를 냈습니다')
    if r == '가위':
        print('졌습니다')
        cscore = cscore + 1
    elif r == '바위':
        print('비겼습니다')
    else:
        print('이겼습니다')
        pscore = pscore + 1
else:
    print('컴퓨터는 보를 냈습니다.')
    if r == '가위':
        print('이겼습니다')
        pscore = pscore + 1
    elif r == '바위':
        print('졌습니다')
        cscore = cscore + 1
    else:
        print('비겼습니다')
print(pscore, cscore)
if pscore > cscore:
    print('You win')
elif pscore < cscore:
    print('You lose')
else:
    print('Happy draw')