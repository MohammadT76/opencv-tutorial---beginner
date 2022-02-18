import cv2


img = cv2.imread('./images/image_1.jpg' , 1)

cv2.imshow('Image 1' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

