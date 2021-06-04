Voice---->

import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) there can be multiple voices in your system like voice[0], voice[1], etc. Choose as per your choice


Modules/Libraries-->

Install in you CLI using the command ==> 'pip install module_name'

1. pyttsx3: for voice

2. datetime: This is Python's Date and Time library

3. speechRecognition: For using Google's Web API for speech-to-text

4. Wikipedia : for searching queries on wikipedia.com

5. webbrowser: for opening websites

6. os: for system calls like opening files, shutting or restarting the system, etc.





References--->
https://en.wikipedia.org/wiki/Microsoft_Speech_API
https://www.programiz.com/python-programming/datetime/strftime
