class My_Error(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


res_list = []
while True:
    input_str = input("Введите число: ")

    if input_str.lower() == "stop":
        break
    try:
        if not input_str.isdigit():
            raise My_Error(f"'{input_str}' не является числом, повторите попытку")

        res_list.append(int(input_str))
    except My_Error as e:
        print(e)

print(res_list)
