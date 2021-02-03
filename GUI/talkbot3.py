import logging
import time

import speech_recognition as sr
import pyttsx3

import json
import random
import re 
import tkinter
from tkinter import *
from datetime import datetime
from tkinter import simpledialog
import textwrap
import MySQLdb

db = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "#root9694",
    database = "chatbotdb"
    )

cursor = db.cursor()
db.autocommit(True)
name_of_talkbot = "Cia"
cursor.execute("CREATE TABLE IF NOT EXISTS scoreboard (Name varchar(255) NOT NULL DEFAULT ' ', Stone_Paper_Scissors int DEFAULT 0, Tic_Tac_Toe_Single int DEFAULT 0, Tic_Tac_Toe_Multi int DEFAULT 0, Frequency int DEFAULT 0,Total_wins int DEFAULT 0)")
cursor.execute("CREATE TABLE IF NOT EXISTS chathistory (Name varchar(255) DEFAULT ' ', Frequency int DEFAULT 0, User varchar(255) DEFAULT ' ', Cia varchar(500) DEFAULT ' ', Date_and_Time timestamp DEFAULT current_timestamp)")

yt_flag = False

def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)
    global count
    global name
    if msg != '' and count == 0:
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg, 
        wraplength=200, font=("Arial", 10, "bold"), bg="skyblue", bd=4, justify="left"))
        ChatLog.insert(END,'\n ', "left")
        ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
        ChatLog.yview(END)
        name = msg
        cursor.execute("INSERT INTO scoreboard (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name,name))
        cursor.execute("INSERT INTO chathistory (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name,name))
        count+= 1
        return
    #elif msg == ''
    elif msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg, 
        wraplength=200, font=("Arial", 10, "bold"), bg="skyblue", bd=4, justify="left"))
        ChatLog.insert(END,'\n ', "left")
        ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
        ChatLog.yview(END)
        cursor.execute("INSERT INTO chathistory (User) VALUES (%s)",(msg,))
            # if 'Facts' in msg or 'facts' in msg or 'fact' in msg or 'Fact' in msg:
            #     from facts import facts_func
            #     fact = facts_func()
            #     cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(fact,name))
            #     cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))
            #     print("Cia: "+fact)

        if 'games' in msg or 'Games' in msg or 'game' in msg:
            games()
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))

        elif 'Language' in msg or 'language' in msg or 'Translator' in msg or 'translator' in msg or 'Translate' in msg or 'translate' in msg:
            print("Cia: ")
            from langtranslate2 import text_translator
            text_translator(cursor)
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))

        elif 'YouTube' in msg or 'Download' in msg or 'youtube' in msg or 'download a youtube video' in msg:
            from ytdownloader2 import ytfunc
            #print("Cia: ",end="")
            err_msg = "Error: Progressive Stream Unavailable"
            link = simpledialog.askstring("Input", "Enter the link of video to be downloaded :",parent=base)
            link_db = "Enter the link of video to be downloaded: "
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(link_db,name))
            cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(link,name))    
            quality = simpledialog.askstring("Input","Select video quality : 1. Highest resolution available 2. 1080p 3. 720p 4. 480p 5. Lowest resolution available",parent=base)
            select_quality = "Select video quality : 1. Highest resolution available 2. 1080p 3. 720p 4. 480p 5. Lowest resolution available"
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(select_quality,name))
            cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(quality,name))
            vd=int(quality)
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))
            global yt_flag
            yt_flag = ytfunc(cursor,link,name,vd)
            if yt_flag:
                dc_db = "Download Completed !"
                receive(dc_db)
                return
            receive(err_msg)
            return
            
        else:
            response = chat(msg)
            receive(response)
    #msg

        # response = "Welcome, I am Cia!"
        # ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
        # ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=response, 
        # wraplength=200, font=("Arial", 10, "bold"), bg="lightgreen", bd=4, justify="left"))
        # ChatLog.insert(END, '\n ', "right")
        # ChatLog.config(state=DISABLED)
        # ChatLog.yview(END)

def accept():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg, 
        wraplength=200, font=("Arial", 10, "bold"), bg="skyblue", bd=4, justify="left"))
        ChatLog.insert(END,'\n ', "left")
        ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
        ChatLog.yview(END)
    return msg

#function to receive the response from CIA and print it on screen
def receive(response):        
    ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
    ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=response, 
    wraplength=200, font=("Arial", 10, "bold"), bg="#DDDDDD", bd=4, justify="left"))
    ChatLog.insert(END, '\n ', "right")
    ChatLog.config(state=DISABLED)
    #ChatLog.insert(END, '\n ', "right")
    ChatLog.yview(END)
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(response,))

#Creating tkinter object
base = Tk()
base.title("Hello")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

#ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send)

# AcceptButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
#                     bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
#                     command= accept)

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=436, width=370)
EntryBox.place(x=6, y=451, height=50, width=250)
SendButton.place(x=262, y=451, height=50, width = 70)
# AcceptButton.place(x=334, y=451, height=50, width = 70)


def chat(req):

    f = open ('intents.json', "r") 
    
    # Reading from file 
    data = json.loads(f.read())
    req = re.sub(r'[^\w\s]', '', req).capitalize().rstrip() # to ignore punctuations and capitalising input string

    for intents in data['intents']:
        if req in intents['patterns']:
            res = intents['responses']
        
    return (random.choice(res))

def tic_tac_toe_mult():
    cursor.execute("INSERT INTO chathistory (Cia) VALUES ('3')")
    from tic_tac_toe_mult2 import tttm
    tttm(cursor)

