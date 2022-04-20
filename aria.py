import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import datetime
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

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

    speak("How are you doing ?,what can i help you with?")    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail,com', 587)
    server.ehlo()
    server.login('', '')
    server.sendmail('', to, content)
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
        query= takeCommand().lower()
        if 'wikipedia' in query:
            speak('Ok give me a sec...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com") 

        elif 'open gmail' in query:
            webbrowser.open("https://www.gmail.com")     

        elif 'open outlook' in query:
            webbrowser.open("https://www.outlook.com")

        elif 'open gogoanime' in query:
            webbrowser.open("https://gogoanime.pe")  


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
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
                
        elif 'joke' in query:
            speak(pyjokes.get_joke("en","all"))     
        
        elif 'how are you' in query:            
            speak("I am fine, Thank you")            
            speak("How are you, Sir")          
        
        elif 'fine' in query or "good" in query:            
            speak("It's good to know that your fine")    
            
        elif "what's your name" in query or "What is your name" in query:            
            assname = "Aria"
            speak("My friends call me")            
            speak(assname)            
            print("My friends call me", assname)    
            
        elif "who made you" in query or "who created you" in query:            
            speak("I have been created by Anuj and Darshan.")     
            
        elif "who i am" in query:            
            speak("If you talk then definitely your human.")         
                
        elif "why you came to world" in query:            
            speak("Thanks to Gaurav. further It's a secret")    
            
        elif 'is love' in query:            
            speak("It is 7th sense that destroy all other senses")         
            
        elif "who are you" in query:            
            speak("I am your virtual assistant created by Anuj") 
        
