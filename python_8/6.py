from random import *
str = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = choices(str, [1, 1, 1, 1, 1, 1, 9, 1, 1, 1], k = 3)
print(a)
s = a.count(7)
if s == 3:
    print('Lucky!')
elif s == 2:
    print('Good~')
else:
    print('So so.')