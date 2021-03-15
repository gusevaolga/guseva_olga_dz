
dur = int(input("Введите количество секунд:"))

if dur >= 0 and dur <= 59:
    print(str(dur) + " sec")
elif dur >= 59 and dur <= 3599:
    print((str(dur // 60) + " min") + " "+ (str(dur % 60) + " sec"))
if dur >= 3600:
    print("Количество секунд превышает промежуток min и sec")
print("Finish")
