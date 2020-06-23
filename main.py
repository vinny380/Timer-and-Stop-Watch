import time



#Getting what the user wants touse
Modes = int(input("What do you want to use?\n1)Timer\n2)Stopwatch\n"))



#Defining the timer
def timer():
  time_set = int(input("Welcome to your Timer, set a time to continue\n" )) #Here the user sets how much time he wants to count
  #While the time is different then 0, the code is gonna reduce by one the amount set
  while time_set != 0:
    time_set= time_set - 1
    time.sleep(1)#It waits for one second
    print(time_set)



#This is defining the Stop Watch
def StopWatch():
  time_count = 0 #Sets the time to 0
  start_stop = int(input('Press 1 to start and 2 to stop\n'))#Ask if the user wants to start
  
  if start_stop == 1: #If user choose option 1, the code will add one
    while start_stop != 2: 
      time_count = time_count + 1
      print(time_count)
      time.sleep(1) #waits one second


if Modes == 1: #It will start the Timer
  timer()
elif Modes == 2: #It will start the Stop Watch
  StopWatch()
else:
  print("Choose 1 or 2") #If user chooses something different then 1 or 2, it will ask to choose between one of them



  



