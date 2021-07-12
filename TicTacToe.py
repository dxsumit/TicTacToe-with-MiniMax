# tic tac toe game with minimax algorithm...

from math import inf as infinity
import random

board = {1 : ' ', 2 : ' ', 3 : ' ',
         4 : ' ', 5 : ' ', 6 : ' ',
         7 : ' ', 8 : ' ', 9 : ' '}

# reference board print...
def demoBoard(board):
    print(" ** REFERENCE POSITIONS **")
    count = 0
    for each in board:
        count += 1
        if(count % 3 != 0):
            print(count , end=" | ")
        else:
            print(count)
            if(count != 9):
                print('-'*10)

    print('_'*18)


class TicTacToe(object):
    def __init__(self, board):
        self.board = board

        count = 0
        print()
        for each in board:
            count += 1
            if(count % 3 != 0):
                print(board[each] , end=" | ")
            else:
                print(board[each])
                if(count != 9):
                    print('-'*10)
                

    def isSpacefree(self, position):
        if(position in range(10) and board[position] == " "):
            return True
        else:
            return False


    def checkWin(self, board):
        # row
        if(board[1] == board[2] == board[3] != " "):
            return [True, board[1]]
        elif(board[4] == board[5] == board[6] != " "):
            return [True, board[4]]
        elif(board[7] == board[8] == board[9] != " "):
            return [True, board[7]]
        # column
        elif(board[1] == board[4] == board[7] != " "):
            return [True, board[1]]
        elif(board[2] == board[5] == board[8] != " "):
            return [True, board[2]]
        elif(board[3] == board[6] == board[9] != " "):
            return [True, board[3]]
        # diagonal
        elif(board[1] == board[5] == board[9] != " "):
            return [True, board[1]]
        elif(board[3] == board[5] == board[7] != " "):
            return [True, board[3]]

        else:
            return [False]


    def checkDraw(self, board):
        # if board is fully filled...
        if(not any([True if board[x] == ' ' else False for x in board])):
            return True
        
        return False


    def insertPosition(self, position, letter = 'O'):
        if(self.isSpacefree(position)):
            board[position] = letter
            self.__init__(board)
            res = self.checkWin(board)
            if(res[0]):
                print(f'  Player {res[1]} won  ')
                exit()
            
            # if board is fully filled and none is winner then it is a draw...  
            if(not any([True if board[x] == ' ' else False for x in board]) and not res[0]):
                print("  Draw ")
                exit()

        else:
            position = int(input("  ==>> Space is either not free or NOT valid choose valid position..  "))
            self.insertPosition(position)

    

    def playMove(self, letter='O'):
        position = int(input(" Choose Position   "))
        self.insertPosition(position, letter)

    
    def MiniMax(self, board, depth, isMaximizing):
        # check for base conditions who won..
        winner = self.checkWin(board)
        if(winner[0]):
            # 'X' = bot, 'O' = player
            # return 1 if(winner[1] == 'X') else -1
            empty_spaces = [1 if board[x] == ' ' else 0 for x in board].count(1)
            if(winner[1] == 'X'):
                return 1*(empty_spaces + 1)
            else:
                return -1*(empty_spaces + 1)

        elif(self.checkDraw(board)):
            return 0

        if(isMaximizing):
            bestScore = -infinity
            for each in board:
                if(board[each] == " "):
                    board[each] = 'X'
                    # calling the minimax function for letter 'O'
                    score = self.MiniMax(board, 0, False)
                    # undo the move for next iter check
                    board[each] = " "
                    bestScore = max(score, bestScore)
            
            return bestScore
        
        else:
            bestScore = infinity
            for each in board:
                if(board[each] == " "):
                    board[each] = 'O'
                    # calling the minimax function with letter 'X' for maximization
                    score = self.MiniMax(board, 0, True)
                    # undo the move for next iter check
                    board[each] = " "
                    bestScore = min(score, bestScore)

            return bestScore


    def compMove(self, letter='X'):
        bestMove = 0
        bestScore = -infinity

        for each in board:
            if(board[each] == " "):
                board[each] = letter
                # calling the minimax function for letter 'O'
                score = self.MiniMax(board, 0, False)
                # undo the move for next iter check
                board[each] = " "
                # maxEval = max(eval, maxEval)
                if(score > bestScore):
                    bestScore = score
                    bestMove = each

        self.insertPosition(bestMove, letter)
        return

                

demoBoard(board)
obj = TicTacToe(board)
# pos = random.randint(1, 9)
# obj.insertPosition(pos, 'X')

while(True):
    obj.compMove('X')
    obj.playMove('O')
    
    
#  end of program    
