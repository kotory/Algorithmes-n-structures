with open('Лухтан_ЗИТ_23_vvod.txt', 'r') as f:
    a = [[int(num) for num in line.split(',')] for line in f]

n = len(a)

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
            with open('Лухтан_ЗИТ_23_vivod.txt', 'w') as f:
                f.write('Матрица не является магическим квадратом')
            return
    with open('Лухтан_ЗИТ_23_vivod.txt', 'w') as f:
        f.write('Матрица не является магическим квадратом')

def reverse_columns(a):
    for i in range(n):
        t = a[i][0]
        a[i][0] = a[i][-1]
        a[i][-1] = t
    with open("Лухтан_ЗИТ_23_vivod.txt", "w") as f:
        for line in a:
            for elem in line:
                f.write(str(elem), )
            f.write('\n')

i = int(input())

match i:
    case 1: is_magic(a)
    case 2: reverse_columns(a)
    case _: print('Не тот код')
