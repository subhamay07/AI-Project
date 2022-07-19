import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    
    elif hour>=18 and hour<22:
        speak("Good Evening!") 

    else:
        speak("Good Night!")  

    speak("Hi,I am Subhamay. How can I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
   
        query = takeCommand().lower()

    
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'hello' in query:
            speak("hello")    
            
        elif 'who are you' in query:
            speak("I am Subhamay. I born on 8th august 2000. I completed Madhyamik in 2017 and also completed Higher Secondary in 2019. Now I am Studing B.Tech in Computer Science and Engineering")
        
        elif 'how are you' in query:
            speak("I am Fine and how are you")
            
        elif 'in which class you are studing' in query:
            speak("I am a B.Tech 3rd year student in Computer Science and Engineering")
            
          

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            
        elif 'open telegram' in query:
            webbrowser.open("telegram.com")
        
          


        elif 'play music' in query:
           
            music_dir = 'E:\\favmusic'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

       