import cv2
from cv2 import ROTATE_90_CLOCKWISE


img = cv2.imread('./images/image_1.jpg' , 1)

img = cv2.resize(img , (400,600))
img = cv2.rotate(img, rotateCode=ROTATE_90_CLOCKWISE)

cv2.imshow('Image 1' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(type(img))
print(img.shape)

print(img[0:2])


