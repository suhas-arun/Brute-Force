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
        self.root.resizable(False, False)
        self.element = None
        self.elements = []
        self.bg_colour = "gray20"
        self.fg_colour = "gray90"
        self.entry = None

        self.initialise_elements()
        self.get_new_element()

        self.root.mainloop()

    def initialise_elements(self):
        """Read csv file and return list of elements"""
        with open("periodic-table.csv") as csvfile:
            elements = csv.reader(csvfile, delimiter=",")
            for element in list(elements)[1:]:
                self.elements.append(Element(element))

    def get_new_element(self):
        """Randomly selects new element"""
        self.element = random.choice(self.elements)
        self.display()

    def submit(self):
        """Submit answer"""
        answer = self.entry.get().title()
        self.entry.delete(0, "end")
        if answer in [self.element.symbol, self.element.name]:
            self.correct_answer()
        else:
            self.wrong_answer(answer)

    def correct_answer(self):
        """Called when user gets a right answer"""
        tkinter.messagebox.showinfo("Correct!", "You got it right!")
        self.element.show_info()
        self.get_new_element()

    def wrong_answer(self, answer):
        """
        Called when user gets the question wrong. If the answer is wrong
        but a valid element is entered, the element's atomic number is shown.
        """

        end = False
        popup_message = (
            f"You got it wrong.\n\nYou have {4-self.element.hints} guess(es) left.\n\n"
        )

        for element in self.elements:
            if answer in [element.symbol, element.name]:
                popup_message += (
                    f"You guessed {element.name} which is number {element.number}.\n\n"
                )
                break

        hint = self.element.get_hint()
        self.element.hints += 1

        if hint:
            popup_message += f"Hint: {hint}"
        else:
            popup_message += (
                f"The correct answer was {self.element.symbol} - {self.element.name}."
            )
            end = True

        tkinter.messagebox.showinfo("Incorrect answer", popup_message)

        if end:
            self.element.show_info()
            self.get_new_element()

    def show_answer(self):
        """Shows answer"""
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
        ).grid(row=0, columnspan=4)

        # element symbol label
        tkinter.Label(
            text=self.element.number,
            font="roboto 48 bold",
            fg="orange",
            width=10,
            pady=10,
            bg=self.bg_colour,
        ).grid(row=1, columnspan=4)

        self.entry = tkinter.Entry(font="roboto 12")

        # create placeholder in entry box
        self.entry.insert(0, "Enter symbol:")

        # remove placeholder when entry box is clicked on
        self.entry.bind("<FocusIn>", lambda args: self.entry.delete("0", "end"))

        self.entry.grid(row=2, columnspan=4)

        # show answer button
        tkinter.Button(
            text="Show\nanswer",
            width=7,
            fg=self.fg_colour,
            bg=self.bg_colour,
            font="roboto 12",
            command=self.show_answer,
        ).grid(row=4, column=0, pady=10)

        # reset button
        tkinter.Button(
            text="Reset",
            width=7,
            fg=self.fg_colour,
            bg=self.bg_colour,
            font="roboto 12",
            command=self.get_new_element,
        ).grid(row=4, column=1, pady=10)

        # submit button
        tkinter.Button(
            text="Submit",
            width=7,
            fg=self.fg_colour,
            bg=self.bg_colour,
            font="roboto 12 bold",
            command=self.submit,
        ).grid(row=4, column=2, pady=10)

        # exit button
        tkinter.Button(
            text="Exit",
            width=7,
            fg=self.fg_colour,
            bg=self.bg_colour,
            font="roboto 12",
            command=self.root.destroy,
        ).grid(row=4, column=3, pady=10)


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
