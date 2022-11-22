
def strw(n):
    c = 0
    for m in range(n, 0, -1):
        if n % m == 0:
            c += 1
    print(c)


strw(28)
