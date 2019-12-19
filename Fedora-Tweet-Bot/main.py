"""
Twitter bot that scrapes article names and urls from fedoramagazine.org and tweets them.
"""
import sys
from getpass import getpass
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_posted_articles():
    """returns the names of the articles already posted by the bot.
    This prevents it from reposting old articles each time the program is run."""

    posted_articles = []
    with open("Fedora-Tweet-Bot/posted_articles.txt", "r") as articles:
        for article in articles:
            posted_articles.append(article)

    return posted_articles


def update_posted_articles(article):
    """adds the article name of a new article to posted_articles.txt"""
    with open("Fedora-Tweet-Bot/posted_articles.txt", "a") as articles:
        articles.write("\n" + article)


def get_new_articles(driver):
    """Uses Selenium to scrape the new article names and urls from the magazine website"""

    pages = 72
    new_articles = []
    posted_articles = get_posted_articles()

    for page in range(1, pages):
        url = f"https://fedoramagazine.org/page/{page}/"
        driver.get(url)
        articles_on_page = driver.find_elements_by_class_name("post-title")

        for article in articles_on_page:
            name = article.text
            url = article.find_element_by_css_selector("a").get_attribute("href")

            if name not in posted_articles:
                new_articles.append((name, url))

            else:
                break
        else:
            continue
        break
            # if the program finds an article on the page that has already been tweeted,
            # there is no point in checking the following pages as the older articles will also
            # have been posted before. The else: continue break is to break from both loops

    new_articles.reverse()  # so that the articles are oldest -> newest
    return new_articles


def login(driver):
    """login to twitter using selenium"""
    driver.get("https://twitter.com/login")

    username = driver.find_element_by_css_selector(
        "input[placeholder='Phone, email or username']"
    )
    password = driver.find_element_by_css_selector("input[class='js-password-field']")
    username_input = input("Enter username: ")
    password_input = getpass(prompt="Enter password: ")
    username.send_keys(username_input)
    password.send_keys(password_input)
    submit = driver.find_element_by_xpath(
        '//*[@id="page-container"]/div/div[1]/form/div[2]/button'
    )
    submit.click()


def tweet(driver, message):
    """function for sending a tweet using selenium"""
    driver.get("https://twitter.com/compose/tweet")
    sleep(5)

    textbox = driver.find_element_by_xpath(
        "/html/body/div/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/span/br"
    )
    textbox.send_keys(message)

    tweet_button = driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]'
    )
    tweet_button.click()


def tweet_articles(driver, articles):
    """Tweets the names and url of all the new articles on fedora magazines"""
    for article in articles:
        name, url = article
        message = f"{name}: {url}"
        tweet(driver, message)
        update_posted_articles(name)


def main():
    """main function"""
    webdriver = "/usr/bin/chromedriver"
    driver = Chrome(webdriver)
    print("Fetching articles...")
    articles = get_new_articles(driver)
    print("Articles fetched.")
    if articles:
        print("Going to Twitter now.")
        login(driver)
        if driver.current_url not in ["https://twitter.com", "https://twitter.com/home"]:
            print("Username or password incorrect.")
            sys.exit(1)
        print("Login successful!")
        print("Tweeting...")
        tweet_articles(driver, articles)
        print("Tweeted")
    else:
        print("There are no new articles.")


if __name__ == "__main__":
    main()
