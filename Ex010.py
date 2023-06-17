side_a = int(input('Введите "a" сторону треугольника: '))
side_b = int(input('Введите "b" сторону треугольника: '))
side_c = int(input('Введите "c" сторону треугольника: '))
if side_a + side_b >= side_c and side_a + side_c >= side_b and side_c + side_b >= side_a:
    print('Треугольник существует')
    if side_a == side_b and side_b == side_c:
        print('и является равносторонним')
    elif side_a == side_b or side_b == side_c or side_a == side_c:
        print('и является равнобедренным')
    else:
        print('и является разносторонним')
else:
    print('Треугольник не существует')
