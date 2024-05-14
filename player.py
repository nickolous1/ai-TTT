class player:
    def __init__(self):
        pass

    def display(self, board):
        print("     |      |     ")
        print(" ", board[1], " |  ", board[2], " |  ", board[3])
        print("_____|______|_____")
        print("     |      |     ")
        print(" ", board[4], " |  ", board[5], " |  ", board[6])
        print("_____|______|_____")
        print("     |      |     ")
        print(" ", board[7], " |  ", board[8], " |  ", board[9])
        print("     |      |     ")

    def evaluate(self, board):
        points = 0
        winCombos = [(0,1,2), (3,4,5), (6,7,8),
                     (0,3,6), (1,4,7), (2,5,8),
                     (0,4,8), (2,4,6)]

        for combo in winCombos:
            xCount = 0
            oCount = 0
            if(board[combo[0]] == board[combo[1]] or board[combo[1]] == board[combo[2]]):
                points += 0.8
            if (board[combo[0]] == board[combo[1]] and board[combo[1]] == board[combo[2]]):
                points += 1
            if (board[combo[0]] != 'X' and board[combo[1]] != 'X' and board[combo[2]] != 'X'):
                points += 0.1
            for num in combo:
                if(board[num] == 'X'):
                    xCount += 1
                if(board[num] == 'O'):
                    oCount += 1
            if (xCount == 2 and oCount == 0):
                points = -10
            if (oCount == 3):
                points = 10
        #print()
        #self.display(board)
        #print(points)
        return points

    def move(self, board):

        states = []
        pointsArray = []
        highPoint = -10
        highState = None

        for spot in board:
            if(spot.isnumeric()):
                tempBoard = board.copy()
                tempBoard[int(spot) - 1] = 'O'
                states.append(tempBoard)

        for state in states:
            pointsArray.append(self.evaluate(state))

        for i in range(len(pointsArray)):
            if(pointsArray[i] >= highPoint):
                highPoint = pointsArray[i]
                highState = states[i]

        return highState

