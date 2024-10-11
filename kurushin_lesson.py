# Вычисление суммы ряда от 0 до 88888888

# from datetime import datetime
#
# to = datetime.now()
#
# s1 = sum(range(88888888))
# print(datetime.now() - to, s1)

# Вычисление средн. арифм.

# from numpy import mean
#
# A = [3, 4, 56, 100, 2, 2, 3]
#
# s = 0
#
# print(mean(A))
#
# for i in range(len(A)):
#     s += A[i]
# print(s / len(A))
# print(sum(A) / len(A))

# Помена строки в python
# НЕЛЬЗЯ ПОМЕНЯТЬ СОДЕРЖИМОЕ СТРОКИ ТОЛЬКО ПЕРЕПРИСОВИТЬ

# A = 'asdxxxxxfghyxyx'

# A = A.replace('x', 'y')

# print(A)

# Задача посчитать поризведение из списка кратные 3 и 5

# A = [3, 4, 56, 106, 15, 2, 20, 30]
# p = 1
#
# for a in A:
#     if a % 3 + a % 5 == 0:
#         p *= a
#
# print(p)

# import numpy as np
#
# A = np.array([3, 4, 56, 100, 15, 2, 20, 30])
# A_3 = A[A % 3 == 0]
# A_5 = A[A % 5 == 0]
# A_3_5 = np.intersect1d(A_3, A_5)
#
# print(A_3_5.prod())

# Управление GPIO

# Платы, поддерживающие Python
# - С операционной системой
# - Без нее

# Для работы с GPIO нужен adafruit Python
# У GPIO контакта есть 3 состояния: вход, выход, ничего (дефолтное значение).

# led = DigitalInOut(board.LED)
# lde.direction = Direction.OUTPUT

# Управление GPIO

# Платы, поддерживающие Python
# - С операционной системой
# - Без нее

# Для работы с GPIO нужен adafruit Python
# У GPIO контакта есть 3 состояния: вход, выход, ничего (дефолтное значение).

# led = DigitalInOut(board.LED)
# lde.direction = Direction.OUTPUT

m = []
s = ' '
while s != '':
    s = str(input())
    m.append(s)
m.remove('')
n = max(m, key=len)
m = m[::-1]
for i in range(len(m)):
    if len(m[i]) % 2 == 0:
        m[i] = '-' * ((len(n) - len(m[i])) // 2) + str(m[i]) + '-' * ((len(n) - len(m[i])) // 2)
        if len(m[i]) != len(n):
            m[i] = str(m[i]) + '-'
    else:
        m[i] = '-' * ((len(n) - len(m[i])) // 2) + str(m[i]) + '-' * ((len(n) - len(m[i])) // 2)
        if len(m[i]) != len(n):
            m[i] = str(m[i]) + '-'
for i in m:
    print(i)