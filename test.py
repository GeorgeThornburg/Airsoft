import numpy as np
import cv2



cap = cv2.VideoCapture(2)
  




while(cap.isOpened()):
  ret, frame = cap.read()

  
  cap2 = frame.copy()
  gray = cv2.cvtColor(cap2, cv2.COLOR_BGR2GRAY)

  cv2.imshow('Match',gray)
  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()