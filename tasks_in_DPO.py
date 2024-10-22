import random
import matplotlib.pyplot as plt

num_points = 1000000

points = []
hits = 0

for i in range(num_points):
    x, y = random.random(), random.random()
    if x * x + y * y < 1.0:
        hits += 1
        points.append((x, y, "red"))
    else:
        points.append((x, y, "blue"))

x, y, colors = zip(*points)
flg, ax = plt.subplots()

ax.scatter(x, y, c=colors)

plt.show()
fractions = hits / num_points
print(4 * fractions)

