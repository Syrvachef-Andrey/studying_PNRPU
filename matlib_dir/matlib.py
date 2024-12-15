# Создание области приложения для графика

# import matplotlib.pyplot as plt
#
# plt.figure(num="my_figure", figsize=[6.0, 5.0], dpi=100)
#
# plt.show()

# Создание графика sin на области

# import matplotlib.pyplot as plt
# import numpy as np
#
# plt.figure(num="my_figure", figsize=[6.0, 5.0], dpi=100)
#
# x = np.linspace(-np.pi * 2, 2 * np.pi, 500)
#
# y = np.sin(x)
#
# plt.plot(x, y, label='y=sin(x)')
#
# plt.show()

# Создание двух графиков одновременно

# import matplotlib.pyplot as plt
# import numpy as np
#
# x_1 = np.linspace(-np.pi * 2, np.pi * 2, 100)
# x_2 = np.linspace(-5, 5, 100)
#
# y_1 = np.sin(x_1)
# y_2 = []
# for i in range(100):
#     y_2.append(x_2[i] - 4)
# print(len(x_2), len(y_2))
# plt.figure(num="y = sin(x)", figsize=[6.0, 5.0], dpi=100)
# plt.plot(x_1, y_1, label='y = sin(x)')
# plt.show(block=False)
#
# plt.figure(num="y = x - 4", figsize=[6.0, 5.0], dpi=100)
# plt.plot(x_2, y_2, label='y = x - 4')
# plt.show()

# Создание графика с сеткой

# import matplotlib.pyplot as plt
# import numpy as np
#
# plt.figure(num="my plot", figsize=[6.0, 5.0], dpi=100)
#
# x = np.linspace(-np.pi * 2, np.pi * 2, 100)
#
# y = np.sin(x)
#
# plt.plot(x, y, label="y = sin(x)")
#
# plt.grid()
#
# plt.show()

# Создание графика с подписью осей и заголовком

# import matplotlib.pyplot as plt
# import numpy as np
#
# plt.figure(num="My plot", figsize=[7.0, 5.0], dpi=100)
#
# x = np.linspace(0, np.pi * 2, 100)
#
# y = np.sin(x)
#
# plt.plot(x, y, label="y = sin(x)")
# plt.title(label="Синусоида", loc="center")
# plt.grid()
# plt.xlabel(xlabel="Ось X", loc="center", color='red')
# plt.ylabel(ylabel="Ось Y", loc="center", color='red')
# plt.show()

# Создание графика синуса с ограничениями с отобажениями

import matplotlib.pyplot as plt
import numpy as np

plt.figure(num="my plot", figsize=[6.0, 5.0], dpi=100)

x = np.linspace(0, np.pi * 2, 100)

y = np.sin(x)

plt.plot(x, y, label="y = sin(x)")

plt.title(label="y = sin(x)", loc="center")
plt.grid()
plt.xlabel(xlabel="Ось X", loc="center")
plt.ylabel(ylabel="Ось Y", loc="center")
plt.ylim(top=0.75)
plt.xlim(left=0, right=6)

plt.show()