import turtle
import math
from tkinter import messagebox
#from talkbot2 import total_wins 
from talkbot2 import User_name

import MySQLdb

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
# db = MySQLdb.connect(
#     host = "localhost",
#     user = "root",
#     passwd = "#root9694",
#     database = "chatbotdb"
# )

def ttcwc(cursor):
    taken_msg = "That spot is taken!"
    user_won = "You won the game!"
    cia_won = "CIA won the game!"
    tie_msg = "It's a tie"
    #name_msg = "Enter the name of player:"
    #User_name = input(name_msg)
    #cursor.execute("INSERT INTO scoreboard (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(User_name,User_name))
    #cursor.execute("INSERT INTO chathistory (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(User_name,User_name))
    #cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(name_msg,User_name))

    def drawBoard():
        for i in range(2):
            drawer.penup()
            drawer.goto(-300,100 - 200 * i)
            drawer.pendown()
            drawer.forward(600)

        drawer.right(90)

        for i in range(2):
            drawer.penup()
            drawer.goto(-100 + 200 * i, 300)
            drawer.pendown()
            drawer.forward(600)

        num = 1
        for i in range(3):
            for j in range(3):
                drawer.penup()
                drawer.goto(-290 + j * 200, 280 - i * 200)
                drawer.pendown()
                drawer.write(num, font = ("Arial",12))
                num += 1

        screen.update()

    def drawX(x,y):
        drawer.penup()
        drawer.goto(x,y)
        drawer.pendown()

        drawer.setheading(60)

        for i in range(2):
            drawer.forward(75)
            drawer.backward(150)
            drawer.forward(75)
            drawer.left(60)

        screen.update()

    def drawO(x,y):
        drawer.penup()
        drawer.goto(x,y + 75)
        drawer.pendown()

        drawer.setheading(0)

        for i in range(180):
            drawer.forward((150 * math.pi)/180)
            drawer.right(2)

        screen.update()

    def checkWon(letter):
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == letter:
                return True

            if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == letter:
                return True

        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == letter:
            return True
        
        if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == letter:
            return True
        return False

    def checkDraw():
        count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == "x":
                    count += 1 

        if count > 3:
            return True
        else:
            return False

    def addO():
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "o"
                    if checkWon("o"):
                        drawO(-200 + 200 * j, 200 - 200 * i)
                        return
                    board[i][j] = " "

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "x"
                    if checkWon("x"):
                        board[i][j] = "o"
                        drawO(-200 + 200 * j, 200 - 200 * i)
                        return
                    board[i][j] = " "

        for i in range(0,3,2):
            for j in range(0,3,2):
                if board[i][j] == " ":
                    board[i][j] = "o"
                    drawO(-200 + 200 * j, 200 - 200 * i)
                    return

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "o"
                    drawO(-200 + 200 * j, 200 - 200 * i)
                    return

    def activate(functions):
        for i in range(9):
            screen.onkey(functions[i], str(i + 1))

    def deactivate():
        for i in range(9):
            screen.onkey(None, str(i + 1))

    def addX(row, column):
        #check
        if board[row][column] == "x" or board[row][column] == "o":
            messagebox.showinfo("Tic-Tac-Toe", "That spot is taken!")
            screen.update()
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(taken_msg,User_name))

        else:
            drawX(-200 + 200 * column , 200 - 200 * row)
            #add on comp's board
            board[row][column] = "x"

        if checkWon("x"):
            messagebox.showinfo("Tic-Tac-Toe", "You won the game!")
            cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(user_won,User_name))
            cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Single = Tic_Tac_Toe_Single+1 WHERE Name=%s",(User_name,))
            screen.update()
            deactivate()
            cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name=%s",(User_name,))

        else:
            addO()
            if checkWon("o"):
                messagebox.showinfo("Tic-Tac-Toe", "CIA won the game!")
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(cia_won,User_name))
                cursor.execute("UPDATE scoreboard SET Tic_Tac_Toe_Single = Tic_Tac_Toe_Single+1 WHERE Name = 'Cia'")
                screen.update()
                deactivate()
                cursor.execute("UPDATE scoreboard SET Total_wins = Total_wins+1 WHERE Name= 'Cia'")

            elif checkDraw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie")
                cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(tie_msg,User_name))
                screen.update()
                deactivate()

    def squareOne():
        addX(0,0)

    def squareTwo():
        addX(0,1)

    def squareThree():
        addX(0,2)

    def squareFour():
        addX(1,0)

    def squareFive():
        addX(1,1)

    def squareSix():
        addX(1,2)

    def squareSeven():
        addX(2,0)

    def squareEight():
        addX(2,1)

    def squareNine():
        addX(2,2)

    functions = [squareOne , squareTwo , squareThree , squareFour , squareFive , squareSix , squareSeven , squareEight , squareNine]

    drawer = turtle.Turtle()

    drawer.pensize(10)
    drawer.ht()

    screen = turtle.Screen()
    screen.tracer(0)

    drawBoard()

    #create board
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
        board.append(row)

    activate(functions)
    screen.listen()
    turtle.mainloop()
    #db.commit()
