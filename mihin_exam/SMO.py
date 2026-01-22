import numpy as np
import matplotlib.pyplot as plt
import random


def generate_data(n=30):
    # Первый массив: итерации от 1 до n
    array1 = np.arange(1, n + 1)

    array2 = [0, 0, 0, 1, 1, 1, 2, 3, 3, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9, 9, 10, 10, 11, 12, 12, 12]

    # СЛУЧАЙНОЕ РАСПРЕДЕЛЕНИЕ, РАСКОМЕНТИРОВАТЬ ЭТО ДЛЯ ПРОВЕРКИ РАБОТЫ ПРОГИ И ЗАКОМЕНТИТЬ array2 ВЫШЕ
    # Второй массив: случайные изменения
    # array2 = np.zeros(n)
    # array2[0] = 0  # начальное значение
    # for i in range(1, n):
    # # Генерируем случайное число от 0 до 1
    #     rand_val = random.random()
    #     # Если выпало 0.5 или больше, прибавляем 1 к предыдущему
    #     if rand_val >= 0.5:
    #         array2[i] = array2[i - 1] + 1
    #     else:
    #         array2[i] = array2[i - 1]  # оставляем как есть

    # Третий массив: второй массив делённый на первый массив
    array3 = array2 / array1

    return array1, array2, array3


