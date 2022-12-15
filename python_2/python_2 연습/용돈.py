go = int(input("심부름 횟수 = "))
work = int(input("안마 횟수 = "))
home = int(input("집안일 횟수 = "))
three = go * 500 + work * 700 + home * 100
one = three / 7
print("다음 주 용돈 = %d\n하루에 쓸 수 있는 돈 = %.1f" % (three, one))
