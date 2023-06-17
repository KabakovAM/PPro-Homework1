data = 0
while data < 1 or data > 99999:
    data = int(input('Введите число: '))
check = 0
for i in range(1,data+1):
    if data % i == 0:
        check += 1
if check == 2:
    print(f'{data} - простое число')
else:
    print(f'{data} - составное число')