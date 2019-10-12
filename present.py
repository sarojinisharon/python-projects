import time
import webbrowser
import random
#The User can set the time they want to wake up. 
#The String the user puts in must be the same as the example to work.
print("What time do you want to wake up?")
print("Use this form.\nExample: 06:30")
Alarm = input("> ")
#I first need to state the Time variable so it's usable in the while-loop
Time = time.strftime("%H:%M")

#This opens the text file with the youtube links
	#the urls are stored in the content variable 
content =["https://www.youtube.com/watch?v=CjodB1lAT90",
          "https://www.youtube.com/watch?v=CjodB1lAT90",
          "https://www.youtube.com/watch?v=YM2hx5vopeA"]
#When the Time does not equal the Alarm time string given above, print the time
while Time != Alarm:
	
	print("The time is " + Time)
	
	#Restating the Time variable allows the time to refresh
	#When I tried keeping the variable outside of the loop it 
    #just repeated the inital time
	Time = time.strftime("%H:%M")
	
	#This keeps the loop from flooding the command line with updates of the time :P
	time.sleep(30)

#If the Time variable is equal to the Alarm string, this code activates
if Time == Alarm:

	print("Time to Wake up!")
	#from the variable content, a random link is chosen and then that link 
    #is stored in random_video variable
	random_video =random.choice(content)
	#Using the webbrowser library, it opens this youtube video link.
	webbrowser.open(random_video)



