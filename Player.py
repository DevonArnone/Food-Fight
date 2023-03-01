import Input
import Items
import random

class Chef:
  TYPE_HUMAN = 1
  TYPE_ROBOT = 2

  def __init__(self, name, type):
    self.name = name
    self.type = type
    self.score = 0

  def selectItem(self, items):
    if self.type == Chef.TYPE_HUMAN:
      for x in range(0,len(items)):
        print(x,"-", items[x].name)
      p = "{}, which item do you select? "
      prompt = p.format(self.name)
      itemNum = Input.Validator.get_integer(prompt, 0, len(items)-1)
    elif self.type == Chef.TYPE_ROBOT:
      itemNum = random.randrange(0,len(items))
    return items[itemNum]

  def addScore(self, scoreIncrease):
    self.score += scoreIncrease
    
