import random
r = random.randint(1, 6)
s = random.randint(1, 6)
print(r, s)
me = r
you = s
r = random.randint(1, 6)
s = random.randint(1, 6)
print(r, s)
me = me + r
you = you + s
print(me, you)
if me > you:
    print('내가 이김 ㅋㅋ')
elif me < you:
    print('너가 이김...')
else:
    print('비겼다고라고?')