# Уточненный метод Эйлера (модифицированный, Эйлера-Коши)

# Параметры
h = 0.25  # шаг интегрирования
t_end = 1.0  # конечное время
y = 1.0  # начальное условие y(0)
z = 0.5  # начальное условие z(0)
t = 0.0  # начальное время

print("Уточненный метод Эйлера для системы:")
print("dy/dt = -2y + x, где x(t) = t - 0.01")
print("dz/dt = 0.1y - 3z - y*z")
print(f"Шаг h = {h}")
print()

print(f"{'t':>4} {'x(t)':>8} {'y':>10} {'z':>10}")
print("-" * 40)

step = 0
print(f"{t:4.2f} {t - 0.01:8.4f} {y:10.6f} {z:10.6f}")

# Цикл интегрирования
while t < t_end:
    # Текущие производные
    x_curr = t - 0.01
    f1_curr = -2 * y + x_curr  # dy/dt в текущей точке
    f2_curr = 0.1 * y - 3 * z - y * z  # dz/dt в текущей точке

    # Предиктор (предсказание) - обычный метод Эйлера
    y_pred = y + h * f1_curr
    z_pred = z + h * f2_curr

    # Производные в прогнозируемой точке
    x_next = (t + h) - 0.01
    f1_pred = -2 * y_pred + x_next  # dy/dt в прогнозируемой точке
    f2_pred = 0.1 * y_pred - 3 * z_pred - y_pred * z_pred  # dz/dt в прогнозируемой точке

    # Корректор (уточнение) - среднее производных
    y = y + h * (f1_curr + f1_pred) / 2
    z = z + h * (f2_curr + f2_pred) / 2
    t = t + h

    step += 1
    print(f"{t:4.2f} {x_next:8.4f} {y:10.6f} {z:10.6f}")

print("-" * 40)
print(f"Результат в t = {t_end}:")
print(f"y({t_end}) = {y:.6f}")
print(f"z({t_end}) = {z:.6f}")
print()

# Сравнение с простым методом Эйлера
print("Сравнение с простым методом Эйлера:")
print("-" * 50)
print("Метод             y(1)        z(1)")
print("-" * 50)

# Простой метод Эйлера (пересчитываем)
y_simple, z_simple, t_simple = 1.0, 0.5, 0.0
while t_simple < t_end:
    x_simple = t_simple - 0.01
    f1_simple = -2 * y_simple + x_simple
    f2_simple = 0.1 * y_simple - 3 * z_simple - y_simple * z_simple
    y_simple = y_simple + h * f1_simple
    z_simple = z_simple + h * f2_simple
    t_simple = t_simple + h

print(f"Простой Эйлер    {y_simple:10.6f} {z_simple:10.6f}")
print(f"Уточненный Эйлер {y:10.6f} {z:10.6f}")
print("-" * 50)

# Разница между методами
diff_y = y - y_simple
diff_z = z - z_simple
print(f"Разница: Δy = {diff_y:.6f}, Δz = {diff_z:.6f}")
print(f"Относительная разница y: {abs(diff_y / y) * 100:.2f}%")
print(f"Относительная разница z: {abs(diff_z / z) * 100:.2f}%")