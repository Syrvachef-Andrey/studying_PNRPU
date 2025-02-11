from math import cos, sin, radians


import numpy as np


a0 = np.array([
 [3, 2, 1],
    [7, 3, 1],
    [2, 6, 1],
])


T0 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [-2, 0, 1]
])

T1 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [2, 0, 1]
])

R0 = np.array([
    [cos(-radians(63.44)), sin(-radians(63.44)), 0],
    [-sin(-radians(63.44)), cos(-radians(63.44)), 0],
    [0, 0, 1]
])

R1 = np.array([
    [cos(radians(63.44)), sin(radians(63.44)), 0],
    [-sin(radians(63.44)), cos(radians(63.44)), 0],
    [0, 0, 1]
])

M = np.array([
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]
])

a1 = a0 @ T0 @ R1  @ M @ R0 @ T1

print(a1)
