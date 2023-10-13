from engine import *
import pygame as pg, random as rd, math as mt

screen = Screen()

class Map(CollisionObject):
  def __init__(self, x, y, x2, y2, color="black", shape="rectangle"):
    super().__init__(x, y, x2, x2)
    self.color = color
    self.shape = shape

  def draw(self, screen):
    if self.shape = "rectangle":
      pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.x2, self.y2))
    else:
      print("shape not supported")
    

while True:
  screen.fill("black")

  screen.update()
  clock.tick(60)
