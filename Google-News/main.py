"""
Google News API implementation using tkinter
"""
import tkinter
import webbrowser
from io import BytesIO

import requests
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("Google News API")

URL = (
    "https://newsapi.org/v2/everything?"
    "q=Android AND Linux AND Open-Source&"
    "sortBy=publishedAt&"
    "language=en&"
    "apiKey=303810ce6731494180f232b883dac6d2"
)

response = requests.get(URL)

articles = response.json()["articles"]
images = []

title_label = tkinter.Label(text="GOOGLE NEWS API", font=("Verdana", 20, "bold"))
title_label.grid(row=0, columnspan=6)

subtitle_label = tkinter.Label(
    text="Showing the latest results related to 'Android', 'Linux' and 'Open-Source'.",
    font=("ms sans serif", 14),
)
subtitle_label.grid(row=1, columnspan=6)


def open_article(url):
    """Opens the article in the default browser"""
    webbrowser.open(url, new=0, autoraise=True)


for i in range(6):
    article_frame = tkinter.Frame(relief="ridge", padx=5, pady=10, bd=2)
    article_frame.grid(row=(2 * i) % 6 + 2, column=0 if i < 3 else 1, padx=10, pady=10)
    article = articles[i]

    IMG_SIZE = (150, 150)

    img_url = article["urlToImage"]

    if img_url:
        img = Image.open(BytesIO(requests.get(img_url).content))
        img.thumbnail(IMG_SIZE)
    else:
        img = Image.new("RGB", IMG_SIZE, color="white")

    img_tk = ImageTk.PhotoImage(img)

    # the images are stored in a list as tkinter does not display them if not
    images.append(img_tk)

    WIDTH = 450

    # create image for article
    img_canvas = tkinter.Canvas(article_frame, width=IMG_SIZE[0], height=IMG_SIZE[1])
    img_canvas.grid(rowspan=4)
    img_canvas.create_image(0, 0, anchor="nw", image=img_tk)

    article_title = tkinter.Label(
        article_frame,
        text=article["title"],
        font=("Helvetica", 12, "bold"),
        wraplength=WIDTH,
        justify="left",
    )
    article_title.grid(row=0, column=1)

    date_time = article["publishedAt"]
    date_time = date_time.replace("T", " at ").replace("Z", "")

    date_time_label = tkinter.Label(
        article_frame,
        text="from " + article["source"]["name"] + " on " + date_time,
        font=("Helvetica", 10),
        wraplength=WIDTH,
        justify="left",
    )
    date_time_label.grid(row=1, column=1)

    article_description = tkinter.Label(
        article_frame,
        text=article["description"],
        font=("Helvetica", 10),
        wraplength=WIDTH,
        justify="left",
    )
    article_description.grid(row=2, column=1)

    read_article_button = tkinter.Button(
        article_frame,
        text="Read full article",
        command=lambda i=i: open_article(articles[i]["url"]),
    )
    read_article_button.grid(row=3, column=1)

root.mainloop()
