
from random import randrange, choice

list_1 = ["инспектор", "водитель", "инженер", "строитель", "кладовщик", "проектировщик"]
list_2 = ["всегда", "иногда", "редко", "часто", "бывает"]
list_3 = ["чихает", "спит", "плачет", "поет", "медитирует"]


def get_jokes (n):
    """
    Generates a list of jokes

    :param n: number of jokes

    :return: list of jokes
    """

    joke_list = []
    while len(joke_list) != n:
        res_1 = choice(list_1)
        res_2 = choice(list_2)
        res_3 = choice(list_3)
        res_joke = (f'{res_1} {res_2} {res_3}')
        joke_list.append(res_joke)
    print(joke_list)


get_jokes(5)







