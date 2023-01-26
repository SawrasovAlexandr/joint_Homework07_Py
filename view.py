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
    menu = input('   Выберите пункт меню: ')
    return menu

def show_database(data_base: list) -> None:
    os.system('cls')
    key = init.get_main_db_keys()
    id = 'ID'
    for i, item in enumerate(data_base):
        if i == 0:
            print(f'\033[1m\033[4m{id:>4} | {item[key[0]]:14} | {item[key[1]]:10} | {item[key[2]]:18} | {item[key[3]]}\033[0m')
        else: print(f'{i:>4} | {item[key[0]]:13} | {item[key[1]]:10} | {item[key[2]]:18} | {item[key[3]]}')  
    print()
    
def second_menu(text):
    return input(text)

def select_key(text: str) -> str:
    keys = init.get_main_db_keys()
    for i, item in enumerate(keys, 1):
        print(f'{i}. {item}')
    index = input(text)
    return keys[int(index) - 1] if index in ('1', '2', '3', '4') else ''

def data_cont() -> dict:
    keys = init.get_main_db_keys()
    cont_data = {}
    print('Введите данные контакта:')
    for item in keys:
        cont_data[item] = input(item + ': ')
    return cont_data