def tic_tac_toe_with_cia():
    cursor.execute("INSERT INTO chathistory (Cia) VALUES ('2')")
    from tic_tac_toe_with_cia2 import ttcwc
    flag = ttcwc(cursor)
    if flag:
        cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Single = Tic_Tac_Toe_Single+1 WHERE Name=%s",(name,))
        cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name,))
    cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Single = Tic_Tac_Toe_Single+1 WHERE Name = 'Cia'")
    cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name= 'Cia'")


def stone_paper_scissors():
    cursor.execute("INSERT INTO chathistory (Cia) VALUES ('1')")
    from stone_paper_scissors2 import spsm
    spsm(cursor)

def games(): 
    gamemsg = "What would you like to play?\n1. Stone Paper Scissors\n2. Tic-Tac-Toe-With-Cia\n3. Tic-Tac-Toe-Mult"
    gamemsg_db = "What would you like to play? 1. Stone Paper Scissors 2. Tic-Tac-Toe 3. Tic-Tac-Toe-Mult" 
    #print("Cia: "+ gamemsg)
    receive(gamemsg_db)
    top = Toplevel()
    top.title("Game-Menu")
    SendButton = Button(top, font=("Verdana",12,'bold'), text="1", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command = stone_paper_scissors).pack()
    SendButton = Button(top, font=("Verdana",12,'bold'), text="2", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= tic_tac_toe_with_cia).pack()
    SendButton = Button(top, font=("Verdana",12,'bold'), text="3", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= tic_tac_toe_mult).pack()
    top.mainloop()

bye_msg = "Bye, have a great day!"
now = datetime.now()
current_time = now.strftime("%D - %H:%M \n")
name = ''
flag = False

# def text(msg):
    

#         else:
#             res = chat(msg)
#             #print("Cia: "+ res)
#             receive(res)
#             #send(res)
#             cursor.execute("INSERT into chathistory (Cia) VALUES(%s)", [res])
        

def audio():
    # base = Tk()
    # base.title("Hello")
    # base.geometry("400x500")
    # base.resizable(width=FALSE, height=FALSE)

    # #Create Chat window
    # ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

    # #ChatLog.config(state=DISABLED)

    # #Bind scrollbar to Chat window
    # scrollbar = Scrollbar(base, command=ChatLog.yview)
    # ChatLog['yscrollcommand'] = scrollbar.set

    # #Create Button to send message
    # SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
    #                     bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
    #                     command= send)

    # # AcceptButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
    # #                     bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
    # #                     command= accept)

    # #Create the box to enter message
    # EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
    # #EntryBox.bind("<Return>", send)


    # #Place all components on the screen
    # scrollbar.place(x=376,y=6, height=386)
    # ChatLog.place(x=6,y=6, height=436, width=370)
    # EntryBox.place(x=6, y=451, height=50, width=250)
    # SendButton.place(x=262, y=451, height=50, width = 70)

    welmsg1 = "Welcome, I am Siya!"      
    #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",[welmsg1])
    engine.say(welmsg1)
    receive(welmsg)
    engine.runAndWait()

    #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",[namemsg])
    engine.say(namemsg)
    receive(namemsg)
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
        receive(nm)
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
            print('Cia: ' + bye_msg + nm)
            exit()
        
        elif 'games' in req2 or 'Games' in req2 or 'game' in req2:
            gamemsg_db = "What would you like to play? 1. Stone Paper Scissors 2. Tic-Tac-Toe"
            gamemsg = "What would you like to play?\n1. Stone Paper Scissors\n2. Tic-Tac-Toe\n"
            print(gamemsg)
            engine.say(gamemsg)
            engine.runAndWait()
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)  ON DUPLICATE KEY UPDATE Name=%s",(gamemsg_db,nm))
            games()
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(nm,))

        elif 'Language' in req2 or 'language' in req2 or 'Translator' in req2 or 'translator' in req2 or 'Translate' in req2 or 'translate' in req2:
            # from subprocess import call
            # call(["python", "langtranslate.py"])
            from langtranslate import speech_translate
            speech_translate(cursor)
            time.sleep(5)
            engine.runAndWait()
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(nm,))

        elif 'YouTube' in req2 or 'video download' in req2 or 'downloader' in req2 or 'Downloader' in req2: 
            from ytdownloader import ytfunc
            print("Cia: ")
            engine.say(ytfunc(cursor))
            engine.runAndWait()            
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(nm,))

        else:
            res = chat(req2)
            engine.say(res)
            engine.runAndWait()
            cursor.execute("INSERT into chathistory (Cia) VALUES(%s) ON DUPLICATE KEY UPDATE Name=%s", (res,nm))

if __name__ == "__main__":

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    r=sr.Recognizer()

    inmode = input("Interactive mode : Audio/Text ? ")
    #to accept name from user in the first run.

    # ask = "What is your name ?"
    # print(ask)
    # cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",[ask])
    # name = input()
    
    count = 0
    namemsg="What is your name ?"
    welmsg="Welcome, I am Cia!"
    #print(welmsg)
    receive(welmsg)
    receive(namemsg)
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",[welmsg])
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",[namemsg])

    # if(inmode=="Text" or inmode == "TEXT" or inmode=="text"):
    #     text()
    
    if(inmode=="Audio" or inmode=="AUDIO" or inmode=="audio"):
        audio()

    #cursor.execute("ALTER table scoreboard ORDER BY Total_wins DESC")
    #db.commit()

base.mainloop()
