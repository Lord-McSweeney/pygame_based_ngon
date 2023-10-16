from engine import *
import pygame as pg, random as rd, math as mt

class Map(CollisionObject):
  def __init__(self, x, y, x2, y2, color="gray", shape="rectangle"):
    super().__init__(x, y, x2, x2)
    self.color = color
    self.shape = shape

  def draw(self, screen):
    if self.shape == "rectangle":
      pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.x2, self.y2))
    else:
      print("shape not supported")
    
Map(10, 10, 100, 100)
Map(300, 300, 200, 200)
while True:
  Screen.screen.fill("black")
  DisplayObject.render()
  pygame.display.update()
  clock.tick(60)
