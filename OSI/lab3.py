import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid
from scipy import signal

# Добавлен файл ninety.txt в список
files = [
    ('zero.txt', '0% помех'),
    ('five.txt', '5% помех'),
    ('thirty.txt', '30% помех'),
    ('sixty.txt', '60% помех'),
    ('ninty.txt', '90% помех')
]

# Задаем уникальные цвета для каждого уровня помех, чтобы графики не сливались
colors = ['black', 'blue', 'orange', 'green', 'red']


def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().replace(',', '.')
    data = np.loadtxt(content.splitlines())
    t = data[:, 0]
    u = data[:, 1]
    y = data[:, 2]
    return t, u, y


plt.figure(figsize=(14, 8))

print(f"{'Файл':<12} | {'a3':>10} | {'a2':>10} | {'a1':>10} | {'a0':>10}")
print("-" * 62)  # Исправлена синтаксическая ошибка печати разделителя

N_points = 101
y_zero = None

for idx, (fname, label) in enumerate(files):
    t, u, y = load_data(fname)
    c = colors[idx]

    iy1 = cumulative_trapezoid(y, t, initial=0)
    iy2 = cumulative_trapezoid(iy1, t, initial=0)
    iy3 = cumulative_trapezoid(iy2, t, initial=0)

    iu1 = cumulative_trapezoid(u, t, initial=0)
    iu2 = cumulative_trapezoid(iu1, t, initial=0)
    iu3 = cumulative_trapezoid(iu2, t, initial=0)

    A = np.column_stack([y[:N_points], iy1[:N_points], iy2[:N_points], iy3[:N_points]])
    B = iu3[:N_points]

    coeffs, _, _, _ = np.linalg.lstsq(A, B, rcond=None)
    a3, a2, a1, a0 = coeffs
    print(f"{fname:<12} | {a3:10.4f} | {a2:10.4f} | {a1:10.4f} | {a0:10.4f}")

    sys = signal.TransferFunction([1.0], [a3, a2, a1, a0])
    t_sim, y_sim = signal.step(sys, T=t)

    # Отрисовка чистого сигнала один раз для ориентира
    if idx == 0:
        y_zero = y.copy()
        plt.plot(t, y_zero, color='black', linestyle='--', linewidth=2.5, label='Чистый сигнал (0%)')
        plt.plot(t_sim, y_sim, color='black', linewidth=1.5, label='Модель (0%)')
    else:
        # Исходные данные с шумом рисуем точками, чтобы они не перекрывали линии моделей
        plt.plot(t, y, '.', color=c, alpha=0.25, label=f'Эксп. {label}')

        # Если модель не ушла в бесконечность из-за шума, рисуем её
        if np.max(np.abs(y_sim)) < 10:
            plt.plot(t_sim, y_sim, '-', color=c, linewidth=2, label=f'Модель {label}')

plt.title("Идентификация параметров МНК (от 0% до 90% помех)")
plt.xlabel('Время t, с')
plt.ylabel('Выход y(t)')
plt.grid(True)

# Легенда разбита на 2 колонки, чтобы уместить все 9-10 элементов
plt.legend(fontsize=10, loc='lower right', ncol=2)
plt.tight_layout()
plt.show()