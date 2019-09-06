width = int(input("Введите вершину прямоугольника: "))
height = int(input("Введите высоту прямоугольника: "))

for x in range(height):
    for y in range(width):
        print('*', end='')
    print()