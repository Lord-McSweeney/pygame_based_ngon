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
  renderList = []
  def render():
        for i in DisplayObject.renderList:
            if i.visible:
                i.draw(Screen.global_screen)
    
  def __init__(self, x, y, visible = True):
    self.x = x
    self.y = y
    self.visible = visible

    renderList.append(self)

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

class CollisionObject(DisplayObject):
  collisionList = []
  def render():
        for i in CollisionObject.collisionList:
          for j in CollisionObject.collisionList:
            if i.visible:
                i.collision(i, j)

  def __init__(x2, y2):
    self.x2 = x2
    self.y2 = y2

    collisionList.append(self)

  def collision(self, other_object):
    if self.x >= other_object.x and self.x2 <= other_object.x2 and self.y >= other_object.y and self.y2 <= other_object.y2:
      return(self, other_object)
