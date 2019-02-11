import math

class Point():

  def __init__(self):
    self.x = 10
    self.y = 12

  def distance_between_points(self):

    distance = math.sqrt(self.x**2 + self.y**2)
    return distance

  def print_point(self):
    print ('(%g, %g)' % (self.x, self.y))



p1 = Point()

c = p1.distance_between_points()

print(p1.distance_between_points())
p1.print_point()
