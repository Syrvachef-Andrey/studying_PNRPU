import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Параметры системы (реальные значения)
J1 = 0.0028  # момент инерции двигателя, кг·м² (АИР80А4)
J2 = 0.005  # момент инерции механизма, кг·м²
C12 = 1000  # жесткость упругой связи, Н·м/рад

# Номинальный момент двигателя
P_nom = 1100  # Вт
omega_nom = 1420 * np.pi / 30  # рад/с (перевод об/мин в рад/с)
M_nom = P_nom / omega_nom  # номинальный момент


# Функция для моделирования
def two_mass_system(y, t, M_motor_func, M_load_func):
    omega1, omega2, M12 = y

    # Момент двигателя (зависит от времени)
    M_motor = M_motor_func(t)

    # Момент нагрузки (может быть постоянным или зависеть от скорости)
    M_load = M_load_func(t, omega2)

    # Уравнения двухмассовой системы
    domega1 = (M_motor - M12) / J1
    domega2 = (M12 - M_load) / J2
    dM12 = C12 * (omega1 - omega2)

    return [domega1, domega2, dM12]


# Функция момента двигателя (пуск + работа)
def motor_torque(t):
    if t < 0.5:
        # Пусковой момент (обычно 2-2.5 от номинального)
        return 2.2 * M_nom * (t / 0.5)  # плавный пуск
    else:
        return 2.2 * M_nom  # постоянный пусковой момент


# Функция момента нагрузки
def load_torque(t, omega):
    # Момент нагрузки конвейера (постоянный + зависимый от скорости)
    if t < 2.0:
        return 0  # холостой ход
    elif t < 3.0:
        # Наброс нагрузки
        return 0.8 * M_nom * ((t - 2.0) / 1.0)
    else:
        return 0.8 * M_nom  # номинальная нагрузка


# Начальные условия
y0 = [0, 0, 0]  # omega1, omega2, M12

# Время моделирования
t = np.linspace(0, 5, 5000)

# Решение системы уравнений
solution = odeint(two_mass_system, y0, t, args=(motor_torque, load_torque))
omega1 = solution[:, 0]
omega2 = solution[:, 1]
M12 = solution[:, 2]

# Расчет ускорений
domega1 = np.gradient(omega1, t)
domega2 = np.gradient(omega2, t)

# Построение графиков
fig, axes = plt.subplots(3, 1, figsize=(10, 8))

# График скоростей
axes[0].plot(t, omega1 * 30 / np.pi, 'b-', label='ω1 (двигатель)', linewidth=1.5)
axes[0].plot(t, omega2 * 30 / np.pi, 'r--', label='ω2 (механизм)', linewidth=1.5)
axes[0].set_ylabel('Скорость, об/мин')
axes[0].legend()
axes[0].grid(True)
axes[0].set_title('Скорости вращения масс')

# График момента в упругой связи
axes[1].plot(t, M12, 'g-', linewidth=1.5)
axes[1].set_ylabel('Момент M12, Н·м')
axes[1].set_xlabel('Время, с')
axes[1].grid(True)
axes[1].set_title('Момент в упругой связи')
axes[1].axhline(y=M_nom, color='k', linestyle='--', label='Ном. момент')
axes[1].legend()

# График ускорений
axes[2].plot(t, domega1, 'b-', label='ε1 (двигатель)', linewidth=1)
axes[2].plot(t, domega2, 'r--', label='ε2 (механизм)', linewidth=1)
axes[2].set_ylabel('Ускорение, рад/с²')
axes[2].set_xlabel('Время, с')
axes[2].legend()
axes[2].grid(True)
axes[2].set_title('Ускорения масс')

plt.tight_layout()
plt.show()

# Вывод параметров модели
print("Параметры модели:")
print(f"Двигатель: АИР80А4")
print(f"Момент инерции двигателя J1 = {J1} кг·м²")
print(f"Момент инерции механизма J2 = {J2} кг·м²")
print(f"Жесткость связи C12 = {C12} Н·м/рад")
print(f"Номинальный момент M_nom = {M_nom:.2f} Н·м")
print(f"Номинальная скорость: {omega_nom * 30 / np.pi:.0f} об/мин")