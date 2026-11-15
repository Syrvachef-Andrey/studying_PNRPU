import numpy as np

x1 = np.array([0.0, 0.5, 1.0, 2.0, 4.0])
x2 = np.array([0.0, 1.5, 2.0, 4.0, 5.0])
y_exp = np.array([0.0, 3.222, 4.351, 8.867, 11.990])


def model(b, x1, x2):
    return (b[0] ** 3) * (x1**2) + (b[1] ** 2) * x2


def loss(b, x1, x2, y):
    return np.sum((y - model(b, x1, x2)) ** 2)


def jacobian(b, x1, x2):
    dYm_db1 = 3 * (b[0] ** 2) * (x1**2)
    dYm_db2 = 2 * b[1] * x2
    return np.column_stack((dYm_db1, dYm_db2))


b_gz = np.array([0.5, 1.5], dtype=float)
h = 1.0

print("МЕТОД ГАУССА-ЗЕЙДЕЛЯ (МАТРИЧНЫЙ ВИД)")
for k in range(50):
    f_val = loss(b_gz, x1, x2, y_exp)
    print(f"Итерация {k}: b1 = {b_gz[0]:.6f}, b2 = {b_gz[1]:.6f}, F = {f_val:.6f}")

    if f_val < 0.001:
        print(f"Решение найдено на итерации {k}!\n")
        break

    X = jacobian(b_gz, x1, x2)
    E = y_exp - model(b_gz, x1, x2)
    A = X.T @ X
    Z = X.T @ E
    db = np.linalg.inv(A) @ Z

    b_gz = b_gz + h * db

    if np.linalg.norm(h * db) < 1e-4:
        print(
            f"Итерация {k+1}: b1 = {b_gz[0]:.6f}, b2 = {b_gz[1]:.6f}, F = {loss(b_gz, x1, x2, y_exp):.6f}"
        )
        print(f"--> Остановка по норме шага ||db|| < 1e-4!\n")
        break

b_gd = np.array([0.5, 1.5], dtype=float)
lr = 0.001

print("ГРАДИЕНТНЫЙ МЕТОД")
for k in range(5000):
    f_val = loss(b_gd, x1, x2, y_exp)

    if k < 5 or k % 10 == 0 or f_val < 0.001:
        print(
            f"Итерация {k}: b1 = {b_gd[0]:.6f}, b2 = {b_gd[1]:.6f}, F = {f_val:.6f}"
        )

    if f_val < 0.001:
        print(f"Решение найдено на итерации {k}!")
        break

    X = jacobian(b_gd, x1, x2)
    E = y_exp - model(b_gd, x1, x2)

    grad_F = -2 * (X.T @ E)
    db = -lr * grad_F

    b_gd = b_gd + db

    if np.linalg.norm(db) < 1e-4:
        print(
            f"Итерация {k+1}: b1 = {b_gd[0]:.6f}, b2 = {b_gd[1]:.6f}, F = {loss(b_gd, x1, x2, y_exp):.6f}"
        )
        print(f"Остановка по норме шага ||db|| < 1e-4!")
        break