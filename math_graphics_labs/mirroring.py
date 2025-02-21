import numpy as np

a = np.array([
    [0, 0, 4, 1],
    [4, 0, 4, 1],
    [0, 0, 0, 1],
    [4, 0, 0, 1],
    [0, 4, 4, 1],
    [4, 4, 4, 1],
    [4, 4, 0, 1],
    [0, 4, 0, 1],
    [2, 6, 0, 1],
    [2, 6, 4, 1]
])

T = np.array([[0.7, 0.5, 0, 0.05],  
              [0, 0.7, 0, -0.07],  
              [0.7, -0.5, 0, -0.05],  
              [0, 0, 0, 1], ])

vanishing_points = np.array([
    [1, 0, 0, 0],  
    [0, 1, 0, 0],  
    [0, 0, 1, 0],  
])

distortion = np.array([
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
])

d = a @ T
b = vanishing_points @ T
e = distortion @ T

for i in range(len(d)):
    for j in range(len(d[i])):
        d[i][j] = d[i][j] / d[i][-1]
for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = b[i][j] / b[i][-1]
for i in range(len(e)):
    for j in range(len(e[i])):
        e[i][j] = e[i][j] / e[i][-1]

print(b, "\n")

print(d, "\n")

print(e)