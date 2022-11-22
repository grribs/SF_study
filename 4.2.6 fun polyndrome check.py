
def poly(n):
    n = n.lower()
    n = n.replace(" ", "")
    if n[::1] == n[::-1]:
        print(True)
    else:
        print(False)
    return(print(n))

poly("Кит на море не романтик")
