import csv
import argparse
from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


def wait_class(c_name="ga-footer-links"):
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, c_name)
            )
        )
    except Exception:
        pass
    finally:
        pass


def fill_google_analytics(login, passwd, account):
    driver.get(START_URL)
    login_elem = driver.find_element_by_id(LOGIN_ID)
    login_elem.click()
    login_elem.send_keys(login)
    sleep(randint(1, 3))
    login_elem.send_keys(Keys.RETURN)
    sleep(3)
    # wait_class()
    passwd_elem = driver.find_element_by_xpath(
        '//input[@type="password"][@name="password"]'
    )
    passwd_elem.click()
    passwd_elem.send_keys(passwd)
    sleep(randint(1, 3))
    passwd_elem.send_keys(Keys.RETURN)
    wait_class()
    search_res = '/admin/trackingorgainc-search-sources/'
    admin_url = driver.current_url.replace('report-home/', '') + search_res
    sleep(3)
    driver.get(admin_url)
    wait_class('ID-adminTable')
    # print(driver.find_element_by_xpath('//div[@class="ID-adminTable"'))
    try:
        with open(SEARCHERS_PATH, 'r') as r_file:
            dict_reader = csv.DictReader(r_file, delimiter=',')
            for count, row in enumerate(dict_reader, 1):
                # ID-shortcutAction ACTION-action TARGET-addOrganicSearchClicked _GAYe _GAgib _GAy
                print(f'[{count}:] {row["Domain"]}?{row["Parameter"]}')
                sleep(5)
                button = driver.find_element_by_xpath(
                    # '//input[@type="submit"]'
                    # '//input[@class="ID-shortcutAction"]'
                    '//div[@id="ID-m-content-content-tableControl"]'
                )
                # for i, e in enumerate(button):
                #     print(f'{i} - {e}')
                button.click()
                wait_class('W_DECORATE_ELEMENT')
                domain = driver.find_element_by_xpath(
                    '//input[@data-name="domainName"]')
                domain.click()
                domain.send_keys(row['Domain'])
                # W_DECORATE_ELEMENT _GASh _GAepb _GAmc-_GAxD-_GAmc
                param = driver.find_element_by_xpath(
                    '//input[@data-name="queryParam"]')
                param.click()
                param.send_keys(row['Parameter'])
                spam = input('Waiting...')
                button = driver.find_element_by_xpath(
                    '//button[@type="submit"]')
                button.click()
                wait_class()
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
