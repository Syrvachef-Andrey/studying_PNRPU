# import cv2
# Дефолтный вывод изоюражения с перерасчетом размера изображения
# image = cv2.imread('test.png')
# print(image.shape)
# image = cv2.resize(image, (500, 600))
# cv2.imshow('test', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# import cv2
# Вывод потока кадров с камеры
# cap = cv2.VideoCapture(0)
# cap.set(3, 300)
# cap.set(4, 500)
# while True:
#     win, image = cap.read()
#     cv2.imshow('Image', image)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#
# import cv2
# Изменение размера изображения ровно в 2 раза
# image = cv2.imread('test.png')
# image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
# image1 = cv2.imread('test.png')
# cv2.imshow('test', image)
# cv2.imshow('test_2', image1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# import cv2
# Перевод из одной цветовой схемы в другую
# image = cv2.imread('test.png')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('test_grey', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# import cv2
# merge and split image
# image = cv2.imread('test.png')
# b, g, r = cv2.split(image)
# cv2.imshow('blue', b)
# cv2.imshow('green', g)
# cv2.imshow('red', r)
# image_merge = cv2.merge([b, g, r])
# cv2.imshow('merged_image', image_merge)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# Очистка изображения
# image = cv2.imread('test.png')
# image_blur = cv2.GaussianBlur(image, (5, 5), 200)
# cv2.imshow('test', image_blur)
# image_filtred = cv2.bilateralFilter(image, 10, 75, 75)
# cv2.imshow('image_filtred', image_filtred)
# image_flipped = cv2.flip(image, -1)
# cv2.imshow('test_flipped', image_flipped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# photo = np.zeros((500, 500, 3), dtype='uint8') # ((количество строк, количество столбцов,
# # количество слоёв цвета), формат чисел)
#
# photo[0:100, 0:100] = 119, 201, 105
# # заливка цветом по срезам пикселей
# cv2.rectangle(photo, (10, 100), (100, 200), (153, 241, 241), 3)
# # (изображение, левый верхний угол (точка), нижний правый угол (точка), цвет обводки, толщина обводки)
# cv2.rectangle(photo, (10, 200), (100, 300), (153, 241, 241), cv2.FILLED)
# # (изображение, левый верхний угол (точка), нижний правый угол (точка), цвет обводки, заливка)
# cv2.line(photo, (10, 300), (30, 400), (105, 24, 155), 3)
# # (изображение, начальная точка, конечная точка, цвет, толщина)
# cv2.circle(photo, (50, 450), 50, (50, 50, 234), cv2.FILLED)
# # (изображение, центр круга, радиус, цвет, толщина обводки или заливка)
# cv2.putText(photo, 'Berserk', (300, 300), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1)
#
# cv2.imshow('Photo', photo)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Обнаружение номеров машины с помощью каскадов данных opencv

# import cv2
#
# number_cascade = cv2.CascadeClassifier('cascades/haarcascade_russian_plate_number.xml')
# img = cv2.imread('images/number_2.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# numbers = number_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=30)
# for x, y, w, h in numbers:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
# cv2.imshow('Number detect', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Обнаружение часов на картинке с помошью каскадов данных opencv

# import cv2
#
# clock_cascade = cv2.CascadeClassifier('cascades/haarcascade_wallclock.xml')
# img = cv2.imread('images/clock1.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# clock = clock_cascade.detectMultiScale(gray, scaleFactor=1.001, minNeighbors=30)
# for x, y, w, h in clock:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
# cv2.imshow('Clock detect', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Программа находящая лицо на картинке

# import cv2
# face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
#
# img = cv2.imread('images/face_img.jpg')
# img = cv2.resize(img, (img.shape[1] // 7, img.shape[0] // 7))
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
#
# for x, y, w, h in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#     roi_color = img[y:y + h, x:x + w]
#     roi_gray = gray[y:y + h, x:x + w]
#
# cv2.imshow('FACE DETECT', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()