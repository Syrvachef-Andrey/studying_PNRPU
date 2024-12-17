from random import randint as rn
import numpy as np


def find_connected_components(matrix):
    n = len(matrix)  # Количество вершин
    visited = [False] * n  # Отслеживаем посещенные вершины
    components = []  # Список компонент связности

    for i in range(n):
        if not visited[i]:
            # Находим все вершины, связанные с текущей вершиной i
            component = []
            queue = [i]
            visited[i] = True

            while queue:
                vertex = queue.pop(0)
                component.append(vertex)
                # Ищем все смежные вершины
                for j in range(n):
                    if matrix[vertex][j] == 1 and not visited[j]:
                        queue.append(j)
                        visited[j] = True

            components.append(component)

    return components


def mat_print(matrix):
    for row in matrix:
        print(*row)


r = int(input('Введите размерность матрицы - '))
a = int(input('Построить матрицу:\n 0 - вручную\n 1 - автоматически \n'))

if a:
    matrix = [[rn(0, 1) for i in range(r)] for i in range(r)]
else:
    matrix = []
    for i in range(r):
        row_input = input(f"{i + 1} строка : ")
        row = [int(x) for x in row_input.split()]
        matrix.append(row)

print("Заполненная матрица:")
mat_print(matrix)

for i in range(r):
    for j in range(r):
        if (i == j and matrix[i][j] != 1):
            matrix[i][j] = 1

print("Заполненнение диагонали:")
mat_print(matrix)

print("Умножение матриц:")
copy = [i[:] for i in matrix]
for i in range(r - 1):
    matrix = np.dot(matrix, copy)

matrix[matrix > 0] = 1

mat_print(matrix)
print('Транспонированная матрица:')
# транспонирование
transp =np.transpose(matrix)
mat_print(transp)

print('Умножение транспонированной матрицы на полученную:')
# умножение транспонированной на полученную
result = transp * matrix
mat_print(result)

print(find_connected_components(result))