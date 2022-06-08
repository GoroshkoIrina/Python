class My_Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def str_to_date(cls, date_str):
        res_date = date_str.split('-')
        return [int(res_date[0]), int(res_date[1]), int(res_date[2])]

    @staticmethod
    def validate(date_str):
        res_date = date_str.split('-')
        if 1 <= int(res_date[0]) <= 31:
            if 1 <= int(res_date[1]) <= 12:
                if 2022 >= int(res_date[2]) >= 0:
                    return f'Дата корректна'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


new_date = My_Date('07-06-2022')
print(new_date.str_to_date('01-06-2022'))
print(My_Date.str_to_date('01-06-2022'))
print(My_Date.validate('01-07-2022'))
print(My_Date.validate('01-23-2022'))