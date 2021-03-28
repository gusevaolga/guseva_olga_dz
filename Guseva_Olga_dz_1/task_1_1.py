
dur = int(input("Введите количество секунд:"))

if dur >= 0 and dur <= 59:
    print(str(dur) + " sec")
elif dur >= 59 and dur <= 3599:
    print((str(dur // 60) + " min") + " " + (str(dur % 60) + " sec"))
elif dur >= 3600 and dur <= 86399:
    print(((str(dur // 3600) + "h") + " " + (str(dur % 3600 // 60)) + "min") + " " + (str((dur - 3600) % 60) + "sec"))
print("Finish")
