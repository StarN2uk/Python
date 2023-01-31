from random import *
str = [0, 1, 2, 3, 4, 5]
a = choice(str)
if a == 0:
    print('Loss!')
else:
    print('No.%d Spot!'% a)