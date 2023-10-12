import pygame as pg

pg.init()
pg.font.init()

clock = pygame.time.Clock()

class Screen:
  width = 500
  height = 500
  global_screen = pg.display.set_mode((Screen.width, Screen.height))

  def update():
    pygame.display.update()

class DisplayObject:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def draw(self, screen):
    pass

class TextField(DisplayObject):
  def __init__(text, font='Courier New', color='black', size=12):
    self.text = text
    self.font = pygame.font.SysFont(font, size)
    self.color = color
    self.size = size

  def draw(self, screen):
    font_surface = self.font.render(self.text, False, self.color)
    screen.blit(font_surface, (self.x, self.y))
