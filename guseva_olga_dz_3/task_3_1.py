
transl_dict = {"zero": "ноль",
               "one": "один",
               "two": "два",
               "three": "три",
               "four": "четыре",
               "five": "пять",
               "six": "шесть",
               "seven": "семь",
               "eight": "восемь",
               "nine": "девять",
               "ten": "десять"}


def num_translate (num_1):
    print(transl_dict.get(num_1))


num_translate("nine")
num_translate("twenty")