# Загрузка прошла успешно True неуспешно False
import csv
import init

def load_file(path_file: str, database: list = []) -> list:
    try:
        with open(path_file, 'r', newline='', encoding = 'utf-8') as data:
            colomn = init.get_main_db_keys()
            load_base = list(csv.DictReader(data, fieldnames=colomn, delimiter=';'))
        if database: load_base.pop(0)
        # for item in load_base:
        #     database.append(item)
        database.extend(load_base)
    except:
        print('\nОшибка загрузки файла!\n')
    # return database
