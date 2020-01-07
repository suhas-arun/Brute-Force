# 20 Queens (For Google Code-In)

Recursive algorithm that solves the 20 queens problem in Python.

I used a `numpy` array to represent the board, which is initialised with 0s. Queens are represented as 1s in this array.

The recursive function `solve` places a queen on the first square in the current row that is available (which is checked using the function `check_square`) and then calls itself for the next row in the board. The base case of the function is when all the rows have been filled and all the queens have been placed.

In the first row, the position of the queen is randomly generated so that a different board is produced each time the program is run. Note, this randomness sometimes leads to a great difference in time taken to generate the board.

I used the `PIL` library to create an image of the board with the queens on it. [board.png](./board.png) is just one example of an image of the board but if the program is run again then the file will be updated with the image of a new board that is (almost definitely) different.