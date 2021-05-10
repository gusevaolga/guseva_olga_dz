
temp_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

temp_2 = []
for numb in temp_1:
    is_number = False
    if numb.isnumeric():
        new_numb = f'{int(numb):02}'
        is_number = True
    elif numb[0] in ['+', '-'] and numb[1:].isnumeric():
        new_numb = f'{numb[0]}{int(numb[1:]):02}'
        is_number = True
    if is_number:
        temp_2.append('"')
        temp_2.append(new_numb)
        temp_2.append('"')
    else:
        temp_2.append(numb)
temp_3 = ' '.join(temp_2)
print(temp_3)




