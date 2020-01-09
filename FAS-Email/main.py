"""Script that returns the email from a username associated with an FAS account"""
import sys
from getpass import getpass

from fedora.client import AuthError
from fedora.client.fas2 import AccountSystem

username = input("Enter your username: ")
password = getpass("Enter your password: ")

try:
    FAS = AccountSystem(username=username, password=password)

    username_query = input("Enter username to query: ")

    response = FAS.person_by_username(username=username_query)

    print(f"\nEmail found: {response['email']}")

except AuthError:
    # handles the user entering their username and password wrong
    print("\nYou entered your details wrong.")
    sys.exit(1)

except KeyError:
    # handles the user entering a non-existent username.
    print("\nUsername not found. Please enter a valid username.")
