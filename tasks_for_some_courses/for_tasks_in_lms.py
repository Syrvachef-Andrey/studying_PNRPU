import numpy as np
import matplotlib.pyplot as plt

# Данные
X = np.array([2, 4, 6, 8, 10, 11, 13, 14, 15, 16])
Y = np.array([4, 8, 2, 9, 5, 12, 9, 13, 10, 12])

# Коэффициенты параболы
A0 = 2.992
A1 = 0.381
A2 = 0.0138

print("Уравнение параболы:")
print(f"Y = {A0:.3f} + {A1:.3f}X + {A2:.4f}X²")

# Создаём точки для гладкой параболы
X_smooth = np.linspace(1, 17, 100)
Y_smooth = A0 + A1 * X_smooth + A2 * X_smooth**2

# Вычисляем предсказанные значения для исходных точек
Y_pred = A0 + A1 * X + A2 * X**2

# Построение графика
plt.figure(figsize=(12, 8))

# Парабола регрессии
plt.plot(X_smooth, Y_smooth, 'r-', linewidth=3,
         label=f'Y = {A0:.3f} + {A1:.3f}X + {A2:.4f}X²')

# Экспериментальные точки
plt.scatter(X, Y, color='blue', s=100, zorder=5,
           label='Экспериментальные точки')

# Линии ошибок (расстояния от точек до параболы)
for i in range(len(X)):
    plt.plot([X[i], X[i]], [Y[i], Y_pred[i]], 'g--', alpha=0.7, linewidth=1)

# Настройки графика
plt.title('Квадратичная регрессия', fontsize=14, pad=20)
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)

# Подписи точек
for i, (x, y) in enumerate(zip(X, Y)):
    plt.annotate(f'({x}, {y})', (x, y), xytext=(5, 10 if i % 2 == 0 else -15),
                 textcoords='offset points', fontsize=10,
                 ha='center', bbox=dict(boxstyle="round,pad=0.3",
                                       facecolor="lightblue", alpha=0.7))

# Вычисляем статистику
errors = Y - Y_pred
SSE = np.sum(errors**2)  # Сумма квадратов ошибок
MSE = SSE / len(X)       # Средняя квадратичная ошибка
RMSE = np.sqrt(MSE)      # Корень из средней квадратичной ошибки

# Добавляем информацию о качестве модели
plt.figtext(0.02, 0.02,
           f'Сумма квадратов ошибок (SSE) = {SSE:.2f}\n'
           f'Средняя квадратичная ошибка (MSE) = {MSE:.2f}\n'
           f'Корень из MSE (RMSE) = {RMSE:.2f}\n'
           f'Количество точек: n = {len(X)}',
           fontsize=10, bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8))

plt.xlim(1, 17)
plt.ylim(0, 16)
plt.tight_layout()
plt.show()

# Дополнительная таблица с расчётами
print("\n" + "="*50)
print("ТАБЛИЦА СРАВНЕНИЯ РЕАЛЬНЫХ И ПРЕДСКАЗАННЫХ ЗНАЧЕНИЙ")
print("="*50)
print(f"{'X':>3} {'Y_real':>8} {'Y_pred':>8} {'Ошибка':>8}")
print("-"*35)
for i in range(len(X)):
    print(f"{X[i]:3d} {Y[i]:8.1f} {Y_pred[i]:8.3f} {errors[i]:8.3f}")

print(f"\nСумма квадратов ошибок (SSE): {SSE:.4f}")
print(f"Средняя квадратичная ошибка (MSE): {MSE:.4f}")
print(f"Корень из MSE (RMSE): {RMSE:.4f}")

# Дополнительный график с остатками
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(X, errors, color='red', s=80)
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
plt.title('График остатков')
plt.xlabel('X')
plt.ylabel('Ошибка (Y - Ŷ)')
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.scatter(Y_pred, errors, color='purple', s=80)
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
plt.title('Остатки vs Предсказанные значения')
plt.xlabel('Предсказанное Y (Ŷ)')
plt.ylabel('Ошибка (Y - Ŷ)')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Проверка коэффициентов через встроенную функцию numpy
print("\n" + "="*50)
print("ПРОВЕРКА ЧЕРЕЗ NUMPY (np.polyfit)")
print("="*50)

# Используем polyfit для проверки (коэффициенты в обратном порядке)
coefficients_np = np.polyfit(X, Y, 2)
print(f"Коэффициенты через np.polyfit:")
print(f"A2 = {coefficients_np[0]:.4f}")
print(f"A1 = {coefficients_np[1]:.4f}")
print(f"A0 = {coefficients_np[2]:.4f}")

print(f"\nСравнение с нашими вычислениями:")
print(f"A2: наше = {A2:.4f}, numpy = {coefficients_np[0]:.4f}")
print(f"A1: наше = {A1:.4f}, numpy = {coefficients_np[1]:.4f}")
print(f"A0: наше = {A0:.4f}, numpy = {coefficients_np[2]:.4f}")