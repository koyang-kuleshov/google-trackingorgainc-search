import sys
import csv
from time import sleep

from pynput import keyboard


SEARCHERS_PATH = 'searchers1.csv'
WHITE_BUTTON_COORD = (2175, 493)
WHITE_BUTTON_COLOR = [255, 255, 255]  # RGB
BLUE_BUTT0N_COORD = (2175, 750)
BLUE_BUTTON_COLOR = [74, 140, 248]  # RGB


def fill_google_analytics():
    kb = keyboard.Controller()
    # while True:
    #     print('White')
    #     print('Blue')
    with open(SEARCHERS_PATH, 'r') as r_file:
        dict_reader = csv.DictReader(r_file, delimiter=',')
        for count, row in enumerate(dict_reader, 1):
            print(f'[{count}] {row["Domain"]}?{row["Parameter"]}')
            while True:
                with keyboard.Events() as events:
                    event = events.get()
                if event.key == keyboard.Key.ctrl:
                    sleep(0.3)
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
                    break
                elif event.key == keyboard.Key.esc:
                    break
                    sys.exit(1)
    print('Task done')
    sys.exit(1)


if __name__ == "__main__":
    print('Для заполнения поля Домен и Параметр нажми CTRL'
          '\nДля остановки скрипта ESC')
    fill_google_analytics()
