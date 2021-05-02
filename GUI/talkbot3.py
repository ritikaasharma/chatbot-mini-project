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
    passwd = "tanmay1210",
    database = "chatbotdb"
    )
bspace="               "
cursor = db.cursor()
db.autocommit(True)
name_of_talkbot = "Cia"
cursor.execute("CREATE TABLE IF NOT EXISTS scoreboard (Name varchar(255) NOT NULL DEFAULT ' ', Stone_Paper_Scissors int DEFAULT 0, Tic_Tac_Toe_Single int DEFAULT 0, Tic_Tac_Toe_Multi int DEFAULT 0, Frequency int DEFAULT 0,Total_wins int DEFAULT 0)")
cursor.execute("CREATE TABLE IF NOT EXISTS chathistory (Name varchar(255) UNIQUE DEFAULT ' ', Frequency int DEFAULT 0,  Date_and_Time timestamp DEFAULT current_timestamp ON UPDATE current_timestamp, History varchar(13000) DEFAULT '')")
Ciastr = ""
yt_flag = False

def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)
    global Ciastr
    global count
    global name
    global bspace
    if msg != '' and count == 0:
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "thistle"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg, 
        wraplength=200, font=("Monserrat", 10, "bold"), bg="medium purple", bd=4, justify="left"))
        ChatLog.insert(END,'\n ', "left")
        ChatLog.config(foreground="#0000CC", font=("Monserrat", 9))
        ChatLog.yview(END)
        name = msg
        cursor.execute("INSERT INTO scoreboard (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name,name))
        cursor.execute("INSERT IGNORE INTO chathistory (Name) VALUES (%s)",(name,))
        count+= 1
        return
    #elif msg == ''
    elif msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "thistle"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg, 
        wraplength=200, font=("Monserrat", 10, "bold"), bg="medium purple", bd=4, justify="left"))
        ChatLog.insert(END,'\n ', "left")
        ChatLog.config(foreground="#0000CC", font=("Monserrat", 9))
        ChatLog.yview(END)
        #cursor.execute("INSERT INTO chathistory (User) VALUES (%s)",(msg,))
        Ciastr+=bspace+"You: "+msg+"\n"
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
            from langtranslate2 import lang_translate
            lang_translate(cursor, name)
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))

        elif 'YouTube' in msg or 'Download' in msg or 'youtube' in msg or 'download a youtube video' in msg:
            from ytdownloader2 import ytfunc
            #print("Cia: ",end="")
            err_msg = "Error: Progressive Stream Unavailable"
            lvd="Enter the link of video to be downloaded :"
            link = simpledialog.askstring("Input", "Enter the link of video to be downloaded :",parent=base)
            svd="Select video quality : 1. Highest resolution available 2. 1080p 3. 720p 4. 480p 5. Lowest resolution available"
            quality = simpledialog.askstring("Input","Select video quality : 1. Highest resolution available 2. 1080p 3. 720p 4. 480p 5. Lowest resolution available",parent=base)
            #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(quality,name))
            Ciastr+=bspace+"Cia: "+lvd+'\n'
            Ciastr+=bspace+"You: "+link+'\n'
            Ciastr+=bspace+"Cia: "+svd+'\n'
            Ciastr+=bspace+"You: "+quality+'\n'
            vd=int(quality)
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))
            global yt_flag
            yt_flag = ytfunc(cursor,link,name,vd)
            if yt_flag:
                dc_db = "Download Completed !"
                Ciastr+=bspace+"Cia: "+dc_db+'\n'
                receive(dc_db)
                return
            receive(err_msg)
            
        else:
            bye_responses = ["Bye", "Have a great day", "See you soon", "Take care", "See you"]
            response = chat(msg)
            if response in bye_responses:
                receive(response)
                #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(response, name))
                Ciastr+=bspace+"Cia: "+response+'\n'
                #Ciastr.rjust(15)
                # cursor.execute("INSERT IGNORE INTO chathistory (Name) VALUES (%s)",(name,))
                cursor.execute("UPDATE chathistory SET History=CONCAT(History, %s) WHERE Name=%s",(Ciastr,name))  
                exit()
            else:
                receive(response)
                #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(response, name))
                Ciastr+=bspace+"Cia: "+response+'\n'
                #cursor.execute("INSERT INTO chathistory (Name,Cia) VALUES (%s,%s)",(name,Ciastr))

            

