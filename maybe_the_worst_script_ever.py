#!/usr/bin/env python3

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Liker:
    """
    Run this and log in at tinder.com, the app will do the rest...
    """
    def __init__(self):
        driver_path = os.path.dirname(os.path.realpath(__file__))
        self.login_link = 'https://tinder.com/'
        self.main_link = 'https://tinder.com/app/recs'
        self.browser = webdriver.Firefox(
            executable_path = driver_path + '/geckodriver')
        self.browser.get(self.login_link)

    def log_in_check(self):
        if self.browser.current_url == self.main_link:
            return True
        else:
            return False

    def spam_like_button(self):
        """ Spam the hell outta this button """
        page_body = self.browser.find_elements_by_css_selector('body')[0]
        page_body.send_keys(Keys.RIGHT)

    def run(self):
        print('Log into your account.')
        while True:
            if self.log_in_check():
                self.spam_like_button()
            sleep(1)


if __name__ == '__main__':

    try:
        app = Liker()
        app.run()
    except Exception as e:
        print(e)
        app.browser.quit()
        print('\nWebdriver has stopped')