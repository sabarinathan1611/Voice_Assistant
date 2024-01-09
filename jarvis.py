from datetime import datetime
from re import T
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import  os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
print(engine)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    Time()
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")
    



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.../")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)

    try:
        speak("Wait For Few Moments")
        query = r.recognize_google(audio, Language='en-in').lower()
        print("User Sayed", query)
    except Exception as e:
        print("SAY THAT AGAIN PLEASE")
        speak("SAY THAT AGAIN PLEASE")
        
        return False
    print(query)
   
    return query

def Time():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {strTime}")

def note():
        import subprocess
        import datetime

        def note(text):
            date = datetime.datetime.now()
            file_name = str(date).replace(":", "-") + "-note.txt"
            with open(file_name, "w") as f:
                f.write(text)
            notepad = "C:\\Program Files\\Notepad++"

            subprocess.Popen([notepad, file_name])





if __name__ == "__main__":
    wish()
    
    

    while True:
        query =takecommand()
             

        if 'wikipedia' in query:
            speak("searching in wikipedia")
            query = query.replace("wikipedia" , "")
            wikipedia.summary(query)
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'the time' in query:
          Time()


        elif 'open youtube' in query:
            speak("Opening Wait For Few Moments")
            webbrowser.open("https://www.youtube.com/", new=1)
            break

        elif 'browser'  in query:
            edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(edgePath)

        elif "spotify" or "play music" in query:
            musicPath = "C:\\Users\\Subha\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(musicPath)
        elif 'note' or "notepad" in query:
            note()

        elif 'go offline'in query:
            speak("ok,,bye!")
            break


