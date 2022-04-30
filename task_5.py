list1 = [57.8, 46.51, 97, 35.03, 5.2, 98.90, 12.17, 25.3]

print('Задание № 4.a')
result = ''
for el in list1:
    print(f'{int(el)} руб. {int(el * 100 % 100):02} коп.', end=', ')

print('\n\nЗадание № 4.b')
print(f'Список цен: {list1} \nсписок id: {id(list1)}')
list1.sort()
print(f'Список цен, отсортированный по возрастанию: {list1} \nсписок id: {id(list1)}')

print('\n\nЗадание № 4.c')
new_list = sorted(list1, reverse=1)
print(f'Список цен, отсортированный по убыванию: {new_list} \nсписок id: {id(new_list)}')

print('\n\nЗадание № 4.d')
print('Цены пяти самых дорогих товаров:', list1[-5:])