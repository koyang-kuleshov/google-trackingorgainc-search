import sys
import csv
from time import sleep, monotonic

from pynput import keyboard
import pyautogui

from collections import namedtuple
import pyscreenshot as ImageGrab

SEARCHERS_PATH = 'searchers.csv'
CatchingObj = namedtuple('CatchingObj', ['bbox', 'color'])
grey_background = CatchingObj((2120, 487, 2121, 488), (204, 204, 204))
blue_button = CatchingObj((2120, 760, 2121, 761), (74, 139, 245))


def wait_object(obj):
    """Function waits until the object appears on the screen"""
    while True:
        sleep(0.5)
        im = ImageGrab.grab(bbox=obj.bbox)
        tmp_color = im.convert('RGB').getcolors()[0][1]
        if tmp_color == obj.color:
            break


def fill_google_analytics():
    start_time = monotonic()
    kb = keyboard.Controller()
    with open(SEARCHERS_PATH, 'r') as r_file:
        dict_reader = csv.DictReader(r_file, delimiter=',')
        for count, row in enumerate(dict_reader, 1):
            print(f'[{count}] {row["Domain"]}?{row["Parameter"]}')
            pyautogui.click(2250, 510)
            wait_object(blue_button)
            sleep(0.5)
            kb.press(keyboard.Key.tab)
            kb.release(keyboard.Key.tab)
            kb.press(keyboard.Key.tab)
            kb.release(keyboard.Key.tab)
            kb.type(row['Domain'])
            kb.press(keyboard.Key.tab)
            kb.release(keyboard.Key.tab)
            kb.type(row.get('Parameter'))
            kb.press(keyboard.Key.tab)
            kb.release(keyboard.Key.tab)
            kb.press(keyboard.Key.tab)
            kb.release(keyboard.Key.tab)
            kb.press(keyboard.Key.enter)
            kb.release(keyboard.Key.enter)
            sleep(1)
            wait_object(grey_background)
    end_time = monotonic() - start_time
    print(f'Task done. Time: {end_time}')
    sys.exit(1)


if __name__ == "__main__":
    print('1. Запустить скрипт',
          '2. Перейти на страницу "Источники обычных результатов поиска" в Google Analytics'
          '3. Программа автоматически заполнит все параметры из файла searchers.csv',
          sep='\n')
    fill_google_analytics()
