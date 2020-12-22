import logging
import time
import pyttsx3

import speech_recognition as sr

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

import MySQLdb

db = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "chatbotdb"
)

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS scoreboard (No int NOT NULL AUTO_INCREMENT PRIMARY KEY, Name varchar(255) NOT NULL, Stone_Paper_Scissors varchar(255) NOT NULL, Tic_Tac_Toe_Single varchar(255) NOT NULL, Tic_Tac_Toe_Multi varchar(255) NOT NULL, Frequency int NOT NULL)")

# cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")

def games():
    #if ans == 'yes' or ans == 'Yes' or ans == 'YES':
    
    gameip = int(input())
    if gameip == 1:
        from subprocess import call
        call(["python", "stone_paper_scissors.py"])
    else:
        from subprocess import call
        call(["python", "tic_tac_toe_mult.py"])

def ytd():
    #if ans == 'yes' or ans == 'Yes' or ans == 'YES':
    from subprocess import call
    call(["python", "ytdownloader.py"])


def text():
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
            gamemsg = "What would you like to play?\n1. Stone Paper Scissors\n2. Tic-Tac-Toe\n"
            print(gamemsg)
            print("Cia: ",games())
        elif 'Language' in request or 'language' in request or 'Translator' in request or 'translator' in request or 'Translate' in request or 'translate' in request:
            print("Cia: ", end="")
            from langtranslate import text_translator
            text_translator()
        elif 'YouTube' in request or 'Download' in request or 'youtube' in request or 'download a youtube video' in request:
            print('Cia: ',ytd())
        else:
            res = my_bot.get_response(text = request)
            print("Cia:",res)
        
        

def audio():
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
    engine.say(tmsg)
    engine.runAndWait()      
    while True:
        print("Speak something...")
        engine.say("Speak something...") 
        engine.runAndWait() 
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
            gamemsg = "What would you like to play?\n1. Stone Paper Scissors\n2. Tic-Tac-Toe\n"
            print(gamemsg)
            engine.say(gamemsg)
            games()
            engine.runAndWait()
        elif 'Language' in req2 or 'language' in req2 or 'Translator' in req2 or 'translator' in req2 or 'Translate' in req2 or 'translate' in req2:
            from langtranslate import speech_translate
            speech_translate()
            time.sleep(5)
            engine.runAndWait()
        elif 'YouTube' in req2 or 'video download' in req2 or 'downloader' in req2 or 'Downloader' in req2: 
            engine.say(ytd())
            engine.runAndWait()            
        else:
            res = my_bot.get_response(text = req2)
            engine.say(res)
            engine.runAndWait()

if __name__ == "__main__":

    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    r=sr.Recognizer()

    #read_only=True : used to disable chatbots ability to learn after the training
    #chatterbot.logic.MathematicalEvaluation : helps to solve maths problems
    #chatterbot.logic.BestMatch : used to choose best match from the list of responses
    my_bot = ChatBot(name = 'PyBot', read_only = True, logic_adapters = ['chatterbot.logic.MathematicalEvaluation',
                                                                            'chatterbot.logic.BestMatch']) 
    trainer = ChatterBotCorpusTrainer(my_bot)


    trainer.train("chatterbot.corpus.english")

    inmode = input("Interactive mode : Audio/Text ? ")

    #cur.execute("INSERT INTO cbdata (Name) VALUES (%s)", (name))
    #db.commit()
    #db.close()

    namemsg="What is your name ?"

    if(inmode=="Text" or inmode == "TEXT" or inmode=="text"):
        text()
    
    if(inmode=="Audio" or inmode=="AUDIO" or inmode=="audio"):
        audio()
