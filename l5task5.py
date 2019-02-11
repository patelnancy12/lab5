#Creating a point class 

class Point():
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __str__(self):
    reurn "str method" + str(self.x) "," + str(self.y)

p = Point(25,7)
