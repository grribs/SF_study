

L = [(int(input()) % 2 == 0 and int(input()) % 2 != 0) for i in range(2)]
print( any(L))


# coorect//    any(L) and not all(L)