def audiobuttonfunc():
    global Ciastr
    global bspace
    engine.say("Speak something...")
        # cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",[speak_msg,nm]) 
    engine.runAndWait() 
    with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source, duration=0.2)
        req=r.listen(source)
        req2=r.recognize_google(req)
        # try:
        #     ask_db = "Your response: "
        #         # using google speech recognition
        #     receive(ask_db + r.recognize_google(req))
        #         # cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",[ask_db,nm])
        # except:
        #     sry_msg = "Sorry, I did not get that"
        #     receive(sry_msg)
        if 'games' in req2 or 'Games' in req2 or 'game' in req2:
            games()
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))

        elif 'Language' in req2 or 'language' in req2 or 'Translator' in req2 or 'translator' in req2 or 'Translate' in req2 or 'translate' in req2:
            #print("Cia: ")
            from langtranslate2 import lang_translate
            lang_translate(cursor, name)
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))

        elif 'YouTube' in req2 or 'Download' in req2 or 'youtube' in req2 or 'download a youtube video' in req2:
            from ytdownloader2 import ytfunc
            #print("Cia: ",end="")
            err_msg = "Error: Progressive Stream Unavailable"
            lvd="Enter the link of video to be downloaded :"
            link = simpledialog.askstring("Input", "Enter the link of video to be downloaded :",parent=base)
            svd="Select video quality : 1. Highest resolution available 2. 1080p 3. 720p 4. 480p 5. Lowest resolution available"
            quality = simpledialog.askstring("Input","Select video quality : 1. Highest resolution available 2. 1080p 3. 720p 4. 480p 5. Lowest resolution available",parent=base)
            #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(quality,name))
            Ciastr+=bspace+"Cia: "+lvd+'\n'
            Ciastr+=bspace+"You: "+link+'\n'
            Ciastr+=bspace+"Cia: "+svd+'\n'
            Ciastr+=bspace+"You: "+quality+'\n'
            vd=int(quality)
            cursor.execute("UPDATE chathistory SET Frequency = Frequency + 1 where Name =%s",(name,))
            global yt_flag
            yt_flag = ytfunc(cursor,link,name,vd)
            if yt_flag:
                dc_db = "Download Completed !"
                Ciastr+=bspace+"Cia: "+dc_db+'\n'
                receive(dc_db)
                return
            receive(err_msg)
            
        else:
            bye_responses = ["Bye", "Have a great day", "See you soon", "Take care", "See you"]
            res = chat(req2)
            if res in bye_responses:
                engine.say(res)
                engine.runAndWait()
                receive(req2)
                #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(res, name))
                Ciastr+=bspace+"Cia: "+res+'\n'
                #cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(req2, name))
                Ciastr+=bspace+"You: "+req2+'\n'
                #Ciastr.rjust(15)
                # cursor.execute("INSERT IGNORE INTO chathistory (Name) VALUES (%s)",(name,))
                cursor.execute("UPDATE chathistory SET History=CONCAT(History, CHAR(10), %s) WHERE Name=%s",(Ciastr,name))
                exit()
            else:
                engine.say(res)
                engine.runAndWait()
                receive(req2)
                #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(res, name))
                Ciastr+=bspace+"Cia: "+res+'\n'
                #cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(req2, name))
                Ciastr+=bspace+"You: "+req2+'\n'
                #Ciastr.rjust(15)
                #cursor.execute("INSERT INTO chathistory (Name,Cia) VALUES (%s,%s)",(name,Ciastr))
            

    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, current_time+' ', ("small", "right", "thistle"))
    ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res, 
    wraplength=200, font=("Monserrat", 10, "bold"), bg="medium purple", bd=4, justify="left"))
    ChatLog.insert(END,'\n ', "left")
    ChatLog.config(foreground="#0000CC", font=("Monserrat", 9))
    ChatLog.yview(END)

    
    
