"""Periodic table guessing game"""
import csv
import random
import tkinter
import tkinter.messagebox


class Game:
    """Class that controls the game mechanisms"""

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Periodic Table Game")
        self.element = None
        self.elements = []
        self.bg_colour = "gray20"
        self.fg_colour = "gray90"
        self.entry = None

        self.get_new_element()

        self.root.mainloop()

    def get_new_element(self):
        """Gets new element from the data and appends it to list of already used elements"""
        with open("periodic-table.csv") as csvfile:
            elements = csv.reader(csvfile, delimiter=",")
            self.element = Element(random.choice(list(elements)[1:]))
            while self.element in self.elements:
                self.element = Element(random.choice(list(elements)[1:]))
            self.elements.append(self.element)

        self.display()

    def submit(self):
        """Submit answer"""
        answer = self.entry.get().title()
        self.entry.delete(0, "end")
        if answer in [self.element.symbol, self.element.name]:
            self.correct_answer()
        else:
            self.wrong_answer()

    def correct_answer(self):
        """Called when user gets a right answer"""
        tkinter.messagebox.showinfo("Correct!", "You got it right!")
        self.element.show_info()
        self.get_new_element()

    def wrong_answer(self):
        """Called when user gets the question wrong"""
        tkinter.messagebox.showinfo(
            "Incorrect",
            f"You got it wrong.\n\nYou have {4-self.element.hints} guess(es) left",
        )
        hint = self.element.get_hint()
        self.element.hints += 1

        if hint:
            tkinter.messagebox.showinfo("Hint", "Hint: " + hint)
        else:
            tkinter.messagebox.showinfo(
                "Unlucky",
                f"The correct answer was {self.element.symbol} - {self.element.name}.",
            )
            self.element.show_info()
            self.get_new_element()

    def give_up(self):
        """Goes to the next symbol"""
        tkinter.messagebox.showinfo(
            "Unlucky",
            f"The correct answer was {self.element.symbol} - {self.element.name}.",
        )
        self.element.show_info()
        self.get_new_element()

    def display(self):
        """Displays game"""
        self.root.config(bg=self.bg_colour)

        # title label
        tkinter.Label(
            text="Periodic Table Guessing Game",
            bg=self.bg_colour,
            fg=self.fg_colour,
            font="roboto 20 bold",
            padx=20,
        ).grid(row=0, columnspan=3)

        # element symbol label
        tkinter.Label(
            text=self.element.number,
            font="roboto 48 bold",
            fg="orange",
            width=10,
            pady=10,
            bg=self.bg_colour,
        ).grid(row=1, columnspan=3)

        self.entry = tkinter.Entry(font="roboto 12")

        # create placeholder in entry box
        self.entry.insert(0, "Enter symbol:")

        # remove placeholder when entry box is clicked on
        self.entry.bind("<FocusIn>", lambda args: self.entry.delete("0", "end"))

        self.entry.grid(row=2, columnspan=3)

        buttons_frame = tkinter.Frame(pady=10, bg=self.bg_colour)
        buttons_frame.grid(row=3, columnspan=3)

        # give up button
        tkinter.Button(
            buttons_frame,
            text="Give up",
            fg=self.fg_colour,
            bg=self.bg_colour,
            font="roboto 12 bold",
            command=self.give_up,
        ).grid(row=0, column=0)

        # submit button
        tkinter.Button(
            buttons_frame,
            text="Submit",
            fg=self.fg_colour,
            bg=self.bg_colour,
            font="roboto 12 bold",
            command=self.submit,
        ).grid(row=0, column=1)

        # exit button
        tkinter.Button(
            buttons_frame,
            text="Exit",
            fg=self.fg_colour,
            bg=self.bg_colour,
            font="roboto 12 bold",
            command=self.root.destroy,
        ).grid(row=0, column=2)


class Element:
    """Class that models an element"""

    def __init__(self, data):
        self.number = data[0]
        self.name = data[1]
        self.symbol = data[2]
        self.extra_info = data[3:7]
        # weight, group, phase, type

        self.hints = 0

    def get_hint(self):
        """Returns a hint if the user enters a wrong answer"""

        group, phase, element_type = self.extra_info[1:]
        if self.hints == 0:
            hint = f"This element is in group {group}."
        elif self.hints == 1:
            hint = f"This element is a {element_type.lower()}."
        elif self.hints == 2:
            if phase == "artificial":
                hint = "This element was artificially created."
            else:
                hint = f"This element is a {phase} at room temperature."
        elif self.hints == 3:
            hint = "You are out of hints!"
        else:
            return None

        return hint

    def show_info(self):
        """Show element info"""
        weight, group, phase, element_type = self.extra_info
        weight = round(float(weight), 2)
        text = f"{self.name}, {self.symbol}\n\nAtomic number: {self.number}\nAtomic weight: {weight}\nGroup: {group}\nPhase: {phase}\nType: {element_type}"
        tkinter.messagebox.showinfo(self.name, text)


if __name__ == "__main__":
    GAME = Game()
