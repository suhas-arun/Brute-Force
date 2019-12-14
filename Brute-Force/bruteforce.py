import zipfile


def extract_file(zip_file, password):
    """Function for extracting zip files to test if the password works"""
    try:
        zip_file.extractall(pwd=password)
        return True
    except:
        pass 


# creates a list storing all the possible passwords
words: list = []
with open("words.txt", 'r') as f:
    for word in f:
        words.append(word.rstrip("\n"))

ZIP_FILE = zipfile.ZipFile('test.zip')

for word in words:
    print("Trying \"{}\"".format(word))
    # If the file was extracted, you found the right password.
    if extract_file(ZIP_FILE, str.encode(word)):
        print('\n\nSuccess!')
        print('Password found: {}'.format(word))
        exit(0)

print("Password not found.")
