import matplotlib.pyplot as plt

len_1 = 6
len_2 = 6
len_3 = 6

a = [0, 0]
b = [0, 2]
c = [6, 2]
d = [6, 0]
e = [3, 2]
f = [e[0], e[1] + len_1]
g = [e[0], f[1] + len_2]
i = [e[0] + len_3, g[1]]

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
plt.title("MATH GRAPHICS")

plt.grid(True)
plt.show()

print("Начальное положение")
