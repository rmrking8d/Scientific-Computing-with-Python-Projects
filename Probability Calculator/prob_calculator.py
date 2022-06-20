import copy
import random
# Consider using the modules imported above.
class Hat:
  def __init__(self, **kwargs): #remember *args/**kwargs for variable arguments!!!
    self.contents = [] 
    for key,val in kwargs.items():
      for i in range(val):
        self.contents.append(key)
  def draw(self,number):
    drawn = []
    if number > len(self.contents):
      return self.contents
    for i in range(number):
      removed = self.contents.pop(int(random.random() * len(self.contents)))
      drawn.append(removed)
    return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  sucess = 0
  for i in range(num_experiments):
    #Use copy so that balls for experiement #2-\inf stay the same
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colors_gotten = hat_copy.draw(num_balls_drawn)
    #reduce # in expected
    for color in colors_gotten:
      if color in expected_copy:
        expected_copy[color] -= 1
    if (all(x<=0 for x in expected_copy.values())):
      sucess +=1
  return sucess / num_experiments
