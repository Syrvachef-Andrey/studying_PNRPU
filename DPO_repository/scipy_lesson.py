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

