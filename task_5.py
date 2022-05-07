"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных
из трех случайных слов, взятых из трёх списков (по одному из каждого).

Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий
повторы слов в шутках (когда каждое слово можно использовать
только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n, repeat=False):
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes = []
    list_min = min(no, adv, adj)
    while n and len(list_min):
        number = randrange(len(list_min))
        if repeat:
            jokes.append(f"{no.pop(number)} {adv.pop(number)} {adj.pop(number)}")
        else:
            jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return jokes

print(get_jokes(10, True))
print(get_jokes(10, False))