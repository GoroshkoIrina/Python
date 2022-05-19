result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:

    for line in f:
        list1 = line.replace('"', '').split(' ')
        tuple1 = (list1[0], list1[5], list1[6])
        result.append(tuple1)

print(result)
