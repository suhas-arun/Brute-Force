"""Encodes and decodes text in an image"""
import sys
import os
from PIL import Image


def show_commands(commands):
    """prints the usable commands"""

    print("The following commands can be used:")
    for command, description in commands.items():
        print(f"\t{command}: {description}")


def validate_args():
    """checks if the arguments are valid"""

    commands = {
        "-e": "encode text in an image",
        "-d": "decode text in an image",
        "-h": "show this help message"
    }

    if len(sys.argv) == 1:  # no arguments are passed
        show_commands(commands)
        sys.exit(1)

    if len(sys.argv) == 2:
        command = sys.argv[1]
        if command not in commands:
            print(f"{command} is not a valid command.\n")
            show_commands(commands)
            sys.exit(1)
        if command in ["-e", "-d"]:
            print(
                "-e and -d take an additional parameter (the png file to encode/decode)")
            sys.exit(1)
        else:
            show_commands(commands)
            sys.exit(1)

    if len(sys.argv) > 3:  # too many arguments are passed
        show_commands(commands)
        sys.exit(1)

    file_name = sys.argv[2]

    if not os.path.isfile(f"./{file_name}"):  # if file does not exist
        print("Please make sure you choose a file that exists in the current directory")
        sys.exit(1)

    if file_name[-3:] != "png":  # if file extension is not .png
        print("File format unsupported. Please choose a .png file")
        sys.exit(1)


def make_msg_binary(msg):
    """converts the message to be encoded into 8 bit binary codes
    so it can be added to the pixels"""

    binary_msg = []
    for char in msg:
        binary_msg.append(format(ord(char), '08b'))

    return binary_msg


def modify_pixels(pixels, msg):
    """
    modifies the pixels in the image based on the message to be encoded.
    The pixels are read in groups of 3 and the last value of the 3rd pixel
    is used to encode the message. This value is either odd (to store a 1) or
    even (to store a 0)
    """

    data = make_msg_binary(msg)
    imdata = iter(pixels)

    for i, msg_data in enumerate(data):
        pixels = []
        for pixel in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]:
            pixels.append(pixel)

        for j in range(8):
            if msg_data[j] == "0" and pixels[j] % 2 != 0:
                pixels[j] -= 1

            elif msg_data[j] == "1" and pixels[j] % 2 == 0:
                pixels[j] -= 1

        if i == len(data) - 1:
            if pixels[-1] % 2 == 0:
                pixels[-1] -= 1
        else:
            if pixels[-1] % 2 != 0:
                pixels[-1] -= 1

        yield pixels[:3]
        yield pixels[3:6]
        yield pixels[6:9]


def modify_image(image, msg):
    """modifies the image by placing the modified pixels in the image"""

    width = image.size[0]
    (x_pos, y_pos) = (0, 0)

    for pixel in modify_pixels(image.getdata(), msg):
        pixel = tuple(pixel)
        image.putpixel((x_pos, y_pos), pixel)
        if x_pos == width - 1:
            x_pos = 0
            y_pos += 1
        else:
            x_pos += 1


def encode(file_name):
    """encodes text in the image file"""

    image = Image.open(file_name, 'r')
    msg = input("Enter message to hide: ")
    while not msg:
        msg = input("Message can't be empty: ")

    new_image = image.copy()
    modify_image(new_image, msg)

    name, extension = file_name.split(".")
    new_file_name = name + "_copy." + extension
    new_image.save(new_file_name, extension.upper())
    print("Success!")
    print(f"New file saved as {new_file_name}")


def decode(file_name):
    """decodes text from the image file"""

    image = Image.open(file_name, 'r')
    msg = ''
    imdata = iter(image.getdata())

    while True:
        pixels = []
        for pixel in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]:
            pixels.append(pixel)

        char_binary = ''

        for i in pixels[:8]:
            if i % 2 == 0:
                char_binary += '0'
            else:
                char_binary += '1'

        msg += chr(int(char_binary, 2))

        if pixels[-1] % 2 == 1:
            print(msg)
            return


def main():
    """main function"""
    validate_args()
    command = sys.argv[1]
    if command == "-e":
        file_name = sys.argv[2]
        encode(file_name)
    elif command == "-d":
        file_name = sys.argv[2]
        decode(file_name)


if __name__ == "__main__":
    main()
