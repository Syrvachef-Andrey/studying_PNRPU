import numpy as np
import matplotlib.pyplot as plt
import random


def generate_data(n=30):
    """Генерация трёх массивов"""
    # Первый массив: итерации от 1 до n
    array1 = np.arange(1, n + 1)

    # Второй массив: случайные изменения
    array2 = np.zeros(n)
    array2[0] = 0 # начальное значение

    for i in range(1, n):
        # Генерируем случайное число от 0 до 1
        rand_val = random.random()
        # Если выпало 0.5 или больше, прибавляем 1 к предыдущему
        if rand_val >= 0.5:
            array2[i] = array2[i - 1] + 1
        else:
            array2[i] = array2[i - 1]  # оставляем как есть

    # Третий массив: второй массив делённый на первый массив
    array3 = array2 / array1

    return array1, array2, array3


def print_data(array1, array2, array3):
    """Вывод данных в табличном виде"""
    print("\n" + "=" * 60)
    print("Сгенерированные данные:")
    print("=" * 60)
    print(f"{'i':>3} | {'Первый':>8} | {'Второй':>8} | {'Третий':>8}")
    print("-" * 60)

    for i in range(len(array1)):
        print(f"{i + 1:3d} | {array1[i]:8.1f} | {array2[i]:8.2f} | {array3[i]:8.4f}")

    print("=" * 60)
    print(f"Среднее третьего массива: {np.mean(array3):.4f}")
    print(f"Медиана третьего массива: {np.median(array3):.4f}")
    print(f"Максимум третьего массива: {np.max(array3):.4f}")
    print(f"Минимум третьего массива: {np.min(array3):.4f}")


# Основная часть программы
def main():
    # Запрос количества элементов у пользователя
    while True:
        try:
            n = int(input("Введите количество элементов (по умолчанию 30): ") or "30")
            if n > 0:
                break
            else:
                print("Число должно быть положительным!")
        except ValueError:
            print("Пожалуйста, введите целое число!")

    # Генерация данных
    print(f"\nГенерация {n} элементов...")
    array1, array2, array3 = generate_data(n)

    # Вывод данных
    print_data(array1, array2, array3)

    # Построение итогового графика
    print("\nПостроение графика (ось Y ограничена от 0 до 1)...")

    plt.figure(figsize=(14, 8))

    # Основной график
    plt.plot(array1, array3, 'b-', linewidth=3, marker='o', markersize=8,
             markerfacecolor='red', markeredgecolor='black', markeredgewidth=1.5,
             label='Третий массив (array2/array1)')

    # Добавляем аннотации для некоторых точек
    step = max(1, len(array1) // 8)  # Показываем примерно 8 аннотаций
    for i in range(0, len(array1), step):
        plt.annotate(f'{array3[i]:.3f}',
                     xy=(array1[i], array3[i]),
                     xytext=(10, 10), textcoords='offset points',
                     fontsize=10, fontweight='bold',
                     bbox=dict(boxstyle="round,pad=0.4",
                               facecolor="yellow", alpha=0.8,
                               edgecolor='black'))

    # Линия тренда
    z = np.polyfit(array1, array3, 1)
    p = np.poly1d(z)
    plt.plot(array1, p(array1), "r--", linewidth=2, alpha=0.8,
             label=f'Линейный тренд: y = {z[0]:.4f}x + {z[1]:.4f}')

    # ВЕРТИКАЛЬНЫЕ ЛИНИИ для каждого деления на оси X
    for x_val in array1:
        plt.axvline(x=x_val, color='gray', linestyle=':', alpha=0.3, linewidth=0.7)

    # ГОРИЗОНТАЛЬНЫЕ ЛИНИИ для делений на оси Y
    for y_val in np.arange(0, 1.1, 0.1):
        plt.axhline(y=y_val, color='gray', linestyle=':', alpha=0.3, linewidth=0.7)
        # Подписываем основные горизонтальные линии
        if y_val in [0, 0.2, 0.4, 0.6, 0.8, 1.0]:
            plt.axhline(y=y_val, color='black', linestyle='--', alpha=0.5, linewidth=1)

    # Настройки графика
    plt.title(f'График: Третий массив по первому массиву (n={n})',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Первый массив (array1 = итерации)', fontsize=14)
    plt.ylabel('Третий массив (array3 = array2/array1)', fontsize=14)
    plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.7)

    # ФИКСИРУЕМ ОСЬ Y ОТ 0 ДО 1
    plt.ylim(0, 1)

    # Настройка осей
    plt.xticks(array1[::max(1, n // 10)], fontsize=10)  # показываем каждую n/10-ю метку
    plt.yticks(np.arange(0, 1.1, 0.1), fontsize=10)  # деления с шагом 0.1

    # Легенда
    plt.legend(fontsize=12, loc='upper right', framealpha=0.9)

    # Добавляем дополнительную информацию на график
    plt.text(0.02, 0.98,
             f'Среднее: {np.mean(array3):.4f}\nМедиана: {np.median(array3):.4f}\nМакс: {np.max(array3):.4f}\nМин: {np.min(array3):.4f}',
             transform=plt.gca().transAxes,
             verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
             fontsize=10)

    # Добавляем закрашенную область между графиком и осью X
    plt.fill_between(array1, 0, array3, alpha=0.2, color='blue')

    # Подпись оси Y с пояснением
    plt.text(-0.05, 0.5, 'Диапазон: [0, 1]',
             transform=plt.gca().transAxes,
             rotation=90, verticalalignment='center',
             fontsize=10, fontweight='bold',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

    plt.tight_layout()
    plt.show()

    # Также можно показать простую статистику
    print("\nСтатистика третьего массива:")
    print("-" * 40)
    print(f"Диапазон значений: от {np.min(array3):.4f} до {np.max(array3):.4f}")
    print(f"Среднее значение: {np.mean(array3):.4f}")
    print(f"Стандартное отклонение: {np.std(array3):.4f}")
    print(f"Процент значений > 0.5: {np.sum(array3 > 0.5) / len(array3) * 100:.1f}%")
    print(f"Процент значений < 0.2: {np.sum(array3 < 0.2) / len(array3) * 100:.1f}%")


if __name__ == "__main__":
    main()