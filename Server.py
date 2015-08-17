#!/usr/bin/python
import os
import serial

import time
from subprocess import Popen
index=0
def processFile(currentDir): #Function to list out all movie files in a directory
recursively

 # Get the absolute path of the currentDir parameter
 currentDir = os.path.abspath(currentDir)
 global index

 filesInCurDir = os.listdir(currentDir)
 # Traverse through all files
 for file in filesInCurDir:
 curFile = os.path.join(currentDir, file)
 # Check if it's a normal file or directory
 if os.path.isfile(curFile):
 # Get the file extension
 curFileExtension = curFile[-3:]


 # Check if the file has an extension of typical video files
 if curFileExtension in ['avi', 'dat', 'mp4', 'mkv', 'vob']:
 # We have got a video file! Increment the counter
 index+=1
 list.append(curFile) #store the absolute path to movie files in a tuple called
list

bytes = str.encode(file)
ZigBee Home Automation Controller
By Mohit Garg and Varun Chopra Page 112
 print(index, file)
counter=str.encode(str(index))
ser.write(counter) #Writing the movie file name serially so it can be
displayed to controller
 ser.write(". ");
ser.write(bytes)
#time.sleep(1)
 ser.write("\n")
#time.sleep(1)
 else:
 # We got a directory, enter into it for further processing
 processFile(curFile)

 def printchoice():
 print "Enter your choice"
 choice()
 def choice():
 global index
ser.flushInput()
time.sleep(1)
 choice1 = ser.readline().strip()
length=len(choice1)
 if(length == 3):
 if( choice1 =="R1M"): #Code to refresh the page on server side
 index=0
 ser.flush();
 time.sleep(2);
 processFile(currentDir)
 ser.write("R1MEOF");
 ser.write("\n");
 printchoice()
 elif(length == 4):
 substring1 = choice1[:3]
 substring2 = choice1[3]
 if ( substring1 == "R1M" ) :
 choice1 = int(substring2) #Take the choice as input from user
 path = list[choice1-1] #Initialising path using the choice
 omxp = Popen(['omxplayer',path]) #Playing the movie file according to user
choice
 else:
 choice()
else :
 choice()

# Get the current working directory
 def Start() :
 global index 
ZigBee Home Automation Controller

 ser.flushInput()
 print('Starting processing in %s' % currentDir)
 # Set the number of processed files equal to zero

 global list
 list = [ ]
 # Start Processing
 processFile(currentDir)

 print('\n -- %s Movie File(s) found in directory %s --' \
 % (index, currentDir))
 ser.write("R1MEOF");
ser.write("\n");
 printchoice()
 def Authentication():
 string1 = ser.readline().strip()
 print(string1)
 time.sleep(1)
 if( string1 == "R1M" ):
 Start();
 else:
 Authentication()
if __name__ == '__main__':

 global currentDir

 currentDir = os.getcwd()
 global ser
 locations=['/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3']
 for device in locations: #Try To connect to zigbee Device
 global ser
 try:

 ser = serial.Serial(device,38400)
 break
 except:
 print "Failed"
 


 ser.flushInput()
 while (true):
 Authentication()
