"""Fill Google Analytics"""
import sys
from collections import namedtuple
import csv
from time import sleep, monotonic

from pynput import keyboard
import pyautogui
import pyscreenshot as ImageGrab


SEARCHERS_PATH = 'searchers.csv'
CatchingObj = namedtuple('CatchingObj', ['bbox', 'color'])
GREY_BACKGROUND = CatchingObj((2120, 487, 2121, 488), (204, 204, 204))
BLUE_BUTTON = CatchingObj((2120, 760, 2121, 761), (74, 139, 245))
DELAY = 0.3


def wait_object(obj):
    """Function waits until the object appears on the screen"""

    while True:
        sleep(DELAY)
        image = ImageGrab.grab(bbox=obj.bbox)
        tmp_color = image.convert('RGB').getcolors()[0][1]

        if tmp_color == obj.color:
            break


def fill_google_analytics():
    """Fill Regular Search information"""
    start_time = monotonic()
    keybrd = keyboard.Controller()
    with open(SEARCHERS_PATH, 'r') as r_file:
        dict_reader = csv.DictReader(r_file, delimiter=',')

        for count, row in enumerate(dict_reader, 1):
            print(f'[{count}] {row["Domain"]}?{row["Parameter"]}')
            pyautogui.click(2250, 510)
            wait_object(BLUE_BUTTON)
            sleep(DELAY)
            keybrd.press(keyboard.Key.tab)
            keybrd.release(keyboard.Key.tab)
            keybrd.press(keyboard.Key.tab)
            keybrd.release(keyboard.Key.tab)
            keybrd.type(row['Domain'])
            keybrd.press(keyboard.Key.tab)
            keybrd.release(keyboard.Key.tab)
            keybrd.type(row.get('Parameter'))
            keybrd.press(keyboard.Key.tab)
            keybrd.release(keyboard.Key.tab)
            keybrd.press(keyboard.Key.tab)
            keybrd.release(keyboard.Key.tab)
            keybrd.press(keyboard.Key.enter)
            keybrd.release(keyboard.Key.enter)
            sleep(DELAY)
            wait_object(GREY_BACKGROUND)
    end_time = monotonic() - start_time
    print(f'Task done. Time: {end_time}')
    sys.exit(1)


if __name__ == "__main__":
    print('1. Запустить скрипт',
          '2. Перейти на страницу "Источники обычных результатов поиска"',
          ' в Google Analytics'
          '3. Программа автоматически заполнит все параметры из файла'
          ' searchers.csv',
          sep='\n')
    fill_google_analytics()
