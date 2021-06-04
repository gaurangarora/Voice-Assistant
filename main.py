import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

me = "Sir"  # The name assistant will call you


import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(phrase):
    newVoiceRate = 145
    engine.setProperty('rate', newVoiceRate)
    engine.say(phrase)
    engine.runAndWait()


def greeting():
    '''Assistant will wish us according to time'''

    hour = int(datetime.datetime.now().hour)  # 24-hour format
    if hour >= 0 and hour < 12:
        speak("Good morning" + me)
    elif hour >= 12 and hour < 17:
        speak("Good afternoon" + me)
    elif hour >= 17 and hour < 20:
        speak("Good evening" + me)
    else:
        speak("Good night" + me)

    speak("How can I be of help?")

def giveCommand():
    '''Command input via voice and returns the output in form of string'''

    rec = sr.Recognizer() #Recognizer class will recognise audio input
    with sr.Microphone() as source: #from where the audio should be captured
        print("Please speak...")
        rec.pause_threshold = 1
        #pause_threshold is seconds of non-speaking audio before a phrase is considered complete, default is 0.8, we have increased it to give us some gap to speak
        audio = rec.listen(source)

    try:
        print("Recognizing...")
        query = rec.recognize_google(audio, language = "en-in") #using the Google Web API for speech recognisation.
        print("You said: ", query)

    except Exception as exc:
        #print(exc) #this will show the error if unable to comprehend command
        print("Sorry, didn't catch that, please say again...")
        return "None" #remove this if you are printing line 58

    return query

if __name__ == "__main__":
    greeting() #we are keeping greeting out of while loop, because we want it to run only once
    while True: #this loop ensures that the assistant is always ready for commands
        query = giveCommand().lower() #converting query to lowercase for easier implementation
        if 'wikipedia' in query:
            speak("Searching for" + query)
            query = query.replace("wikipedia", "")
            wikiResult = wikipedia.summary(query, sentences = 2) #sentences is the number of lines it will speak from wikipedia search results
            print(wikiResult)
            speak(wikiResult)

        elif 'spotify' in query:
            webbrowser.open("open.spotify.com")

        elif 'google' in query:
            webbrowser.open('google.com')
            #Similary we can add more websites

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Public\\Music\\Sample Music' #give the path to the folder where your music files are
            songs = os.listdir(music_dir)
            print(songs)
            randomSong = random.randint(0,3)
            os.startfile(os.path.join(music_dir, songs[randomSong])) #this will play a random music fromthe list

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'time' in query:
            currentTime = datetime.datetime.now().strftime(("%H:%M:%S"))
            print(currentTime)
            speak(currentTime)

        elif 'date' in query:
            currentDate = datetime.datetime.now().strftime("%m/%d/%Y")
            print(currentDate)
            speak(currentDate)

        elif 'chrome' in query:
            chromeDir = 'C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe' #replace it with your own path as it may differ
            os.startfile(chromeDir)
        #similary we can add more apps and softwares


        elif 'bye' or 'goodbye' or 'quit' or 'exit' in query:
            speak("Goodbye, take care")
            quit()