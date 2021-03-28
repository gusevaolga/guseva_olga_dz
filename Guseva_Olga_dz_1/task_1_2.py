
numb_list = []

for item in range (1, 1001, 2):
    numb_list.append(item ** 3)

result_sum = 0
for number in numb_list:
    number_summ = 0
    item = number
    while number != 0:
        number_summ += (number % 10)
        number = number // 10
    if number_summ % 7 == 0:
        result_sum += item

for dev in numb_list:
    dev_summ = dev + 17
    resul_dev = dev_summ

    dev_i = 0
    dev_finish = 0

    while resul_dev != 0:
        dev_i += (resul_dev % 10)
        resul_dev = resul_dev // 10
    if dev_i % 7 == 0:
        dev_finish += dev_summ
        print(dev_finish)




