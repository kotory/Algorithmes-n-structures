n = int(input('Введите размер квадратной матрицы:'))
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)

print('Матрица:')
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

def is_magic(arr):
    summ = sum(arr[0])
 
    for i in range(len(arr)):
        temp = 0
        for j in range(len(arr)):
            temp += arr[j][i]
        if temp != summ or sum(arr[i]) != summ:
            print('Матрица не является магическим квадратом')
            return
    print('Матрица является магическим квадратом')

def reverse_columns(a):
    for i in range(n):
        t = a[i][0]
        a[i][0] = a[i][-1]
        a[i][-1] = t
    return a

i = int(input())

match i:
    case 1: is_magic(a)
    case 2: print(reverse_columns(a))
    case _: print('Не тот код')
