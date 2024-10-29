import cv2
import numpy as np

photo = np.zeros((300, 300, 3), dtype='uint8') # ((количество строк, количество столбцов,
# количество слоёв цвета), формат чисел)

photo[100:150, 200:280] = 119, 201, 105

cv2.imshow('Phot', photo)
cv2.waitKey(0)
cv2.destroyAllWindows()