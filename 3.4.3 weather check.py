x = int(input("Ввод скорости ветра \n"))

if x in [1, 2, 3, 4]:
    print("Weak")
elif 5 <= x <= 10:
    print("Moderate")
elif 11 <= x <= 18:
    print("Strong")
elif x >= 19:
    print("Hurracane")
else:
    print("Input error")

'''
    else:  # x > 0, y < 0
        print("Четвертая четверть")
else:
   :  # x < 0, y > 0
        
    else:  # x < 0, y < 0
        
'''
