import random
#import pymysql
import tkinter
from tkinter import *
from datetime import datetime
from tkinter import simpledialog
now = datetime.now()
current_time = now.strftime("%D - %H:%M \n")
import textwrap
#from talkbot3 import Ciastr_sps
#from talkbot3 import bspace_sps
#from talkbot2 import total_wins
#from trial2 import User_name, receive, accept
#from talkbot2 import cursor, db, User_name
## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
Ciastr_sps = "*"
bspace_sps="               " 
player = ''
rounds = 0
user_choice = 0
final_ciastr=""
def spsm(cursor):
	global Ciastr_sps
	global bspace_sps
	global final_ciastr
	# def accept():
	# 	global player
	# 	player = name_entry.get("1.0", 'end-1c').strip()
	# 	name_entry.delete("0.0", END)

	# 	if player != '':
	# 		ChatLog.config(state=NORMAL)
	# 		ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
	# 		ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=player, 
	# 		wraplength=200, font=("Arial", 10, "bold"), bg="skyblue", bd=4, justify="left"))
	# 		ChatLog.insert(END,'\n ', "left")
	# 		ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
	# 		ChatLog.yview(END)

	#to store the choice input

	# def choice_fun(msg): 
	# 	global user_choice
	# 	user_choice = msg

	def send():
		global Ciastr_sps
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
			# choice_fun(msg) 
		# else:
		# 	ChatLog.config(state=NORMAL)
		# 	ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
		# 	ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg, 
		# 	wraplength=200, font=("Arial", 10, "bold"), bg="skyblue", bd=4, justify="left"))
		# 	ChatLog.insert(END,'\n ', "left")
		# 	ChatLog.config(foreground="#0000CC", font=("Helvetica", 9))
		# 	ChatLog.yview(END)

	#function to receive the response from CIA and print it on screen
	def receive(response):        
		ChatLog.insert(END, current_time+' ', ("small", "thistle", "left"))
		ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=response, 
		wraplength=200, font=("Monserrat", 10, "bold"), bg="gray87", bd=4, justify="left"))
		ChatLog.insert(END, '\n ', "right")
		ChatLog.config(state=DISABLED)
		#ChatLog.insert(END, '\n ', "right")
		ChatLog.yview(END)
		#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(response,))
			

	top = Toplevel()
	top.title("Stone-Paper-Scissor")
	top.geometry("400x450")
	top.resizable(width=FALSE, height=FALSE)
	ChatLog = Text(top, bd=0, bg="gray71", height="8", width="50", font="Monserrat",)
	# nameButton = Button(top, font=("Verdana",12,'bold'), text="Accept", width="12", height=5,
	# 					bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
	# 					command= accept)

	#player = simpledialog.askstring("Input", "What is your first name?",parent=top)


	#Bind scrollbar to Chat window
	scrollbar = Scrollbar(top, command=ChatLog.yview)
	ChatLog['yscrollcommand'] = scrollbar.set

	#Create Button to send message
	SendButton = Button(top, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
						bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
						command= send)

	# AcceptButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
	#                     bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
	#                     command= accept)

	#Create the box to enter message
	#name_entry = Text(top, bd=0, bg="white",width="29", height="5", font="Arial")
	EntryBox = Text(top, bd=0, bg="white",width="29", height="5", font="Arial")
	#EntryBox.bind("<Return>", send)


	#Place all components on the screen
	scrollbar.place(x=376,y=6, height=438)
	ChatLog.place(x=6,y=6, height=436, width=370)
	#name_entry.place(x=6,y=6, height=50, width=250)
	#EntryBox.place(x=6, y=451, height=50, width=250)
	#SendButton.place(x=262, y=451, height=50, width = 70)
	#nameButton.place(x=262, y=6, height=50, width = 70)
	global player
	player = simpledialog.askstring("Input", "Enter the name of player:",parent=top)
	#print(type(rounds))
	name_msg = "Enter the name of player:"
	Ciastr_sps+=bspace_sps+"Cia: "+name_msg+'\n'
	Ciastr_sps+=bspace_sps+"You: "+player+'\n'
	#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name_msg,player))
	cursor.execute("INSERT INTO chathistory (Username) VALUES (%s) ON DUPLICATE KEY UPDATE Username=%s",(player,player))
	sps_db = "Rules for the game:1) Rock vs Scissor => Rock wins 2) Rock vs Paper => Paper wins 3) Scissor vs Paper => Scissor wins"
	Ciastr_sps+=bspace_sps+"Cia: "+sps_db+'\n'
	# rules = """\nRules for the game:\n1) Rock vs Scissor => Rock wins\n+
	# 								2) Rock vs Paper => Paper wins\n +
	# 								3) Scissor vs Paper => Scissor wins\n"""
	receive(sps_db)
	##cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(sps_db,player))

	winner_db = "Cia won the game. Better luck next time!"
	tie_msg = "It's a tie!"
	user_count = 0
	comp_count = 0
	i = 0
	rounds_db = "How many rounds would you like to play?"
	Ciastr_sps+=bspace_sps+"Cia: "+rounds_db+'\n'
	n = simpledialog.askstring("Input", "How many rounds would you like to play?",parent=top) #no. of rounds
	Ciastr_sps+=bspace_sps+"You: "+n+'\n'
	global rounds
	rounds = int(n)

	##cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ",(rounds_db,))
	##cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ",(n,))
	
	while i < rounds:
		choice_db = "Enter your choice: 1) Rock 2) Paper 3) Scissor"
		Ciastr_sps+=bspace_sps+"Cia: "+choice_db+'\n'
		receive(choice_db)
		user_choice = int(simpledialog.askstring("Input", "Your choice:",parent=top))
		Ciastr_sps+=bspace_sps+"You: "+str(user_choice)+'\n'
		#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ",(choice_db,))
		#cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ",(user_choice,))
		# while(user_choice > 3 or user_choice < 1):
		# 	valid_msg = "Enter valid choice:"
		# 	receive(valid_msg)
		# 	#user_choice = int(input(valid_msg + "\n"))
		# 	#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(valid_msg,))
		# 	#cursor.execute("INSERT INTO chathistory (User) VALUES (%s)",(user_choice,))

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
		c_choice = "Cia chooses..."
		Ciastr_sps+=bspace_sps+"Cia: "+c_choice+'\n'
		#print (c_choice + comp_choice_name)
		receive(c_choice)
		receive(comp_choice_name)
		#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(c_choice,))
		#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(comp_choice_name,))

		vs_msg = user_choice_name + " v/s " + comp_choice_name
		Ciastr_sps+=bspace_sps+"Cia: "+vs_msg+'\n'
		receive(vs_msg)
		#print (user_choice_name + " v/s " + comp_choice_name)

		if ((user_choice == 1 and comp_choice == 2) or
			(user_choice == 2 and comp_choice == 1)):
			p_win = "Paper wins.."
			#print (p_win)
			Ciastr_sps+=bspace_sps+"Cia: "+p_win+'\n'
			receive(p_win)
			#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(p_win,))
			result = 'Paper'
		elif ((user_choice == 1 and comp_choice == 3) or 
			(user_choice == 3 and comp_choice == 1)):
			r_win = "Rock wins.."
			Ciastr_sps+=bspace_sps+"Cia: "+r_win+'\n'
			#print (r_win)
			receive(r_win)
			#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(r_win,))
			result = 'Rock'
		else:
			s_win = "scissor wins.."
			Ciastr_sps+=bspace_sps+"Cia: "+s_win+'\n'
			#print (s_win)
			receive(s_win)
			#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(s_win,))
			result = 'Scissor'

		if (user_choice_name == result):
			user_count += 1
			user_won = "You win this round!"
			Ciastr_sps+=bspace_sps+"Cia: "+user_won+'\n'
			#print(user_won)
			receive(user_won)
			#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(user_won,))
		else:
			comp_count += 1
			cia_won = "Cia wins this round!"
			Ciastr_sps+=bspace_sps+"Cia: "+cia_won+'\n'
			#print(cia_won)
			receive(cia_won)
			#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(cia_won,))
		i = i + 1

	if (comp_count > user_count):
		cursor.execute("UPDATE scoreboard SET Stone_Paper_Scissors = Stone_Paper_Scissors+1 WHERE Username = 'Cia'")
		cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Username= 'Cia'")
		#print ("\n" + winner_db)
		Ciastr_sps+=bspace_sps+"Cia: "+winner_db+'\n'
		receive(winner_db)
		#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(winner_db,))
	elif (comp_count == user_count):
		Ciastr_sps+=bspace_sps+"Cia: "+tie_msg+'\n'
		#print (tie_msg)
		receive(tie_msg)
		#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(tie_msg,))
	else:
		cursor.execute("UPDATE scoreboard SET Stone_Paper_Scissors = Stone_Paper_Scissors+1 WHERE Username=%s",(player,))
		cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Username=%s",(player,))
		#print ("\nHurray!!" +player+ " won!!")
		last_game_msg = "Hurray!!" +player+ " won!!"
		Ciastr_sps+=bspace_sps+"Cia: "+last_game_msg+'\n'
		receive(last_game_msg)
		#cursor.execute("INSERT INTO chathistory (Cia) VALUES ('Hurray')")
		#cursor.execute("INSERT INTO chathistory (Cia) VALUES ('You')")
		#cursor.execute("INSERT INTO chathistory (Cia) VALUES ('won')")

	score_msg = "Score: Cia: " + str(comp_count) + " You" + ":" + str(user_count)
	#print("\nScore:\nCia: " + str(comp_count) + "\n" + "You" + ":" + str(user_count))
	Ciastr_sps+=bspace_sps+"Cia: "+score_msg+'\n'
	receive(score_msg)
	final_msg = "Thanks for playing! I hope you had fun!"
	Ciastr_sps+=bspace_sps+"Cia: "+final_msg+'\n'
	receive(final_msg)
	#print(Ciastr_sps)
	
	#cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(final_msg,))
	#from talkbot3 import Ciastr
	#db.commit()
	# print(cursor.rowcount, "record inserted")
	top.mainloop()
	from talkbot3 import kadak
	kadak(Ciastr_sps)
#def cia_msg():
	#global Ciastr_sps
	#return Ciastr_sps
