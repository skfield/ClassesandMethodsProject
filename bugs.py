import pygame
import mybugs

#colors gotten from rgb website

green = (0, 255, 0)
blue = (0, 0, 255)
brown = (125, 100, 100)
yellow = (255, 255, 0)


pygame.init()
size = [1400,1050]
screen=pygame.display.set_mode(size)

class Garden:
  def show()
    pygame.draw.rect(screen,brown,[0, 700, 1400, 325])
    pygame.draw.rect(screen,green,[0, 600, 1400, 125])
    pygame.draw.rect(screen,blue,[0, 0, 1400, 600])
    pygame.draw.ellipse(screen,yellow,[900, 100, 100, 50])
