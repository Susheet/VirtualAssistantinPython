import pyttsx3  #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

print("Initialising now...")

MASTER = "Mister Soosheet"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',125)

#Speak function will pronounce the string which is  passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

# this function will wish as per the current time
def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    # print(hour)

    if(hour >= 0 and hour <12):
        speak("Good Morning" + MASTER + "  Welcome to the future")
    elif(hour >= 12 and hour <18):
        speak("Good Afternoon" + MASTER + " Welcome to the future")
    else:
        speak("Good Evening" + MASTER + " Welcome to the future")
   
    speak("Initialising ...")
    speak("I am Sooshhant how may I help you")

# this function will take  command from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please") 
        query = None

    return query

def sendEmail(to, content):
    server =  smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kumarhercules4@gmail.com','')
    server.sendmail("susheet13@gmaili.com",to,content)
    server.close()

#Main Program starts here

wishMe()

query = takeCommand()

#Logic for executing tasks as per the query
if 'wikipedia' in query.lower():
    speak('searching Wikipedia...')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences =2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    # webbrowser.open("youtube.com")
    url = "youtube.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    # webbrowser.open("youtube.com")
    url = "google.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")

elif 'open code' in query.lower():
    codePath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

elif 'play music' or 'play song' in query.lower():
    songs_dir = "B:\\Songs\\Audio Song\\songs"
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir,songs[0]))
elif 'email to kumarhercules' in query.lower():
    try:
        speak("what should I send")
        content = takeCommand()
        to = "susheet13@gmail.com"
        sendEmail(to,content)
        speak("Email has been sent succesfully")

    except Exception as e:
        print(e)
