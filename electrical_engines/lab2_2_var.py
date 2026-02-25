import matplotlib.pyplot as plt

# Данные для характеристик динамического торможения
# Точки (0,0) добавляются, так как момент равен 0 при нулевой скорости

# Таблица 5: It = 2.5 A, Rt = 0
m5 = [0, 2.92, 4.56, 5.21, 5.33, 5.53]
w5 = [0, 20.94, 51.83, 65.97, 86.91, 140.31]

# Таблица 6: It = 2.5 A, Rt = Rt1
m6 = [0, 2.26, 3.8, 4.7, 5.61, 5.97]
w6 = [0, 26.18, 53.4, 84.82, 109.95, 134.55]

# Таблица 7: It = 3.25 A, Rt = 0
m7 = [0, 4.13, 7.09, 9.3, 9.8, 10.13]
w7 = [0, 23.77, 50.26, 78.53, 94.24, 109.95]

# Таблица 8: It = 3.25 A, Rt = Rt1
m8 = [0, 1.85, 3.71, 5.75, 6.71, 7.83]
w8 = [0, 32.98, 58.64, 80.63, 91.62, 100.52]

# Перевод моментов во 2-й квадрант (M < 0)
m5_neg = [-x for x in m5]
m6_neg = [-x for x in m6]
m7_neg = [-x for x in m7]
m8_neg = [-x for x in m8]

plt.figure(figsize=(10, 7))

# Отрисовка сплошными линиями разных цветов с маркерами
plt.plot(m5_neg, w5, 'o-', label='It=2.5A, Rt=0 (Табл. 5)', linewidth=2)
plt.plot(m6_neg, w6, 's-', label='It=2.5A, Rt=Rt1 (Табл. 6)', linewidth=2)
plt.plot(m7_neg, w7, 'v-', label='It=3.25A, Rt=0 (Табл. 7)', linewidth=2)
plt.plot(m8_neg, w8, 'd-', label='It=3.25A, Rt=Rt1 (Табл. 8)', linewidth=2)

# Оформление
plt.title('Cтатические механические характеристики ω(M)\n в режиме динамического торможения с независимым возбуждением', fontsize=14)
plt.xlabel('Тормозной момент M, Н·м', fontsize=12)
plt.ylabel('Угловая скорость $\omega$, рад/с', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Отображение осей
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Легенда
plt.legend(fontsize=10, loc='upper left')

# Настройка границ осей для наглядности
plt.xlim(min(m7_neg) - 1, 0.5)
plt.ylim(-5, max(w5) + 10)

plt.show()