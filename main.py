import time
from datetime import datetime
import pytz



#________________________USER'S INPUT_____________________________
Modes = int(input("What do you want to use?\n1)Timer\n2)Stopwatch\n3)Date and Time\n"))
print()



#________________________TIMER________________________________
def timer():
  time_set = int(input("Welcome to your Timer, set a time to continue\n" )) #Here the user sets how much time he wants to count
  #While the time is different then 0, the code is gonna reduce by one the amount set
  while time_set != 0:
    time_set= time_set - 1
    time.sleep(1)#It waits for one second
    print(time_set)



#_______________________STOP WATCH______________________________
def StopWatch():
  time_count = 0 #Sets the time to 0
  start_stop = int(input('Press 1 to start and 2 to stop\n'))#Ask if the user wants to start
  
  if start_stop == 1: #If user choose option 1, the code will add one second a time
    while start_stop != 2: 
      time_count = time_count + 1
      print(time_count)
      time.sleep(1) #waits one second



#______________________CALLING PYTZ_______________________________
def dateTime():
  print("This is the Brazilian/East Time, aside London's time")

  tz_BR = pytz.timezone('Brazil/East') #Getting the Brazilian/East time
  datetime_Brazil = datetime.now(tz_BR) #Defining the variable
  print("Brazil time:", datetime_Brazil.strftime("%H:%M:%S"))#Defining the model

  tz_London = pytz.timezone('Europe/London')#Getting London's time
  datetime_London = datetime.now(tz_London)#Defining the variable
  print("London time:", datetime_London.strftime("%H:%M:%S"))#Defining the model



#___________________________STARTING____________________________
if Modes == 1: #It will start the Timer
  timer()
elif Modes == 2: #It will start the Stop Watch
  StopWatch()
elif Modes == 3:#It starts the clock with the Brazilian/London time
  dateTime()
else:
  print("Choose 1, 2 or 3") #If user chooses something different then 1 or 2, it will ask to choose between one of them


#By: V2P
#Even though it's simple, feel free to use the source code


  



