src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_src = [el for el in src if src.count(el) == 1]
print(unique_src)

unique_src2 = set() #решаем через мноества
tmp = set()
for el in src:
    if el not in tmp:
        unique_src2.add(el)
    else:
        unique_src2.discard(el)
    tmp.add(el)
print(unique_src2)

unique_src2_ord = [el for el in src if el in unique_src2] #делаем сортировку как в изначальном списке
print(unique_src2_ord)


