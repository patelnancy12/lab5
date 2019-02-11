class Point():
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def __add__(self,other):
    print (self.x+other.x,self.y+other.y)

  def add(self,other):
    if isinstance(other,tuple):
      print(self.x+other[0],self.y+other[1])
    else:
      print(self+other)

p = Point(2,3)
p1 = Point(4,5)
p.add(p1)
p1.add((4,5))

