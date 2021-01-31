from tkinter import *
from tkinter import messagebox
#from trial2 import User_name,receive
#from talkbot2 import total_wins
#from talkbot2 import cursor 
count = 0
selected = True             #setting the first turn of the game  
name1 = ''
name2 = ''
def tttm(cursor):
        #function and GUI to accept names of players
        def names():   
            
            top = Toplevel()
            top.title("Names")
            top.geometry("400x300")
            top.resizable(width=FALSE, height=FALSE)
            def name1_func():
                global name1
                name1 = EntryBox1.get("1.0", 'end-1c').strip()
                EntryBox1.delete("0.0", END)
            def name2_func():
                global name2
                name2 = EntryBox2.get("1.0", 'end-1c').strip()
                EntryBox2.delete("0.0", END)
            EntryBox1 = Text(top, bd=0, bg="white",width="29", height="5", font="Arial")
            EntryBox2 = Text(top, bd=0, bg="white",width="29", height="5", font="Arial")
            name1Button = Button(top, font=("Verdana",12,'bold'), text="P1", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= name1_func)
            name2Button = Button(top, font=("Verdana",12,'bold'), text="P2", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= name2_func)
            destButton = Button(top, font=("Verdana",12,'bold'), text="Submit", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= top.destroy)
            EntryBox1.place(x=15,y = 50, height=50, width=250)
            EntryBox2.place(x=15,y = 150,height=50, width=250)
            name1Button.place(x=267,y = 50, height=50, width=70)
            name2Button.place(x=267,y = 150, height=50, width=70)
            destButton.place(x= 45, y = 250, height=30, width=120)
            top.mainloop()

        end_msg = "Thanks for playing! I hope you had fun!"
        cursor.execute("INSERT INTO scoreboard (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name1,name1))
        cursor.execute("INSERT INTO chathistory (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name1,name1))
        cursor.execute("INSERT INTO scoreboard (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name2,name2))
        cursor.execute("INSERT INTO chathistory (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name2,name2))
        top = Toplevel()
        top.title('Tic-Tac-Toe')
        

        b1 = Button(top , text = " ", font=("Geneva", 20), height = 3 , width = 6 , bg ="SystemButtonFace", command=lambda: click(b1))
        b2 = Button(top , text = " ", font=("Geneva", 20), height = 3 , width = 6 , bg ="SystemButtonFace", command=lambda: click(b2))
        b3 = Button(top , text = " ", font=("Geneva", 20), height = 3 , width = 6 , bg ="SystemButtonFace", command=lambda: click(b3))
        b4 = Button(top , text = " ", font=("Geneva", 20), height = 3 , width = 6 , bg ="SystemButtonFace", command=lambda: click(b4))
        b5 = Button(top , text = " ", font=("Geneva", 20), height = 3 , width = 6 , bg ="SystemButtonFace", command=lambda: click(b5))
        b6 = Button(top , text = " ", font=("Geneva", 20), height = 3 , width = 6 , bg ="SystemButtonFace", command=lambda: click(b6))
        b7 = Button(top , text = " ", font=("Geneva", 20), height = 3 , width = 6 , bg ="SystemButtonFace", command=lambda: click(b7))
        b8 = Button(top , text = " ", font=("Geneva", 20), height = 3 , width = 6 , bg ="SystemButtonFace", command=lambda: click(b8))
        b9 = Button(top , text = " ", font=("Geneva", 20), height = 3 , width = 6 , bg ="SystemButtonFace", command=lambda: click(b9))

        def click(b):
            global selected , count
            if b["text"] == " " and selected == True:
                b["text"] = "X"
                count += 1
                selected = False        
                check()

            elif b["text"] == " " and selected == False:
                b["text"] = "O"
                count += 1
                selected = True
                check()

            else:
                messagebox.showerror("Tic-Tac-Toe", "Select other box!")

        def check():
            winner = False
            n1=name1+" is the winner !!"
            n2=name2+" is the winner !!"

            if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
                b1.config(bg="#00FF00")
                b2.config(bg="#00FF00")
                b3.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n1)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n1,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s", (name1,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name1,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
                b4.config(bg="#00FF00")
                b5.config(bg="#00FF00")
                b6.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n1)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n1,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s", (name1,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name1,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))
            
            elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
                b7.config(bg="#00FF00")
                b8.config(bg="#00FF00")
                b9.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n1)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n1,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s", (name1,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name1,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
                b1.config(bg="#00FF00")
                b4.config(bg="#00FF00")
                b7.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n1)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n1,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s",(name1,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name1,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
                b2.config(bg="#00FF00")
                b5.config(bg="#00FF00")
                b8.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n1)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n1,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s",(name1,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name1,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
                b3.config(bg="#00FF00")
                b6.config(bg="#00FF00")
                b9.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n1)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n1,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=?",(name1,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name1,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
                b3.config(bg="#00FF00")
                b5.config(bg="#00FF00")
                b7.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n1)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n1,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s",(name1,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name1,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
                b1.config(bg="#00FF00")
                b5.config(bg="#00FF00")
                b9.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n1)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n1,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s",(name1,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name1,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            #player2's win-->
            elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
                b1.config(bg="#00FF00")
                b2.config(bg="#00FF00")
                b3.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n2)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n2,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s",(name2,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name2,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
                b4.config(bg="#00FF00")
                b5.config(bg="#00FF00")
                b6.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n2)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n2,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s",(name2,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name2,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
                b7.config(bg="#00FF00")
                b8.config(bg="#00FF00")
                b9.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n2)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n2,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s",(name2,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name2,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
                b1.config(bg="#00FF00")
                b4.config(bg="#00FF00")
                b7.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n2)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n2,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s",(name2,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name2,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
                b2.config(bg="#00FF00")
                b5.config(bg="#00FF00")
                b8.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n2)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n2,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s",(name2,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name2,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
                b3.config(bg="#00FF00")
                b6.config(bg="#00FF00")
                b9.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n2)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n2,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s",(name2,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name2,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
                b3.config(bg="#00FF00")
                b5.config(bg="#00FF00")
                b7.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n2)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n2,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s",(name2,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name2,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
                b1.config(bg="#00FF00")
                b5.config(bg="#00FF00")
                b9.config(bg="#00FF00")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe",n2)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(n2,))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Multi = Tic_Tac_Toe_Multi + 1 WHERE Name=%s",(name2,))
                disable_all_buttons()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(name2,))
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

            #tie-condition
            if count == 9 and winner == False:
                messagebox.showinfo("Tic-Tac-Toe", "It's a Tie ! \nNo one wins.")
                disable_all_buttons()
                print ("\n" + end_msg)
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(end_msg,))

        def disable_all_buttons():
            b1.config(state=DISABLED)
            b2.config(state=DISABLED)
            b3.config(state=DISABLED)
            b4.config(state=DISABLED)
            b5.config(state=DISABLED)
            b6.config(state=DISABLED)
            b7.config(state=DISABLED)
            b8.config(state=DISABLED)
            b9.config(state=DISABLED)


        def reset():
            #from subprocess import call
            #call(["python", "names"])
            names()
            selected = True
            count = 0
            n3="The game has started "+name1+" is first."
            messagebox.showinfo("Tic-Tac-Toe", n3)

            #positions of buttons
            b1.grid(row = 0, column = 0)
            b2.grid(row = 0, column = 1)
            b3.grid(row = 0, column = 2)
            b4.grid(row = 1, column = 0)
            b5.grid(row = 1, column = 1)
            b6.grid(row = 1, column = 2)
            b7.grid(row = 2, column = 0)
            b8.grid(row = 2, column = 1)
            b9.grid(row = 2, column = 2)

        # basic_menu = Menu(top)
        # top.config(menu=basic_menu)

        # options = Menu(basic_menu, tearoff=False)
        # basic_menu.add_cascade(label="options", menu=options)
        #options.add_command(label="Reset Game",command=reset)
        #options.add_separator()
        # options.add_command(label="Exit",command=top.quit)
        reset()
        top.mainloop()
