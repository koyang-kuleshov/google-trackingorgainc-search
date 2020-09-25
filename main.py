import csv
import argparse
from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

SEARCHERS_PATH = 'searchers.csv'
START_URL = 'https://analytics.google.com'
LOGIN_ID = 'identifierId'


def read_params():
    parser = argparse.ArgumentParser(description='Filling regular search result'
                                     ' in Google Analytics')
    parser.add_argument(
        'login',
        type=str,
        default=None,
        help='Google Analytics login'
    )
    parser.add_argument(
        'password',
        type=str,
        default=None,
        help='Google Analytics login'
    )
    parser.add_argument(
        'account',
        type=str,
        default=None,
        help='Specify the account to fill in'
    )
    parser.add_argument(
        '-s',
        '--silent',
        type=bool,
        default=True,
        help='Specify False to see the filling process'
    )
    namespace = parser.parse_args()
    return (namespace.login, namespace.password, namespace.account,
            namespace.silent)


def fill_google_analytics(login, passwd, account):
    driver.get(START_URL)
    login_elem = driver.find_element_by_id(LOGIN_ID)
    login_elem.click()
    login_elem.send_keys(login)
    sleep(randint(1, 3))
    login_elem.send_keys(Keys.RETURN)
    sleep(3)
    passwd_elem = driver.find_element_by_xpath('//input[@type="password"][@name="password"]')
    passwd_elem.click()
    passwd_elem.send_keys(passwd)
    sleep(randint(1, 3))
    passwd_elem.send_keys(Keys.RETURN)
    home_url = 'https://analytics.google.com/analytics/web/#/report-home/a179018364w247575293p229801232'
    admin_url = 'https://analytics.google.com/analytics/web/#/a179018364w247575293p229801232/admin'
    spam = input('Waiting...')
    try:
        with open(SEARCHERS_PATH, 'r') as r_file:
            dict_reader = csv.DictReader(r_file, delimiter=',')
            for row in dict_reader:
                print(row.items())
    except OSError as err:
        print('Ошибка чтения файла: ', err)
    else:
        pass
    driver.quit()
    print('Task done')


if __name__ == "__main__":
    login, password, account, silent = read_params()
    # TODO: Delete row below
    silent = False
    options = None
    if silent:
        options = Options()
        options.add_argument('--headless')
    driver = webdriver.Firefox(
        executable_path='/usr/bin/geckodriver',
        firefox_binary='/usr/bin/firefox',
        options=options
    )
    fill_google_analytics(login, password, account)
