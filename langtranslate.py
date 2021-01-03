import pyttsx3

import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS 
from talkbot2 import User_name
import os 


import MySQLdb

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "#root9694",
    database = "chatbotdb"
)

cursor = db.cursor()

languages = {"English": 'en', "French": 'fr', 
                 "Spanish": 'es', "German": 'de', "Italian": 'it', 
                 "Hindi": 'hi', "Marathi": 'mr', "Bengali":'bn', "Chinese(simplified)": 'zh-cn', 
                 "Chinese(traditional)": 'zh-tw', "Arabic": 'ar', "Japanese": 'ja', "Urdu": 'ur'}
print("Language", " : ", "Code") 
for x in languages: 
    print(x, " : ", languages[x])

def text_translator():
    translator = Translator()
    
    select_msg = "Select a source and target language (enter codes)"
    print(select_msg) 
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(select_msg,User_name))
    source_db = "Source: "
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(source_db,User_name))
    user_lang = input("\nSource:")
    cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(user_lang,User_name))
    dest_db = "Destination: "
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(dest_db,User_name))
    op_lang = input("Destination:")
    cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(op_lang,User_name))
    choice_db = "Enter your input: "
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(choice_db,User_name))
    user_ip = input("Enter your input:")
    cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(user_ip,User_name))

    result = translator.translate(user_ip , src=user_lang, dest=op_lang)
    #result_db = result.text
    #op_lang_db = "Your sentence in selected language is:"
    #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s,%s) ON DUPLICATE KEY UPDATE Name=%s",(op_lang_db,result_db,User_name))
    print("Your sentence in",op_lang,"is:",result.text)


def speech_translate():
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
        engine.runAndWait()


        recog1.adjust_for_ambient_noise(source, duration=0.2)
        to_lang = recog1.listen(source)
        to_lang1 = recog1.recognize_google(to_lang)
        cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(to_lang1,User_name))
        choose_db = "You want to translate in "
        cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(choose_db,User_name))
        print(choose_db + to_lang1)
        engine.say(choose_db + to_lang1)
        engine.runAndWait()
            
        speak_db = "Speak a sentence..."    
        cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(speak_db,User_name))
        engine.say(speak_db) 
        engine.runAndWait()
        recog1.adjust_for_ambient_noise(source, duration=0.2) 
            
            # Storing the speech into audio variable 
        audio = recog1.listen(source) 
            
            # Using recognize.google() method to 
            # convert audio into text 
        get_sentence = recog1.recognize_google(audio) 
            # Using try and except block to improve 
            # its efficiency. 
        try: 
                
                # Printing Speech which need to 
                # be translated. 
            tbt_db = "Phase to be Translated : "
            print(tbt_db + get_sentence) 
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
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(text,User_name))
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
            print(unk_err_db) 
                
        except spr.RequestError as e: 
            req_err_db = "Unable to provide Required Output"
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(req_err_db,User_name))
            print("Unable to provide Required Output".format(e)) 

inmode_ = input("Interactive mode : Audio/Text ? ")

if(inmode_=="Text" or inmode_ == "TEXT" or inmode_=="text"):
    text_translator()
    
if(inmode_=="Audio" or inmode_=="AUDIO" or inmode_=="audio"):
    speech_translate()
