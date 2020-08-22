#import pyttsx3
import os

#pyttsx3.speak("Welcome to my tools")


while True:
	print("chat with me with your requirements : "  , end='')
	p = input()

	# print(p)
	# os.system(p)
	
	# Chrome
	if (("run" in p)  or  ("open" in p )) and (("chrome" in p) or  ("google" in p )):
	  os.system("chrome")

	#Notepad
	elif (("run" in p) or  ("execute" in p ) or  ("open" in p )) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")
	
	# Movie Maker
	elif (("run" in p) or  ("execute" in p ) or ("play" in p) or  ("open" in p )) and  (("movie" in p) or ("movie maker" in p) ) :
	  os.system("MovieMaker")

	#Visual Studio
	elif (("run" in p) or  ("execute" in p ) or  ("open" in p )) and  (("Visual" in p) or ("visual studio" in p) or ("studio" in p)) :
	  os.system("Code")

	#Droid Cam App
	elif (("run" in p) or  ("execute" in p ) or  ("open" in p )) and  (("droid" in p) or ("droidcam" in p) or ("droid cam" in p) or ("droid camera" in p)) :
	  os.system("DroidCamApp")

	#Star UML
	elif (("run" in p) or  ("execute" in p ) or  ("open" in p )) and  (("uml" in p) or ("staruml" in p) or ("Star Uml" in p) or ("uml" in p)) :
	  os.system("StarUML")		

	#Adobe Photoshop
	elif (("run" in p) or  ("execute" in p ) or  ("open" in p )) and  (("adobe photoshop" in p) or ("photoshop" in p) or ("Photoshop" in p) or("Adobe Photoshop" in p)):
	  os.system("Photoshop")


	elif (("run" in p) or  ("execute" in p ) or  ("open" in p )) and  (("ms edge" in p) or ("edge" in p) or ("Edge" in p) or("MS Edge" in p)):
	  os.system("msedge")
	elif (("run" in p) or  ("execute" in p ) or  ("open" in p )) and  (("OBS" in p) or ("obs" in p) or ("OBS Studio" in p) or("Studio" in p)):
	  os.system("obs64")
	elif (("run" in p) or  ("execute" in p ) or  ("open" in p )) and  (("photo gallery" in p) or ("Photo" in p) or ("Photo Gallery" in p) or("Photos" in p)):
	  os.system("WLXPhotoGallery")
	elif (("run" in p) or  ("execute" in p ) or  ("open" in p )) and  (("Sublime Text Editor" in p) or ("Sublime" in p) or ("sublime" in p) or("sublime text editor" in p)):
	  os.system("sublime_text")	





	elif  ("exit" in p)  or ("quit" in p):
	  break

	else:
	  print("don't support")










#NOT WORKING
	#elif (("run" in p) or  ("execute" in p ) or  ("open" in p )) and  (("adobe creative cloud" in p) or ("adobe cloud" in p)) :
	#  os.system("Creative Cloud")
	#elif (("run" in p) or  ("execute" in p ) or  ("open" in p )) and  (("adobe illustrator" in p) or ("illustrator" in p) or ("Illustrator" in p) or("Adobe Illustrator" in p)):
	#  os.system("Illustrator")
	#elif (("run" in p) or  ("execute" in p ) or  ("open" in p )) and  (("team" in p) or ("team viewer" in p) ) :
	#  os.system("TeamViewer")
	#elif (("run" in p) or  ("execute" in p ) or  ("open" in p ))  and (("Snipping Tool" in p) or ("Snip tool" in p) or ("tool" in p)):
	#  os.system("snippingtool")