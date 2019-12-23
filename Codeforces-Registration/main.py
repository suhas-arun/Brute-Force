"""Script that automates the process of registering for Codeforces"""
import sys
from getpass import getpass

from selenium.webdriver import Chrome


def get_info():
    """Gets user input for the account credentials"""

    handle = input("Enter handle: ")
    email = input("Enter email: ")
    password = getpass()
    password2 = getpass("Confirm password: ")

    if password != password2:
        print("Passwords don't match.")
        sys.exit(1)

    return (handle, email, password)


def register():
    """Registers an account"""

    driver.get("https://codeforces.com/register")
    handle, email, password = get_info()

    handle_field = driver.find_element_by_xpath(
        "/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[1]/td[2]/input"
    )
    email_field = driver.find_element_by_xpath(
        "/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[5]/td[2]/input"
    )
    password_field = driver.find_element_by_xpath(
        "/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[6]/td[2]/input"
    )
    password2_field = driver.find_element_by_xpath(
        "/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[8]/td[2]/input"
    )

    register_button = driver.find_element_by_class_name("submit")

    handle_field.send_keys(handle)
    email_field.send_keys(email)
    password_field.send_keys(password)
    password2_field.send_keys(password)

    register_button.click()


if __name__ == "__main__":
    WEB_DRIVER = "/usr/bin/chromedriver"
    driver = Chrome(WEB_DRIVER)
    register()
