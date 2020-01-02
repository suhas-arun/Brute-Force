# Fedora Infrastructure Telegram Bot (For Google Code-In)

The bot has the following commands: 
* `/start`
* `/forks`
* `/help`

`/forks` displays the total number of forks of the fedora-infra repositories on Github. This is done by calling the Github API and then totalling the `forks_count` value for each repository. These values are also used to find the repository with the most forks.

The code is in [main.py](https://github.com/suhas-arun/Google-Code-In/tree/master/Fedora-Telegram-Bot/main.py). For the callback functions, `*_` is used as the second argument as there is usually an extra argument for `context` which is not used in the functions.

Press Ctrl + C to stop the bot.


Below is a conversation with @FedoraInfraBot:

![Conversation with the bot](https://github.com/suhas-arun/Google-Code-In/tree/master/Fedora-Telegram-Bot/example.png)
