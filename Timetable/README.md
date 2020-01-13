# School Timetable Generator (For Google Code-In)

The program generates a timetable for 6 classes for 4 periods a day. Each class has 5 subjects (Maths, Programming, Physics, Chemistry and Biology) and one teacher per subject. There are 2 teachers per subject, and **the subject and number of hours for each teacher is read from a file** ([teachers.txt](./teachers.txt)). A teacher of course cannot teach more than one class at once. Note that the total number of hours for each subject's teachers must add up to at least 24 (as 6 classes have 4 periods of one subject per week).

The order of subjects is randomly generated repeatedly, until the timetable is full and there are no clashes. **Due to the algorithm being based on randomness, the execution time varies greatly.** While the timetable is being generated, there is a progress bar that indicates how close the timetable is to being generated.

The timetable for each class is then converted to a `PrettyTable` and this table is stored in a file [timetable.txt](./timetable.txt)