def audio():
    speak_msg = "Speak something..."
    receive(speak_msg)
    
     
    with sr.Microphone() as source0:
        #r.adjust_for_ambient_noise(source, duration=0.2)
        name=r.listen(source0)
        nm=r.recognize_google(name)
        # User_name = nm
        # cursor.execute("INSERT INTO scoreboard (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(nm,nm))
        # cursor.execute("INSERT INTO chathistory (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(nm,nm))
        # try:
        #     # using google speech recognition
        #     ask_db = "Your response: "
        #     # cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",[ask_db,nm])
        #     receive(ask_db +r.recognize_google(name))
        # except:
        #     sry_msg = "Sorry, I did not get that"
        #     # cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",[sry_msg,nm])
        #     receive(sry_msg)
    
    help_db = "Hey how can I help you ?"
    # cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",[help_db,nm])
    tmsg="Hey"+nm+"How can I help you ?"  
    Ciastr = "Cia: " + tmsg + "\n"
    engine.say(tmsg)
    receive(tmsg)
    cursor.execute("UPDATE chathistory SET History=CONCAT(History, CHAR(10), %s) WHERE Name=%s",(Ciastr,nm))
    engine.runAndWait() 
         

def accept():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "thistle"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg, 
        wraplength=200, font=("Monserrat", 10, "bold"), bg="medium purple", bd=4, justify="left"))
        ChatLog.insert(END,'\n ', "left")
        ChatLog.config(foreground="#0000CC", font=("Monserrat", 9))
        ChatLog.yview(END)
    return msg

#function to receive the response from CIA and print it on screen
def receive(response):
    global Ciastr
    global bspace        
    ChatLog.insert(END, current_time+' ', ("small", "thistle", "left"))
    ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=response, 
    wraplength=200, font=("Monserrat", 10, "bold"), bg="gray87", bd=4, justify="left"))
    ChatLog.insert(END, '\n ', "right")
    ChatLog.config(state=DISABLED)
    #ChatLog.insert(END, '\n ', "right")
    ChatLog.yview(END)
    #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(response,))
    #Ciastr+=bspace+response+'\n'

#Creating tkinter object
base = Tk()
base.title("TalkBot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)
base.bind('<Return>', send)
#Create Chat window
ChatLog = Text(base, bd=0, bg="gray71", height="8", width="50", font="Monserrat",)

#ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Arial",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="medium purple", activebackground="medium purple",fg='#ffffff',
                    command= send)

# display of audio button
photo = PhotoImage(file = r"D:\Codes\Python codes\TalkBot3GUI\favicon-32x32.png") 
AudioButton = Button(base, font=("Monserrat",12,'bold'),
                    bd=0, fg='#ffffff', image = photo,
                    command = audiobuttonfunc)


#Create the box to enter message
EntryBox = Text(base, bd=0, bg="gray81",width="29", height="5", font="Monserrat")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=438)
ChatLog.place(x=6,y=6, height=436, width=370)
EntryBox.place(x=6, y=451, height=40, width=250)
SendButton.place(x=262, y=451, height=40, width = 70)
AudioButton.place(x=332, y=451, height=40, width = 50)


def chat(req):

    f = open ('D:\Codes\Python codes\TalkBot3GUI\intents.json', "r") 
    
    # Reading from file 
    data = json.loads(f.read())
    req = re.sub(r'[^\w\s]', '', req).capitalize().rstrip() # to ignore punctuations and capitalising input string

    for intents in data['intents']:
        if req in intents['patterns']:
            response = random.choice(intents['responses'])
        
    return response

def tic_tac_toe_mult():
    global Ciastr
    global bspace
    #cursor.execute("INSERT INTO chathistory (Cia) VALUES ('3')")
    Ciastr+=bspace+"Cia: "+'3'+'\n'
    from tic_tac_toe_mult2 import tttm
    tttm(cursor)

