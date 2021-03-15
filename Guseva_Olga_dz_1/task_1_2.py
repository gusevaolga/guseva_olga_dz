spisok = ['1111']

for a in range (1, 1001, 2):
    b = (a**3)

    c = 0
    while b > 0:
        c = c + (b % 10)
        b = b // 10

    res = (c % 7)
    if res == 0:
        res1 = str(a**3)
        res2 = res1 +









