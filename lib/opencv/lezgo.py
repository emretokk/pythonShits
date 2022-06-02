import cv2
import numpy
from matplotlib import pyplot

# img = cv2.imread("neofetch.png",0)
# #cv2.imshow("neo", img)
# #cv2.imwrite("neofetch_black.png", img)

# pyplot.imshow(img, cmap="gray", interpolation="bicubic")
# #pyplot.xticks([])
# #pyplot.yticks([])
# pyplot.show()


                      # webcam
cap = cv2.VideoCapture(0)

while (True):
	value, frame = cap.read()
	cv2.imshow("MEESEEKES LOOK AT MEE", frame)
	key = cv2.waitKey(1)
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()
