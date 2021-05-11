
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

def generate_tutors (first_list, second_list):
    diff = len(first_list) - len((second_list))
    if diff > 0:
        second_list.append([None for i in range(diff)])
    for t, k, in zip(first_list, second_list):
        yield t,k

res_tuple = generate_tutors(tutors,klasses)

print(list(res_tuple))


