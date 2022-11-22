x = int(input("Введите X"))
y = int(input("Введите Y"))

if x > 0 and y > 0:
    print("Первая четверть")
elif x < 0 and y > 0:
    print("Вторая четверть")
elif x < 0 and y < 0:
    print("Третья четверть")
elif x > 0 and y < 0:
    print("Четвертая четверть четверть")
else:
    print(None)


'''
    else:  # x > 0, y < 0
        print("Четвертая четверть")
else:
   :  # x < 0, y > 0
        
    else:  # x < 0, y < 0
        
'''