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

# Программа находящая лицо, губы и глаза на картинке

# import cv2
#
# cap = cv2.VideoCapture(0)
# faces_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier('cascades/haarcascade_smile.xml')
#
# while True:
#     win, img = cap.read()
#     gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     faces = faces_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=15)
#
#     for x, y, w, h in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
#         roi_color = img[y:y + h, x:x + w]
#         roi_gray = gray_img[y:y + h, x:x + w]
#         eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.2, minNeighbors=15)
#         for ex, ey, ew, eh in eyes:
#             cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)
#         smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=38)
#         for sx, sy, sw, sh in smiles:
#             cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (255, 0, 0), 3)
#
#     cv2.imshow('original', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# Выделение контуров на изображении

# import cv2
# import numpy as np
#
# image = cv2.imread('images/OpenCV.jpg')
#
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (5, 5), 0)
#
# contour_image = cv2.Canny(gray, 100, 140)
#
# con, hir = cv2.findContours(contour_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#
# cv2.drawContours(contour_image, con, -1, (230, 111, 58), 5)
#
# cv2.imshow('contour_image', contour_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Выделение прямоугольником контура
#
# import cv2
#
# img = cv2.imread("images/OpenCV.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
#
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (12, 12))
#
# dilation = cv2.dilate(thresh1, rect_kernel, iterations=3)
#
# contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#
# im2 = img.copy()
#
# crop_number = 0
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#
#     # Рисуем ограничительную рамку на текстовой области
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow("Result", im2)
# cv2.waitKey(0)

# Выделение цветных фигур контурами

# import cv2
#
# image = cv2.imread('images/cockerel.jpg')
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
#
# contour_image = cv2.Canny(gray_image, 50, 100)
#
# con, hin = cv2.findContours(contour_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#
# cv2.drawContours(image, con, -1, (255, 0, 0), 2)
#
# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()