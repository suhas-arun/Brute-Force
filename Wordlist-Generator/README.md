# Custom Word List Generator (For Google Code-In)

The program takes input from the user of first name, last name, birth day, month and year, and any additional keywords the user wants. The month name is also found from the month number and added to the keywords.

These words are then converted to 1337 mode and appended to the list of keywords.

Each pair of words is then iterated over using `itertools.permutations` and is written to the file [output.txt](./output.txt) in lower case, upper case and capitalised.

Below is a recording of the program running.

[![asciicast](https://asciinema.org/a/291885.svg)](https://asciinema.org/a/291885)