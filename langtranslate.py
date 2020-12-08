
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS 
import os 

languages = {"English": 'en', "French": 'fr', 
                 "Spanish": 'es', "German": 'de', "Italian": 'it', 
                 "Hindi": 'hi', "Marathi": 'mr', "Bengali":'bn', "Chinese(simplified)": 'zh-cn', 
                 "Chinese(traditional)": 'zh-tw', "Arabic": 'ar', "Japanese": 'ja', "Urdu": 'ur'}
print("Language", " : ", "Code") 
for x in languages: 
    print(x, " : ", languages[x])

def text_translator():
    translator = Translator()
     
    print("Select a source and target language (enter codes)") 

    user_lang = input("\nSource: ")
    op_lang = input("Destination: ")
    user_ip = input("Enter your input: ")

    result = translator.translate(user_ip , src=user_lang, dest=op_lang)

    print("Your sentence in",op_lang,"is:",result.text)


def speech_translate():
    # Creating Recogniser() class object 
    recog1 = spr.Recognizer() 

    # Creating microphone instance 
    mc = spr.Microphone() 


    # Capture Voice 
    with mc as source: 
        print("Speak 'hello' to initiate the Translation !") 
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
        recog1.adjust_for_ambient_noise(source, duration=0.2) 
        audio = recog1.listen(source) 
        MyText = recog1.recognize_google(audio) 
        MyText = MyText.lower() 

    # Here initialising the recorder with 
    # hello, whatever after that hello it 
    # will recognise it. 
    if 'hello' in MyText: 
        
        # Translator method for translation 
        translator = Translator() 
        
        # short form of english in which 
        # you will speak 
        from_lang = 'en'
        
        # In which we want to convert, short 
        # form of hindi 
        
        with mc as source: 
            print("Which language would you like to convert in?")
            recog1.adjust_for_ambient_noise(source, duration=0.2)
            to_lang = recog1.listen(source)
            to_lang1 = recog1.recognize_google(to_lang)
            print("You want to translate in " + to_lang1)
            
            print("Speak a sentence...") 
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
                print("Phase to be Translated : "+ get_sentence) 

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
                print("Unable to Understand the Input") 
                
            except spr.RequestError as e: 
                print("Unable to provide Required Output".format(e)) 
# text_translator()
#speech_translate()