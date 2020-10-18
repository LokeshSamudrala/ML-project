import random
import datetime
import pyttsx3

time=datetime.datetime.now().hour

def greetings():
    """
    This function is to greet the user. 

    """
    l=[]
    l.append("Hello...! , May i Know Your Name..")
    l.append("Hi Buddy..! This is bot.. What's your Name..")
    print(random.choice(l)+"🤗")
    voice_msg([random.choice(l)])

def introduce(name):

    """
    This function is to enter user name and wish the user by his/her name by using present time.

    """
    greet="Good Morning..!"
    if time>20:
        greet="Good Evening..!"
    elif time>15:
        greet="Good Evening..!"
    elif time>=11:
        greet="Good Afternoon..!"
    print(greet+" "+name+", I can u help to book ur movie ticket..🎥")
    voice_msg([greet+" "+name+", I can u help to book ur movie ticket"])
    

def voice_msg(var):

    """
    This function is used to convert text to speech and it speaks to the user.
    Source: "https://pypi.org/project/pyttsx3/"

    """
    speak = pyttsx3.init()
    speak.setProperty('rate',170)
    voices = speak.getProperty('voices')
    speak.setProperty('voice', voices[1].id)
    for i in var:
        speak.say(i)
    speak.runAndWait()