import json

result = {}

with open('users.csv', 'r', encoding='utf-8') as f_users, open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
    line_users = f_users.readline().strip()
    line_hobby = f_hobby.readline().strip()
    while line_users:
        result[line_users] = line_hobby
        line_users = f_users.readline().strip()
        line_hobby = f_hobby.readline().strip()
        if not line_hobby:
            line_hobby = None
    if line_hobby:
        exit(1)

print(result)

with open('result.json', 'w', encoding='utf-8') as f_result:
    json.dump(result, f_result, ensure_ascii=False)

with open('result.json', 'r', encoding='utf-8') as f_result:
    result = json.load(f_result)
print(result)
