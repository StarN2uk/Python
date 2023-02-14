sum = 0
h_list = [159, 163, 173, 158, 169]
for h in h_list:
    sum += h
print("sum : %d" % sum)
print("avg : %.2f" % (sum / len(h_list)))