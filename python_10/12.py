for i in range(2, 10):
    print("< %d 단 >" % i)
    for j in range(1, 10):
        print("%d * %d = %2d" % (i, j, i * j))
    print()