# Основная часть программы
def main():
    # Запрос количества элементов у пользователя
    n = 30
    try:
        user_input = input("Введите количество элементов (по умолчанию 30): ")
        if user_input.strip():
            n = int(user_input)
            if n < 10:
                print("Минимум 10 элементов! Используется 10.")
                n = 10
    except:
        print("Используется значение по умолчанию: 30")

    # Запрос точности
    accuracy = 85
    try:
        user_input = input("Введите точность в % (по умолчанию 85): ")
        if user_input.strip():
            accuracy = float(user_input)
    except:
        print("Используется точность по умолчанию: 85%")

    # Генерация данных
    print(f"\nГенерация {n} элементов...")
    array1, array2, array3 = generate_data(n)

    # Вычисляем срединное значение только с 10-го элемента
    if n >= 10:
        center_value = np.median(array3[9:])  # с 10-го элемента (индекс 9)
        print(f"Срединное значение рассчитано по элементам с 10-го по {n}-й")
    else:
        center_value = np.median(array3)
        print(f"Срединное значение рассчитано по всем элементам")

    # ОКРУГЛЯЕМ СРЕДИННОЕ ЗНАЧЕНИЕ ДО СОТЫХ
    center_value = round(center_value, 2)

    # Вычисляем границы
    tolerance = (1 - accuracy / 100)
    upper_bound = center_value + tolerance * center_value
    lower_bound = center_value - tolerance * center_value

    # Ограничиваем от 0 до 1
    upper_bound = min(upper_bound, 1.0)
    lower_bound = max(lower_bound, 0.0)

    # ОКРУГЛЯЕМ ГРАНИЦЫ ДО СОТЫХ
    upper_bound = round(upper_bound, 2)
    lower_bound = round(lower_bound, 2)

    # Создаем массивы для горизонтальных линий
    center_line = np.full_like(array1, center_value)
    upper_line = np.full_like(array1, upper_bound)
    lower_line = np.full_like(array1, lower_bound)

    # Находим первую точку, которая вошла в диапазон и после которой все остальные в диапазоне
    special_point_idx = -1

    # Проверяем точки с начала
    for i in range(n):
        # Проверяем, находится ли текущая точка в диапазоне
        in_range = lower_bound <= array3[i] <= upper_bound

        if in_range:
            # Проверяем, все ли последующие точки тоже в диапазоне
            all_future_in_range = True
            for j in range(i + 1, n):
                if not (lower_bound <= array3[j] <= upper_bound):
                    all_future_in_range = False
                    break

            if all_future_in_range:
                special_point_idx = i
                break

    # Построение графика
    plt.figure(figsize=(12, 6))

    # Закрашиваем область между границами
    plt.fill_between(array1, lower_line, upper_line, color='lightgreen', alpha=0.3)

    # Основной график данных
    plt.plot(array1, array3, 'b-', linewidth=2, marker='o', markersize=6,
             markerfacecolor='blue', markeredgecolor='black')

    # Горизонтальные линии
    # 1. Центральная линия (срединное значение)
    plt.axhline(y=center_value, color='green', linestyle='--', linewidth=2,
                label=f'Срединное значение: {center_value:.2f}')

    # 2. Верхняя граница
    plt.axhline(y=upper_bound, color='green', linestyle=':', linewidth=1.5,
                label=f'Верхняя граница: {upper_bound:.2f}')

    # 3. Нижняя граница
    plt.axhline(y=lower_bound, color='green', linestyle=':', linewidth=1.5,
                label=f'Нижняя граница: {lower_bound:.2f}')

    # Отмечаем специальную точку, если она найдена
    if special_point_idx != -1:
        x_special = array1[special_point_idx]
        y_special = array3[special_point_idx]

        # Увеличиваем маркер для специальной точки
        plt.scatter([x_special], [y_special], s=200, color='red',
                    zorder=5, label='Точка входа')

        # Добавляем подробную информацию о точке
        info_text = (f'Точка входа (итерация {x_special}):\n'
                     f'Значение: {y_special:.4f}\n'
                     f'Срединное: {center_value:.2f}\n'
                     f'Отклонение: {y_special - center_value:+.4f}\n'
                     f'Все последующие точки в диапазоне')

        # Рисуем рамку с информацией
        plt.annotate(info_text,
                     xy=(x_special, y_special),
                     xytext=(15, 15),
                     textcoords='offset points',
                     fontsize=9,
                     bbox=dict(boxstyle="round,pad=0.5",
                               facecolor="yellow",
                               alpha=0.9,
                               edgecolor="red",
                               linewidth=2),
                     arrowprops=dict(arrowstyle="->",
                                     connectionstyle="arc3,rad=.2",
                                     color="red"))

    # Настройка графика
    plt.title(f'График с коридором точности {accuracy}%', fontsize=14)
    plt.xlabel('Первый массив (итерации)', fontsize=12)
    plt.ylabel('Третий массив (array2/array1)', fontsize=12)

    # Фиксируем ось Y от 0 до 1
    plt.ylim(0, 1)

    # Увеличиваем немного ось X для подписей
    plt.xlim(0.5, n + 2)

    # Сетка
    plt.grid(True, alpha=0.3)

    # Деления на оси Y
    plt.yticks(np.arange(0, 1.1, 0.1))

    # Легенда
    plt.legend(fontsize=9, loc='upper right')

    # Подписываем границы справа (ОКРУГЛЕННЫЕ ДО СОТЫХ)
    plt.text(array1[-1] + 0.5, upper_bound, f'Верх: {upper_bound:.2f}',
             fontsize=9, verticalalignment='center')
    plt.text(array1[-1] + 0.5, center_value, f'Центр: {center_value:.2f}',
             fontsize=9, verticalalignment='center')
    plt.text(array1[-1] + 0.5, lower_bound, f'Низ: {lower_bound:.2f}',
             fontsize=9, verticalalignment='center')

    plt.tight_layout()
    plt.show()

    # Простая статистика (ОКРУГЛЕННАЯ ДО СОТЫХ)
    print(f"\nСтатистика:")
    print(f"Срединное значение: {center_value:.2f}")
    print(f"Точность: {accuracy}%")
    print(f"Верхняя граница: {upper_bound:.2f}")
    print(f"Нижняя граница: {lower_bound:.2f}")
    print(f"Минимальное значение: {np.min(array3):.4f}")
    print(f"Максимальное значение: {np.max(array3):.4f}")

    # Информация о специальной точке
    if special_point_idx != -1:
        special_iteration = special_point_idx + 1
        n_critical = special_iteration * 2

        print(f"\n{'=' * 60}")
        print("ТОЧКА ВХОДА НАЙДЕНА:")
        print(f"{'=' * 60}")
        print(f"Итерация особой точки: {special_iteration}")
        print(f"Значение: {array3[special_point_idx]:.4f}")
        print(f"Срединное значение: {center_value:.2f}")
        print(f"Отклонение: {array3[special_point_idx] - center_value:+.4f}")
        print(f"Все точки с {special_iteration}-й по {n}-ю находятся в диапазоне")
        print(f"{'=' * 60}")
        print(f"N критическое = {special_iteration} * 2 = {n_critical}")
        print(f"{'=' * 60}")
    else:
        print(f"\nТочка входа не найдена")
        print("(Нет точки, после которой все остальные в диапазоне)")


if __name__ == "__main__":
    main()