import matplotlib.pyplot as plt
import numpy as np

# Номинальные данные
K_nom = 1.883
omega_nom = 104.67
omega_0 = 220 / K_nom  # ≈ 116.83

# Экспериментальные данные
I_est = [0.65, 1.6, 2.64, 3.7, 5.72]
w_est = [131.74, 127.44, 123.36, 122.21, 111.00]

I_reo1 = [0.76, 1.7, 2.7, 3.7, 4.7]
w_reo1 = [122.52, 113.10, 106.82, 97.38, 84.82]

I_reo2 = [0.77, 1.7, 2.7, 4.95, 5.3]
w_reo2 = [113.10, 91.11, 64.93, 0.0, -10.47]

I_osl = [0.75, 1.7, 2.7, 3.7, 5.0]
w_osl = [104.72, 99.48, 98.44, 97.38, 97.38]

I_din1 = [0.0, -1.44, -2.4, -3.4, -4.4]
w_din1 = [0.0, 13.61, 25.13, 37.70, 49.74]

I_din2 = [0.0, -0.8, -1.8, -2.8, -3.0, -3.8]
w_din2 = [0.0, 18.33, 48.69, 73.30, 76.45, 97.38]

# Построение
plt.figure(figsize=(10, 7))

plt.plot(I_est, w_est, 'o-', label='Естественная (эксп.)', linewidth=2, markersize=8)
plt.plot(I_reo1, w_reo1, 's-', label='Реостатная Rд1', linewidth=2, markersize=8)
plt.plot(I_reo2, w_reo2, '^-', label='Противовключение Rд2', linewidth=2, markersize=8)
plt.plot(I_osl, w_osl, 'd-', label='Ослабленный поток', linewidth=2, markersize=8)
plt.plot(I_din1, w_din1, '*-', label='Динамическое Rт1', linewidth=2, markersize=8)
plt.plot(I_din2, w_din2, 'x-', label='Динамическое Rт2', linewidth=2, markersize=8)

# Расчётная точка холостого хода
plt.scatter(0, omega_0, color='red', s=120, zorder=5, label=f'ω₀ расч. = {omega_0:.2f} рад/с')
plt.scatter(0, omega_nom, color='blue', s=100, zorder=5, label=f'ωн = {omega_nom} рад/с')

# Оформление
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlabel('Ток якоря Iя, А')
plt.ylabel('Угловая скорость ω, рад/с')
plt.title('Статические электромеханические характеристики ДПТ НВ')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='best')
plt.xlim(-5, 7)
plt.ylim(-20, 160)

plt.tight_layout()
plt.show()