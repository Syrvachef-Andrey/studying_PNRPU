import numpy as np
import matplotlib.pyplot as plt

# 1. Исходные данные
Pn = 1100        # Номинальная мощность (Вт)
w0 = 104.67      # Синхронная угловая скорость (рад/с)
n0 = 1000        # Синхронная скорость (об/мин)
n_nom = 940      # Номинальная скорость из опыта (об/мин)
lambda_m = 2     # Перегрузочная способность (Mmax/Mnom)

# 2. Расчет промежуточных параметров
Sn = (n0 - n_nom) / n0   # Номинальное скольжение (0.06)
wn_rad = n_nom / 9.55    # Номинальная угловая скорость (~98.4 рад/с)
M_nom = Pn / wn_rad      # Номинальный момент (~11.18 Нм)
M_max = lambda_m * M_nom # Максимальный (критический) момент (~22.35 Нм)

# Критическое скольжение (S_k) по методичке: Sk = Sn * (lambda + sqrt(lambda^2 - 1))
Sk = Sn * (lambda_m + np.sqrt(lambda_m**2 - 1)) # ~0.224

# 3. Генерация данных по формуле Клосса
# Задаем диапазон скольжения S от 0.001 (близко к холостому ходу) до 1 (пуск)
S = np.linspace(0.001, 1, 500)
# Формула Клосса: M = (2 * Mmax) / (S/Sk + Sk/S)
M = (2 * M_max) / (S/Sk + Sk/S)
# Угловая скорость: w = w0 * (1 - S)
W = w0 * (1 - S)

# 4. Построение графика
plt.figure(figsize=(10, 6))
plt.plot(W, M, label='Естественная характеристика (Клосс)', color='blue', linewidth=2.5)

# Отметка ключевых точек
plt.scatter([wn_rad], [M_nom], color='green', zorder=5, label=f'Номинальный режим ($M_н={M_nom:.2f}$ Нм)')
plt.scatter([w0 * (1 - Sk)], [M_max], color='red', zorder=5, label=f'Критический режим ($M_{{max}}={M_max:.2f}$ Нм)')

# Оформление
plt.title('Естественная механическая характеристика асинхронного двигателя $M(\omega)$', fontsize=14)
plt.xlabel('Угловая скорость $\omega$, рад/с', fontsize=12)
plt.ylabel('Электромагнитный момент M, Н·м', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.legend(fontsize=11)
plt.xlim(0, 110)
plt.ylim(0, 25)

plt.show()