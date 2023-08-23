"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.

"""

from pathlib import Path
import pickle


SOME_CSV = Path.cwd() / 'task_6.csv'


def some_function(path_to_file):
    with open(path_to_file, 'rb') as file:
        print(pickle.dumps(file.read()))


if __name__ == '__main__':
    Path(Path.cwd()).mkdir(parents=True, exist_ok=True)
    try:
        some_function(SOME_CSV)
    except Exception as err:
        print(err)