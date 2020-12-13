import pyttsx3
import random
import speech_recognition as sr
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r=sr.Recognizer()

user_count = 0
comp_count = 0
i = 0
n = "How many rounds would you like to play?"
engine.say(n)

engine.runAndWait()
print("Speak something...")

with sr.Microphone() as source:
    req=r.listen(source)
    req2=int(r.recognize_google(req))
    try:
        # using google speech recognition
        print("Your response: "+r.recognize_google(req))
    except:
        print("Sorry, I did not get that")
while req2 < n:
    user_c = "Enter your choice: 1) Rock 2) Paper 3) Scissor"
    engine.say(user_c)
    engine.runAndWait()	

    with sr.Microphone() as source2:
        #r.adjust_for_ambient_noise(source, duration=0.2)
        rq=r.listen(source2)
        user_choice=r.recognize_google(rq)
        try:
            # using google speech recognition
            print("Your response: "+r.recognize_google(rq))
        except:
            print("Sorry, I did not get that")		
    
    while(user_choice > 3 or user_choice < 1):
        user_c2 = "Enter valid choice:"
        engine.say(user_c2)
        engine.runAndWait()

    if user_choice == 1:
        user_choice_name = 'Rock'
    elif user_choice == 2:
        user_choice_name = 'Paper'
    else:
        user_choice_name = 'Scissor'

    comp_choice = random.randint(1, 3)

    while comp_choice == user_choice: 
            comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'


    print ("TalkBot chooses..." + comp_choice_name)
    engine.say(comp_choice_name)
    engine.runAndWait()	
    print(user_choice_name + " v/s " + comp_choice_name)
    engine.say(user_choice_name + " v/s " + comp_choice_name)
    engine.runAndWait()

    if ((user_choice == 1 and comp_choice == 2) or
        (user_choice == 2 and comp_choice == 1)):
        print("Paper wins..")
        pwin="Paper wins"
        engine.say(pwin)
        engine.runAndWait()			
        result = 'Paper'
    elif ((user_choice == 1 and comp_choice == 3) or 
        (user_choice == 3 and comp_choice == 1)):
        print ("Rock wins..")
        rwin="Rock wins"
        engine.say(rwin)
        engine.runAndWait()			
        result = 'Rock'
    else:
        print ("Scissor wins..")
        swin="Scissor wins"
        engine.say(swin)
        engine.runAndWait()
        result = 'Scissor'

    if (user_choice_name == result):
        user_count += 1
        print("You win this round!")
        ywin="You win this round!"
        engine.say(ywin)
        engine.runAndWait()			
    else:
        comp_count += 1
        print("TalkBot wins this round!")
        twin="TalkBot wins this round!"
        engine.say(twin)
        engine.runAndWait()				

    i = i + 1
    #ans = input("Do you want to play again? (Yes/No)")
    #if ans == 'No' or ans == 'no' or ans == 'NO':
    #break
if (comp_count > user_count):
    print ("\nTalkBot won the game. Better luck next time!")
    twin2="TalkBot won the game. Better luck next time!"
    engine.say(twin2)
    engine.runAndWait()		
elif (comp_count == user_count):
    print ("It's a tie!")
    tie="It's a tie!"
    engine.say(tie)
    engine.runAndWait()		
else:
    print ("\nHurray!! You won!!")
    ywin2="Hurray!! You won!!"
    engine.say(ywin2)
    engine.runAndWait()		
print("\nScore:\nTalkBot: " + str(comp_count) + "\nYou: " + str(user_count))

print ("\nThanks for playing! I hope you had fun!")
