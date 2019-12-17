"""tkinter application with three options to perform tasks. Made in Fedora 31"""
import tkinter
import subprocess

ROOT = tkinter.Tk()
ROOT.title("Application Launcher")


def launch_google():
    """launches google.com from the terminal"""
    subprocess.call(["xdg-open", "https://google.com"])


def launch_github():
    """launches github.com from the terminal"""
    subprocess.call(["xdg-open", "https://github.com"])


def launch_spotify():
    """opens spotify from the terminal"""
    subprocess.call(["spotify"])


GOOGLE_BUTTON = tkinter.Button(text="Open Google", font=(
    "Helvetica", 20), height=3, command=launch_google)
GITHUB_BUTTON = tkinter.Button(text="Open Github", font=(
    "Helvetica", 20), height=3, command=launch_github)
SPOTIFY_BUTTON = tkinter.Button(text="Open Spotify", font=(
    "Helvetica", 20), height=3, command=launch_spotify)

GOOGLE_BUTTON.grid(row=0, column=0)
GITHUB_BUTTON.grid(row=0, column=1)
SPOTIFY_BUTTON.grid(row=0, column=2)

ROOT.mainloop()
