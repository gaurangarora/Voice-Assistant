Voice---->

#For Windows users

#*******************

#import pyttsx3

#engine = pyttsx3.init('sapi5')

#voices = engine.getProperty('voices')

#engine.setProperty('voice', voices[0].id) 
#voice[0] is male voice and voice[1] is female voice

#*******************



#for OS X users

#*******************

import subprocess

def speak(phrase): #Assigning voice to the assistant
   
 subprocess.call(['say', phrase])

#*******************






Modules/Libraries-->

1. pyttsx3 or subprocess

2. datetime

3. speechRecognition





References--->


sapi5

https://en.wikipedia.org/wiki/Microsoft_Speech_API


https://www.programiz.com/python-programming/datetime/strftime