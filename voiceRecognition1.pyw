# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 12:34:48 2022

@author: PCUSER
"""

import pyttsx3
import speech_recognition as sr
# import wikipedia
import webbrowser
import os
from tkinter import *
# init pyttsx

# try:
#     chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#     str_url = webbrowser.get(chrome_path)
# except:
#     str_url =  webbrowser


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)  # 1 for female and 0 for male voice
engine. setProperty("rate", 123)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query

# speak("Your voice assistant is activated")
top = Tk()
top.geometry("410x190")
#top.overrideredirect(1)
#top.attributes('-toolwindow', True)
# top.eval('tk::PlaceWindow . center')
top.eval('tk::PlaceWindow . bottom')
# top.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
txt=Label(top,text="Press Button and Speak")
#txt.pack()
top.title("Voice Assistant")
top.resizable(0,0)

# Label
text = Label(top,text="1) Open Google")
text.place(x=10,y=10)
# text.pack(side="left")

text1 = Label(top,text="2) Open YouTube")
text1.place(x=10,y=40)
# text1.pack(side="left")

text = Label(top,text="3) What to do")
text.place(x=10,y=70)
# text.pack(side="left")

text = Label(top,text="4) Exit")
text.place(x=10,y=100)
# text.pack(side="left")

speak("Your voice assistant is activated")

query=""
def comnd():
    txt.config(text="Listening...")
    top.title("Listening...")
    #txt.pack()
    global query
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        txt.config(text="Recognizing...")
        top.title("Recognizing...")
        #txt.pack()
        query = r.recognize_google(audio, language='en-in')
        txt.config(text="You said:" + query)
        top.title("You said:" + query)
        #txt.pack()
    except Exception as e:
        print(e)
        top.title("Didn't understand")
        speak("Didn't understand")
        query="None"
        top.title("Voice Assistant")
        return
    query=query.lower()
    if 'open youtube' in query:
        # speak("opening youtube")
        # webbrowser.open("youtube.com")
        speak("what do you want to search on youtube")
        query=''
        query = take_command().lower()

        top.title("You said:" + query)

        # str_url.open(f"https://youtube.com/results?search_query={query}")
        webbrowser.open(f"https://youtube.com/results?search_query={query}")
    elif 'open google' in query:
        speak("what do you want to search in google")
        query=''
        query = take_command().lower()
        top.title("You said:" + query)
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif 'what to do' in query:
        speak("I'm opening Google, search something on google")
        webbrowser.open("https://www.google.com")
    # elif 'website' in query:
    #     speak("Opening CADEM Softwares official website")
    #     str_url.open("http://www.cadem.net")
    # elif 'open pvd' in query:
    #     speak("opening cadem pvd")
    #     loc = "C:\\Users\\PCUSER\\AppData\\Roaming\\CADEM Softwares\\CademPVD - V22.02\\CademPVD.exe"
    #     os.startfile(loc)     
    elif 'exit' in query or 'close' in query:
        speak("Closing voice assistant application")
        exit()
    else:
        speak("Command not found")
    top.title("Voice Assistant")
    query=""
Button(top, text = 'Press & Speak',activeforeground = "black",activebackground = "pink",pady = 10, command=comnd).pack(side=BOTTOM)
top.mainloop()

# def wake_up():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         # speak("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         # speak("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print("You said:" + query + "\n")
#     except Exception as e:
#         # print(e)
#         # speak("I didnt understand, please try again")
#         # return "None"
#         pass
#     # print('cheching if condition')
#     if 'start' not in query:
#         query = ''
#         wake_up()
#     return query
#     return 'None'

# if __name__ == '__main__':
#     # top.mainloop()
#     while True:
#         query = wake_up().lower()
#         if 'start' in query:
#             comnd()