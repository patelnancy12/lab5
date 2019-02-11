from l5task1 import Point
import copy

class Rectangle(object):
  def __init__(self):
    self.width = 100.0
    self.height = 200.0
 
    self.corner = Point()
    self.corner.x = 0.0
    self.corner.y = 0.0

  def find_center(r):
    p = Point()
    p.x = r.corner.x + r.width/2.0
    p.y = r.corner.y + r.height/2.0
    return p

  def print_point(p):
    print('(%g, %g)' % (p.height, p.width))

  def move_rectangle(r,dx,dy):
    r.corner.x += dx
    r.corner.y += dy

  def modify_move_rectangle(r,dx,dy):
    rm = copy.deepcopy(r)
    r.move_rectangle(dx,dy)
    return rm

r = Rectangle()
c= r.find_center()
r.print_point()

r.move_rectangle(100,50)
print('(%g, %g)' % (r.corner.x,r.corner.y))

new_rectangle = r.modify_move_rectangle(10,20)
print('(%g, %g)' % (new_rectangle.corner.x, new_rectangle.corner.y))
