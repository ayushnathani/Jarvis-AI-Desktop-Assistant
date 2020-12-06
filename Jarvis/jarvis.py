import pyttsx3
import datetime
import speech_recognition as sr
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
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak('Good morning sir!')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon sir!')

    else:
        speak('Good Evening Sir!')

    speak('I am Jarvis. Please tell me how can i help you')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print('Say that again please...')
        return "None"

    return query


def sendEmail(to, content):
    '''you need to allow access to less secure apps by searching on google " less secure app gmail"'''

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ayush28nathani@gmail.com', '@yush2807')
    server.sendmail('ayush28nathani@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.get(chromepath).open("youtube.com")

        elif "open google" in query:
            webbrowser.get(chromepath).open("google.com")

        elif "play music" in query:
            music_dir = 'C:\\Users\\Ayush Nathani\\Documents\\Downloads\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strtime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Ayush Nathani\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to ayush' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "ayush1005.cse18@chitkara.edu.in"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry unable to send email at the moment")

        elif 'quit' in query:
            speak('Quitting... Hope I was helpful')
            exit()
