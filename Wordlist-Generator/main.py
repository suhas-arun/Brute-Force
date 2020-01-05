"""Password generator from keywords entered by user"""
from itertools import permutations


def get_keywords():
    """Returns a list of keywords that are used for generating words"""
    keywords = []

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    birth_day = input("Enter birth day (DD): ")
    birth_month = input("Enter birth month (MM): ")
    birth_year = input("Enter birth year (YYYY): ")

    keywords.append(first_name.lower())
    keywords.append(last_name.lower())
    keywords.append(birth_year)
    keywords.append(birth_month)
    keywords.append(birth_day)

    if birth_month.isdigit():
        month = get_month(birth_month)

        keywords.append(month)

        # E.g. jan, feb
        keywords.append(month[:3])

    # 2003 -> 03
    keywords.append(birth_year[-2:])

    extra = input("Enter extra keywords, space separated: ").split()
    for i, word in enumerate(extra):
        extra[i] = word.lower()

    keywords += extra

    return keywords


def get_month(month_no):
    """Returns month name from month number"""

    months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december"
    ]

    month = months[int(month_no) - 1]

    return month


def leet(keywords):
    """Adds the 1337 versions of the keywords to the keywords list"""
    leet_words = []
    for word in keywords:
        leet_word = (
            word.replace("a", "4")
            .replace("i", "1")
            .replace("o", "0")
            .replace("e", "3")
            .replace("t", "7")
        )
        if leet_word != word:
            leet_words.append(leet_word)
    keywords += leet_words
    return keywords


def create_wordlist(keywords):
    """Creates words and writes them to the file"""
    with open("output.txt", "w") as wordlist:
        for pair in permutations(keywords, 2):
            word = "".join(pair)

            wordlist.write(word + "\n")
            print(word)

            wordlist.write(word.title() + "\n")
            print(word.title())

            wordlist.write(word.upper() + "\n")
            print(word.upper())


if __name__ == "__main__":
    words = leet(get_keywords())

    create_wordlist(words)

    print("\n\nWordlist saved in output.txt")
