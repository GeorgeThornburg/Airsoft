import numpy as np
import pygame
import cv2


color = (255,0,0)
cap = cv2.VideoCapture(2)
template = cv2.imread('screen.png', 0)

h, w = template.shape

methods = ['cv.TM_CCOEFF']


while(cap.isOpened()):
  ret, frame = cap.read()

  
  cap2 = frame.copy()
  gray = cv2.cvtColor(cap2, cv2.COLOR_BGR2GRAY)
  result = cv2.matchTemplate(gray, template, cv2.TM_CCORR)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

  location = max_loc
  bottom_right = (location[0] + w, location[1] + h)
  cv2.rectangle(cap2, location, bottom_right, 255, 5)


  cv2.imshow('Match', cap2)
  
  

  if cv2.waitKey(1) == ord('q'):
    pygame.display.quit()
    pygame.quit()
    break

cap.release()
cv2.destroyAllWindows()