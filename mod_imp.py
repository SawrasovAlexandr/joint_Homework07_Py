# Загрузка прошла успешно True неуспешно False
import csv
import init

def load_file(path_file: str, database: list) -> list:
    try:
        with open(path_file, 'r', newline='', encoding = 'utf-8') as data:
            load_base = list(csv.DictReader(data, fieldnames=init.get_main_db_keys(), delimiter=';'))
        if database: load_base.pop(0)
        for i, item in enumerate(load_base, len(database)):
            item['ID'] = i
            load_base.append(item)
        load_base = database.extend(load_base)
    except:
        print('Ошибка загрузки файла!')
        load_base = []
    return load_base
