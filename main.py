import time

Modes = int(input("What do you want to use?\n1)Timer\n2)Stopwatch\n"))


def timer():
  time_set = int(input("Welcome to your Timer, set a time to continue\n" ))
  while time_set != 0:
    time_set= time_set - 1
    time.sleep(1)
    print(time_set)

    

def StopWatch():
  time_count = 0
  start_stop = int(input('Press 1 to start and 2 to stop\n'))
  
  if start_stop == 1:
    while start_stop != 2:
      time_count = time_count + 1
      print(time_count)
      time.sleep(1)




if Modes == 1:
  timer()
elif Modes == 2:
  StopWatch()
else:
  print("Choose 1 or 2")



  



