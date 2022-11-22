
def search(n):
    if n == 1:
        return 1
    return n + search(n-1)


print(search(4))

