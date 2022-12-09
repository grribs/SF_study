
def start():
    print("Добро пожаловать!")
    print("-----------------")
    print("Формат ввода: X Y")
    global A
    global B
    A = input("Введите имя первого игрока (X): \n")
    B = input("Введите имя второго игрока (0): \n")

    return A, B


def table():
    print("╔════════════════╗")
    print("║    0 | 1  |  2 ║")
    print("╟────────────────╢")
    for i in range(3):
        print(f"║{i}│", end="")
        for j in range(3):
            print(f"{field[j][i]} {' '.join('│')}", end="")
        print(" ")
    print("╚════════════════╛")


def check():
    global cnt
    global x
    global y
    if not(x.isdigit()) or not(y.isdigit()):
        return print("Введите цифры, диапазон 0-2!")
    x, y = int(x), int(y)
    if x < 0 or x > 2 or y < 0 or y > 2:
        return print("Диапазон координат поля: 0-2")
    if field[x][y] != "   ":
        return print("Клетка занята")
    if cnt % 2 != 0:
        field[x][y] = " 0 "
        cnt += 1
    else:
        field[x][y] = " X "
        cnt += 1


def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_coord:
        symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])
        if symbols == [" X ", " X ", " X "]:
            print(f"Выиграл {A}!!!")
            return True
        if symbols == [" 0 ", " 0 ", " 0 "]:
            print(f"Выиграл {B}!!!")
            return True
    return False


field = [['   '] * 3 for i in range(3)]

start()
table()

cnt = 0
x = None
y = None

while True:
    if cnt == 9:
        print("В игре ничья!")
        break
    if cnt % 2 == 0:
        coords = input(f"Ходит игрок {A}:").split()
        if len(coords) != 2:
            print("Введите 2 координаты")
            continue
        x, y = coords
        check()
        table()
        if check_win():
            break
    else:
        coords = input(f"Ходит игрок {B}:").split()
        if len(coords) != 2:
            print("Введите 2 координаты")
            continue
        x, y = coords
        check()
        table()
        if check_win():
            break