import matplotlib.pyplot as plt

# --- 1. ВВОД ДАННЫХ ---
w_1 = [189.53, 186.39, 180.10, 178.01, 176.96]  # Основная (220В)
w_2 = [174.87, 168.59, 166.49, 162.30, 158.12]  # 200В
w_3 = [126.70, 124.61, 118.32, 116.23, 115.18]  # 150В
w_4 = [83.77, 77.49, 73.30, 73.30, 72.25]  # 100В
w_5 = [61.78, 54.45, 52.36, 50.26, 47.12]  # 75В
w_6 = [219.90, 207.33, 198.95, 197.91, 190.58]  # Ослабл. поле (220В)

Iy_1 = [0.20, 0.29, 0.35, 0.39, 0.44]
Iy_2 = [0.21, 0.28, 0.33, 0.37, 0.41]
Iy_3 = [0.20, 0.24, 0.28, 0.31, 0.34]
Iy_4 = [0.18, 0.20, 0.23, 0.25, 0.27]
Iy_5 = [0.17, 0.19, 0.20, 0.22, 0.23]
Iy_6 = [0.24, 0.32, 0.39, 0.43, 0.48]

M_1 = [0.231, 0.341, 0.425, 0.479, 0.543]
M_2 = [0.239, 0.331, 0.394, 0.453, 0.515]
M_3 = [0.236, 0.287, 0.353, 0.397, 0.439]
M_4 = [0.214, 0.256, 0.311, 0.338, 0.370]
M_5 = [0.205, 0.259, 0.284, 0.325, 0.362]
M_6 = [0.239, 0.338, 0.429, 0.475, 0.550]

labels = [
    'Основная (220В, Iв=Iвн)',
    'Сниженное (200В)',
    'Сниженное (150В)',
    'Сниженное (100В)',
    'Сниженное (75В)',
    'Ослаб. поле (220В, Iв<Iвн)'
]
colors = ['blue', 'green', 'orange', 'red', 'purple', 'magenta']
markers = ['o', 's', '^', 'D', 'v', 'x']

# --- 2. ПОСТРОЕНИЕ ГРАФИКОВ ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Отрисовка линий
ax1.plot(Iy_1, w_1, marker=markers[0], color=colors[0], label=labels[0], linewidth=2)
ax1.plot(Iy_2, w_2, marker=markers[1], color=colors[1], label=labels[1], linewidth=2)
ax1.plot(Iy_3, w_3, marker=markers[2], color=colors[2], label=labels[2], linewidth=2)
ax1.plot(Iy_4, w_4, marker=markers[3], color=colors[3], label=labels[3], linewidth=2)
ax1.plot(Iy_5, w_5, marker=markers[4], color=colors[4], label=labels[4], linewidth=2)
ax1.plot(Iy_6, w_6, marker=markers[5], color=colors[5], label=labels[5], linewidth=2)

ax2.plot(M_1, w_1, marker=markers[0], color=colors[0], label=labels[0], linewidth=2)
ax2.plot(M_2, w_2, marker=markers[1], color=colors[1], label=labels[1], linewidth=2)
ax2.plot(M_3, w_3, marker=markers[2], color=colors[2], label=labels[2], linewidth=2)
ax2.plot(M_4, w_4, marker=markers[3], color=colors[3], label=labels[3], linewidth=2)
ax2.plot(M_5, w_5, marker=markers[4], color=colors[4], label=labels[4], linewidth=2)
ax2.plot(M_6, w_6, marker=markers[5], color=colors[5], label=labels[5], linewidth=2)

# --- 3. НАСТРОЙКА ОСЕЙ (Стиль "как в учебнике") ---
titles = ['Электромеханические характеристики $\omega(I_я)$', 'Механические характеристики $\omega(M)$']
x_labels = ['Ток якоря $I_я$, А', 'Момент $M$, Н·м']

for ax, xlabel, title in zip([ax1, ax2], x_labels, titles):
    # Убираем верхнюю и правую рамки
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Сдвигаем левую и нижнюю оси к нулю
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    # Делаем оси более жирными
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)

    # Добавляем стрелочки на концах осей
    ax.plot((1), (0), ls="", marker=">", ms=8, color="k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (1), ls="", marker="^", ms=8, color="k", transform=ax.get_xaxis_transform(), clip_on=False)

    # Задаем лимиты графика (чтобы начинался строго от 0)
    ax.set_xlim(left=0, right=0.6)
    ax.set_ylim(bottom=0, top=250)

    # Добавляем подписи осей рядом со стрелочками
    ax.text(0.58, -10, xlabel, fontsize=12, fontweight='bold', ha='right')
    ax.text(-0.02, 245, '$\omega$, с$^{-1}$', fontsize=12, fontweight='bold', ha='right')

    # Заголовок, сетка и легенда
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(fontsize=10, loc='lower right')

plt.tight_layout()
plt.show()