import csv
import init

def unload_file(path_file: str, database: list) -> None:
    database = list(map(lambda item: item.pop('ID'), database))
    with open(path_file, 'w', newline='', encoding='utf-8-sig') as data:
        colomn = init.get_temp_db_keys()
        data_csv = csv.DictWriter(data, fieldnames=colomn, delimiter=';')
        data_csv.writeheader()
        data_csv.writerows(database)
    return