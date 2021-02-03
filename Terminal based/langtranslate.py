import pyttsx3

import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS 
from talkbot2 import User_name
import os 


import MySQLdb

'''db = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "#root9694",
    database = "chatbotdb"
)'''
select_msg = "Select a source and target language (enter codes)"
source_db = "Source: "
dest_db = "Destination: "
choice_db = "Enter your input: "
#cursor = db.cursor()
    

def text_translator(cursor):
    languages = {"English": 'en', "French": 'fr', 
                    "Spanish": 'es', "German": 'de', "Italian": 'it', 
                    "Hindi": 'hi', "Marathi": 'mr', "Bengali":'bn', "Chinese(simplified)": 'zh-cn', 
                    "Chinese(traditional)": 'zh-tw', "Arabic": 'ar', "Japanese": 'ja', "Urdu": 'ur'}
    print("Language", " : ", "Code") 
    for x in languages: 
        print(x, " : ", languages[x])
    translator = Translator()
    
    print(select_msg) 
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(select_msg,))
    
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(source_db,))
    user_lang = input("\nSource:")
    cursor.execute("INSERT INTO chathistory (User) VALUES (%s)",(user_lang,))
    
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(dest_db,))
    op_lang = input("Destination:")
    cursor.execute("INSERT INTO chathistory (User) VALUES (%s)",(op_lang,))
    
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(choice_db,))
    user_ip = input("Enter your input:")
    cursor.execute("INSERT INTO chathistory (User) VALUES (%s)",(user_ip,))

    result = translator.translate(user_ip , src=user_lang, dest=op_lang)
    op_lang_db = "Your sentence in selected language is:"
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(op_lang_db,))
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(result.text.encode("utf-8"),))
    print("Your sentence in",op_lang,"is:",result.text)


def speech_translate(cursor):
    languages = {"English": 'en', "French": 'fr', 
                    "Spanish": 'es', "German": 'de', "Italian": 'it', 
                    "Hindi": 'hi', "Marathi": 'mr', "Bengali":'bn', "Chinese(simplified)": 'zh-cn', 
                    "Chinese(traditional)": 'zh-tw', "Arabic": 'ar', "Japanese": 'ja', "Urdu": 'ur'}
    print("Language", " : ", "Code") 
    for x in languages: 
        print(x, " : ", languages[x])
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


# if __name__ == "__main__":
    
#     inmode_ = input("Interactive mode : Audio/Text ? ")

#     if(inmode_=="Text" or inmode_ == "TEXT" or inmode_=="text"):
#         text_translator()
        
#     if(inmode_=="Audio" or inmode_=="AUDIO" or inmode_=="audio"):
#         speech_translate()

#db.commit()
