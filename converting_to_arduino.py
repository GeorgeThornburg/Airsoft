import pygame
import cv2
import sys
import numpy as np
from pyfirmata import Arduino, util
from time import sleep
############# ARDUINO BOARD SETUP##########################
#board = Arduino('/dev/ttyUSB0')
board = Arduino('/dev/ttyACM0')
board.digital[8].write(0) #RIGHT - ORANGE
board.digital[9].write(0) #LEFT - BLUE
board.digital[10].write(0) #UP - WHITE
board.digital[11].write(0) #DOWN - GREY
board.digital[7].write(0) #SHOOT - PURPLE

############# R-PI BOARD SETUP ############################
#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
#GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW) 
#GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW) 
#GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW) 
#GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW) 
#GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
######################### SETTINGS #########################

camera = cv2.VideoCapture(4)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1922)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
template = cv2.imread('broom.png', 0)
h, w = template.shape
methods = ['cv.TM_CCOEFF']
pygame.init()
pygame.display.set_caption("Shooting Game")
screen = pygame.display.set_mode([1920, 1080])

############################################################

def control():
  events = pygame.event.get()
  
  if pygame.key.get_pressed()[pygame.K_UP]:
    board.digital[10].write(1) #UP - WHITE
  if pygame.key.get_pressed()[pygame.K_DOWN]:
    board.digital[11].write(1) #DOWN - GREY
  if pygame.key.get_pressed()[pygame.K_LEFT]:
    board.digital[9].write(1) #LEFT - BLUE
  if pygame.key.get_pressed()[pygame.K_RIGHT]:
    board.digital[8].write(1) #RIGHT - ORANGE
  if pygame.key.get_pressed()[pygame.K_SPACE]:
    board.digital[7].write(1) #SHOOT - PURPLE

  if pygame.key.get_pressed()[pygame.K_UP] == False:
    board.digital[10].write(0) #UP - WHITE
  if pygame.key.get_pressed()[pygame.K_DOWN] == False:
    board.digital[11].write(0) #DOWN - GREY
  if pygame.key.get_pressed()[pygame.K_LEFT] == False:
    board.digital[9].write(0) #LEFT - BLUE
  if pygame.key.get_pressed()[pygame.K_RIGHT] == False:
    board.digital[8].write(0) #RIGHT - ORANGE
  if pygame.key.get_pressed()[pygame.K_SPACE] == False:
    board.digital[7].write(0) #SHOOT - PURPLE
  
  
  if pygame.key.get_pressed()[pygame.K_ESCAPE]:
    board.digital[8].write(0) #RIGHT - ORANGE
    board.digital[9].write(0) #LEFT - BLUE
    board.digital[10].write(0) #UP - WHITE
    board.digital[11].write(0) #DOWN - GREY
    board.digital[7].write(0) #SHOOT - PURPLE
    board.exit()
    pygame.display.quit()
    pygame.quit()
    pygame.quit()
    cv2.destroyAllWindows()
    camera.release()


# def automated(target, bullseye, crosshair, collide):
#     pygame.draw.rect(screen, (0,128,0), target, 3)
#     pygame.draw.rect(screen, 255, bullseye, 3)
#     if crosshair[1] > bullseye[1]:
#         print("move up")
#     if crosshair[1] < bullseye[1]:
#         print("move down")
#     if crosshair[0] > bullseye[0]:
#         print("move left")
#     if crosshair[0] < bullseye[0]:
#         print("move right")
#         
#     if collide:
#         print("boom")
    
    


def main():
  while True:

    ret, frame = camera.read()
#     cap2 = frame.copy()
# 
#     new = cv2.cvtColor(cap2, cv2.COLOR_BGR2GRAY)
#     result = cv2.matchTemplate(new, template, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#     location = max_loc
    #print(max_val)    



    #cv2.imshow("cv2", cap2)
    frame = frame.swapaxes(0, 1)
    #print(frame.shape)
    pygame.surfarray.blit_array(screen, frame)
    
    crosshair = pygame.Rect(935, 500, 10, 10)
    pygame.draw.rect(screen, (255, 0, 0), crosshair,3)
    
    
    #bottom_right = pygame.Rect(location[0]+ 10, location[1] - 20, 100, 100)
    #pygame.draw.rect(screen, (0, 255, 0), bottom_right, 3) 
    #target = pygame.Rect(location[0], location[1], w, h)
    

    #print("bullseye X axis: " + str(bullseye[0]) + "bullseye Y axis: " + str(bullseye[1]))
    #print("crosshair X axis: " + str(crosshair[0]) + "crosshair Y axis: " + str(crosshair[1]))
#     bottom_right = pygame.Rect(location[0]+ 10, location[1] - 20, 100, 100)
#     pygame.draw.rect(screen, (0, 255, 0), bottom_right, 3)
#     bullseye = pygame.Rect((location[0]+ 10) + 45, (location[1] - 20) + 45, 10, 10)
#     pygame.draw.rect(screen, (255, 0, 255), bullseye, 0)
    

#     if max_val > .8:
# 
#         collide = pygame.Rect.colliderect(crosshair, bullseye)
#         if crosshair[1] > bullseye[1]:
#             board.digital[10].write(1) #UP - WHITE
#         elif crosshair[1] < bullseye[1]:
#             board.digital[11].write(1) #DOWN - GREY
#         elif crosshair[0] > bullseye[0]:
#             board.digital[9].write(1) #LEFT - BLUE
#         elif crosshair[0] < bullseye[0]:
#             board.digital[8].write(1) #RIGHT - ORANGE
#         elif collide:
#             board.digital[7].write(1) #SHOOT - PURPLE
#             time.sleep(1000)
#     if max_val < .8:
#         board.digital[8].write(0) #RIGHT - ORANGE
#         board.digital[9].write(0) #LEFT - BLUE
#         board.digital[10].write(0) #UP - WHITE
#         board.digital[11].write(0) #DOWN - GREY
#         board.digital[7].write(0) #SHOOT - PURPLE
#     print(crosshair[0] + bullseye[0])


      
    pygame.display.update()


    control()
    

main()
pygame.quit()
v2.destroyAllWindows()
camera.release()