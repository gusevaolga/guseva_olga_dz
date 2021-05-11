import json

res_dict = {}

with open('users.csv', 'r', encoding='utf-8') as users, open('hobby.csv', 'r', encoding='utf-8') as hobby:
    user_line = users.readline().strip()
    hobby_line = hobby.readline().strip()
    while user_line:
        res_dict.update({user_line: hobby_line})
        user_line = users.readline().strip()
        hobby_line = hobby.readline().strip()
print(res_dict)

with open('result_for_task_6_3.json', 'w+', encoding='utf-8') as f:
    json.dump(res_dict, f)
