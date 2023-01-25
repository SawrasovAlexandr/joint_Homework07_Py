import csv
import init

def unload_file(path_file: str, database: list) -> None:
    temp_data = []
    for item in database:
        temp = {}
        temp = item.copy()
        temp.pop('ID')
        temp_data.append(temp)
    with open(path_file, 'w', newline='', encoding='utf-8-sig') as data:
        colomn = init.get_temp_db_keys()
        data_csv = csv.DictWriter(data, fieldnames=colomn, delimiter=';')
        data_csv.writeheader()
        data_csv.writerows(temp_data)
    return