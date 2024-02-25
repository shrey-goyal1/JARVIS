import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
engine =  pyttsx3.init('sapi5') # sapi5 : used for taking voice , by Microsoft ! chahiye to google kr lo sapi5!!!
voices = engine.getProperty('voices')
#print (voices[0].id) only for showing the voices present in the pc
engine.setProperty('voice',voices[0].id)

def speak(audio): # speak function made to let the code speak
    engine.say(audio)   # i think engine is used for letting the code to speak!
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour <12:
        speak ("Good Morning!")

    elif hour>= 12 and hour<18:
        speak ("Good Afternoon!")

    else :
        speak ("Good Evening!")

    speak ("I am Jarvis! . What u want to do today ?")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r =  sr.Recognizer() # class used to recognize the audio from the microphone!
    with sr.Microphone() as source: # sr.Microphone is the command used to access microphone .
        print ("Listening.....")
        r.pause_threshold = 1 #pause_threshold (press Ctrl+ Click... for more info why its used!)used for checking the phrase is complete or not!
        #r.energy_threshold = 500
        # can use r.energy_threshold =  300+ (more than 300 ) if there are disturbance all over the environment!
        audio  = r.listen(source) # r.listen came from speech recognition class!

    try:
        print("Recognizing....")
        query =  r.recognize_google(audio,language= 'en-in') # uses google for any query ... also can we change the language?
        print(f"User said : {query}\n")

    except Exception as e:
        # print (e) [This statement will show the error! so keeping it in comment!]

        print ("Say that again please...")
        return "None"
    return query
"""def sendEmail(to , content):
    wont use this since we have to enable less secured apps in our gmail account so sorry
    #after enabling less secured apps in our email account
    server = smtplib.STMP('smtp.gmail.com', 587(#port))
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com' , 'your-password-here(#keep password in such a way that no one can see or access that easily)')
    server.sendmail('youremail@gmail.com', to , content)
    server.close()
"""

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing task based on query!
        if 'wikipedia' in query:
            speak ('Searching Wikipedia...')
            query =  query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak ("According to Wikipedia")
            print((results).encode('utf8')) #here .encode('utf8') was helping in simplifying the error in the code. so its not mentioned in the video! but using the net i wrote it ! always will be finding the solutuion for it!
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open music ' in query:
            webbrowser.open("https://www.jiosaavn.com/")
        #isnt working completely!
        elif 'open google ' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime =  datetime.datetime.now().strftime("%H:%M:%S")
            speak (f"Sir the time is {strTime}")
            print(strTime)
    
        elif 'open stack overflow ' in query:
            webbrowser.open("https://stackoverflow.com/")

        #nhi hua!!! dont know !! isnt starting!!
        elif 'open vscode' in query:
            codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  #code for opening any command!
            os.startfile(codePath)      #to start the file for which the location is been specified above!
        
        elif 'open mobile' in query:
            emulator = 'C:\\Program Files (x86)\\Microvirt\\MEmu\\MEmu.exe'
            os.startfile(emulator)
        
        
        elif 'open discord' in query:
            discord = 'C:\\Users\\shrey\\AppData\\Local\\Discord\\app-1.0.9025\\Discord.exe'
            os.startfile(discord)

        elif 'nice work' in query:
            speak ("Thank U Sir")

        elif 'good job' in query:
            speak ("Thank U Sir!")
            
        elif 'open download' in query:
            download_dir = 'C:\\Users\\admin\\Downloads'
            os.startfile(download_dir)


        elif 'open epic game' in query:
            eg_dir = 'G:\\EPIC GAMES\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe'
            os.startfile(eg_dir)
        elif 'open setting' in query:
           # Use os.environ to get the Windows directory
           windir = os.environ.get('SystemRoot', 'C:\\Windows')
           setting_dir = os.path.join(windir, 'System32', 'Control.exe')
           os.startfile(setting_dir)


        
        elif 'open steam' in query:
            steam_dir = 'G:\\STEAM\\steam.exe'
            os.startfile(steam_dir)
        
 
        elif ' bye' or 'quit' in query:
            speak("bye bye sir Take care...")
            exit()
            break
