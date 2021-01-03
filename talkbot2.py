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
    passwd = "#root9694",
    database = "chatbotdb"
)
cursor = db.cursor()
name_of_talkbot = "Cia"
cursor.execute("CREATE TABLE IF NOT EXISTS scoreboard (Name varchar(255) NOT NULL DEFAULT ' ', Stone_Paper_Scissors int DEFAULT 0, Tic_Tac_Toe_Single int DEFAULT 0, Tic_Tac_Toe_Multi int DEFAULT 0, Frequency int DEFAULT 0)")
cursor.execute("CREATE TABLE IF NOT EXISTS chathistory (Name varchar(255) DEFAULT ' ', Frequency int DEFAULT 0, User varchar(255) DEFAULT ' ', Cia varchar(500) DEFAULT ' ', Date_and_Time timestamp DEFAULT current_timestamp)")
cursor.execute("INSERT INTO scoreboard (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name_of_talkbot,name_of_talkbot))
# cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")

User_name = ''

def games(): 
    #if ans == 'yes' or ans == 'Yes' or ans == 'YES':
    #total_wins = 0
    gameip = int(input())
    cursor.execute("INSERT INTO chathistory (User) VALUES (%s)",(gameip,))
    if gameip == 1:
        from subprocess import call
        call(["python", "stone_paper_scissors.py"])
    elif gameip == 2:
        from subprocess import call
        call(["python", "tic_tac_toe_mult.py"])

def ytd():
    #if ans == 'yes' or ans == 'Yes' or ans == 'YES':
    from subprocess import call
    call(["python", "ytdownloader.py"])

bye_msg = "Bye, have a great day!"
gamemsg = "What would you like to play?\n1. Stone Paper Scissors\n2. Tic-Tac-Toe\n"
gamemsg_db = "What would you like to play? 1. Stone Paper Scissors 2. Tic-Tac-Toe"

def text():
    welmsg="Welcome, I am Cia!"
    print(welmsg)
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",[welmsg])
    ask = "What is your name ?"
    print(ask)
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",[ask])
    name = input()
    User_name = name
    cursor.execute("INSERT INTO scoreboard (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name,name))
    cursor.execute("INSERT INTO chathistory (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name,name))
    while True:
        req_inp = name + ': '
        print(req_inp , end = "")
        request = input()
        #req = req.upper()
        cursor.execute("INSERT INTO chathistory (User) VALUES (%s)",(request,))
        if 'Bye' in request or 'bye' in request or 'BYE' in request:
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(bye_msg,name))
            print('Cia: ' + bye_msg)
            break
        elif 'Facts' in request or 'facts' in request or 'fact' in request or 'Fact' in request:
            from facts import facts_func
            fact = facts_func()
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(fact,name))
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))
            print("Cia: ",fact)
        elif 'games' in request or 'Games' in request or 'game' in request: 
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(gamemsg_db,))
            print(gamemsg)
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))
            print("Cia: ",games())
        elif 'Language' in request or 'language' in request or 'Translator' in request or 'translator' in request or 'Translate' in request or 'translate' in request:
            print("Cia: ", end="")
            from subprocess import call
            call(["python", "langtranslate.py"])
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))
        elif 'YouTube' in request or 'Download' in request or 'youtube' in request or 'download a youtube video' in request:
            print('Cia: ',ytd())
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))
        else:
            res = my_bot.get_response(text = request)
            print("Cia:",res)
            cursor.execute("INSERT into chathistory (Cia) VALUES(%s)", [res])
        
        

def audio():
    welmsg1 = "Welcome, I am Siya!"
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",[welmsg1])
    engine.say(welmsg1)
    engine.runAndWait()

    engine.say(namemsg)
    engine.runAndWait()

    speak_msg = "Speak something..."
    print(speak_msg)
     
    with sr.Microphone() as source0:
        #r.adjust_for_ambient_noise(source, duration=0.2)
        name=r.listen(source0)
        nm=r.recognize_google(name)
        User_name = nm
        cursor.execute("INSERT INTO scoreboard (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(nm,nm))
        cursor.execute("INSERT INTO chathistory (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(nm,nm))
        try:
            # using google speech recognition
            ask_db = "Your response: "
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",[ask_db,nm])
            print(ask_db +r.recognize_google(name))
        except:
            sry_msg = "Sorry, I did not get that"
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",[sry_msg,nm])
            print(sry_msg)
    
    help_db = "Hey how can I help you ?"
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",[help_db,nm])
    tmsg="Hey"+nm+"How can I help you ?"  
    engine.say(tmsg)
    engine.runAndWait()      
    while True:
        print("Speak something...")
        engine.say("Speak something...")
        cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",[speak_msg,nm]) 
        engine.runAndWait() 
        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source, duration=0.2)
            req=r.listen(source)
            req2=r.recognize_google(req)
            try:
                # using google speech recognition
                print(ask_db + r.recognize_google(req))
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",[ask_db,nm])
            except:
                print(sry_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",[sry_msg,nm])
        
        if 'Bye' in req2 or 'bye' in req2 or 'BYE' in req2:
            engine.say(bye_msg)
            engine.runAndWait()
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",[bye_msg,nm])
            exit()
        elif  'Facts' in req2 or 'facts' in req2 or 'fact' in req2 or 'Fact' in req2 :
            from facts import facts_func
            fact = facts_func()
            engine.say(fact)
            engine.runAndWait()
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(fact,nm))
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(nm,))
        elif 'games' in req2 or 'Games' in req2 or 'game' in req2:
            print(gamemsg)
            engine.say(gamemsg)
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)  ON DUPLICATE KEY UPDATE Name=%s",(gamemsg_db,nm))
            games()
            engine.runAndWait()
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(nm,))
        elif 'Language' in req2 or 'language' in req2 or 'Translator' in req2 or 'translator' in req2 or 'Translate' in req2 or 'translate' in req2:
            from subprocess import call
            call(["python", "langtranslate.py"])
            time.sleep(5)
            engine.runAndWait()
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(nm,))
        elif 'YouTube' in req2 or 'video download' in req2 or 'downloader' in req2 or 'Downloader' in req2: 
            engine.say(ytd())
            engine.runAndWait()            
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(nm,))
        else:
            res = my_bot.get_response(text = req2)
            engine.say(res)
            engine.runAndWait()
            cursor.execute("INSERT into chathistory (Cia) VALUES(%s) ON DUPLICATE KEY UPDATE Name=%s", [res])


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

    #cursor.execute("ALTER table scoreboard ORDER BY Total_wins DESC")
    db.commit()


