"""Scales images so that they have a width of 300px"""
import os
import sys

from PIL import Image


def check_arg():
    """Checks if one argument is provided - the file name"""
    if len(sys.argv) != 2:
        print("The program takes one argument (the file to be scaled)")
        sys.exit(1)

    file_name = sys.argv[1]
    if not os.path.isfile(f"./{file_name}"):
        print("File does not exist. Make sure it is in the current directory")
        sys.exit(1)


def get_image():
    """returns the image from the filename provided"""
    try:
        file_name = sys.argv[1]
        image = Image.open(file_name)
    except IOError:
        print("Unsupported file type")
        sys.exit(1)

    return image


def get_ratio(old_image):
    """returns the aspect ratio of the original image"""
    width = float(old_image.size[0])
    height = float(old_image.size[1])
    ratio = height / width

    return ratio


def save_file(new_image):
    """saves new image"""
    old_file_name = sys.argv[1]

    name, extension = old_file_name.split(".")
    new_file_name = f"{name}_copy.{extension}"

    new_image.save(new_file_name)
    print("Successfully resized.")


def resize():
    """resizes the image"""
    old_image = get_image()

    ratio = get_ratio(old_image)

    new_width = 300
    new_height = int(new_width * ratio)

    new_size = (new_width, new_height)
    new_image = old_image.resize(new_size, Image.ANTIALIAS)

    save_file(new_image)


if __name__ == "__main__":
    check_arg()
    resize()