def tic_tac_toe_with_cia():
    #cursor.execute("INSERT INTO chathistory (Cia) VALUES ('2')")
    global Ciastr
    global bspace
    Ciastr+=bspace+"Cia: "+'2'+'\n'
    from tic_tac_toe_with_cia2 import ttcwc
    flag = ttcwc(cursor)
    if flag:
        cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Single = Tic_Tac_Toe_Single+1 WHERE Name=%s",(name,))
        cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name,))
    cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Single = Tic_Tac_Toe_Single+1 WHERE Name = 'Cia'")
    cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name= 'Cia'")


def stone_paper_scissors():
    global Ciastr
    global bspace
    #cursor.execute("INSERT INTO chathistory (Cia) VALUES ('1')")
    Ciastr+=bspace+"Cia: "+'1'+'\n'
    from stone_paper_scissors2 import spsm
    spsm(cursor)

def games(): 
    gamemsg = "What would you like to play?\n1. Stone Paper Scissors\n2. Tic-Tac-Toe-With-Cia\n3. Tic-Tac-Toe-Mult"
    gamemsg_db = "What would you like to play? 1. Stone Paper Scissors 2. Tic-Tac-Toe 3. Tic-Tac-Toe-Mult" 
    #print("Cia: "+ gamemsg)
    receive(gamemsg_db)
    top = Toplevel()
    top.geometry("150x310")
    top.title("Game-Menu")
    SendButton1 = Button(top, font=("Montserrat",22,'bold'), text="1", width="12", height=5,
                    bd=0, bg="medium purple", activebackground="medium purple",fg='#ffffff',
                    command = stone_paper_scissors)
    SendButton2 = Button(top, font=("Montserrat",22,'bold'), text="2", width="12", height=5,
                    bd=0, bg="medium purple", activebackground="medium purple",fg='#ffffff',
                    command= tic_tac_toe_with_cia)
    SendButton3 = Button(top, font=("Montserrat",22,'bold'), text="3", width="12", height=5,
                    bd=0, bg="medium purple", activebackground="medium purple",fg='#ffffff',
                    command= tic_tac_toe_mult)

    SendButton1.place(x=0,y=0,height = 100, width = 150)
    SendButton2.place(x=0,y=105,height = 100, width = 150)
    SendButton3.place(x=0,y=210,height = 100, width = 150)
    top.mainloop()

# bye_msg = "Bye, have a great day!"
now = datetime.now()
current_time = now.strftime("%D - %H:%M \n")
name = ''
flag = False
        
if __name__ == "__main__":

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    r=sr.Recognizer()

    inmode = input("Interactive mode : Audio/Text ? ")
    #to accept name fromuser in the first run.

    # ask = "What is your name ?"
    # print(ask)
    # cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",[ask])
    # name = input()
    count = 0
    namemsg="What is your name ?"
    welmsg="Welcome, I am Cia!"
    #print(welmsg)
    receive(welmsg)
    Ciastr += "Cia: " + welmsg + "\n" + bspace + "Cia: " + namemsg + "\n"
    receive(namemsg)
    # cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",[welmsg])
    # cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",[namemsg])

    # if(inmode=="Text" or inmode == "TEXT" or inmode=="text"):
    #     text()
    
    if(inmode=="Audio" or inmode=="AUDIO" or inmode=="audio"):
        r=sr.Recognizer()      
        # cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",[welmsg1])
        engine.say("Welcome, I am Siya!")
        receive(welmsg)
        engine.runAndWait()

        Ciastr += "Cia: " + welmsg + "\n" + namemsg + "\n"
        
        engine.say(namemsg)
        receive(namemsg)
        engine.runAndWait()
        # cursor.execute("UPDATE chathistory SET History=CONCAT(History, CHAR(10), %s) WHERE Name=%s",(Ciastr,name))
        audio()

    #cursor.execute("ALTER table scoreboard ORDER BY Total_wins DESC")
    #db.commit()

base.mainloop()
