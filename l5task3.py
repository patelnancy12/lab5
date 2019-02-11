import datetime 

def getTime():
  sec = timedelta(seconds=int(input('enter number of seconds ')))
  d = datetime(1,1,1) + sec


  print("days:hours:mins:seconds")
  print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))


getTime()
