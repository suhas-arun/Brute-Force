# Automated codeforces registration (For Google Code-In)

The script does the following:

* Opens https://codeforces.com/register in the default browser.
* Gets input from the user for handle, email and password (passwords are entered using `getpass` i.e. they are not echoed in the terminal).
* Asks the user to confirm the password and if it does not match the first entry, there is a suitable message and the program stops.
* Finds the input elements for handle, email and password on the website using their xpath.
* Fills in these fields with the entered data.
* Finds the register button on the page and clicks it.

[succesful-registration.png](https://github.com/suhas-arun/Google-Code-In/blob/master/Codeforces-Registration/successful-registration.png) is a screenshot of my window after the program executed showing that registration was successful.

![Successful Registration](https://github.com/suhas-arun/Google-Code-In/blob/master/Codeforces-Registration/successful-registration.png)
