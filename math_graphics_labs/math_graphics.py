import matplotlib.pyplot as plt
import numpy as np

len_1 = 6
len_2 = 6
len_3 = 6

a = [-2.5, -2]
b = [-2.5, 0]
c = [2.5, 0]
d = [2.5, -2]
e = [0, 0]
f = [e[0], e[1] + len_1]
g = [e[0], f[1] + len_2]
i = [e[0], g[1] + len_3]

print("Начальное положение")
print("A:", a, "B:", b, "C:", c, "D:", d, "E:", e, "F:", f, "G:", g, "I:", i)

plt.plot([a[0], b[0]], [a[1], b[1]])
plt.plot([b[0], c[0]], [b[1], c[1]])
plt.plot([c[0], d[0]], [c[1], d[1]])
plt.plot([a[0], d[0]], [a[1], d[1]])
plt.plot([e[0], f[0]], [e[1], f[1]])
plt.plot([f[0], g[0]], [f[1], g[1]])
plt.plot([g[0], i[0]], [g[1], i[1]])

plt.scatter(e[0], e[1], color='red')
plt.scatter(a[0], a[1], color='red')
plt.scatter(b[0], b[1], color='red')
plt.scatter(d[0], d[1], color='red')
plt.scatter(c[0], c[1], color='red')
plt.scatter(f[0], f[1], color='red')
plt.scatter(g[0], g[1], color='red')
plt.scatter(i[0], i[1], color='red')

plt.axis('equal')

plt.xlabel('X')
plt.ylabel('Y')
plt.title("MATH GRAPHICS\nTHE FIRST POSITION")

plt.grid(True)
plt.show()

print("Укажите на сколько увеличиться звено l: ", end='')
l = int(input())
print("Укажите на сколько увеличиться звено k: ", end='')
k = int(input())
print("Укажите на какое расстояние передвинется корпус манипулятор (если движение влево значит с минусом): ", end="")
dx = int(input())
print("Укажите в какой угол нужно встать звену в качестве угла alfa в градусах: ", end="")
alfa = int(input())
print("Укажите в какой угол нужно встать звену в качестве угла betta в градусах: ", end="")
betta = int(input())

plt.clf()

a = [-2.5 + dx, -2]
b = [-2.5 + dx, 0]
c = [2.5 + dx, 0]
d = [2.5 + dx, -2]
e = [0 + dx, 0]
f = [e[0], e[1] + len_1 + l]
g = [f[0] + len_2 * np.cos(np.radians(alfa)), f[1] + len_2 * np.sin(np.radians(alfa))]
i = [g[0] + (len_3 + k) * np.cos(np.radians(betta)), g[1] + (len_3 + k) * np.sin(np.radians(betta))]

print("New coordinates")
print("A:", a, "B:", b, "C:", c, "D:", d, "E:", e, "F:", f, "G:", g, "I:", i)

plt.plot([a[0], b[0]], [a[1], b[1]])
plt.plot([b[0], c[0]], [b[1], c[1]])
plt.plot([c[0], d[0]], [c[1], d[1]])
plt.plot([a[0], d[0]], [a[1], d[1]])
plt.plot([e[0], f[0]], [e[1], f[1]])
plt.plot([f[0], g[0]], [f[1], g[1]])
plt.plot([g[0], i[0]], [g[1], i[1]])

plt.scatter(e[0], e[1], color='red')
plt.scatter(a[0], a[1], color='red')
plt.scatter(b[0], b[1], color='red')
plt.scatter(d[0], d[1], color='red')
plt.scatter(c[0], c[1], color='red')
plt.scatter(f[0], f[1], color='red')
plt.scatter(g[0], g[1], color='red')
plt.scatter(i[0], i[1], color='red')

plt.axis('equal')

plt.xlabel('X')
plt.ylabel('Y')
plt.title("MATH GRAPHICS\nNEXT POSITION")

plt.grid(True)
plt.show()