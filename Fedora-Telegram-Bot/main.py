"""
Telegram Bot which fetches the number of forks from the Fedora-Infra repositories.
"""

import logging
import requests
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


# callback functions:


def start(update, _):
    """Send a start message when the /start command is used"""

    update.message.reply_text(
        "Hello I am the Fedora Infra bot.\nUse /help to see the usable commands."
    )


def help_command(update, _):
    """Show the available commands when /help is used"""

    update.message.reply_text(
        "/start: Show the bot's starting message\n\n/forks [repo name]: Get the number of forks of a Fedora-Infra repository\n\n/help: Show this help message"
    )


def forks(update, context):
    """Show the number of forks of a Fedora-Infra repo"""

    repo_name = " ".join(context.args)

    if not repo_name:
        update.message.reply_text(
            "Please include a repository name with the /forks command."
        )
        return

    repo_info = get_repo_forks(repo_name)

    if repo_info:
        fork_count, url = repo_info
        update.message.reply_text(
            f"'{repo_name}' has {fork_count} forks.\n\nVisit the repository here\n{url}."
        )
    else:
        update.message.reply_text(
            f"The '{repo_name}' repository could not be found.\nPlease try another repository."
        )


def unknown(update, _):
    """Send a message when an unknown command is used"""

    update.message.reply_text(
        "Sorry, I didn't understand that command.\nUse /help to see the usable commands."
    )


def get_repos_data():
    """Returns the repo data for the fedora-infra repos"""

    url = "https://api.github.com/orgs/fedora-infra/repos"
    response = requests.get(url)
    repos = response.json()

    return repos


def get_repo_forks(name):
    """Fetch number of forks from a Fedora-infra repo"""

    repos = get_repos_data()

    for repo in repos:
        if repo["name"] == name:
            fork_count = repo["forks_count"]
            url = repo["html_url"]

            return (fork_count, url)


def main():
    """main function"""

    token = ""

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
