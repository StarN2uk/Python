s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = s[0]
for i in range(10):
    a = int(input())
    s[i] = a
    if b < a:
        b = s[i]
print("가장 큰 수: %d" % b)