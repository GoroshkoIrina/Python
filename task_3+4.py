"""
Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
в которых фамилия начинается с соответствующей буквы
"""
def thesaurus(*args):
    result_dict = {}
    for el in args:
        if result_dict.get(el[0][0]):
            result_dict[el[0][0]].append(el)
        else:
            result_dict[el[0][0]] = [el]
    return result_dict


def thesaurus_adv(*args):
    result_dict = {}
    for el in args:
        full_name = el.split()
        full_name.reverse()
        if result_dict.get(full_name[0][0]):
            result_dict[full_name[0][0]].append(el)
        else:
            result_dict[full_name[0][0]] = [el]
    for key in result_dict:
        result_dict[key] = thesaurus(*result_dict[key])
    return result_dict

print(thesaurus_adv("Роман Кисилев", "Иван Сергеев", "Инна Серова", "Петр Алексеев", "Софья Агафонова", "Илья Иванов", "Анна Савельева"))