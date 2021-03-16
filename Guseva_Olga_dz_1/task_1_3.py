org_word = str("Процент")
key_input = int(input("Введите число:"))

if key_input == 0:
    print(str(key_input) + " " + (org_word+str("ов.")))
elif key_input > 0 and key_input < 2:
    print(str(key_input) + " " + (org_word) + str("."))
elif key_input > 1 and key_input < 4:
    print(str(key_input) + " " + (org_word) + str("а."))
elif key_input > 4 and key_input <= 20:
    print(str(key_input) + " " + (org_word) + str("ов."))