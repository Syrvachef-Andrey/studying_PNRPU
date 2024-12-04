import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, ifft

print("Введите диапазон определений по условию (0, 4)")

while True:
    print("Введите количество элементов в ряде: ", end='')
    n = int(input())
    if type(n) != int or n <= 4:
        print("Неправильно введено значение количества элементов")
        print("Введите заново")
    else:
        break

x_arr = np.array([])
y_arr = np.array([])

step = (4 - 0) / n
x = 0

while x < 4:
    y = 4 - x
    x_arr = np.append(x_arr, x)
    y_arr = np.append(y_arr, y)
    x += step

y_arr_ryad = fft(x_arr)
print(y_arr_ryad)
plt.plot(x_arr, y_arr, x_arr, y_arr_ryad)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = 4 - x')
plt.grid(True)
plt.show()