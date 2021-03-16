list_numb = []
spisok_1 = []
for numb in range (1, 1001, 2):
    numb_cube = (numb ** 3)
    list_numb.append(numb_cube)

summ_numb = 0
result_numb = 0

for i in list_numb:
    test_elem = i
    while test_elem > 0:
        summ_numb = summ_numb + (test_elem % 10)
        test_elem = test_elem // 10
    spisok_1.append(summ_numb)
    print(spisok_1)
    if spisok_1 % 7 == 0:
        result_numb += spisok_1
        print(result_numb)





