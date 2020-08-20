import pyttsx3
import os

# pyttsx3.speak("welcome to my first program")

while True: 
	print("chat with me and tell what you want:" , end=" ")
	a=input()
	# print(a)
	# os.system(a) 

	if ("run" in a or "open" in a) and ("chrome" in a):
	   os.system("chrome")

	elif ((("run" in a) or ("execute" in a)) or ("open" in a)) and("notepad" in a or "editor" in a):
	   os.system("notepad")

	elif ("run" in a or "open in a") and (" player" in a) and ("media" in a) and ("vlc" in a):
	   os.system("VLC")

	elif ("run" in a or "open in a") and ("paint" in a):
	   os.system("mspaint")
	
	elif ("run" in a or "open in a") and ("task manager" in a):
	   os.system("taskmgr")

	elif ("exit" in a) or ("quit" in a):
	   break
		

	else:
	   print("please try again")