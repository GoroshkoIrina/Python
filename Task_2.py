result = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:

    for line in f:
        list1 = line.replace('"', '').split(' ')
        if result.get(str(list1[0])):
            result[str(list1[0])] = result[str(list1[0])] + 1
        else:
            result[str(list1[0])] = 1

print('Количество спам-запросов: ', max(result.values()))

for key in result:
    if result[key] == max(result.values()):
        print('IP спамера: ', key)
