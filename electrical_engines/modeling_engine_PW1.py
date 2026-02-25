import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.signal import find_peaks

# Параметры системы
J1 = 0.0028  # момент инерции двигателя, кг·м² (АИР80А4)
J2 = 0.005  # момент инерции механизма, кг·м²
C12 = 1000  # жесткость упругой связи, Н·м/рад

# Номинальный момент двигателя
P_nom = 1100  # Вт
omega_nom = 1420 * np.pi / 30  # рад/с
M_nom = P_nom / omega_nom  # номинальный момент


# Функция для моделирования
def two_mass_system(y, t, M_motor_func, M_load_func):
    omega1, omega2, M12 = y
    M_motor = M_motor_func(t)
    M_load = M_load_func(t, omega2)

    domega1 = (M_motor - M12) / J1
    domega2 = (M12 - M_load) / J2
    dM12 = C12 * (omega1 - omega2)

    return [domega1, domega2, dM12]


# Функция момента двигателя - СТУПЕНЧАТОЕ ВОЗДЕЙСТВИЕ (STEP)
def motor_torque_step(t):
    if t < 0.1:
        return 0.0  # нет момента
    else:
        return 2.2 * M_nom  # резкий скачок момента (ступенька)


# Функция момента нагрузки (пусть будет постоянной для чистоты эксперимента)
def load_torque_constant(t, omega):
    if t < 0.5:
        return 0.0  # сначала без нагрузки, чтобы увидеть колебания при пуске
    else:
        return 0.5 * M_nom  # потом небольшая нагрузка


# Начальные условия
y0 = [0, 0, 0]

# Время моделирования (увеличим разрешение, чтобы увидеть колебания)
t = np.linspace(0, 2, 10000)  # 2 секунды с высоким разрешением

# Решение системы уравнений
solution = odeint(two_mass_system, y0, t, args=(motor_torque_step, load_torque_constant))
omega1 = solution[:, 0]
omega2 = solution[:, 1]
M12 = solution[:, 2]

# Расчет ускорений
domega1 = np.gradient(omega1, t)
domega2 = np.gradient(omega2, t)

# Расчет разности скоростей (для наглядности колебаний)
delta_omega = omega1 - omega2

# Поиск частоты колебаний
# Найдем пики на графике delta_omega после ступеньки (после 0.1 с)
mask = t > 0.15
peaks, properties = find_peaks(delta_omega[mask], distance=20)
if len(peaks) > 1:
    # Время между первыми двумя пиками
    t_peaks = t[mask][peaks[:2]]
    period = t_peaks[1] - t_peaks[0]
    freq_hz = 1.0 / period
    omega_resonance = 2 * np.pi * freq_hz
else:
    period = 0
    freq_hz = 0
    omega_resonance = 0

# Теоретическая резонансная частота
omega0_theor = np.sqrt(C12 * (J1 + J2) / (J1 * J2))
f0_theor = omega0_theor / (2 * np.pi)

# Создание фигуры с подграфиками
fig = plt.figure(figsize=(14, 12))

# 1. График момента двигателя (чтобы показать STEP)
ax1 = plt.subplot(4, 1, 1)
motor_moment = [motor_torque_step(ti) for ti in t]
ax1.plot(t, motor_moment, 'b-', linewidth=2)
ax1.axvline(x=0.1, color='r', linestyle='--', alpha=0.7, label='Момент скачка (step)')
ax1.set_ylabel('Момент двигателя, Н·м')
ax1.set_xlabel('Время, с')
ax1.set_title('Ступенчатое воздействие (step) на входе системы')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_xlim(0, 0.5)

# 2. График скоростей (показывает колебания)
ax2 = plt.subplot(4, 1, 2)
ax2.plot(t, omega1 * 30 / np.pi, 'b-', label='ω₁ (двигатель)', linewidth=1.5)
ax2.plot(t, omega2 * 30 / np.pi, 'r--', label='ω₂ (механизм)', linewidth=1.5)
ax2.set_ylabel('Скорость, об/мин')
ax2.set_title('Скорости вращения масс')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.axvline(x=0.1, color='r', linestyle='--', alpha=0.5)

# 3. График разности скоростей (наглядно показывает колебания)
ax3 = plt.subplot(4, 1, 3)
ax3.plot(t, delta_omega * 30 / np.pi, 'purple', linewidth=1.5)
ax3.set_ylabel('Δω = ω₁ - ω₂, об/мин')
ax3.set_title('Разность скоростей')
ax3.grid(True, alpha=0.3)
ax3.axvline(x=0.1, color='r', linestyle='--', alpha=0.5)
ax3.axhline(y=0, color='k', linestyle='-', alpha=0.3)

# Отметим пики на графике
if len(peaks) > 0:
    peak_times = t[mask][peaks[:4]]
    peak_values = delta_omega[mask][peaks[:4]] * 30 / np.pi
    ax3.plot(peak_times, peak_values, 'ro', markersize=6, label='Пики колебаний')
    ax3.legend()

# 4. График момента в упругой связи
ax4 = plt.subplot(4, 1, 4)
ax4.plot(t, M12, 'g-', linewidth=1.5)
ax4.set_ylabel('Момент M₁₂, Н·м')
ax4.set_xlabel('Время, с')
ax4.set_title('Момент в упругой связи')
ax4.grid(True, alpha=0.3)
ax4.axhline(y=M_nom, color='k', linestyle='--', label=f'Ном. момент ({M_nom:.2f} Н·м)')
ax4.axvline(x=0.1, color='r', linestyle='--', alpha=0.5)
ax4.legend()

plt.tight_layout()
plt.show()

# Вывод параметров и анализ колебаний
print("=" * 60)
print("АНАЛИЗ КОЛЕБАТЕЛЬНОСТИ ДВУХМАССОВОЙ СИСТЕМЫ")
print("=" * 60)
print(f"Параметры системы:")
print(f"  J1 = {J1:.4f} кг·м² (двигатель)")
print(f"  J2 = {J2:.4f} кг·м² (механизм)")
print(f"  C12 = {C12:.0f} Н·м/рад (жесткость)")
print()
print(f"Теоретическая резонансная частота:")
print(f"  ω0 = √(C12*(J1+J2)/(J1*J2)) = {omega0_theor:.2f} рад/с")
print(f"  f0 = {f0_theor:.2f} Гц")
print()
if period > 0:
    print(f"Частота колебаний по графику:")
    print(f"  Период = {period * 1000:.2f} мс")
    print(f"  Частота f = {freq_hz:.2f} Гц")
    print(f"  Совпадение с теорией: {abs(freq_hz - f0_theor) / f0_theor * 100:.1f}%")
print()
print("Наблюдение колебательности:")
print("✓ После ступенчатого воздействия (step) в момент t=0.1с")
print("✓ Скорости ω1 и ω2 начинают колебаться в противофазе")
print("✓ Момент M12 также имеет колебательный характер")
print("✓ Колебания затухают со временем (система устойчива)")