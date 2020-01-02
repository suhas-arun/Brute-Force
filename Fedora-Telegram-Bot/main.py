"""
Telegram Bot which fetches the number of forks from the Fedora-Infra repositories.
"""

import logging
import requests
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


# callback functions:


def start(update, *_):
    """Send a start message when the /start command is used"""

    update.message.reply_text(
        "Hello I am the Fedora Infra bot.\nUse /help to see the usable commands."
    )


def help_command(update, *_):
    """Show the available commands when /help is used"""

    update.message.reply_text(
        "/start: Show the bot's starting message\n/forks: Get the number of forks from the Fedora-Infra repositories\n/help: Show this help message"
    )


def forks(update, *_):
    """Show the number of forks from the Fedora-Infra repos when /forks is used"""

    forks_count, most_forked, highest_fork_count = get_forks()

    url = "https://github.com/fedora-infra"

    update.message.reply_text(
        f"The Fedora-Infra repositories currently have {forks_count} total forks\nThe most forked repository is '{most_forked}' with {highest_fork_count} forks\n\nVisit the Fedora Infrastructure Github page here:\n{url}"
    )


def unknown(update, *_):
    """Send a message when an unknown command is used"""

    update.message.reply_text(
        "Sorry, I didn't understand that command.\nUse /help to see the usable commands."
    )


def get_forks():
    """Fetch number of forks from the Fedora-infra repos and the most forked repo"""

    url = "https://api.github.com/orgs/fedora-infra/repos"
    response = requests.get(url)
    repos = response.json()

    forks_count = 0
    most_forked = ""
    highest_fork_count = 0

    for repo in repos:
        fork_count = repo["forks_count"]
        forks_count += fork_count

        if fork_count > highest_fork_count:
            most_forked = repo["name"]
            highest_fork_count = fork_count

    return (forks_count, most_forked, highest_fork_count)


def main():
    """main function"""

    token = "1027172895:AAEKPuL-9wYVI2kCUzNFNQ1wjFkYROqqrek"

    updater = Updater(token, use_context=True)

    dispatcher = updater.dispatcher

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)

    help_handler = CommandHandler("help", help_command)
    dispatcher.add_handler(help_handler)

    fork_handler = CommandHandler("forks", forks)
    dispatcher.add_handler(fork_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
