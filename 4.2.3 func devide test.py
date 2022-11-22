a = input("Введите число \n")
n = input("Введите делитель \n")


def numb_check():
    c = int(a) % int(n)
    if c == 0:
        result = print(f"Число делится на {n}")
    else:
        result = print(f"Число не делится на {n}")
    return result


numb_check()
