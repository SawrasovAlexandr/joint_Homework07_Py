import csv

def main_db(path_file: str) -> list:
    with open(path_file, 'r', newline='', encoding = 'utf-8') as data:
        database = list(csv.DictReader(data, fieldnames=get_main_db_keys(), delimiter=';'))
        
    return list(database)

def get_main_db_keys() -> list:
        return ['Фамилия', 'Имя', 'Телефон', 'Комментарий']
    