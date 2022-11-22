x = int(input("Какая температура за окном? \n"))

if 20 < x < 30:
    rain = str(input("Есть осадки? y/n \n"))
    if rain in ['y', 'Y']:
        print("Футболку шорты и дождевик")
    else:
        print("Футболку шорты")
elif x < 20:
    temp2 = str(input("Температура выше 0? y/n \n"))
    if temp2 in ['y', 'Y']:
        rain2 = str(input("Есть осадки? y/n \n"))
        if rain2 in ['y', 'Y']:
            heavy_rain = str(input("Осадки сильные? \n"))
            if heavy_rain in ['y', 'Y']:
                print("Пальто резиновые сапоги и зонт")
            else:
                print("Пальто и дождевик")
        else:
            print("Пальто")
    else:
        print("Пуховик")



'''

by SF

 #Запрашиваем ввод температуры
temperature = int(input("Input temperature: "))

#для указания начальных статусов дождливости воспользуемся False или None
rainy = None
heavyRain = None

#если температура <0 то про дождь спрашивать бессмысленно
if temperature > 0:
   rainy = input("Is rainy: ") == "yes"
#если идет дождь спросим насколько он серьезный
   if rainy:
       heavyRain = input("Is heavy rain: ") == "yes"


#реализуем логику по схеме
decision = "Не решил что брать. Останусь дома."
if (temperature) > 20 and (temperature < 30) :
   if rainy:
       decision = "Взять футболку шорты и дождевик"
   else:
       decision = "Взять футболку и шорты"
elif temperature > 0:
   if rainy:
       if heavyRain:
           decision = "Взять пальто, резиновые сапоги и зонт"
       else:
           decision = "Взять пальто и дождевик"
   else:
       decision = "Взять пальто"
else:
   decision = "Взять пуховик"


#Выведем наше решение на экран
print(decision)




'''