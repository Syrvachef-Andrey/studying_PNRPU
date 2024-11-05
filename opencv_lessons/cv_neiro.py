import cv2

image = cv2.imread('images/cockerel.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

contour_image = cv2.Canny(gray_image, 50, 100)

con, hin = cv2.findContours(contour_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, con, -1, (255, 0, 0), 2)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()