import csv

def main_db(path_file: str) -> list:
    with open(path_file, 'r', newline='', encoding = 'utf-8') as database:
        main_db = csv.DictReader(database, fieldnames=get_main_db_keys(), delimiter=';')
    return list(main_db)
    
def temp_db(main_db: list) -> list:
    temp_db = []
    for i, item in enumerate(main_db):
            item['ID'] = i
            temp_db.append(item)
    return temp_db
        
def get_main_db_keys() -> list:
        return ['Фамилия', 'Имя', 'Телефон', 'Комментарий']
    
def get_temp_db_keys() -> list:
        return ['ID', 'Фамилия', 'Имя', 'Телефон', 'Комментарий']
    