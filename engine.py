import pygame

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

class Screen:
  width = 500
  height = 500
  screen = pygame.display.set_mode((600, 600))

class DisplayObject:
  renderList = []
  def render():
        for i in DisplayObject.renderList:
            if i.visible:
                i.draw(Screen.screen)
    
  def __init__(self, x, y, visible = True):
    self.x = x
    self.y = y
    self.visible = visible

    DisplayObject.renderList.append(self)

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
      i.draw(Screen.screen)
        #for i in CollisionObject.collisionList:
         # for j in CollisionObject.collisionList:
          #  if i != j and i.visible and j.visible:
           #     i.collision(i, j)

  def __init__(self, x, y, x2, y2):
    self.x = x
    self.y = y
    self.x2 = x2
    self.y2 = y2

    CollisionObject.collisionList.append(self)

  def collision(self, other_object):
    if self.x >= other_object.x and self.x2 <= other_object.x2 and self.y >= other_object.y and self.y2 <= other_object.y2:
      return(self, other_object)
