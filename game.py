from engine import *
import pygame, random, math, sys

starting= [
  (
    (0, 0),
    (600, 50),
    1
  ),
  (
    (0, 0),
    (50, 600),
    1
  ),
  (
    (0, 550),
    (600, 600),
    1
  )
]

class Map(CollisionObject):
  def __init__(self, x, y, x2, y2, color="gray", shape="rectangle"):
    super().__init__(x, y, x2, y2)
    self.color = color
    self.shape = shape
    self.width = self.x2 - self.x
    self.height = self.y2 - self.y
    if self.width < 0:
        self.width = self.x - self.x2
    if self.height < 0:
        self.height = self.y - self.y2

  def draw(self, screen):
    if self.shape == "rectangle":
      pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
    else:
      print("shape not supported")

def makeMap(mapn = starting, difficulty = 1):
  for mapItem in mapn:
    if mapItem[2] == 1: #block
        Map(mapItem[0][0], mapItem[0][1], mapItem[1][0], mapItem[1][1])

class Player(CollisionObject):
    def __init__(self, x, y, x2, y2):
        super().__init__(x, y, x2, y2)
        self.yvel = 0
        self.xvel = 0
        self.crouched = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", ((abs(self.x2-self.x))/2+self.x, (abs(self.y2-self.y))/2+self.y), (abs(self.x2-self.x))/2)

    def controls(self):
        keys = pygame.key.get_pressed()
       
        if keys[pygame.K_LEFT]:
            self.xvel = -10
        if keys[pygame.K_RIGHT]:
            self.xvel = 10
        if keys[pygame.K_UP]:
            self.yvel = -10
        if keys[pygame.K_DOWN]:
            self.crouched = 1

    def move(self):
      self.x += self.xvel
      self.y += self.yvel
      self.x2 += self.xvel
      self.y2 += self.yvel
      self.xvel = 0
      for object in CollisionObject.collisionList:
        if self.collision(object) == True:
          pass
        else:
          self.yvel += 1
       

makeMap()
player = Player(100, 100, 200, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    Screen.screen.fill("black")
    DisplayObject.render()
    Player.controls(player)
    Player.move(player)
    pygame.display.update()
    clock.tick(60)
