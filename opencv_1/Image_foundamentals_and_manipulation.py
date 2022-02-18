from email.mime import image
import cv2
import random

img = cv2.imread('./images/image_2.jpg' , 1)
img = cv2.resize(img , (500,600))

print(img)
print(type(img))
img[300:400,300:400] = random.randint(0,100)

cv2.imshow('Image 2' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
