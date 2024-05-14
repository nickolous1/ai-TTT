from player import player
def display(board):
    print("     |      |     ")
    print(" " , board[0] , " |  " , board[1] , " |  " , board[2])
    print("_____|______|_____")
    print("     |      |     ")
    print(" " , board[3] , " |  " , board[4] , " |  " , board[5])
    print("_____|______|_____")
    print("     |      |     ")
    print(" " , board[6] , " |  " , board[7] , " |  " , board[8])
    print("     |      |     ")

def winCheck(board):
    winCombos = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]

    for combo in winCombos:
        xCount = 0
        oCount = 0
        for num in combo:
            if (board[num] == 'X'):
                xCount += 1
            if (board[num] == 'O'):
                oCount += 1
        if (xCount == 3):
            print("X won!")
            return True
        if (oCount == 3):
            print("O won!")
            return True

def game(AI):

    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    display(board)
    running = True
    validNum = True
    counter = 0

    while (running):
        while (validNum):
            player = int(input("Where would you like to go? "))
            if (player >= 1 and player <= 9 and board[player - 1].isnumeric()):
                board[player - 1] = 'X'
                counter += 1
                if (winCheck(board)):
                    running = False
                elif (counter == 9):
                    running = False
                    print("It is a tie")
                validNum = False
            else:
                print("That's not a valid number")

        board = AI.move(board).copy()
        counter += 1
        if (winCheck(board)):
            running = False
        validNum = True
        display(board)


if __name__ == '__main__':

    print("Welcome to TicTacToe\nYou will play against an AI\nYou start as X, the AI is O")
    AI = player()
    while(True):
        playCount = (input("Do you want to play TicTacToe? Type 1 to play, or 2 to exit\n"))
        if(playCount == '1'):
            game(AI)
        elif(playCount == '2'):
            break
        else:
            print("Please enter 1 or 2\n")



