list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0

while i < len(list1):
    item = list1[i]
    if item[-1].isdigit():
        list1.insert(i, '"')
        i +=1
        str_len = 3 if item.startswith(('+', '-')) else 2
        if len(item) < str_len:
            item = item.zfill(str_len)
            list1[i] = item
        i += 1
        list1.insert(i, '"')
    i += 1

i = 0
result = ''
while i < len(list1):
    item = list1[i]
    if item == '"':
        item = ''.join(list1[i:i+3])
        i += 2
    result = result + item + ' '
    i += 1

print(list1)
print(result)