import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")     

    speak("How are you doing babe?,what can i help you with?")    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail,com', 587)
    server.ehlo()
    server.login('bhoranuj3@gmail.com', 'anujb109$')
    server.sendmail('bhoranuj3@gmail.com', to, content)
    server.close()
def takeCommand():
    #it will take microphone input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
    #logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Ok give me a sec...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open github' in query:
        webbrowser.open("github.com") 

    elif 'open gmail' in query:
        webbrowser.open("gmail.com")     

    elif 'open outlook' in query:
        webbrowser.open("outlook.com")

    elif 'open gogoanime' in query:
        webbrowser.open("gogoanime.sh")  


    elif 'the time' in query:
        strTime = datetime.datetime.now().strtime("%H:%M:%S")
        speak(f"it's {strTime}")

    elif 'email to anuj' in query:
        try:
            speak("what should i say?")
            content = takeCommand()
            to = "bhoranuj3@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("sorry the email is not been sent")  