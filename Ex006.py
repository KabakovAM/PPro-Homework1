GREGORIAN_CALENDAR = 1582
data = int(input('Введите год: '))
if data < GREGORIAN_CALENDAR:
    result = 'Год введения грегорианского календаря 1582, расчитать високосный год невозможно'
elif data % 400 == 0:
    result = 'Високосный'
elif data % 100 == 0:
    result = 'Невисокосный'
elif data % 4 == 0:
    result = 'Високосный'
else:
    result = 'Невисокосный'
print(result)
