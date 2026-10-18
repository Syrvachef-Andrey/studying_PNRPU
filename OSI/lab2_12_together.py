x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [-5.067, -4.067, -2.198, 0.247, 3.162, 6.486, 10.176, 14.202, 18.539, 23.168, 28.073]

f_zad_1 = 0.001


def find_y(point):
    b1, b2 = point
    F = 0.0
    for i in range(len(x)):
        if x[i] == 0:
            val = b2
        else:
            val = (x[i] ** b1) + b2
        F += (y[i] - val) ** 2
    return F


b1_ds, b2_ds = 1.5, -5.0
delta = 0.1
f_ds = find_y([b1_ds, b2_ds])
iter_ds = 0

while f_ds > f_zad_1 and delta >= 1e-6:
    improved = False
    iter_ds += 1

    for db1 in [delta, -delta]:
        f_trial = find_y([b1_ds + db1, b2_ds])
        if f_trial < f_ds:
            b1_ds += db1
            f_ds = f_trial
            improved = True
            break

    for db2 in [delta, -delta]:
        f_trial = find_y([b1_ds, b2_ds + db2])
        if f_trial < f_ds:
            b2_ds += db2
            f_ds = f_trial
            improved = True
            break

    if not improved:
        delta /= 2.0

step = 0.2
base_point = [1.5, -5.0]
simplex = [
    list(base_point),
    [base_point[0] + step, base_point[1]],
    [base_point[0], base_point[1] + step]
]

alpha = 1.0
gamma = 2.0
rho = 0.5
sigma = 0.5

iter_simp = 0
f_simp = 0

for iteration in range(50000):
    iter_simp += 1
    simplex.sort(key=find_y)

    f_best = find_y(simplex[0])
    f_good = find_y(simplex[1])
    f_worst = find_y(simplex[-1])

    if f_best <= f_zad_1:
        break

    c0 = (simplex[0][0] + simplex[1][0]) / 2.0
    c1 = (simplex[0][1] + simplex[1][1]) / 2.0

    xr = [c0 + alpha * (c0 - simplex[-1][0]), c1 + alpha * (c1 - simplex[-1][1])]
    fr = find_y(xr)

    if fr < f_best:
        xe = [c0 + gamma * (xr[0] - c0), c1 + gamma * (xr[1] - c1)]
        fe = find_y(xe)
        if fe < fr:
            simplex[-1] = xe
        else:
            simplex[-1] = xr
    elif fr < f_good:
        simplex[-1] = xr
    else:
        xc = [c0 + rho * (simplex[-1][0] - c0), c1 + rho * (simplex[-1][1] - c1)]
        fc = find_y(xc)
        if fc < f_worst:
            simplex[-1] = xc
        else:
            for i in range(1, 3):
                simplex[i][0] = simplex[0][0] + sigma * (simplex[i][0] - simplex[0][0])
                simplex[i][1] = simplex[0][1] + sigma * (simplex[i][1] - simplex[0][1])

b1_simp, b2_simp = simplex[0]
f_simp = find_y(simplex[0])

print("=== СРАВНЕНИЕ МЕТОДОВ ОПТИМИЗАЦИИ ===")
print(f"Требуемая точность f_zad_1: {f_zad_1}\n")

print("Метод прямого поиска:")
print(f"   Количество шагов (итераций): {iter_ds}")
print(f"   Достигнутая ошибка (F):      {f_ds:.6f}")
print(f"   Найденные параметры:         b1 = {b1_ds:.4f}, b2 = {b2_ds:.4f}\n")

print("Полный симплекс-метод:")
print(f"   Количество шагов (итераций): {iter_simp}")
print(f"   Достигнутая ошибка (F):      {f_simp:.6f}")
print(f"   Найденные параметры:         b1 = {b1_simp:.4f}, b2 = {b2_simp:.4f}")