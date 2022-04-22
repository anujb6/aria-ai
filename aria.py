import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import datetime
import pyjokes
import cv2
import mediapipe as mp
import wolframalpha
import json
import requests

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

def wolframe():
    speak('I can answer to computational and geographical questions  and what question do you want to ask now')
    question=takeCommand()
    app_id="PH2497-J5JL6GJTYT"
    client = wolframalpha.Client('R2K75H-7ELALHR35X')
    res = client.query(question)
    answer = next(res.results).text
    speak(answer)
    print(answer)     

def weather():
    api_key="8ceb7094aafde1af43748692d3bbd91c"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    speak("what is the city name")
    print("What is the city name?")
    city_name=takeCommand()
    print(f"Lol nice city{city_name}")
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature in kelvin unit is " +
                 str(current_temperature) +
                 "\n humidity in percentage is " +
                 str(current_humidiy) +
                 "\n description  " +
                 str(weather_description))
        print(" Temperature in kelvin unit = " +
                str(current_temperature) +
                 "\n humidity (in percentage) = " +
                 str(current_humidiy) +
                 "\n description = " +
                 str(weather_description))      
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


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"it's {strTime}")

        elif 'ask' in query:
          wolframe()

        elif 'email to anuj' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                speak("Whom To send?")
                to = takeCommand()
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry the email is not been sent")  

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            datetime.sleep(6)
            
        elif "weather" in query:
            weather()


        elif 'joke' in query:
            speak(pyjokes.get_joke("en","all"))     
        
        elif 'how are you' in query:            
            speak("I am fine, Thank you")            
            speak("How are you, Sir")          
        
        elif 'fine' in query or "good" in query:            
            speak("It's good to know that your fine")    
            
        elif "what's your name" in query or "What is your name" in query:            
            asName = "Aria"
            speak("My friends call me")            
            speak(asName)            
            print("My friends call me", asName)    
            
        elif "who made you" in query or "who created you" in query:            
            speak("I have been created by Anuj and Darshan.")     
            
        elif "who i am" in query:            
            speak("If you talk then definitely your human.")         
                
        elif "why you came to world" in query:            
            speak("Thanks to Anuj and Darshan. further It's a secret")    
            
        elif 'is love' in query:            
            speak("It is 7th sense that destroy all other senses")         
            
        elif "who are you" in query:            
            speak("I am your virtual assistant created by Anuj and darshan") 

        
