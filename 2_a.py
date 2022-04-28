list1 = []
for i in range(1, 1001, 2):
    list1.append(i ** 3)
print(list1)

list2 = []
for el in list1:
    sum1 = 0
    i = el
    while el != 0:
        sum1 += el % 10
        el = el // 10
    if sum1 % 7 == 0:
        list2.append(i)
print(sum(list2))