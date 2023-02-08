i = 1
while i <= 5:
    a = int(input("input : "))
    i += 1
    if a % 5 == 0:
        continue
    print("output : %d" % a)