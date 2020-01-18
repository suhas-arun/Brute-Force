"""Reverse WHOIS lookup"""
import requests
from bs4 import BeautifulSoup

name = input("Enter registrant name: ")

response = requests.get(
    f"https://viewdns.info/reversewhois/?q={name}",
    headers={"User-Agent": "Mozilla/5.0"},
)
soup = BeautifulSoup(response.content, "lxml")
rows = soup.find_all("table")[3].find_all("tr")
for row in rows:
    cells = row.find_all("td")
    if len(cells) == 3:
        print(cells[0].text)
    else:
        print("Please enter a valid registrant name.")
        break
