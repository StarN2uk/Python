list = ['토끼와 거북이', '금도끼 은도끼', '피리 부는 늑대', '황금알을 낳는 거위', '개미와 베짱이', '토끼와 거북이']
a = list.count('토끼와 거북이')
if a > 1:
    list.remove('토끼와 거북이')
list.sort()
print(list)