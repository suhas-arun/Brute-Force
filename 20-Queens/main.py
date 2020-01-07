"""Recursive algorithm that solves the 20 queens problem"""
import random
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def check_square(board, x_pos, y_pos):
    """
    Checks if a queen can be placed on the square
    (i.e. has another queen already been placed on the same
    column/row/diagonal). Queens are represented as 1s.
    """

    # checks for queens on column
    if 1 in [row[x_pos] for row in board]:
        return False

    # checks for queens on row
    if 1 in board[y_pos]:
        return False

    # checks left to right diagonal
    if 1 in np.diagonal(board, offset=x_pos - y_pos):
        return False

    # checks right to left diagonal
    # this is done by first flipping the array from left to right and then
    # doing the same as above but with a different offset
    flipped = np.fliplr(board)
    if 1 in np.diagonal(flipped, offset=abs(len(board) - x_pos - 1) - y_pos):
        return False

    return True


def solve(board, y_pos=0):
    """
    Recursive function to solve the 20 queens problem.
    When a queen is placed in the first row, it is done so at a
    random position in that row, so that a different board is produced
    each time the program is run
    """

    size = len(board)
    for x_pos in range(0, size):
        if y_pos == 0:
            x_pos = random.randint(0, size)
        if check_square(board, x_pos, y_pos):
            board[y_pos][x_pos] = 1
            if y_pos == size - 1:
                show_board(board)
            else:
                solve(board, y_pos + 1)
                board[y_pos][x_pos] = 0


def show_board(board):
    """Show the board as an image and save it to ./board.png"""

    # Create new black image of entire board
    width, height = 400, 400

    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    tile_size = 20
    # Draw squares on odd rows
    for x_pos in range(0, width, 2 * tile_size):
        for y_pos in range(0, height, 2 * tile_size):
            draw.rectangle(
                [(x_pos, y_pos), (x_pos + tile_size - 1, y_pos + tile_size - 1)],
                fill="white",
            )

    # Draw squares on even rows
    for x_pos in range(tile_size, width, 2 * tile_size):
        for y_pos in range(tile_size, height, 2 * tile_size):
            draw.rectangle(
                [(x_pos, y_pos), (x_pos + tile_size - 1, y_pos + tile_size - 1)],
                fill="white",
            )

    # Add queens to board
    font = ImageFont.truetype("./arialbd.ttf", 18)
    for x_pos, row in enumerate(board):
        for y_pos, square in enumerate(row):
            if square == 1:
                draw.text(
                    (x_pos * tile_size + 3, y_pos * tile_size),
                    "Q",
                    font=font,
                    fill="red",
                )

    img.save("./board.png")
    img.show()
    sys.exit(0)


def main():
    """main function"""
    size = 20
    board = np.zeros((size, size), dtype=int)
    solve(board)


if __name__ == "__main__":
    main()
