import pyttsx3

import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS 
from talkbot2 import User_name
import os 

import tkinter
from tkinter import *
from tkinter import simpledialog
from datetime import datetime
import textwrap
now = datetime.now()
current_time = now.strftime("%D - %H:%M \n")
user_lang = ''
import MySQLdb
def lang_translate(cursor):
    select_msg = "Select a source and target language (enter codes)"
    source_db = "Source: "
    dest_db = "Destination: "
    choice_db = "Enter your input: "

    top = Toplevel()
    top.title("Language translator")
    top.geometry("400x500")
    #top.resizable(width=FALSE, height=FALSE)

    #Create Chat window
    ChatLog = Text(top, bd=0, bg="white", height="8", width="50", font="Arial",)

    ChatLog.config(state=DISABLED)

    #Bind scrollbar to Chat window
    scrollbar = Scrollbar(top, command=ChatLog.yview)
    ChatLog['yscrollcommand'] = scrollbar.set

    #Create Button to send message
    

    #Create the box to enter message
    EntryBox = Text(top, bd=0, bg="white",width="29", height="5", font="Arial")

    #drop1 = OptionMenu(top, user_lang, *languages)


    scrollbar.place(x=376,y=6, height=386)
    ChatLog.place(x=6,y=6, height=436, width=370)
    EntryBox.place(x=6, y=451, height=50, width=250)
    
    #drop1.place(x=6,y=56, height=50,width = 150)

    inmode_ = simpledialog.askstring("Input", "Interactive mode : Audio/Text ? ",parent=top)

    languages = {"English": 'en', "French": 'fr', 
                        "Spanish": 'es', "German": 'de', "Italian": 'it', 
                        "Hindi": 'hi', "Marathi": 'mr', "Bengali":'bn', "Chinese(simplified)": 'zh-cn', 
                        "Chinese(traditional)": 'zh-tw', "Arabic": 'ar', "Japanese": 'ja', "Urdu": 'ur'}

    def send():
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

    def receive(response):        
        ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=response, 
        wraplength=200, font=("Arial", 10, "bold"), bg="#DDDDDD", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "right")
        ChatLog.config(state=DISABLED)
        #ChatLog.insert(END, '\n ', "right")
        ChatLog.yview(END)
        #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(response,))

    def accept(response): #to print source and desination as users msgs       
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=response, 
        wraplength=200, font=("Arial", 10, "bold"), bg="skyblue", bd=4, justify="left"))
        ChatLog.insert(END,'\n ', "left")
        ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
        ChatLog.yview(END)

    def text_translator():
        #("Language", " : ", "Code") 
        for x in languages: 
            pattern = x + " : " + languages[x]  
            receive(pattern)

        translator = Translator()
        
        receive(select_msg) 
        cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(select_msg,))
        receive(source_db)
        cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(source_db,))
        user_lang = simpledialog.askstring("Input", "Source:",parent=top)
        cursor.execute("INSERT INTO chathistory (User) VALUES (%s)",(user_lang,))
        accept(user_lang)
        receive(dest_db)
        cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(dest_db,))
        op_lang = simpledialog.askstring("Input", "Destination:",parent=top)
        cursor.execute("INSERT INTO chathistory (User) VALUES (%s)",(op_lang,))
        accept(op_lang)
        receive(choice_db)
        cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(choice_db,))
        user_ip = simpledialog.askstring("Input", "Enter the sentence to be translate:",parent=top)
        cursor.execute("INSERT INTO chathistory (User) VALUES (%s)",(user_ip,))
        accept(user_ip)

        result = translator.translate(user_ip , src=user_lang, dest=op_lang)
        op_lang_db = "Your sentence in selected language is:"
        cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(op_lang_db,))
        cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(result.text.encode("utf-8"),))
        end_msg = "Your sentence in "+ op_lang + " is:" + result.text
        receive(end_msg)
    
    SendButton = Button(top, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= send)
    SendButton.place(x=262, y=451, height=50, width = 70)
    
    #cursor = db.cursor()
        




    def speech_translate():
        # languages = {"English": 'en', "French": 'fr', 
        #                 "Spanish": 'es', "German": 'de', "Italian": 'it', 
        #                 "Hindi": 'hi', "Marathi": 'mr', "Bengali":'bn', "Chinese(simplified)": 'zh-cn', 
        #                 "Chinese(traditional)": 'zh-tw', "Arabic": 'ar', "Japanese": 'ja', "Urdu": 'ur'}
        for x in languages: 
            pattern = x + " : " + languages[x]  
            receive(pattern)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        # Creating Recogniser() class object 
        recog1 = spr.Recognizer() 

        # Creating microphone instance 
        mc = spr.Microphone() 
            
        # Translator method for translation 
        translator = Translator() 
            
        # short form of english in which 
        # you will speak 
        from_lang = 'en'
            
        with mc as source:
            which_langmsg = "Which language would you like to convert in?" 
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(which_langmsg,User_name))
            engine.say(which_langmsg)
            receive(which_langmsg)
            engine.runAndWait()


            recog1.adjust_for_ambient_noise(source, duration=0.2)
            to_lang = recog1.listen(source)
            to_lang1 = recog1.recognize_google(to_lang)
            cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(to_lang1,User_name))
            accept(to_lang1)
            choose_db = "You want to translate in " + to_lang1
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(choose_db,User_name))
            #print(choose_db + to_lang1)
            engine.say(choose_db)
            receive(choose_db)
            engine.runAndWait()
                
            speak_db = "Speak a sentence..."    
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(speak_db,User_name))
            engine.say(speak_db) 
            receive(speak_db)
            engine.runAndWait()
            recog1.adjust_for_ambient_noise(source, duration=0.2) 
                
                # Storing the speech into audio variable 
            audio = recog1.listen(source) 
                
                # Using recognize.google() method to 
                # convert audio into text 
            get_sentence = recog1.recognize_google(audio) 
            accept(get_sentence)
                # Using try and except block to improve 
                # its efficiency. 
            try: 
                    
                    # Printing Speech which need to 
                    # be translated. 
                tbt_db = "Phase to be Translated : "
                tbt = tbt_db + get_sentence 
                receive(tbt)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(tbt_db,User_name))
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(get_sentence,User_name))
                    # Using translate() method which requires 
                    # three arguments, 1st the sentence which 
                    # needs to be translated 2nd source language 
                    # and 3rd to which we need to translate in 
                text_to_translate = translator.translate(get_sentence, 
                                                            src= from_lang, 
                                                            dest= to_lang1) 
                    
                    # Storing the translated text in text 
                    # variable 
                text = text_to_translate.text 
                #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(text,User_name))
                op_lang_db = "Your sentence in selected language is:"
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(op_lang_db,))
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(text.encode("utf-8"),))
                end_msg = "Your sentence in "+ to_lang1 + " is:" + text
                receive(end_msg)
                    # Using Google-Text-to-Speech ie, gTTS() method 
                    # to speak the translated text into the 
                    # destination language which is stored in to_lang. 
                    # Also, we have given 3rd argument as False because 
                    # by default it speaks very slowly 
                speak = gTTS(text=text, lang=to_lang1, slow= False) 

                    # Using save() method to save the translated 
                    # speech in capture_voice.mp3 
                speak.save("captured_voice.mp3")	 
                    
                    # Using OS module to run the translated voice. 
                os.system("start captured_voice.mp3") 

                # Here we are using except block for UnknownValue 
                # and Request Error and printing the same to 
                # provide better service to the user. 
            except spr.UnknownValueError: 
                unk_err_db = "Unable to Understand the Input"
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(unk_err_db,User_name))
                #print(unk_err_db) 
                receive(unk_err_db)
                    
            except spr.RequestError as e: 
                req_err_db = "Unable to provide Required Output"
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(req_err_db,User_name))
                #print("Unable to provide Required Output".format(e))     
                receive(req_err_db)

    if(inmode_=="Text" or inmode_ == "TEXT" or inmode_=="text"):
        text_translator()
    elif (inmode_=="Audio" or inmode_=="AUDIO" or inmode_=="audio"):
        speech_translate()
    
    top.mainloop()
