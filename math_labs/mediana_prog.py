import numpy as np
import matplotlib.pyplot as plt

# Функция для вычисления определителя
def determinant(arr_1, arr_2):
    if arr_1[0] * arr_2[1] - arr_1[1] * arr_2[0] != 0:
        return arr_1[0] * arr_2[1] - arr_1[1] * arr_2[0]
    else:
        print("Определитель равен нулю, прямые параллельны или совпадают")
        exit(0)

# Функции для вычисления детерминантных компонент
def determinant_x(arr_1, arr_2):
    return -arr_1[2] * arr_2[1] + arr_2[2] * arr_1[1]

def determinant_y(arr_1, arr_2):
    return -arr_2[2] * arr_1[0] + arr_2[0] * arr_1[2]

# Функции для вычисления центров
def center_point_x(x1, x2):
    return (x1 + x2) / 2

def center_point_y(y1, y2):
    return (y1 + y2) / 2

# Ввод коэффициентов прямых
print("Введите коэффициенты 1 прямой:")
line_a = np.array([float(input()), float(input()), float(input())])
print("Введите коэффициенты 2 прямой:")
line_b = np.array([float(input()), float(input()), float(input())])
print("Введите коэффициенты 3 прямой:")
line_c = np.array([float(input()), float(input()), float(input())])

# Проверка параллельности
if determinant(line_a, line_b) == 0 or determinant(line_b, line_c) == 0 or determinant(line_a, line_c) == 0:
    print("Некоторые прямые параллельны или совпадают")
    exit(1)

# Вычисление точек пересечения (вершины треугольника)
det_ab = determinant(line_a, line_b)
det_bc = determinant(line_b, line_c)
det_ca = determinant(line_c, line_a)

list_of_points = np.array([
    [determinant_x(line_a, line_b) / det_ab, determinant_y(line_a, line_b) / det_ab],
    [determinant_x(line_b, line_c) / det_bc, determinant_y(line_b, line_c) / det_bc],
    [determinant_x(line_c, line_a) / det_ca, determinant_y(line_c, line_a) / det_ca]
])

# Вычисление центров сторон треугольника
list_of_center_points = [
    [center_point_x(list_of_points[0][0], list_of_points[1][0]), center_point_y(list_of_points[0][1], list_of_points[1][1])],  # Середина стороны AB
    [center_point_x(list_of_points[1][0], list_of_points[2][0]), center_point_y(list_of_points[1][1], list_of_points[2][1])],  # Середина стороны BC
    [center_point_x(list_of_points[0][0], list_of_points[2][0]), center_point_y(list_of_points[0][1], list_of_points[2][1])]   # Середина стороны AC
]

# Функция для рисования прямой между двумя точками
def draw_line_between_points(p1, p2, x_range):
    if p2[0] - p1[0] != 0:  # Если прямая не вертикальная
        slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
        intercept = p1[1] - slope * p1[0]
        return [slope * x + intercept for x in x_range]
    else:  # Вертикальная прямая
        return [np.nan] * len(x_range)

# Построение графиков прямых
x_range = np.linspace(-50, 50, 400)

# Прямые треугольника
list_of_points_line_a = [-(line_a[2] + x * line_a[0]) / line_a[1] if line_a[1] != 0 else np.nan for x in x_range]
list_of_points_line_b = [-(line_b[2] + x * line_b[0]) / line_b[1] if line_b[1] != 0 else np.nan for x in x_range]
list_of_points_line_c = [-(line_c[2] + x * line_c[0]) / line_c[1] if line_c[1] != 0 else np.nan for x in x_range]

plt.plot(x_range, list_of_points_line_a, label="Прямая 1")
plt.plot(x_range, list_of_points_line_b, label="Прямая 2")
plt.plot(x_range, list_of_points_line_c, label="Прямая 3")

# Отображение вершин треугольника
plt.scatter(list_of_points[:, 0], list_of_points[:, 1], color="green", label="Вершины")

# Отображение центров сторон
plt.scatter([p[0] for p in list_of_center_points], [p[1] for p in list_of_center_points], color="red", label="Центры сторон")

# Построение медиан
for i in range(3):
    median_y = draw_line_between_points(list_of_points[i], list_of_center_points[(i + 1) % 3], x_range)
    plt.plot(x_range, median_y, label=f"Медиана {i+1}", linestyle='--')

# Настройка графика
plt.axhline(0, color='black', linewidth=0.5)  # Горизонтальная линия (ось x)
plt.axvline(0, color='black', linewidth=0.5)  # Вертикальная линия (ось y)
plt.grid()
plt.legend()
plt.title("Треугольник и его медианы")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()