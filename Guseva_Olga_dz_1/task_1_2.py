sum_ins_number = 0
result = 0

numb_list = []

for item in range (1, 1001, 2):
    numb_list.append(item ** 3)


for numb_in_list in numb_list:
    item_2 = numb_in_list
    while item_2 != 0:
        result = result + item_2 % 10
        item_2 = item_2 // 10
        if result % 7 == 0:
            sum_ins_number = sum_ins_number + numb_in_list
print(sum_ins_number)











