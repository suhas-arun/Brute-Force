"""2048 clone using tkinter"""
import tkinter
import tkinter.messagebox
import random


class Square:
    """represents one square on the board"""

    def __init__(self):
        self.value = ""
        self.position = None

    def get_colour(self):
        """returns the colour corresponding to the square's value"""
        colours = {
            "": "#d9d9d9",  # the default window colour
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f65e3b",
            128: "#edcf72",
            256: "#edcc61",
            512: "#edc850",
            1024: "#edc53f",
            2048: "#edc22e",
        }
        return colours[self.value]

    def __repr__(self):
        return str(self.value)


class Board:
    """represents the board (which is composed of square objects)"""

    def __init__(self):
        self.board = []
        self.parent = root

    def initialise_board(self):
        """creates a 2d array of square objects (composition) to represent the board"""

        for _ in range(4):
            row = [Square(), Square(), Square(), Square()]
            self.board.append(row)

    def display_board(self):
        """displays the value of each square object as a tkinter label in a grid"""
        for i in range(4):
            for j in range(4):
                square = self.board[i][j]
                tkinter.Label(
                    text=square,
                    font=("Helvetica", 16),
                    relief="ridge",
                    bd=2,
                    bg=square.get_colour(),
                    height=4,
                    width=8,
                ).grid(row=i, column=j)

    def spawn_square(self):
        """randomly spawns a square (with value 2 or 4) in a place that has not been taken"""
        row = random.randint(0, 3)
        column = random.randint(0, 3)
        while self.board[row][column].value != "":
            row = random.randint(0, 3)
            column = random.randint(0, 3)

        if random.randint(1, 10) < 9:  # there is a 10% chance of a 4 spawning
            self.board[row][column].value = 2
        else:
            self.board[row][column].value = 4
        self.display_board()


