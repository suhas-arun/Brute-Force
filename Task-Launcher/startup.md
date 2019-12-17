In order to execute the program when the system starts, I did the following:

1. Copy the file to the `usr/bin/` directory

2. Created a crontab file using the `sudo crontab -e` command

2. Added the following line:

    `@reboot usr/bin/python usr/bin/main.py`

3. Saved the file by using the command `:wq`

