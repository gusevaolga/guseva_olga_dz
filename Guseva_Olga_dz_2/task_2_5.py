
numb = [20, 18, 55.7, 2002.2, 1, 15, 18, 32, 10.5, 13, 122, 122.3, 300, 23.1, 99, 199, 202, 2222.2, 2000]

for i in numb:
    rub = i // 1
    pen = i % 1 * 100
    print(f'{rub:.0f} рублей {pen:02.0f} копеек')

numb.sort()
print(numb)

new_numb = numb[::-1]
print(new_numb)

exp_numb = new_numb[0:5]
print(exp_numb)




