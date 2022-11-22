
text1 = str(input("Введите текст"))
text1 = text1.split()
text1 = set(text1)
print(text1)
text2 = str(input("Введите текст"))
text2 = text2.split()
text2 = set(text2)
print(text2)

text1_dif = text1.symmetric_difference(text2)

print(text1_dif)


