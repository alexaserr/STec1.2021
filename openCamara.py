///Este codigo nos ayuda a que abra la camara con la libreria cv2


import numpy as np
import cv2

cap=cv2VideoCapture(0)
while (True):
  ret,frame=cap.read()
  cv2.imshow("Img",grame)
  k=cv2.waitKey(30) and 0xff
  if k==27:
    break
cap.release()
cv2.destroyAllWindows
