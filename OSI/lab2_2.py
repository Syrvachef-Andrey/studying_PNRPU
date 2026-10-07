x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [-5.067, -4.067, -2.198, 0.247, 3.162, 6.486, 10.176, 14.202, 18.539, 23.168, 28.073]

b1 = 1.5
b2 = -5.0
f_zad_1 = 0.01
f_zad_2 = 0.001

def find_y(point):
    B1, B2 = point
    F = 0.0
    for i in range(len(x)):
        if x[i] == 0:
            val = B2
        else:
            val = (x[i] ** B1) + B2
        F += (y[i] - val) ** 2
    return F

step = 0.2
base_point = [b1, b2]

simplex = [
    list(base_point),
    [base_point[0] + step, base_point[1]],
    [base_point[0], base_point[1] + step]
]

max_iter = 50000
alpha = 1.0

for iteration in range(max_iter):
    simplex.sort(key=find_y)

    f_best = find_y(simplex[0])
    f_worst = find_y(simplex[-1])

    if f_best <= f_zad_1:
        print(f"Достигнута точность f_zad_1 ({f_zad_1}) на итерации {iteration}!")
        break

    centroid = [
        (simplex[0][0] + simplex[1][0]) / 2.0,
        (simplex[0][1] + simplex[1][1]) / 2.0
    ]

    reflected = [
        centroid[0] + alpha * (centroid[0] - simplex[-1][0]),
        centroid[1] + alpha * (centroid[1] - simplex[-1][1])
    ]
    f_refl = find_y(reflected)

    if f_refl < f_worst:
        simplex[-1] = reflected
    else:
        for i in range(1, 3):
            for j in range(2):
                simplex[i][j] = simplex[0][j] + 0.5 * (simplex[i][j] - simplex[0][j])

best_point = simplex[0]
best_f = find_y(best_point)

print(f"\nРезультат:")
print(f"b1 = {best_point[0]:.4f}")
print(f"b2 = {best_point[1]:.4f}")
print(f"Финальная ошибка f = {best_f:.6f}")