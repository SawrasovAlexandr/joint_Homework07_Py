import csv
import init

def unload_file(path_file: str, database: list) -> None:
    try:
        with open(path_file, 'w', newline='', encoding='utf-8-sig') as data:
            database.pop(0)
            colomn = init.get_main_db_keys()
            data_csv = csv.DictWriter(data, fieldnames=colomn, delimiter=';')
            data_csv.writeheader()
            data_csv.writerows(database)
    except: print('\nОшибка загрузки файла!\n')
    