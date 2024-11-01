import cv2

clock_cascade = cv2.CascadeClassifier('cascades/haarcascade_wallclock.xml')
img = cv2.imread('images/clock1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

clock = clock_cascade.detectMultiScale(gray, scaleFactor=1.001, minNeighbors=30)
for x, y, w, h in clock:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Clock detect', img)
cv2.waitKey(0)
cv2.destroyAllWindows()