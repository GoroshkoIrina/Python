import itertools

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

def my_generator(list_1, list_2):
    for num in itertools.zip_longest(list_1, list_2, fillvalue=None):
        yield num

mg = my_generator(tutors, classes)
print(next(mg))
print(next(mg))
print(next(mg))
print(next(mg))
print(next(mg))
print(next(mg))
print(next(mg))
print(next(mg))
