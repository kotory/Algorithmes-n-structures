N = int(input('Введите длину массива: '))
array = []
for i in range(N):
    print('Введите', i, 'элемент:')
    array.append(int(input()))
print('Исходный массив:', array)
print()

def find_min_element(array):
    m_element = array[0]
    index_m = 0
    for i in range(N):
        if array[i] < m_element:
            m_element = array[i]
            index_m = i
    return index_m

def create_two_arrays(array):
    second_a = []
    third_a = []
    for i in range(N):
        if array[i] > 0:
            second_a.append(array[i])
        else: third_a.append(array[i])
    return second_a, third_a

a2, a3 = create_two_arrays(array)

i = int(input('''Выберите действие:
1. Найти индекс минимального элемента
2. Переписать все положительные числа во второй массив, а остальные в третий
'''))

match i:
    case 1: print('Индекс минимального элемента массива:', find_min_element(array))
    case 2: print('Массив с положительными числами:', a2, 'и массив с остальными:', a3)
    case _: print('Выбран неверный код!')

