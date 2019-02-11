import datetime

class Time():
  def __intit__(self,t1,t2):
    self.t1 = t1
    self.t2 = t2

  def is_after(self):
    return self.t2 < self.t1


x = 3600
y = 4500
time = Time(x,y)
print(time.is_after())
