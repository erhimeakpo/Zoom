# This is a basic python program for joining a zoom call.
# Make sure you apply changes where needed for this program to run.
# The program will a join call with video turned off

#REQUIREMENTS#
#Zoom is not already running
#Zoom Meeting ID and Passcode
#Preview Zoom video before joining meeting must be enabled
#Join automatically with audio must be enabled
#All photos of join button in the same directory as zoom.py

#import statements
import subprocess
import time
import pyautogui


#Values required for program to run
meeting_id = "Enter your meeting ID."
passcode = "Enter your meeting passcode."
path = "Enter filepath to zoom call." # If on windows you will have to do backslash twice. Ex C:\\Users\\Administrator\\Zoom.exe

#Starts Zoom Desktop Client
subprocess.Popen(path)
time.sleep(3)

#Clicks searches for Join a meeting button and clicks it.
pyautogui.click('join.png')
time.sleep(3)

#Inputs meeting ID and clicks join meeting
pyautogui.write(meeting_id)
pyautogui.click('join0.png')
time.sleep(3)

#Inputs passcode and clicks join
pyautogui.write(passcode)
pyautogui.click('join1.png')
time.sleep(3)

#Selects join with no video. 
pyautogui.click('novideo.png')



