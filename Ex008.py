data = int(input('Введите количество рядов ёлки: '))
for i in range(data + 1):
    print(f"{' '*data}{'*'*(i * 2 - 1)}")
    data -= 1
