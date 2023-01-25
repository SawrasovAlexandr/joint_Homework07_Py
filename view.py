import init
import os

def main_menu():
    print('1. Поиск контактов\n'
          '2. Сортировка списка контактов\n'
          '3. Добавить контакт\n'
          '4. Редактировать контакт\n'
          '5. Удалить контакт\n'
          '6. Импорт контактов\n'
          '7. Экспорт контактов\n'
          '8. Сохранить справочник\n'
          '9. Обновить справочник\n'
          '0. Выход')
    menu = input('Выберите пункт меню: ')
    return menu

def show_database(data_base: list) -> None:
    os.system('cls')
    key = init.get_main_db_keys()
    for item in data_base:
        # item = list(item.values())
        print(f'{item[key[0]]:4} | {item[key[1]]:13} | {item[key[2]]:10} | {item[key[3]]:18} | {item[key[4]]}')  
    
def second_menu(text):
    return input(text)

def select_key(text: str) -> str:
    keys = init.get_main_db_keys()
    for i, item in enumerate(keys, 1):
        print(f'{i}. {item}')
    item = input(text)
    index = int(item) - 1
    return keys[index]

def data_cont() -> dict:
    keys = init.get_temp_db_keys()
    cont_data = {}
    print('Введите данные контакта:')
    for item in keys:
        cont_data[item] = input(item + ': ')
    return cont_data