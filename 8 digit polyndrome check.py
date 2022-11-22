A = str(input("A, 8 цифр: \n"))

A = list(map(int, A))
if A[0:3] == A[-1:-4:-1]:
    x = True
else:
    x = False
print(x)


'''
better solution:

number = 121
string = str(number)
if string == string[::-1]:
    print("Number - палиндром")
else:
    print("Number - не палиндром")
'''