class Game:
    """controls the game"""

    def __init__(self, parent):
        self.parent = parent
        self.board = Board()

    def initialise_game(self):
        """
        initialises the game by creating and displaying the board, binding the arrow keys
        to the game and spawning two squares on the board to start
        """

        self.board.initialise_board()
        self.board.display_board()

        self.parent.bind("<Left>", self.key_pressed)
        self.parent.bind("<Right>", self.key_pressed)
        self.parent.bind("<Up>", self.key_pressed)
        self.parent.bind("<Down>", self.key_pressed)
        root.bind("<Escape>", self.key_pressed)

        # at the start of the game there are 2 squares on the board
        for _ in range(2):
            self.board.spawn_square()

    def key_pressed(self, event):
        """handles key presses: Escape quits the game, arrow keys move the squares"""
        if event.keysym == "Escape":
            self.parent.quit()
        else:
            self.move(event.keysym)

    def move(self, direction):
        """
        moves the squares on the board after a keypress.
        I had to have different logic for each square depending on what row and column
        it is in and by checking the adjacent squares individually (using nested if statements)
        I originally used a while loop to implement the movement in a better way but the tkinter
        mainloop interfered with the while loop so it was a bit messed up.
        """

        if direction == "Left":
            self.move_left()

        elif direction == "Right":
            self.move_right()

        elif direction == "Up":
            self.move_up()

        else:
            self.move_down()


        self.board.spawn_square()
        self.board.display_board()

        if self.check_end_game():
            self.end_game()


    def move_left(self):
        """
        this checks the second, third and fourth squares in each row. For each square it checks if
        the square to its left is empty and if so it moves the square to the left. If the square is
        not empty, it calls the try_merge method to check if the two squares can be merged.
        """
        for row in self.board.board:
            for i, square in enumerate(row):
                if square.value != "":  # if the square is empty it need not be moved
                    if i == 1:  # if the square is in the second column
                        if row[i - 1].value == "":
                            row[i - 1].value, square.value = square.value, ""
                        else:
                            self.try_merge(square, row[i - 1])

                    if i == 2:  # if the square is in the third column
                        if row[i - 1].value == "":
                            row[i - 1].value, square.value = square.value, ""

                            if row[i - 2].value == "":
                                row[i - 2].value, row[i - 1].value = row[i - 1].value, ""
                            else:
                                self.try_merge(row[i - 1], row[i - 2])
                        else:
                            self.try_merge(square, row[i - 1])

                    if i == 3:
                        if row[i - 1].value == "":
                            row[i - 1].value, square.value = square.value, ""

                            if row[i - 2].value == "":
                                row[i - 2].value, row[i - 1].value = row[i - 1].value, ""

                                if row[i - 3].value == "":
                                    row[i - 3].value, row[i - 2].value = row[i - 2].value, ""
                                else:
                                    self.try_merge(row[i - 2], row[i - 3])

                            else:
                                self.try_merge(row[i - 1], row[i - 2])

                        else:
                            self.try_merge(square, row[i - 1])

    def move_right(self):
        """
        checks the first 3 squares of each row and checks the square to the right of
        each one to see if it is free or if the two squares can be merged
        """
        for row in self.board.board:
            for i in range(len(row) - 1, -1, -1):
                square = row[i]
                if square.value != "": # if the square is empty it need not be moved

                    if i == 2:  # if the square is in the third column
                        if row[i + 1].value == "":
                            row[i + 1].value, square.value = square.value, ""
                        else:
                            self.try_merge(square, row[i + 1])

                    if i == 1:  # if the square is in the second column
                        if row[i + 1].value == "":
                            row[i + 1].value, square.value = square.value, ""

                            if row[i + 2].value == "":
                                row[i + 2].value, row[i + 1].value = row[i + 1].value, ""
                            else:
                                self.try_merge(row[i + 1], row[i + 2])
                        else:
                            self.try_merge(square, row[i + 1])

                    if i == 0:  # if the square is in the first column
                        if row[i + 1].value == "":
                            row[i + 1].value, square.value = square.value, ""

                            if row[i + 2].value == "":
                                row[i + 2].value, row[i + 1].value = row[i + 1].value, ""

                                if row[i + 3].value == "":
                                    row[i + 3].value, row[i + 2].value = row[i + 2].value, ""
                                else:
                                    self.try_merge(row[i + 2], row[i + 3])

                            else:
                                self.try_merge(row[i + 1], row[i + 2])

                        else:
                            self.try_merge(square, row[i + 1])

    def move_up(self):
        """
        checks the last three squares in each column and the squares above
        each one to see if it is free or has the same value as the current square
        """

        board = self.board.board

        for row in range(4):
            for column in range(4):
                square = board[row][column]
                if square.value != "":
                    if row == 1:
                        if board[row - 1][column].value == "":
                            board[row - 1][column].value, square.value = square.value, ""
                        else:
                            self.try_merge(square, board[row - 1][column])

                    if row == 2:
                        if board[row - 1][column].value == "":
                            board[row - 1][column].value, square.value = square.value, ""

                            if board[row - 2][column].value == "":
                                board[row - 2][column].value, board[row - 1][column].value = board[row - 1][column].value, ""

                            else:
                                self.try_merge(board[row - 1][column], board[row - 2][column])

                        else:
                            self.try_merge(square, board[row - 1][column])

                    if row == 3:
                        if board[row - 1][column].value == "":
                            board[row - 1][column].value, square.value = square.value, ""

                            if board[row - 2][column].value == "":
                                board[row - 2][column].value, board[row - 1][column].value = board[row - 1][column].value, ""

                                if board[row - 3][column].value == "":
                                    board[row - 3][column].value, board[row - 2][column].value = board[row - 2][column].value, ""

                                else:
                                    self.try_merge(board[row - 2][column], board[row - 3][column])

                            else:
                                self.try_merge(board[row - 1][column], board[row - 2][column])

                        else:
                            self.try_merge(square, board[row - 1][column])

    def move_down(self):
        """
        checks the first three squares in each column and the squares below
        each one to see if it is free or has the same value as the current square
        """
        board = self.board.board

        for row in range(3, -1, -1):
            for column in range(4):
                square = board[row][column]
                if square.value != "":
                    if row == 2:
                        if board[row + 1][column].value == "":
                            board[row + 1][column].value, square.value = square.value, ""

                        else:
                            self.try_merge(square, board[row + 1][column])

                    if row == 1:
                        if board[row + 1][column].value == "":
                            board[row + 1][column].value, square.value = square.value, ""

                            if board[row + 2][column].value == "":
                                board[row + 2][column].value, board[row + 1][column].value = board[row + 1][column].value, ""

                            else:
                                self.try_merge(board[row + 1][column], board[row + 2][column])

                        else:
                            self.try_merge(square, board[row + 1][column])

                    if row == 0:
                        if board[row + 1][column].value == "":
                            board[row + 1][column].value, square.value = square.value, ""

                            if board[row + 2][column].value == "":
                                board[row + 2][column].value, board[row + 1][column].value = board[row + 1][column].value, ""

                                if board[row + 3][column].value == "":
                                    board[row + 3][column].value, board[row + 2][column].value = board[row + 2][column].value, ""

                                else:
                                    self.try_merge(board[row + 2][column], board[row + 3][column])

                            else:
                                self.try_merge(board[row + 1][column], board[row + 2][column])

                        else:
                            self.try_merge(square, board[row + 1][column])

    def try_merge(self, old_square, new_square):
        """checks if two squares can be merged (if they have the same value) and merges them
        if possible"""

        if old_square.value == new_square.value:
            new_square.value *= 2
            old_square.value = ""

    def check_end_game(self):
        """
        checks if the board is full by iterating through each square object in the board
        and checking if the square's value is not an empty string
        """
        for row in self.board.board:
            for square in row:
                if square.value == "":
                    return False
        return True


    def end_game(self):
        """ends the game if the board is full"""
        tkinter.messagebox.showinfo("Game Over!", "You lost!")
        if tkinter.messagebox.askyesno("Game Over!", "Would you like to restart the game?"):
            self.board.board = []
            self.initialise_game()
        else:
            self.parent.destroy()


if __name__ == "__main__":
    root = tkinter.Tk()

    game = Game(root)
    game.initialise_game()

    root.mainloop()
