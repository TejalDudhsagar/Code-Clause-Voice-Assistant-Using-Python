import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audiovoice):
    #engine.say('Hello Dear')
    print(audiovoice)
    engine.say(audiovoice)
    engine.runAndWait()

#speak('my audio voice')

def greet():
    hour=int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<11:
        speak('Good Morning Sir')
    elif hour>11 and hour<15:
        speak('Good Afternoon Sir')
    elif hour>=15 and hour<24:
        speak('Good Evening Sir')
    speak('I am your Personal Assistant')

def askname():
    speak('What is Your Name Sir ?')
    name=takevoicecommand()
    speak('Welcome '+name)
    speak('How Can I Help You Sir')
    

def takevoicecommand():
    global text
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        try:
            audio=r.listen(source,timeout=30,phrase_time_limit=10)
            print("Compiling your voice please wait...")
            text=r.recognize_google(audio,language='en-in')
            print(text)
        except Exception as e:
            speak('Unable to recognize your voice')
        return text

if __name__=='__main__':
    greet()
    askname()
    
    while True:
        work=takevoicecommand().lower()
        if 'how are you' in work:
            speak('I am fine..Thankyou...')
            speak('How are You Sir ?')

        elif 'fine' in work or 'good' in work:
            speak('It is good to know sir that you are fine')
            
        elif 'open notepad' in work:
            path="c:\\windows\\system32\\notepad.exe"
            os.startfile(path)

        elif 'close notepad' in work:
            os.system("TASKKILL /F /IM notepad.exe")
            
        elif 'open chrome' in work or 'open google chrome' in work:
            url="youtube.com"
            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)

        elif 'close chrome' in work:
            os.system("TASKKILL /F /IM chrome.exe")

        
        

        elif 'bye' in work:
            speak('Bye sir...See you again....')
            exit()

        else:
            speak('I cant understand Please speak again')
        

