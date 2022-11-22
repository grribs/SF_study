L = str(1234567)

def rev_numbr(L):
 #   print(L[0])
    if len(L) == 1:
        return L[0]
    return L[-1] + rev_numbr(L[0:-1])


print(rev_numbr(L))


#SF solution:

'''

def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res

'''