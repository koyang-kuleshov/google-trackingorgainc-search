import csv


SEARCHERS_PATH = 'searchers.csv'


def read_params():
    pass


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
    fill_google_analytics()
