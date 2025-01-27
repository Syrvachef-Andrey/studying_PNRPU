import numpy as np
import matplotlib.pyplot as plt

# Функция для вычисления координат звеньев манипулятора
def forward_kinematics(theta1, theta2, l1, l2):
    x1 = l1 * np.cos(theta1)
    y1 = l1 * np.sin(theta1)
    x2 = x1 + l2 * np.cos(theta1 + theta2)
    y2 = y1 + l2 * np.sin(theta1 + theta2)
    return (x1, y1), (x2, y2)

# Параметры манипулятора
l1 = 1.0  # Длина первого звена
l2 = 1.0  # Длина второго звена
theta1 = np.pi / 4  # Угол первого звена (в радианах)
theta2 = np.pi / 6  # Угол второго звена (в радианах)

# Вычисляем координаты звеньев
joint1, joint2 = forward_kinematics(theta1, theta2, l1, l2)

# Визуализация
plt.figure()
plt.plot([0, joint1[0]], [0, joint1[1]], 'b-', label='Звено 1')  # Первое звено
plt.plot([joint1[0], joint2[0]], [joint1[1], joint2[1]], 'r-', label='Звено 2')  # Второе звено
plt.plot(0, 0, 'ko', label='Основание')  # Основание
plt.plot(joint1[0], joint1[1], 'go', label='Соединение 1')  # Соединение 1
plt.plot(joint2[0], joint2[1], 'mo', label='Конец манипулятора')  # Конец манипулятора

# Настройка графика
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.title("2D Манипулятор")
plt.show()