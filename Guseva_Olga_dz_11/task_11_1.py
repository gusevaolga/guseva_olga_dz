from datetime import date


class Data:

    @classmethod
    def number(cls, my_date):
        date_list = []
        for i in my_date.split():
            if i != '-': date_list.append(i)

        return int(date_list[0]), int(date_list[1]), int(date_list[2])


    @classmethod
    def date_to_int(cls, obj):
        return obj.date.split('-')

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <=12:
                if year >=0:
                    return 'Корректная дата'
                else:
                    return 'Некорректный год'
            else:
                return 'Некорректный месяц'
        else:
            return 'Некорректный день'



