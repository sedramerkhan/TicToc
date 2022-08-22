# Check l(O/X) won the match or not
# according to the rules of the game
import time


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[" " for x in range(size)] for y in range(size)]
        self.player ='O'
        self.opponent='X'

    # Check if the player can push the button or not
    def isfree(self, i, j):
        return self.board[i][j] == " "

    # Check the board is full or not
    def isfull(self,board = None):
        if board is None:
            board  =self.board

        for row in self.board:
            if row.count(' ') > 0:
                return False
        return True

    def winner(self, player, board=None):
        size = self.size
        if board is None:
            board = self.board
        # checking rows
        for i in range(size):
            win = True
            for j in range(size):
                if board[i][j] != player:
                    win = False
                    break
            if win:
                # print(f"row {i}")
                return win

        # checking columns
        for i in range(size):
            win = True
            for j in range(size):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                # print(f"col {j}")
                return win

        # checking diagonals
        win = True
        for i in range(size):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            # print(f"dia {i}")
            return win

        win = True
        for i in range(size):
            if self.board[i][size - 1 - i] != player:
                win = False
                break
        if win:
            # print(f"diag {i}")
            return win
        return False

    def evaluate(self,board) :
        player = self.player
        opponent = self.opponent
        size =self.size
        count = 0
        # Checking Rows
        for row in board :
            if row.count(player) == size :
                return 10
            elif row.count(opponent) == size :
                return -10

        # Checking Columns
        for i in range(size):
            l=[]
            for j in range(size):
                l.append(board[j][i])
            # print(l,"   ",l.count('X'))
            if l.count(player) == size :
                return 10
            elif l.count(player) == size :
                # print(l.count('X'))
                return -10


        # Checking Diagonals
        l =[]
        for i in range(size):
            l.append(board[i][i])
        if l.count(player) == size :
            return 10
        elif l.count(opponent) == size :
            return -10

        l =[]
        for i in range(size):
            l.append(board[i][size - 1- i])
        if l.count(player) == size :
            return 10
        elif l.count(opponent) == size :
            return -10

        # Else if none of them have won then return 0
        return 0

    def minimax(self,board, depth, isMax) :
        score = self.evaluate(board)
        # if score == 10 or score == -10: return score

        if self.isfull(board) :
            return score

        if (isMax) :
            best = -1000
            for i in range(self.size) :
                for j in range(self.size) :
                    if (board[i][j]==' ') :
                        board[i][j] = self.player
                        best = max( best, self.minimax(board,depth + 1,not isMax) )
                        board[i][j] = ' '
            return best

        else :
            best = 1000
            for i in range(self.size) :
                for j in range(self.size) :
                    if (board[i][j] == ' ') :
                        board[i][j] = self.opponent
                        best = min(best, self.minimax(board, depth + 1, not isMax))
                        board[i][j] = ' '
            return best

    def lose(self):
        board = self.board
        for i in range(self.size) :
            for j in range(self.size) :
                if (board[i][j] == ' ') :
                    board[i][j] = self.player
                    if(self.winner(self.player,board)):
                        board[i][j] = ' '
                        return i,j
                    board[i][j] = self.opponent
                    if(self.winner(self.opponent,board)):
                        board[i][j] = ' '
                        return i,j
                    board[i][j] = ' '
        return -1,-1




    def alpha_beta(self,board, depth, isMax,alpha,beta) :
        score = self.evaluate(board)
        if score == 10: return score
        if score == -10: return score

        if self.isfull(board) : return 0

        if (isMax) :
            best = -1000
            for i in range(self.size) :
                for j in range(self.size) :
                    if (board[i][j]==' ') :
                        board[i][j] = self.player
                        value = max( best, self.alpha_beta(board,depth + 1,not isMax,alpha,beta) )
                        board[i][j] = ' '
                        best = max( best, value)
                        alpha = max( alpha, best)
                        if beta <= alpha:
                            return best
            return best

        else :
            best = 1000
            for i in range(self.size) :
                for j in range(self.size) :
                    if (board[i][j] == ' ') :
                        board[i][j] = self.opponent
                        val = min(best, self.alpha_beta(board, depth + 1, not isMax,alpha,beta))
                        board[i][j] = ' '

                        best = min(best, val)
                        beta = min(beta, best)
                        if beta <= alpha:
                            return best

            return best

    # returning the best possible move for the pc
    def chooseBestMove(self, board =None) :
        t = time.time()
        best_val = -1000
        best_move = (-1, -1)
        if board is None:
            board = self.board

        loser = self.lose()
        if loser[0] != -1:
            return loser

        for i in range(self.size):
            for j in range(self.size) :
                if board[i][j] == ' ':


                    board[i][j] = 'O'
                    
                    moveVal = self.alpha_beta(board, 0, False,-1000,1000)

                    # moveVal = self.minimax(board, 0, False)

                    board[i][j] = ' '

                    if (moveVal > best_val) :
                        best_move = (i, j)
                        best_val = moveVal

        print("The value of the best Move is :", best_val)
        print(time.time()- t)
        return best_move

    def __str__(self):
        for row in self.board:
            for item in row:
                if item == ' ':
                    item = '-'
                print(item, end=" ")
            print()
        return ""


