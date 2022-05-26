import re


def email_parse(email_str):
    result_dict = {}
    re_mail = re.compile(r'^([\w.%+-]+)@([\w.-]+\.[a-z]+)$')
    ''' [\w.%+-]+ - проверяем username: любые буквенно-численные символы + символы .%+-
        [\w.-]+  - проверяем часть до последней точки: любые буквенно-численные символы + символы .-
        [a-z]+  - проверяем часть после точки: только буквы
    '''
    if re.findall(re_mail, email_str.lower()):
        result_dict["username"] = re.findall(re_mail, email_str.lower())[0][0]
        result_dict["domain"] = re.findall(re_mail, email_str.lower())[0][1]
        return result_dict
    else:
        raise ValueError(f'wrong email: {email_str}')


print(email_parse("someone@geekbrains.ru"))