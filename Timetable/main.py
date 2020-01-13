"""School timetable generator"""
import os
import random

from prettytable import PrettyTable


class Teacher:
    """Class that models a teacher"""

    def __init__(self, number, subject, periods):
        self.number = number
        self.subject = subject
        self.periods_left = periods

    def add_class(self):
        """Reduces number of periods left for a teacher"""
        self.periods_left -= 4

    def __repr__(self):
        return str(self.number)


class Class:
    """Class that models a class"""

    def __init__(self, number):
        self.number = number
        self.teachers = {}
        self.timetable = {
            "Monday": [""] * 4,
            "Tuesday": [""] * 4,
            "Wednesday": [""] * 4,
            "Thursday": [""] * 4,
            "Friday": [""] * 4,
        }

    def add_teacher(self, teacher):
        """Adds teacher"""
        self.teachers[teacher.subject] = teacher.number

    def add_period(self, subject, day, period):
        """Adds lesson"""
        self.timetable[day][period] = subject

    def __repr__(self):
        return str(self.number)


class Timetable:
    """Controls the algorithm"""

    def __init__(self):
        self.classes = [Class(1), Class(2), Class(3), Class(4), Class(5), Class(6)]
        self.teachers = []
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.make_timetable()

    def get_teachers(self):
        """Reads teacher data from teachers.txt"""
        file_name = input("Enter file name to read teacher data from: ")
        while not os.path.isfile(f"./{file_name}"):
            file_name = input("Please enter a valid file name: ")
        self.teachers = []
        with open(file_name, "r") as teachers_file:
            teachers_info = teachers_file.readlines()
            no_of_teachers = int(teachers_info[0].rstrip("\n"))
            for i in range(no_of_teachers):
                teacher = teachers_info[i + 1].rstrip("\n")
                subject, periods = teacher.split(",")
                periods = int(periods)

                self.teachers.append(Teacher(i + 1, subject, periods))

    def assign_teachers(self):
        """Assigns teachers to classes"""
        for teacher in self.teachers:
            for class_ in self.classes:
                if teacher.periods_left >= 4 and not teacher.subject in class_.teachers:
                    class_.add_teacher(teacher)
                    teacher.add_class()

    def assign_periods(self):
        """Assigns periods to classes"""
        for teacher in self.teachers:
            for class_ in self.classes:
                timetable = class_.timetable
                day = random.randint(0, 4)
                day = self.days[day]
                period = random.randint(0, 3)
                if (
                        timetable[day][period] == ""
                        and self.is_teacher_free(teacher, day, period)
                        and timetable[day].count(teacher.subject) < 2
                        and get_subject_count(teacher.subject, timetable) < 4
                ):
                    class_.add_period(teacher.subject, day, period)

    def make_timetable(self):
        """makes timetable"""
        self.get_teachers()
        self.assign_teachers()
        empty_periods = []
        lowest = 120
        while self.get_empty_periods() != 0 or self.check_teacher_clashes():
            empty_periods.append(self.get_empty_periods())

            if self.get_empty_periods() < lowest:
                lowest = self.get_empty_periods()

                # creates progress bar
                percent = ("{0:." + str(1) + "f}").format(
                    100 * ((120 - lowest) / float(120))
                )
                filled_length = int(100 * (120 - lowest) // 120)
                progress_bar = "█" * filled_length + "-" * (100 - filled_length)
                print(
                    f"\rCreating Timetable |{progress_bar}| {percent}% done", end="\r"
                )

            self.assign_periods()

            if self.check_teacher_clashes():
                self.clear_tables()

            if len(empty_periods) > 10:
                if len(set(empty_periods)) == 1:
                    self.clear_tables()
                empty_periods = []

        print("\nTimetable created in timetable.txt")

        self.create_timetables()

    def is_teacher_free(self, teacher, day, period):
        """Checks if a teacher is free on a specific day and period"""
        for class_ in self.classes:
            subject = class_.timetable[day][period]
            if subject:
                if (
                        subject == teacher.subject
                        and class_.teachers[subject] == teacher.number
                ):
                    return False

        return True

    def check_teacher_clashes(self):
        """Checks if a teacher has to teach more than one class at once"""
        table = []
        for class_ in self.classes:
            row = [f"Class {class_.number}"]

            for day in class_.timetable:
                subjects = class_.timetable[day]
                periods = [""] * 4
                for i, subject in enumerate(subjects):
                    if subject:
                        subject += f"\nTeacher {class_.teachers[subject]}\n"
                    periods[i] = subject
                row += periods

            table.append(row)

        for column in range(1, 21):
            period = [i[column] for i in table]
            for subject in period:
                if subject:
                    if period.count(subject) > 1:
                        return True
        return False

    def get_empty_periods(self):
        """Returns the number of empty periods in the timetable"""
        count = 0
        for class_ in self.classes:
            for day in class_.timetable:
                if "" in class_.timetable[day]:
                    count += class_.timetable[day].count("")

        return count

    def clear_tables(self):
        """Clears all timetables"""
        for class_ in self.classes:
            class_.timetable = {
                "Monday": [""] * 4,
                "Tuesday": [""] * 4,
                "Wednesday": [""] * 4,
                "Thursday": [""] * 4,
                "Friday": [""] * 4,
            }

    def create_timetables(self):
        """Creates a prettytable for each class"""
        table = PrettyTable()
        table.field_names = [
            "Class",
            "Monday 1",
            "Monday 2",
            "Monday 3",
            "Monday 4",
            "Tuesday 1",
            "Tuesday 2",
            "Tuesday 3",
            "Tuesday 4",
            "Wednesday 1",
            "Wednesday 2",
            "Wednesday 3",
            "Wednesday 4",
            "Thursday 1",
            "Thursday 2",
            "Thursday 3",
            "Thursday 4",
            "Friday 1",
            "Friday 2",
            "Friday 3",
            "Friday 4",
        ]
        for class_ in self.classes:
            row = [f"Class {class_.number}"]

            for day in class_.timetable:
                subjects = class_.timetable[day]
                for i, subject in enumerate(subjects):
                    if subject:
                        subject += f"\nTeacher {class_.teachers[subject]}\n"
                    subjects[i] = subject
                row += subjects
            table.add_row(row)
            with open(f"timetable.txt", "w") as timetable_file:
                timetable_file.write(str(table))

        return table


def get_subject_count(subject, timetable):
    """Returns the number of times a class has a subject in the week"""
    count = 0
    for day in timetable:
        if subject in timetable[day]:
            count += timetable[day].count(subject)

    return count


if __name__ == "__main__":
    TIMETABLE = Timetable()
