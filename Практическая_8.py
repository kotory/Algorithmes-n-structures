import math

def triangle_area():
    a = int(input('Введите сторону шестиугольника:'))
    return (math.sqrt(3) / 4 * a ** 2)

def hexagon_area():
    return 6 * triangle_area()

S = [] 

def rectangle_area():
    def area(a, b):
        return a * b
    for i in range(3):
        print(f'Введите стороны {i + 1} прямоугольника:')
        a = int(input())
        b = int(input())
        S.append(area(a, b))
    for i in range(3):
        print(f'Площадь {i + 1} прямоугольника' S[i])

i = int(input('''Выберите действие:
1. Посчитать площадь шестиугольника
2. Вычислить площади прямоугольников
'''))

match i:
    case 1: print('Площадь шестиугольника:', triangle_area())
    case 2: print(rectangle_area())
    case _: print('Введён неверный код!')
