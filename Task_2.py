class My_Error(ZeroDivisionError):
    text = "Деление на ноль запрещено"

    def __str__(self):
        return self.text

while True:
        try:
            dividend = float(input("Введите делимое: "))
            divider = float(input("Введите делимое: "))
            if divider != 0:
                print(dividend / divider)
            else:
                raise My_Error
        except My_Error as e:
            print(e)
        except ValueError as err:
            print(err)
            break
