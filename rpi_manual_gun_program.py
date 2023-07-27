import pygame
import cv2
import sys
#import board
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW) #UP ---RIGHT
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW) #DOWN ----LEFT
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW) #LEFT  -----UP
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW) #RIGHT  ----DOWN
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) #SHOOT   

######################### SETTINGS #########################
camera = cv2.VideoCapture(-1)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
#template = cv2.imread('beer.png', 0)
#h, w = template.shape
#methods = ['cv.TM_CCOEFF']
pygame.init()
pygame.display.set_caption("Shooting Game")
screen = pygame.display.set_mode([800, 600])

############################################################

def control():
  events = pygame.event.get()
  
  if pygame.key.get_pressed()[pygame.K_UP]:
    #print("UP")
    GPIO.output(32, GPIO.HIGH)
  if pygame.key.get_pressed()[pygame.K_DOWN]:
    #print("DOWN")
    GPIO.output(36, GPIO.HIGH)
  if pygame.key.get_pressed()[pygame.K_LEFT]:
    #print("LEFT")
    GPIO.output(38, GPIO.HIGH)
  if pygame.key.get_pressed()[pygame.K_RIGHT]:
    #print("RIGHT")
    GPIO.output(40, GPIO.HIGH)
  if pygame.key.get_pressed()[pygame.K_SPACE]:
    #print("SHOOT")
    GPIO.output(22, GPIO.HIGH)

  if pygame.key.get_pressed()[pygame.K_UP] == False:
    GPIO.output(32, GPIO.LOW)
  if pygame.key.get_pressed()[pygame.K_DOWN] == False:
    GPIO.output(36, GPIO.LOW)
  if pygame.key.get_pressed()[pygame.K_LEFT] == False:
    GPIO.output(38, GPIO.LOW)
  if pygame.key.get_pressed()[pygame.K_RIGHT] == False:
    GPIO.output(40, GPIO.LOW)
  if pygame.key.get_pressed()[pygame.K_SPACE] == False:
    GPIO.output(22, GPIO.LOW)
  
  
  if pygame.key.get_pressed()[pygame.K_ESCAPE]:
    GPIO.output(22, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    GPIO.output(36, GPIO.LOW)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.LOW)
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
    #cap2 = frame.copy()

    #new = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #result = cv2.matchTemplate(new, template, cv2.TM_CCOEFF_NORMED)
    #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    #print(max_val)    



    #cv2.imshow("cv2", cap2)
    frame = frame.swapaxes(0, 1)
    #print(frame.shape)
    pygame.surfarray.blit_array(screen, frame)
    
    crosshair = pygame.Rect(387, 290, 10, 10)
    pygame.draw.rect(screen, (255, 0, 0), crosshair,3)
    
    #location = max_loc
    #bottom_right = pygame.Rect(location[0]-15, location[1], 20, 30)
    #pygame.draw.rect(screen, (0, 255, 0), bottom_right, 3) 
    #target = pygame.Rect(location[0], location[1], w, h)
    #bullseye = pygame.Rect(location[0] + (h//2) - 20, location[1] + (w//2) +  10, 10, 10)
    #print("bullseye X axis: " + str(bullseye[0]) + "bullseye Y axis: " + str(bullseye[1]))
    #print("crosshair X axis: " + str(crosshair[0]) + "crosshair Y axis: " + str(crosshair[1]))
    
    #collide = pygame.Rect.colliderect(crosshair, bullseye)


#     if max_val > .5:
#       automated(target, bullseye, crosshair, collide)
#       print(max_val)


      
    pygame.display.update()


    control()
    

main()
pygame.quit()
v2.destroyAllWindows()
camera.release()