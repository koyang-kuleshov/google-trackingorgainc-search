import sys
import csv
from time import sleep

import keyboard

SEARCHERS_PATH = 'searchers.csv'


def fill_google_analytics():
    with open(SEARCHERS_PATH, 'r') as r_file:
        dict_reader = csv.DictReader(r_file, delimiter=',')
        for count, row in enumerate(dict_reader, 1):
            print(f'[{count}] {row["Domain"]}?{row["Parameter"]}')
            while True:
                if keyboard.is_pressed('ctrl'):
                    keyboard.send('tab')
                    keyboard.send('tab')
                    sleep(0.3)
                    keyboard.write(row['Domain'], delay=0.05)
                    keyboard.send('Tab')
                    # TODO: Change to using clipboard
                    try:
                        keyboard.write(row['Parameter'], delay=0.1)
                    except Exception:
                        print(f'Допиши параметр руками: {row["Parameter"]}'
                              ' и нажми Enter')
                    keyboard.send('Tab')
                    keyboard.send('Tab')
                    keyboard.send('Return')
                    break
                if keyboard.is_pressed('esc'):
                    break
                    sys.exit(1)
    print('Task done')
    sys.exit(1)


if __name__ == "__main__":
    print('Для заполнения поля Домен и Параметр нажми CTRL'
          '\nДля остановки скрипта ESC')
    fill_google_analytics()
