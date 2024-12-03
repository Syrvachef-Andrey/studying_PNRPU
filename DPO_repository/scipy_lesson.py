# Задача 1

# import matplotlib.pyplot as plt
# from scipy.misc import face
#
# # Загрузка изображения в оттенках серого
# img = face(gray=True)
#
# # 1. Цветовая карта
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 3, 1)
# plt.imshow(img, cmap='hot')
# plt.title('Цветовая карта: hot')
# plt.axis('off')
#
# # 2. Обрезанное изображение
# cropped_img = img[100:-100, 300:700]
# plt.subplot(1, 3, 2)
# plt.imshow(cropped_img, cmap='gray')
# plt.title('Обрезанное изображение')
# plt.axis('off')
#
# # 3. Выделение лица с помощью круга
# from matplotlib.patches import Circle
#
# plt.subplot(1, 3, 3)
# plt.imshow(img, cmap='gray')
# plt.title('Выделение лица')
# plt.axis('off')
#
# # Определение центра лица (примерно)
# center = (660, 300)
# radius = 180
#
# # Рисование круга
# circle = Circle(center, radius, edgecolor='red', facecolor='none')
# plt.gca().add_patch(circle)
#
# # Отображение всех изображений
# plt.tight_layout()
# plt.show()

# Задача 2

# import numpy as np
# import matplotlib.pyplot as plt
#
# data = np.loadtxt('populations.txt')
# year, hares, lynxes, carrots = data.T
#
# plt.axes([0.2, 0.1, 0.5, 0.8])
#
# plt.plot(year, hares, year, lynxes, year, carrots)
#
# plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5))
#
# plt.show()

# Задача 3

# import numpy as np
# import matplotlib.pyplot as plt
#
# # Определение функции для проверки принадлежности к множеству Мандельброта
# def mandelbrot(c, max_iter):
#     z = 0
#     for n in range(max_iter):
#         if abs(z) > 2:
#             return n
#         z = z*z + c
#     return max_iter
#
# # Параметры
# xmin, xmax, xn = -2.0, 1.0, 600  # Диапазон и количество точек по оси x
# ymin, ymax, yn = -1.5, 1.5, 600  # Диапазон и количество точек по оси y
# max_iter = 100  # Максимальное количество итераций
#
# # Создание сетки значений c = x + 1j*y
# x = np.linspace(xmin, xmax, xn)
# y = np.linspace(ymin, ymax, yn)
# c = x[:,np.newaxis] + 1j*y[np.newaxis,:]
#
# # Выполнение итераций и формирование маски
# mask = np.zeros_like(c, dtype=bool)
# for i in range(xn):
#     for j in range(yn):
#         mask[i, j] = mandelbrot(c[i, j], max_iter) == max_iter
#
# # Создание изображения
# plt.figure(figsize=(10, 10))
# plt.imshow(mask.T, extent=[xmin, xmax, ymin, ymax], cmap='binary')
# plt.title('Множество Мандельброта')
# plt.xlabel('Re(c)')
# plt.ylabel('Im(c)')
# plt.show()