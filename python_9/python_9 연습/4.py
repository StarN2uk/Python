from random import *
a = randint (100, 999)
answer = 0
strike = 0
out = 0
count = 0
print("숫자 야구")
while 1:
    answer = int(input("입력: "))
    a100 = a // 100
    a10 = (a // 10) % 10
    a1 = a % 10
    an100 = answer // 100
    an10 = (answer // 10) % 10
    an1 = answer % 10
    strike = 0
    if a100 == an100:
        strike = strike + 1
    if a10 == an10:
        strike = strike + 1
    if a1 == an1:
        strike = strike + 1
    print("{0} STRIKE {1} OUT".format(strike, 3 - strike))
    count += 1
    if strike == 3:
        print("{0}회 안에 성공하셨습니다! (숫자: {1})".format(count, a))
        break