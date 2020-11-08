"""Filling Google Analytics."""
import csv
from collections import namedtuple
from time import monotonic, sleep

import pyautogui
import pyscreenshot as imagegrab
from pynput import keyboard

SEARCHERS_PATH = 'searchers.csv'
CatchingObj = namedtuple('CatchingObj', ['bbox', 'color'])
GREY_BACKGROUND = CatchingObj((2120, 487, 2121, 488), (204, 204, 204))
BLUE_BUTTON = CatchingObj((2120, 760, 2121, 761), (74, 139, 245))
DELAY = 0.3
ADD_BUTTON = 2250, 510


def wait_object(expected_obj):
    """Wait for an object on the screen.

    Args:
        expected_obj: namedtuple with coordinates and color of expected object.
    """
    while True:
        sleep(DELAY)
        image = imagegrab.grab(bbox=expected_obj.bbox)
        tmp_color = image.convert('RGB').getcolors()[0][1]

        if tmp_color == expected_obj.color:
            break


def press_tab(keybrd, counter):
    """Press tab couner times.

    Args:
        keybrd: keyboard object.
        counter: number of times to press.
    """
    for _ in range(counter):
        keybrd.press(keyboard.Key.tab)
        keybrd.release(keyboard.Key.tab)


def fill_google_analytics():
    """Fill Regular Search information."""
    keybrd = keyboard.Controller()
    with open(SEARCHERS_PATH, 'r') as r_file:
        dict_reader = csv.DictReader(r_file, delimiter=',')
        for count, row in enumerate(dict_reader, 1):
            print(f'[{count}] {row["Domain"]}?{row["Parameter"]}')
            pyautogui.click(ADD_BUTTON)
            wait_object(BLUE_BUTTON)
            sleep(DELAY)
            press_tab(keybrd, 2)
            keybrd.type(row['Domain'])
            press_tab(keybrd, 1)
            keybrd.type(row.get('Parameter'))
            press_tab(keybrd, 2)
            keybrd.press(keyboard.Key.enter)
            keybrd.release(keyboard.Key.enter)
            sleep(DELAY)
            wait_object(GREY_BACKGROUND)


if __name__ == '__main__':
    print('1. Запустить скрипт\n',
          '2. Перейти на страницу "Источники обычных результатов поиска"',
          ' в Google Analytics\n',
          '3. Программа автоматически заполнит все параметры из файла'
          ' searchers.csv',
          )
    start_time = monotonic()
    fill_google_analytics()
    end_time = monotonic() - start_time
    print(f'Task done. Time: {end_time}')
