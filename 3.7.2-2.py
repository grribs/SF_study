S = int(input("Введите количество шагов: \n"))
R = str("*")
F = 1

for N in range(0, S):
    print(R)
    F += 1
    P = R * F
    print(P)



