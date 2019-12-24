import speech_recognition as sr  # Library for speech to text conversion
import wikipedia  # to search your query in wikipedia
from gtts import gTTS  # for text to speech conversion
import webbrowser  # for accessing webbrowser
import os
import datetime


# this function is used to convert text input into voice format and speaks in system default voice
def speak(audio):
    myobj = gTTS(text=audio, lang='en-in')
    myobj.save("Coco.mp3")
    os.system("mpg321 Coco.mp3")


# this function is used to give command to coco
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......\n")
        r.adjust_for_ambient_noise(source)
        # r.pause_threshold=1
        audio = r.listen(source)

    """There might be a possibility that voice may generate some error
        that's why we used try and exception block for handling errors"""
    try:
        print("Recognizing......\n")
        query = r.recognize_google(audio)
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please.....\n")
        return "None"
    return query


# This function is used to  wish user whenever main function runs
def wishme():
    hour = int(datetime.datetime.now().hour)

    """If else conditions to wish according to the time structure"""

    if 0 <= hour <= 12:
        speak("Good Morning!")
    elif 12 < hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Coco Sir. Please tell me, How may I help you?")


# MAIN function start from here
if __name__ == "__main__":
    wishme()
    while True:  # So that program runs till exited by the user
        query = takecommand().lower()

        """If block to search wikipedia for given query"""
        if 'in wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace('in wikipedia', "")
            query = query.replace('search', "")
            results = wikipedia.summary(query, sentences=2)  # return the first two sentences of Wikipedia summary
            speak("According to wikipedia..")
            speak(results)


        elif 'open my youtube channel' in query:  # to open your youtube channel
            webbrowser.open(
                "https://www.youtube.com/channel/UCMG6SdRux8tnjqZVd4s8oDw?view_as=subscriber")  # opens up the link to your channel



        elif 'search youtube' in query:  # to search your query in youtube
            query = query.replace('search youtube', "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")



        elif 'in google' in query:  #to search your query in google
            query = query.replace('in google', "")
            query = query.replace('search')
            webbrowser.open(
                f'https://www.google.com/search?sxsrf=ACYBGNTTUOqzfpoeGiPp5OW-0ycMwIDz-g%3A1577110767708&source=hp&ei'
                f'=78wAXqCMKYKR4-EP0qKKyAE&q={query}&oq='
                f'{query}&gs_l=psy-ab.3..35i39j0i131i67l2j0i131l2j0i67j0i131l3j0i67.3207.5330..5895...2.0..0.250.2405'
                f'.0j2j9......0....1..gws-wiz.....10..35i362i39j0.QHJJ8ztx5gU&ved=0ahUKEwjgv9C4'
                f'-8vmAhWCyDgGHVKRAhkQ4dUDCAY&uact=5')

        elif 'the time' in query:  #to get the time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        
