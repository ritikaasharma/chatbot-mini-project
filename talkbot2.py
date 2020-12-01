#chatterbot-corpus : has all the responses
#import MySQLdb 

#db = MySQLdb.connect(host="localhost",    
#                     user="root",         
 #                    passwd="tanmay1210", 
  #                   db="chatbot")
#cur = db.cursor()                     

#from tkinter import *
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

#from gtts import gTTS
#from playsound import playsound
#import os
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

import speech_recognition as sr
r=sr.Recognizer()

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
#read_only=True : used to disable chatbots ability to learn after the training
#chatterbot.logic.MathematicalEvaluation : helps to solve maths problems
#chatterbot.logic.BestMatch : used to choose best match from the list of responses
my_bot = ChatBot(name = 'PyBot', read_only = True, logic_adapters = ['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch']) 

small_talk = ['Hi',
              'Hey',
              'Hello',
              'Hi there!',
              'How do you do ?',
              'How are you ?']


math_talk = ['Pythagoras Theorem : a² + b² = c²']
math_talk1 = ['Area of circle' ,'3.14r²']
list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk, math_talk1):
    list_trainer.train(item)

"""def Text_to_speech(text):
    Message = text
    speech = gTTS(text = Message)
    speech.save('TS.mp3')
    playsound('TS.mp3')
    os.remove('TS.mp3')
"""

inmode = input("Interactive mode : Audio/Text ? ")

#cur.execute("INSERT INTO cbdata (Name) VALUES (%s)", (name))
#db.commit()
#db.close()
welmsg="Welcome to TalkBot, I am Siya!"
namemsg="What is your name"


if(inmode=="Text"):
    print(welmsg)
    name = input("What is your name ?\n")
    while True:
        req = input(name + ': ')
        #req = req.upper()
    
        if req == 'Bye' or req == 'bye' or req == 'BYE':
            print('TalkBot: Bye, have a great day!')
            break
        else:
            res = my_bot.get_response(text = req)
            print("TalkBot:",res)
        """else:
            ans = input(("Would you like to play a game\n"))
            if ans == 'yes' or ans == 'Yes' or ans == 'YES':
                import stone_paper_scissors
                exec('stone_paper_scissors')"""
        

if(inmode=="Audio"):
    engine.say(welmsg)
    engine.runAndWait()

    engine.say(namemsg)
    engine.runAndWait()

    print("Speak something...")   
    with sr.Microphone() as source0:
        #r.adjust_for_ambient_noise(source, duration=0.2)
        name=r.listen(source0)
        nm=r.recognize_google(name)
        try:
            # using google speech recognition
            print("Your response: "+r.recognize_google(name))
        except:
            print("Sorry, I did not get that")
    tmsg="Hey"+nm+"How can I help you ?"        
    while True:
        engine.say(tmsg)
        engine.runAndWait()
        print("Speak something...")
        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source, duration=0.2)
            req=r.listen(source)
            req2=r.recognize_google(req)
            try:
                # using google speech recognition
                print("Your response: "+r.recognize_google(req))
            except:
                print("Sorry, I did not get that")
            #req = input(name + ': ')
            #req = req.upper()
        
        if req2 == 'Bye' or req2 == 'bye' or req2 == 'BYE':
            byemsg = 'Bye, have a great day!'
            engine.say(byemsg)
            engine.runAndWait()
            break
        else:
            res = my_bot.get_response(text = req2)
            #print("Bot:",res)
            engine.say(res)
            engine.runAndWait()
        """else:
            gamemsg = "Would you like to play a game?"
            engine.say(gamemsg)
            engine.runAndWait()
            with sr.Microphone() as source2:
                #r.adjust_for_ambient_noise(source, duration=0.2)
                ans=r.listen(source2)
                try:
                    # using google speech recognition
                    print("You spoke: "+r.recognize_google(ans))
                except:
                    print("Sorry, I did not get that")
                        
            #ans = input()
            if ans == 'yes' or ans == 'Yes' or ans == 'YES':
                import stone_paper_scissors
                exec('stone_paper_scissors')
        """
        