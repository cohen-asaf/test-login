from selenium import webdriver
from selenium.webdriver.common.by import *
import requests
import time
from validate_email import validate_email


def login():
    driver = webdriver.Chrome()
    LOGIN_PAGE = "https://web.eos.bnk-il.com/auth"
    driver.get(LOGIN_PAGE)
    server_response = requests.get(LOGIN_PAGE)

    ''' verify that the server is responsive and available'''
    assert server_response.status_code == 200, "server is not available"
    time.sleep(3)
    print("server is up and running")

    '''enter email address and verify the email structure'''
    email = input("Enter Email address: ")
    assert validate_email(email), "inValid Email Address"
    print("Valid Email Address")

    '''adding email address and password to the login screen '''
    driver.find_element(By.ID, ":r1:").send_keys(email)
    print(email + " email input succesfully")
    password = input("Enter Password: ")
    driver.find_element(By.ID, ":r2:").send_keys(password)
    print(password + " password input succesfully")
    driver.find_element(By.CSS_SELECTOR, ".MuiButton-contained").click()
    print("user log-in")


login()
