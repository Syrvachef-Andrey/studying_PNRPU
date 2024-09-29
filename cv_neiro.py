# import cv2
#
# image = cv2.imread('test.png')
# print(image.shape)
# image = cv2.resize(image, (500, 600))
# cv2.imshow('test', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# import cv2
#
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
#
# image = cv2.imread('test.png')
# image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
# image1 = cv2.imread('test.png')
# cv2.imshow('test', image)
# cv2.imshow('test_2', image1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# import cv2
#
# image = cv2.imread('test.png')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('test_grey', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# merge and split image
#
# import cv2
#
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
#
# image = cv2.imread('test.png')
# image_blur = cv2.GaussianBlur(image, (5, 5), 200)
# cv2.imshow('test', image_blur)
# image_filtred = cv2.bilateralFilter(image, 10, 75, 75)
# cv2.imshow('image_filtred', image_filtred)
# image_flipped = cv2.flip(image, -1)
# cv2.imshow('test_flipped', image_flipped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()