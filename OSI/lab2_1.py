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

import time

def find_y(B1, B2):
    F = 0
    for i in range(len(x)):
        F += (y[i] - (x[i] ** B1 + B2)) ** 2
    return F

f = find_y(b1, b2)
f_prev = 0

print(f)

while f > f_zad_2:
    f_prev = f
    f_plus_b1 = find_y(b1 + delta, b2)
    f_minus_b1 = find_y(b1 - delta, b2)
    f_plus_b2 = find_y(b1, b2 + delta)
    f_minus_b2 = find_y(b1, b2 - delta)
    if f_plus_b1 < f_prev:
        b1 = b1 + delta
    elif f_minus_b1 < f_prev:
        b1 = b1 - delta
    if f_plus_b2 < f_prev:
        b2 = b2 + delta
    elif f_minus_b2 < f_prev:
        b2 = b2 - delta

    f = find_y(b1, b2)
    print("b1 =", f"{b1:.4f}", " b2 =", f"{b2:.4f}", " f =", f"{f:.4f}", " delta =", delta)

    if f_prev == f:
        delta = delta / 2
        if delta < 0.001:
            break

    time.sleep(0.01)