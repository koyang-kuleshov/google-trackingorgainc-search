import csv
import argparse


SEARCHERS_PATH = 'searchers.csv'


def read_params():
    parser = argparse.ArgumentParser(description='Filling regular search result'
                                     ' in Google Analytics')
    parser.add_argument(
        '-a',
        '--account',
        type=str,
        default=None,
        help='Specify the account to fill in'
    )
    parser.add_argument(
        '-s',
        '--silent',
        type=bool,
        default=False,
        help='Specify True to see the filling process'
    )
    namespace = parser.parse_args()
    print(namespace)


def fill_google_analytics():
    try:
        with open(SEARCHERS_PATH, 'r') as r_file:
            dict_reader = csv.DictReader(r_file, delimiter=',')
            for row in dict_reader:
                print(row.items())
    except OSError as err:
        print('Ошибка чтения файла: ', err)
    else:
        pass


if __name__ == "__main__":
    read_params()
    fill_google_analytics()
