
temp_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
temp_1.remove('5')
temp_1.remove('17')
temp_1.remove('+5')
temp_1.insert(1, '"05"')
temp_1.insert(3, '"17"')
temp_1.insert(8, '"+05"')

temp_2 = ' '.join(temp_1)
print(temp_2)


