

def strw(n):
    b = int(n+1)
    c = str("*" * n)
    for a in range(0, n):
        a += a
        b = b - 1
        m = c[:b]
        print(m)


strw(10)



'''

# vs fine solution

def reverse_stair(n):
   for i in range(n, 0, -1):
       print("*" * i)

reverse_stair(5)


'''