"""
Scales images using PIL so that the longest dimension is 400 and adjusts the
quality so that the file size is less than 64KB.
"""
import os
import sys

from PIL import Image


def get_directory():
    """gets user input for the directory containing the image files to be scaled"""
    directory = input("Enter the directory with the images: ")
    if not os.path.exists(directory):
        print("Directory not found")
        sys.exit(1)

    return directory


def get_image(directory, file_name):
    """returns the image from the file name"""
    try:
        path = f"{directory}/{file_name}"
        image = Image.open(path)
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


def resize(image):
    """resizes each image"""
    ratio = get_ratio(image)

    old_width, old_height = image.size

    if old_width > old_height:
        new_width = 400
        new_height = int(new_width * ratio)
    else:
        new_height = 400
        new_width = int(new_height / ratio)

    new_size = (new_width, new_height)
    new_image = image.resize(new_size, Image.ANTIALIAS)

    return new_image


def save_file(directory, file_name, new_image):
    """Converts to jpg and saves the new image"""

    name = file_name.split(".")[0]
    new_file_name = f"{name}_new.jpg"

    path = f"{directory}/new-images/{new_file_name}"

    new_image = new_image.convert("RGB")

    new_image.save(path)
    file_size = os.stat(path).st_size / 1024

    # if the image size > 64KB, decrease the quality until it isn't
    # in PIL, the default JPEG quality is 75
    quality = 75
    while file_size > 64:
        quality -= 1
        new_image.save(path, quality=quality)
        file_size = os.stat(path).st_size / 1024

    print(
        f"""Successfully resized.\n
    Path: new_images/{new_file_name}\n\
    Dimensions: {new_image.size}\n\
    Size: {round(file_size, 2)}KB\n\
    Quality: {quality}\n"""
    )


if __name__ == "__main__":
    directory = get_directory()

    new_dir = f"{directory}/new-images"
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)

    for file_name in os.listdir(directory):
        if os.path.isfile(f"{directory}/{file_name}"):
            image = get_image(directory, file_name)
            new_image = resize(image)
            save_file(directory, file_name, new_image)
