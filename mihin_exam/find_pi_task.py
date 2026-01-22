import random
import math


def estimate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        # Генерируем случайные точки в квадрате [0,1]×[0,1]
        x = random.random()  # 0..1
        y = random.random()  # 0..1

        # Проверяем, попадает ли точка в четверть круга
        # (x² + y² <= 1)
        if x * x + y * y <= 1.0:
            points_inside_circle += 1

    # Отношение площади четверти круга к площади квадрата = π/4
    # Поэтому π ≈ 4 * (точки в круге / все точки)
    return 4.0 * points_inside_circle / num_points


# Параметры
num_points = 10000  # Количество случайных точек

# Оценка π
pi_estimate = estimate_pi(num_points)

# Вывод результатов
print(f"Количество точек: {num_points}")
print(f"Оценка π: {pi_estimate}")
print(f"Точное π: {math.pi}")
print(f"Разница: {abs(pi_estimate - math.pi)}")
print(f"Округление до 1 знака: {round(pi_estimate, 1)}")