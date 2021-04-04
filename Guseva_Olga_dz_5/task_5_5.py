src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def unic_numers (list_num):
    list_res = []
    for i in list_num:
        if list_num.count(i) == 1:
            list_res.append(i)
    return list_res


numbers = unic_numers(src)
print(numbers)
