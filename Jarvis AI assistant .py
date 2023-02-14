from logging import exception
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import smtplib
import os


engine = pyttsx3.init('sapi5') #used to use inbuild voice in windows (sapi5)
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    '''this function will speak'''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''this functon is just for greeting''' 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Goodmorning sir! Have a good day")
    
    elif hour >12 and hour<18:
        speak("Good Afternoon sir! recomendation from me dont sleep ")

    else:
        speak("Good Evening sir! Time to chill out")

    speak("Hello sir! I am Jarvis an AI created by Sir Om Tarkunde . Please tell me how may I help you")

def takeCommand():
    '''This function will take microphone input from user and return string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        #print(e)

        print("Please say again......")
        return "None"
    return query

def sendEmail(to , content):
    speak("Sir for confirmation please write the three words")
    three_words = input("Enter your password")
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremailid',three_words)
    server.sendmail('youremailid',to,content)


if __name__ == '__main__':
    speak("""All systems getting activated.
    No Threats found. 
    CPU functioning is at its best.
    The system is ready to be used.  """)
    wishMe()

    while True:
        query = takeCommand().lower()
        #logic for executing commands based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences =2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open spotify' in query:
            spotifypath = "C:\\Users\\Om Avinash Tarkunde\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifypath)
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open vs code' in query :
            vscodepath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodepath)
        
        elif 'send email ' in query :
            try : 
                speak("What should I write ?")
                content = takeCommand()
                to = "yourname@email.com"
                sendEmail = (to,content)
                speak("Email has been sent")
            
            except Exception as e:
                print(e)
                print("Sorry sir due to some issues , I am not able to send this email")

        elif 'thank you jarvis' in query:
            exit()
