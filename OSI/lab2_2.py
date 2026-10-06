b1 = 1.5
b2 = -5
f_zad_1 = 0.01
f_zad_2 = 0.001

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [-5.067, -4.067, -2.198, 0.247, 3.162, 6.486, 10.176, 14.202, 18.539, 23.168, 28.073]

if len(x) != len(y):
    print("Wrong length")
    exit()

delta = 0.1

def find_y(point):
    b1, b2, b3 = point
    F = 0.0
    for i in range(len(x)):
        if x[i] == 0 and b2 < 0:
            return float('inf')
        val = b1 * (x[i] ** b2) + b3
        F += (y[i] - val) ** 2
    return F

step = 0.2
base_point = [1.0, 1.5, -5.0]

simplex = [
    list(base_point),  # Вершина 0: (1.0, 1.5, -5.0)
    [base_point[0] + step, base_point[1], base_point[2]],
    [base_point[0], base_point[1] + step, base_point[2]],
    [base_point[0], base_point[1], base_point[2] + step]
]

f_zad_2 = 0.001
max_iter = 2000
alpha = 1.0

for iteration in range(max_iter):
    simplex.sort(key=find_y)

    f_best = find_y(simplex[0])
    f_worst = find_y(simplex[-1])

    if f_best <= f_zad_1:
        print(f"Достигнута точность f_zad_2 на итерации {iteration}!")
        break

    centroid = [0.0, 0.0, 0.0]
    for i in range(3):
        for j in range(3):
            centroid[j] += simplex[i][j] / 3.0

    reflected = [
        centroid[j] + alpha * (centroid[j] - simplex[-1][j])
        for j in range(3)
    ]
    f_refl = find_y(reflected)

    if f_refl < f_worst:
        simplex[-1] = reflected
    else:
        for i in range(1, 4):
            for j in range(3):
                simplex[i][j] = simplex[0][j] + 0.5 * (simplex[i][j] - simplex[0][j])

best_point = simplex[0]
best_f = find_y(best_point)

print("\n--- РЕЗУЛЬТАТЫ ---")
print(f"b1 = {best_point[0]:.4f}")
print(f"b2 = {best_point[1]:.4f}")
print(f"b3 = {best_point[2]:.4f}")
print(f"Финальная f = {best_f:.4e}")