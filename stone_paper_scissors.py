import random

print ("\nRules for the game:\n1) Rock vs Scissor => Rock wins\n"+
							  	"2) Rock vs Paper => Paper wins\n" +
								"3) Scissor vs Paper => Scissor wins\n")

user_count = 0
comp_count = 0
i = 0
n = int (input ("How many rounds would you like to play?\n"))
while i < n:
	user_choice = int(input("Enter your choice: 1) Rock 2) Paper 3) Scissor\n"))

	while(user_choice > 3 or user_choice < 1):
		user_choice = int(input("Enter valid choice:\n"))

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

	print (user_choice_name + " v/s " + comp_choice_name)

	if ((user_choice == 1 and comp_choice == 2) or
		(user_choice == 2 and comp_choice == 1)):
		print ("Paper wins..")
		result = 'Paper'
	elif ((user_choice == 1 and comp_choice == 3) or 
		(user_choice == 3 and comp_choice == 1)):
		print ("Rock wins..")
		result = 'Rock'
	else:
		print ("Scissor wins..")
		result = 'Scissor'

	if (user_choice_name == result):
		user_count += 1
		print("You win this round!")
	else:
		comp_count += 1
		print("TalkBot wins this round!")

	#ans = input("Do you want to play again? (Yes/No)")
	#if ans == 'No' or ans == 'no' or ans == 'NO':
		#break
	i = i + 1

if (comp_count > user_count):
	print ("\nTalkBot won the game. Better luck next time!")
elif (comp_count == user_count):
	print ("It's a tie!")
else:
	print ("\nHurray!! You won!!")
print("\nScore:\nTalkBot: " + str(comp_count) + "\nYou: " + str(user_count))

print ("\nThanks for playing! I hope you had fun!")