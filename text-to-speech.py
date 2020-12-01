from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

root = Tk()
root.geometry("350x200") 
root.configure(bg='white')
root.title("TEXT TO SPEECH CONVERTER")

Label(root, text = "TEXT TO SPEECH", font = "arial 20 bold", bg='white').pack()
Label(font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=25,y=100)

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('TtS.mp3')
    playsound('TtS.mp3')
    os.remove('TtS.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit).place(x=100 , y = 140)
Button(root, font = 'arial 15 bold',text = 'CLEAR', width = '6' , command = Reset).place(x=175 , y = 140)

root.mainloop()