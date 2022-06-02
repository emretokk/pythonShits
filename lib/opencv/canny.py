import cv2
from numpy import *

image1 = cv2.imread("hades.jpg")
image1 = cv2.resize(image1, (900, 600))
imagegray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(imagegray, (3, 3), 0)
canny=cv2.Canny(blur,100,1)
wide = cv2.Canny(blur, 10, 220)
tight = cv2.Canny(blur, 200, 230)
#auto = auto_canny(blur)
cv2.imshow("groot", image1)
cv2.imshow("blur", blur)
# imshow("canny",canny)
cv2.imshow("hepsi", hstack([wide, tight,canny,canny]))
cv2.waitKey(0)
cv2.destroyAllWindows()