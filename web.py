from talkbot import talkbot_func
print("Welcome to Talkbot!")
name = input("What is your name ?\n")
def func(ip):
    if ip == 1:
        talkbot_func()
    elif ip == 2:
        games()
    elif ip == 3:
        exit()
    else:
        print("ENTER VALID CHOICE !!\n")

def games():
    #if ans == 'yes' or ans == 'Yes' or ans == 'YES':
    gameip = input("1. Stone Paper Scissors\n2. Tic-Tac-Toe")
    if gameip == 1:
        import stone_paper_scissors
        exec('stone_paper_scissors')
    elif gameip == 2:
        import tic_tac_toe_mult
        exec('tic_tac_toe_mult.py')

if __name__ == "__main__":
    print ("\nMENU\n1. For talking to Talkbot \n2. To play games\n3. To exit\n") 
    ip = int(input("Enter your choice\n"))
    func(ip)
    ans = input("Do you want to continue using TalkBot?\n")
    while (ans == 'yes' or ans == 'Yes' or ans == 'YES'):
        print ("1. For talking to Talkbot \n2. To play games\n3. To exit")
        ip = int(input("Enter your choice\n"))
        func(ip)
    