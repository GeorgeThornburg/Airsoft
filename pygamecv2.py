import pygame
import cv2
import sys
#import board
#import RPi.GPIO as GPIO
from time import sleep
#i2c = board.I2C()
#scd = adafruit_scd30.SCD30(i2c)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(19, GPIO.OUT)
#GPIO.setup(18, GPIO.OUT)
#GPIO.setup(23, GPIO.OUT)

######################### SETTINGS #########################
camera = cv2.VideoCapture(2)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 4000)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)
#print(camera.shape)
template = cv2.imread('beer.png', 0)
h, w = template.shape
methods = ['cv.TM_CCOEFF']
pygame.init()
pygame.display.set_caption("Pygame Window")
screen = pygame.display.set_mode([1280, 800])

############################################################

def control():
  events = pygame.event.get()

  if pygame.key.get_pressed()[pygame.K_UP]:
    print("UP")
  if pygame.key.get_pressed()[pygame.K_DOWN]:
    print("DOWN")
  if pygame.key.get_pressed()[pygame.K_LEFT]:
    print("LEFT")
    sleep(.5)
  if pygame.key.get_pressed()[pygame.K_RIGHT]:
    print("RIGHT")
    sleep(.5)
  if pygame.key.get_pressed()[pygame.K_SPACE]:
    print("SHOOT")    
  if pygame.key.get_pressed()[pygame.K_ESCAPE]:
    pygame.display.quit()
    pygame.quit()
    pygame.quit()
    cv2.destroyAllWindows()
    camera.release()


def main():
  while True:
    ret, frame = camera.read()
    cap2 = frame.copy()
    

    new = cv2.cvtColor(cap2, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(new, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #print(max_val)    

    location = max_loc
    bottom_right = (location[0] + w, location[1] + h)
    #cv2.rectangle(cap2, location, bottom_right, 255, 25)

    #cv2.imshow("cv2", cap2)
    frame = frame.swapaxes(0, 1)
    #print(frame.shape)
    #print(screen)
    pygame.surfarray.blit_array(screen, frame)
    
    crosshair = pygame.Rect(640, 400, 20, 20)
    target = pygame.Rect(location[0], location[1], w, h)
    bullseye = pygame.Rect(location[0] + (h//2) - 20, location[1] + (w//2) +  10, 10, 10)

    pygame.draw.rect(screen, (255, 0, 0), crosshair,3)
    collide = pygame.Rect.colliderect(crosshair, bullseye)


    if max_val > .4:
      pygame.draw.rect(screen, (0,128,0), target, 3)
      pygame.draw.rect(screen, 255, bullseye, 3)

      if collide:
        print("boom")
    pygame.display.update()


    control()

main()
pygame.quit()
v2.destroyAllWindows()
camera.release()