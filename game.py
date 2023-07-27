import numpy as np
import pygame, sys
import pygame.camera
from pygame.locals import *
import cv2

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((640, 480))

cam = pygame.camera.Camera("/dev/video2", (640, 480))
cam.start()

rectangle = pygame.Rect(300, 200, 25, 25)

while True:
  image = cam.get_image()
  
  
  screen.blit(image, (0,0))
  pygame.draw.rect(screen, 255, rectangle)
  pygame.display.update()

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.display.quit()
      pygame.quit()
      sys.exit()