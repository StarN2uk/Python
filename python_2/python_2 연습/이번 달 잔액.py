money = int(input("지난달 남은 돈은? (잔액) "))
plus = int(input("이번 달 수입? "))
minus = int(input("이번 달 지출? "))
money = money + plus - minus
print("이번 달 잔액은? {0}". format(money))
