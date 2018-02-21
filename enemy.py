from random import randint
from character import Character
class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.name = 'a ghost'
    self.health = randint(1, player.health)
    self.health= 1    
   
 
