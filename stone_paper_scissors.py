import random
import pymysql
#from talkbot2 import total_wins
# from talkbot2 import User_name
from talkbot2 import cursor, db, User_name
## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'

def spsm(cursor):
	name_msg = "Enter the name of player:"
	player = input(name_msg)
	cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name_msg,player))
	cursor.execute("INSERT INTO chathistory (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(player,player))

	sps_db = "Rules for the game:1) Rock vs Scissor => Rock wins 2) Rock vs Paper => Paper wins 3) Scissor vs Paper => Scissor wins"
	print ("\nRules for the game:\n1) Rock vs Scissor => Rock wins\n"+
									"2) Rock vs Paper => Paper wins\n" +
									"3) Scissor vs Paper => Scissor wins\n")

	cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(sps_db,User_name))
	winner_db = "Cia won the game. Better luck next time!"
	tie_msg = "It's a tie!"
	user_count = 0
	comp_count = 0
	i = 0
	rounds_db = "How many rounds would you like to play?"
	n = int (input(rounds_db) + "\n")
	cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ",(rounds_db,))
	cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ",(n,))
	while i < n:
		choice_db = "Enter your choice: 1) Rock 2) Paper 3) Scissor"
		user_choice = int(input(choice_db + "\n"))
		cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ",(choice_db,))
		cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ",(user_choice,))
		while(user_choice > 3 or user_choice < 1):
			valid_msg = "Enter valid choice:"
			user_choice = int(input(valid_msg + "\n"))
			cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(valid_msg,))
			cursor.execute("INSERT INTO chathistory (User) VALUES (%s)",(user_choice,))

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
		print (c_choice + comp_choice_name)
		cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(c_choice,))
		cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(comp_choice_name,))

		print (user_choice_name + " v/s " + comp_choice_name)

		if ((user_choice == 1 and comp_choice == 2) or
			(user_choice == 2 and comp_choice == 1)):
			p_win = "Paper wins.."
			print (p_win)
			cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(p_win,))
			result = 'Paper'
		elif ((user_choice == 1 and comp_choice == 3) or 
			(user_choice == 3 and comp_choice == 1)):
			r_win = "Rock wins.."
			print (r_win)
			cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(r_win,))
			result = 'Rock'
		else:
			s_win = "scissor wins.."
			print (s_win)
			cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(s_win,))
			result = 'Scissor'

		if (user_choice_name == result):
			user_count += 1
			user_won = "You win this round!"
			print(user_won)
			cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(user_won,))
		else:
			comp_count += 1
			cia_won = "Cia wins this round!"
			print(cia_won)
			cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(cia_won,))
		i = i + 1

	if (comp_count > user_count):
		cursor.execute("UPDATE scoreboard SET Stone_Paper_Scissors = Stone_Paper_Scissors+1 WHERE Name = 'Cia'")
		cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name= 'Cia'")
		print ("\n" + winner_db)
		cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(winner_db,))
	elif (comp_count == user_count):
		print (tie_msg)
		cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(tie_msg,))
	else:
		cursor.execute("UPDATE scoreboard SET Stone_Paper_Scissors = Stone_Paper_Scissors+1 WHERE Name=%s",(User_name,))
		cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(User_name,))
		print ("\nHurray!!" +User_name+ " won!!")
		cursor.execute("INSERT INTO chathistory (Cia) VALUES ('Hurray')")
		cursor.execute("INSERT INTO chathistory (Cia) VALUES ('You')")
		cursor.execute("INSERT INTO chathistory (Cia) VALUES ('won')")

	print("\nScore:\nCia: " + str(comp_count) + "\n" + "You" + ":" + str(user_count))
	final_msg = "Thanks for playing! I hope you had fun!"
	print (final_msg)
	cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s)",(final_msg,))

	#db.commit()
	# print(cursor.rowcount, "record inserted")
