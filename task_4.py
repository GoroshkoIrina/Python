list1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
         'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for el in list1:
    firstname = el.split()[-1].capitalize()
    print(f'Привет, {firstname}!')