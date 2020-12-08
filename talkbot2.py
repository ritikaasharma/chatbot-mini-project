#chatterbot-corpus : has all the responses
#import MySQLdb 

#db = MySQLdb.connect(host="localhost",    
#                     user="root",         
 #                    passwd="tanmay1210", 
  #                   db="chatbot")
#cur = db.cursor()                     

#from tkinter import *
def games():
    #if ans == 'yes' or ans == 'Yes' or ans == 'YES':
        gameip = int(input("What would you like to play?\n1. Stone Paper Scissors\n2. Tic-Tac-Toe\n"))
        if gameip == 1:
            from subprocess import call
            call(["python", "stone_paper_scissors.py"])
        else:
            from subprocess import call
            call(["python", "tic_tac_toe_mult.py"])
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
from chatterbot.trainers import ChatterBotCorpusTrainer
#read_only=True : used to disable chatbots ability to learn after the training
#chatterbot.logic.MathematicalEvaluation : helps to solve maths problems
#chatterbot.logic.BestMatch : used to choose best match from the list of responses
my_bot = ChatBot(name = 'PyBot', read_only = True, logic_adapters = ['chatterbot.logic.MathematicalEvaluation',
                                                                        'chatterbot.logic.BestMatch']) 
trainer = ChatterBotCorpusTrainer(my_bot)


trainer.train("chatterbot.corpus.english")

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

namemsg="What is your name ?"


if(inmode=="Text"):
    welmsg="Welcome, I am Cia!"
    print(welmsg)
    name = input("What is your name ?\n")
    while True:
        request = input(name + ': ')
        #req = req.upper()
    
        if 'Bye' in request or 'bye' in request or 'BYE' in request:
            print('Cia: Bye, have a great day!')
            break
        elif 'Facts' in request or 'facts' in request or 'fact' in request or 'Fact' in request:
            from facts import facts_func
            print("Cia: ",facts_func())
        elif 'games' in request or 'Games' in request or 'game' in request: 
            print("Cia: ",games())
        else:
            res = my_bot.get_response(text = request)
            print("Cia:",res)
        
        

if(inmode=="Audio"):
    welmsg1 = "Welcome, I am Siya!"
    engine.say(welmsg1)
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
        
        if 'Bye' in req2 or 'bye' in req2 or 'BYE' in req2:
            byemsg = 'Bye, have a great day!'
            engine.say(byemsg)
            engine.runAndWait()
            exit()
        elif  'Facts' in req2 or 'facts' in req2 or 'fact' in req2 or 'Fact' in req2 :
            from facts import facts_func
            engine.say(facts_func())
            engine.runAndWait()
        elif 'games' in req2 or 'Games' in req2 or 'game' in req2:
            engine.say(games())
            engine.runAndWait()
        else:
            res = my_bot.get_response(text = req2)
            engine.say(res)
            engine.runAndWait()
