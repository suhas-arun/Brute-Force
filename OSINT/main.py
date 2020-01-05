"""
Script that checks if a username is registered on Github, Instagram and Twitter
"""
import requests

WEBSITES = {
    "Instagram": "https://www.instagram.com/",
    "Github": "https://www.github.com/",
    "Twitter": "https://twitter.com/",
}

username = input("Enter username: ")
found = False
for name, url in WEBSITES.items():
    response = requests.get(url + username)
    if response.status_code == 200:
        print(f"'{username}' is on {name}")
        found = True
    else:
        print(f"'{username}' is not on {name}")

if not found:
    print(f"'{username}' is not on Instagram, Github or Twitter ")
