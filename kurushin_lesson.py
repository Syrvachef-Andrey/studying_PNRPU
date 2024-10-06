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

