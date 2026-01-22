import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
queues = [0, 1, 2, 3]  # Количество очередей
throughput = [7.0, 8.6, 9.0, 8.8]  # Пропускная способность
waiting_time = [0.0, 2.467, 4.08, 4.08]  # Среднее время ожидания в очереди

# Преобразуем в numpy массивы
queues_arr = np.array(queues)
throughput_arr = np.array(throughput)
waiting_time_arr = np.array(waiting_time)

# 1. Нормализуем данные (приводим к диапазону 0-1)
def normalize(data):
    """Нормализация данных к диапазону 0-1"""
    min_val = np.min(data)
    max_val = np.max(data)
    if max_val == min_val:
        return np.ones_like(data) * 0.5
    return (data - min_val) / (max_val - min_val)

# Нормализуем пропускную способность (чем больше, тем лучше)
norm_throughput = normalize(throughput_arr)

# Нормализуем время ожидания (чем меньше, тем лучше, поэтому инвертируем)
norm_waiting_inv = 1 - normalize(waiting_time_arr)

# 2. Создаем третью линию: разность нормализованных линий
difference = norm_throughput - norm_waiting_inv

# 3. Находим экстремум (максимум) разности
max_diff_idx = np.argmax(difference)
max_diff_value = difference[max_diff_idx]
opt_queue = queues[max_diff_idx]

# 4. Строим график
plt.figure(figsize=(10, 6))

# Линия 1: Нормированная пропускная способность
plt.plot(queues, norm_throughput, 'o-', linewidth=2, markersize=8,
         label='Пропускная способность (норм.)', color='blue')

# Линия 2: Инвертированное нормированное время ожидания
plt.plot(queues, norm_waiting_inv, 's-', linewidth=2, markersize=8,
         label='Время ожидания (норм., инв.)', color='red')

# Линия 3: Разность двух линий
plt.plot(queues, difference, '^-', linewidth=3, markersize=10,
         label='Разность (Пропуск. - Время ожид.)', color='green')

# Отмечаем точку экстремума
plt.plot(opt_queue, max_diff_value, '*', markersize=20, color='gold',
         markeredgecolor='black', markeredgewidth=2,
         label=f'Экстремум ({opt_queue} очередь)')

# Настройки графика
plt.xlabel('Количество очередей', fontsize=12)
plt.ylabel('Нормированные значения', fontsize=12)
plt.title('Анализ эффективности СМО: 3 линии с экстремумом', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(loc='best')
plt.xticks(queues)  # Всегда показываем все значения по оси X

# Добавляем аннотацию с экстремумом
plt.annotate(f'Максимум разности\nОчередей: {opt_queue}\nЗначение: {max_diff_value:.3f}',
             xy=(opt_queue, max_diff_value),
             xytext=(opt_queue+0.3, max_diff_value-0.1),
             arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
             fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.8))

# Добавляем горизонтальную линию через 0 для reference
plt.axhline(y=0, color='gray', linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()

# 5. Выводим результаты в консоль
print("=" * 60)
print("РЕЗУЛЬТАТЫ АНАЛИЗА")
print("=" * 60)
print(f"{'Очереди':<10} {'Пропускная':<12} {'Время ожид.':<12} {'Разность':<12}")
print(f"{'':<10} {'(норм.)':<12} {'(норм., инв.)':<12} {'(П-В)':<12}")
print("-" * 60)

for i, q in enumerate(queues):
    print(f"{q:<10} {norm_throughput[i]:<12.3f} {norm_waiting_inv[i]:<12.3f} {difference[i]:<12.3f}")

print("=" * 60)
print(f"\nОПТИМАЛЬНОЕ РЕШЕНИЕ:")
print(f"Количество очередей: {opt_queue}")
print(f"Максимальная разность: {max_diff_value:.3f}")
print(f"Пропускная способность (исходная): {throughput[opt_queue]:.1f}")
print(f"Время ожидания (исходное): {waiting_time[opt_queue]:.3f}")
print("\nИНТЕРПРЕТАЦИЯ:")
print("Положительная разность означает, что преимущество пропускной")
print("способности преобладает над недостатком времени ожидания.")
print("Максимальная разность показывает оптимальный баланс.")
print("=" * 60)
