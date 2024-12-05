import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию, которую будем разлагать в ряд Фурье
def f(x):
    return 4 - x

# Параметры разложения
L = 4  # Период функции (в данном случае, функция определена на интервале [-L, L])
N = 100  # Количество членов ряда Фурье

# Создаем массив точек для вычисления интегралов
x = np.linspace(0, 4, 1000)

# Вычисление коэффициентов Фурье
a0 = (1 / L) * np.trapz(f(x), x)
an = lambda n: (1 / L) * np.trapz(f(x) * np.cos(n * np.pi * x / L), x)
bn = lambda n: (1 / L) * np.trapz(f(x) * np.sin(n * np.pi * x / L), x)

# Вычисление ряда Фурье
def fourier_series(x, N):
    result = a0 / 2
    for n in range(1, N + 1):
        result += an(n) * np.cos(n * np.pi * x / L) + bn(n) * np.sin(n * np.pi * x / L)
    return result

# Создаем массив точек для построения графика
x_plot = np.linspace(0, 4, 1000)

# Вычисляем значения функции и ее аппроксимации рядом Фурье
y_exact = f(x_plot)
y_approx = fourier_series(x_plot, N)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_exact, label='Exact function: $4 - x$', linewidth=2)
plt.plot(x_plot, y_approx, label=f'Fourier series (N={N})', linestyle='--', linewidth=2)
plt.title('Fourier Series Approximation of $4 - x$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()