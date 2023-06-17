data = 0
while data < 1 or data > 999:
    data = int(input('Введите число: '))
if data // 10 == 0:
    result = data**2
elif data // 100 == 0:
    result = (data % 10) * (data // 10)
elif data // 1000 == 0:
    result = data % 10 * 100 + data % 100 // 10 * 10 + data // 100
print(result)
