# Hide text inside an image using Steganography (for Google Code-In)

The program takes the following arguments:

    -e <filename>: encode text in an image
	-d <filename>: decode text in an image
	-h: show this help message


The program converts the message into binary and modifies the pixels in the image to store this message.

The pixels in the image are read in groups of 3 and the last value of the 3rd pixel is used to encode the message. This value is made odd to store a one or even to store a 0.

These modified pixels are then placed in a new image file which is stored separately.

[![asciicast](https://asciinema.org/a/288744.svg)](https://asciinema.org/a/288744)