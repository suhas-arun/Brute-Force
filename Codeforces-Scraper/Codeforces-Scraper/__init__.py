"""
Uses Codeforces API to scrape user info.
"""
import tkinter
import urllib.request
import json

root = tkinter.Tk()

def get_info():
    """returns the info for a user handle using the api"""
    username = entry_box.get()
    try:
        response = urllib.request.urlopen("https://codeforces.com/api/user.info?handles="+username)
        data = json.load(response)
        status = data['status']
        info = data['result'][0]

    except urllib.error.HTTPError:
        status = "FAILED"
        info = None

    return (status, info)


def display_info():
    """displays the user info"""

    status, info = get_info()

    if status == "OK":
        try:
            handle = info['handle']
            rating = info['rating']
            rank = info['rank']
            max_rating = info['maxRating']
            max_rank = info['maxRank']

            label_text = f"Handle: {handle}\nRating: {rating}\nRank: {rank}\nMax Rating: {max_rating}\nMax Rank: {max_rank}"

        except KeyError:
            label_text = "Error"


    else:
        label_text = "Error"

    info_label.config(text=label_text)

username_label = tkinter.Label(text="Enter handle:", padx=5, pady=5, font=("Helvetica", 14))
entry_box = tkinter.Entry(font=("Helvetica", 14))
search_button = tkinter.Button(text="Search", font=("Helvetica", 14), command=display_info)
info_label = tkinter.Label(pady=10, font=("Helvetica", 14))


username_label.grid(row=0, column=0)
entry_box.grid(row=0, column=1, columnspan=2)
search_button.grid(row=1, column=1)
info_label.grid(row=2, column=0, columnspan=3)

root.mainloop()
