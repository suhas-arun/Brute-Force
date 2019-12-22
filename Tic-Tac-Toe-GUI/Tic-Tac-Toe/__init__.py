"""
Tic-Tac-Toe (aka Noughts and Crosses) clone made in Python with tkinter
"""
import tkinter
import tkinter.messagebox

class Board:
    """The board is made up of a grid of tkinter Button objects"""
    def __init__(self):
        self.button1 = tkinter.Button(text="", bg="#fff", width=8, height=4, font=("Helvetica", 14))
        self.button2 = tkinter.Button(text="", bg="#fff", width=8, height=4, font=("Helvetica", 14))
        self.button3 = tkinter.Button(text="", bg="#fff", width=8, height=4, font=("Helvetica", 14))
        self.button4 = tkinter.Button(text="", bg="#fff", width=8, height=4, font=("Helvetica", 14))
        self.button5 = tkinter.Button(text="", bg="#fff", width=8, height=4, font=("Helvetica", 14))
        self.button6 = tkinter.Button(text="", bg="#fff", width=8, height=4, font=("Helvetica", 14))
        self.button7 = tkinter.Button(text="", bg="#fff", width=8, height=4, font=("Helvetica", 14))
        self.button8 = tkinter.Button(text="", bg="#fff", width=8, height=4, font=("Helvetica", 14))
        self.button9 = tkinter.Button(text="", bg="#fff", width=8, height=4, font=("Helvetica", 14))

    def display_board(self):
        """Displays the buttons in a grid"""
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)
        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)
        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)



class Game:
    """Controls the game mechanisms"""
    def __init__(self, parent):
        self.current_player = "X"
        self.board = None
        self.parent = parent

    def initialise_game(self):
        """Sets up the board to start the game"""
        self.board = Board()
        self.board.display_board()
        self.bind_buttons()

    def bind_buttons(self):
        """Allows the buttons to be pressed so that they are updated"""
        self.board.button1.config(command=lambda: self.update_square(self.board.button1))
        self.board.button2.config(command=lambda: self.update_square(self.board.button2))
        self.board.button3.config(command=lambda: self.update_square(self.board.button3))
        self.board.button4.config(command=lambda: self.update_square(self.board.button4))
        self.board.button5.config(command=lambda: self.update_square(self.board.button5))
        self.board.button6.config(command=lambda: self.update_square(self.board.button6))
        self.board.button7.config(command=lambda: self.update_square(self.board.button7))
        self.board.button8.config(command=lambda: self.update_square(self.board.button8))
        self.board.button9.config(command=lambda: self.update_square(self.board.button9))


    def update_square(self, square):
        """Updates the text on a button"""
        square.config(text=self.current_player, state="disabled")

        result = self.check_result()

        if result != "game":
            self.show_result(result)
        else:
            self.switch_player()


    def switch_player(self):
        """Switches the player after each turn"""
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def get_board_list(self):
        """Returns a 2d list of the board to help check the result"""
        board = []
        board.append([self.board.button1['text'], self.board.button2['text'], self.board.button3['text']])
        board.append([self.board.button4['text'], self.board.button5['text'], self.board.button6['text']])
        board.append([self.board.button7['text'], self.board.button8['text'], self.board.button9['text']])
        return board

    def check_board_full(self):
        """checks if the board is full (i.e. if there is a draw)"""
        board = self.get_board_list()
        for row in board:
            if '' in row:
                return False

        return True

    def check_result(self):
        """
        checks the result of the game after each turn.
        - "win" means that someone has three in a row,
        - "draw" means that the board is full and no one has three in a row
        - "game" means that the game is still in progress

        the last condition in each if statement (e.g. board[i][0]) checks if the
        square is not empty
        """

        board = self.get_board_list()
        result = "game"

        for i in range(len(board)):
            if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0]: # rows
                result = "win"
                return result
            if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i]: # columns
                result = "win"
                return result

        if board[0][0] == board[1][1] == board[2][2] and board[0][0]: # top-left -> bottom-right
            result = "win"
            return result
        if board[0][2] == board[1][1] == board[2][0] and board[0][2]: #top-right -> bottom-left
            result = "win"
            return result

        if self.check_board_full():
            result = "draw"
            return result

        return result

    def show_result(self, result):
        """A message box shows the result of the game and another asks if they want to restart"""

        if result == "win":
            winner = self.current_player
            tkinter.messagebox.showinfo("Game Over!", f"'{winner}' wins! Well done!")
        else:
            tkinter.messagebox.showinfo("Game Over!", "Draw!")

        if tkinter.messagebox.askyesno("Game Over!", "Would you like to play again?"):
            self.current_player = "X"
            self.initialise_game()
        else:
            self.end_game()

    def end_game(self):
        """ends the game by destroying the tkinter window"""
        self.parent.destroy()

if __name__ == "__main__":
    root = tkinter.Tk()

    game = Game(root)
    game.initialise_game()

    root.mainloop()
