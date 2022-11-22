
A = list("aaabbccccdaaa")
B = []
j = 0
n = 0

for i in range(len(A)):

    if A[i] == A[i-1]:
        n += 1
#       print("Cntr_1", n)
        if j < n:
            j = n
#            print("Max", j)
        if A[i] not in B:
            B.append(A[i])

    if A[i] != A[i-1]:
        if j != 0:
            B.append(j)
            j = 0
        else:
            j = 1
            B.append(j)
        n = 0
        n += 1
#        print("cntr_2", n)
        B.append(A[i])
# Костыль 1 & 2
for i in A[-1]:
    if j == 0:
        j = 1
    B.append(j)

print(B)


#light vers:
'''
text = input()  # получаем строку

last = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text:
    if c == last:  # если символ совпадает с сохраненным, 
        count += 1  # то увеличиваем счетчик
    else:
        result += last + str(count)  # иначе - записываем в результат
        last = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += last + str(count)  # и добавляем в результат последний символ
print(result)
'''