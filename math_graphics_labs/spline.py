import matplotlib.pyplot as plt


def coefficient(xi, xi1, xi2, xi3, yi, yi1, yi2, yi3):
    my_dict = {
        "a0": (xi + 4 * xi1 + xi2) / 6,
        "a1": (xi2 - xi) / 2,
        "a2": (xi - 2 * xi1 + xi2) / 2,
        "a3": (-xi + 3 * xi1 - 3 * xi2 + xi3) / 6,
        "b0": (yi + 4 * yi1 + yi2) / 6,
        "b1": (yi2 - yi) / 2,
        "b2": (yi - 2 * yi1 + yi2) / 2,
        "b3": (-yi + 3 * yi1 - 3 * yi2 + yi3) / 6
    }
    return my_dict


list_of_points = [[2, 3], [3, 3], [4, 5], [6, 5], [7, 3], [6, 3], [4, 2], [3, 1], [2, 0.5], [1, 1], [0.5, 0.5]]
list_of_spline_points = []

# Генерация сплайн-точек
for i in range(len(list_of_points)):
    list_of_indexes = [i, i + 1, i + 2, i + 3]
    for j in range(len(list_of_indexes)):
        if list_of_indexes[j] >= len(list_of_points):
            list_of_indexes[j] = list_of_indexes[j] % len(list_of_points)

    dict_of_coefficients = coefficient(
        list_of_points[list_of_indexes[0]][0], list_of_points[list_of_indexes[1]][0],
        list_of_points[list_of_indexes[2]][0], list_of_points[list_of_indexes[3]][0],
        list_of_points[list_of_indexes[0]][1], list_of_points[list_of_indexes[1]][1],
        list_of_points[list_of_indexes[2]][1], list_of_points[list_of_indexes[3]][1]
    )

    t = 0
    while t <= 1:
        xt = (dict_of_coefficients["a0"] + dict_of_coefficients["a1"] * t +
              dict_of_coefficients["a2"] * t ** 2 + dict_of_coefficients["a3"] * t ** 3)
        yt = (dict_of_coefficients["b0"] + dict_of_coefficients["b1"] * t +
              dict_of_coefficients["b2"] * t ** 2 + dict_of_coefficients["b3"] * t ** 3)
        list_of_spline_points.append([xt, yt])
        t += 0.1

# Отображение исходных точек
for i in range(len(list_of_points)):
    plt.scatter(list_of_points[i][0], list_of_points[i][1], color="red")

# Соединение исходных точек линиями (включая соединение последней точки с первой)
x_points = [point[0] for point in list_of_points]
y_points = [point[1] for point in list_of_points]
x_points.append(list_of_points[0][0])  # Добавляем первую точку в конец
y_points.append(list_of_points[0][1])  # Добавляем первую точку в конец
plt.plot(x_points, y_points, color="red", linestyle="--", label="Исходные точки")

# Отображение сплайн-точек
x_spline = [point[0] for point in list_of_spline_points]
y_spline = [point[1] for point in list_of_spline_points]
plt.scatter(x_spline, y_spline, color="green", s=10, label="Сплайн-точки")

# Построение сплайна
plt.plot(x_spline, y_spline, color="green", label="Сплайн")

# Настройка графика
plt.grid()
plt.title("Сплайн")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")  # Для одинакового масштаба по осям X и Y
plt.show()