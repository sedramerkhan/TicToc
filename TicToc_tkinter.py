# Tic Tac Toe game with GUI
# using tkinter

# importing all necessary libraries
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
from TicTocBoard import Board

turn = 0
who_start = 0
sign = 0


class boardGui:

    def __init__(self, size):
        self.ticTocBoard = Board(size)
        self.size = size

    # checking how is the winner
    def check_win(self, gb):
        can_play = True  # this is for system
        board = self.ticTocBoard.board
        if self.ticTocBoard.winner("X", board):
            gb.destroy()
            can_play = False
            box = messagebox.showinfo("Winner", "Player 1 won the match")
        elif self.ticTocBoard.winner("O", board):
            # gb.destroy()
            can_play = False
            box = messagebox.showinfo("Winner", "Player 2 won the match")
        elif self.ticTocBoard.isfull():
            # gb.destroy()
            can_play = False
            box = messagebox.showinfo("Tie Game", "Tie Game")
        return can_play

    # Configure text on button while playing with another player
    def get_text(self, i, j, gb, l1, p2):
        global turn
        global sign
        board = self.ticTocBoard.board
        if board[i][j] == ' ':
            if sign % 2 == 0:
                l1.config(state=DISABLED)
                p2.config(state=ACTIVE)
                board[i][j] = "X"
            else:
                p2.config(state=DISABLED)
                l1.config(state=ACTIVE)
                board[i][j] = "O"
            sign += 1
            button[i][j].config(text=board[i][j])
            print(self.ticTocBoard)

        self.check_win(gb)

    # Decide the next move of system
    def pc(self):
        best = self.ticTocBoard.chooseBestMove()
        return best
        # possiblemove = []
        # board = self.ticTocBoard.board
        # for i in range(self.size):
        #     for j in range(self.size):
        #         if board[i][j] == ' ':
        #             possiblemove.append([i, j])
        # move = []
        # if possiblemove == []:
        #     return
        # else:
        #     for let in ['O', 'X']:
        #         for move in possiblemove:
        #             boardcopy = deepcopy(board)
        #             boardcopy[move[0]][move[1]] = let
        #             if self.ticTocBoard.winner(let, boardcopy):
        #                 return move
        # corner = []
        # for i in possiblemove:
        #     if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
        #         corner.append(i)
        # if len(corner) > 0:
        #     move = random.randint(0, len(corner) - 1)
        #     return corner[move]
        # edge = []
        # for i in possiblemove:
        #     if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
        #         edge.append(i)
        # if len(edge) > 0:
        #     move = random.randint(0, len(edge) - 1)
        #     return edge[move]

    # Configure text on button while playing with system
    def get_text_pc(self, i, j, gb, p1, p2):
        global turn
        global sign
        board = self.ticTocBoard.board
        if board[i][j] == ' ':
            if sign % 2 == 0:
                p1.config(state=DISABLED)
                p2.config(state=ACTIVE)
                board[i][j] = "X"

            else:
                button[i][j].config(state=ACTIVE)
                p2.config(state=DISABLED)
                p1.config(state=ACTIVE)
                board[i][j] = "O"
                print(self.ticTocBoard)
            sign += 1
            button[i][j].config(text=board[i][j])

            can_play = self.check_win(gb)

            if can_play and sign % 2 != 0:
                move = self.pc()
                print(move)
                button[move[0]][move[1]].config(state=DISABLED)
                self.get_text_pc(move[0], move[1], gb, p1, p2)

    # Create the GUI of game board for play along with system / anotherplayer
    def gameboard(self, game_board, secondPlayer, p1, p2):
        global button
        button = []
        size = self.size
        for i in range(size):
            m = 3 + i
            button.append(i)
            button[i] = []
            for j in range(size):
                n = j
                button[i].append(j)
                if secondPlayer == "Computer":
                    get_t = partial(self.get_text_pc, i, j, game_board, p1, p2)
                else:
                    get_t = partial(self.get_text, i, j, game_board, p1, p2)
                button[i][j] = Button(
                    game_board, bd=5, command=get_t, height=4, width=8)
                button[i][j].grid(row=m, column=n)
        # game_board.geometry("+550+100")
        game_board.eval('tk::PlaceWindow . center ')
        game_board.mainloop()

    # Initialize the game board to play with system / another player
    def initialize(self, game_board, secondPlayer):
        game_board.destroy()
        game_board = Tk()
        # game_board.eval('tk::PlaceWindow . center')

        game_board.title("Tic Tac Toe")
        p1 = Button(game_board, text="Player : X", width=10)
        p1.grid(row=1, column=2)
        p2 = Button(game_board, text=f"{secondPlayer} : O", width=10, state=DISABLED)
        p2.grid(row=2, column=2)
        self.gameboard(game_board, secondPlayer, p1, p2)

    def make_button(self, tk, text, command) -> Button:
        color_bg, color_fg, size, font = "cornflowerblue", "navy", 12, 'helvetica'  # summer font '#fe3e77', 'white'

        button = Button(tk, text=text, command=command,
                        activeforeground=color_fg,
                        activebackground=color_bg, bg=color_bg,
                        fg=color_fg, width=15, font=(font, size, 'bold'), bd=5)
        return button

    # main function
    def play(self):
        menu = Tk()
        # menu.eval('tk::PlaceWindow . center ')
        menu.geometry("300x300+500+100")
        menu.config(bg="snow")
        menu.title("Tic Tac Toe")

        wpc = partial(self.initialize, menu, "Compter")
        wpl = partial(self.initialize, menu, "Player 2")

        head = Label(menu, text="Welcome to tic-tac-toe", bg="snow", fg="black", font='Times 15', height=5)
        B1 = self.make_button(menu, "Single Player", lambda: self.initialize(menu, "Computer"))
        B2 = self.make_button(menu, "Multi Player", wpl)
        B3 = self.make_button(menu, "Exit", menu.quit)

        head.pack(side='top')
        B1.pack(side='top')
        B2.pack(side='top', pady=5)
        B3.pack(side='top')
        # self.center(menu)
        menu.mainloop()

    def center(self, root):
        """
        centers a tkinter window
        :param root: the main window or Toplevel window to center
        """
        root.update_idletasks()
        width = root.winfo_width()
        frm_width = root.winfo_rootx() - root.winfo_x()
        win_width = width + 2 * frm_width
        height = root.winfo_height()
        titlebar_height = root.winfo_rooty() - root.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = root.winfo_screenwidth() // 2 - win_width // 2
        y = root.winfo_screenheight() // 2 - win_height // 2
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        root.deiconify()


# Call main function
if __name__ == '__main__':
    game = boardGui(5)
    game.play()
