a = [2, 5, 11, 7, 2, 5, 1]

def min_fn(a):
    if len(a) == 1:
        return a
    if a[0] < a[1]:
        a[1] = a[0]
    return min_fn(a[1:])


print(min_fn(a))


#frm SF
'''
L = [1, 5, 11, 7, 2, 5]

def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

print(min_list(L))

'''



'''

a = [1, 5, 11, 7, 2, 5]

def max_fn(a):
    if len(a) == 1:
        return a
    if a[0] > a[1]:
        a[1] = a[0]
    return max_fn(a[1:])


print(max_fn(a))

'''