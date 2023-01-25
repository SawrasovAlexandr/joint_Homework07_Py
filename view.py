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

def show_database(data_base):
    os.system('cls')
    for item in data_base:
        item = list(item.values())
        print(f'{item[0]:4} | {item[1]:13} | {item[2]:10} | {item[3]:12} | {item[4]}')  
    
def second_menu(text):
    return input(text)

def select_key(text: str) -> str:
    keys = init.get_main_db_keys()
    for i, item in enumerate(keys, 1):
        print(f'{i}. {item}')
    index = int(input(text)) - 1
    return keys[index] if index in range(len(keys)) else ''

def data_cont() -> dict:
    keys = init.get_main_db_keys()
    cont_data = {}
    print('Введите данные контакта:')
    for item in keys:
        cont_data[item] = input(item)
    return cont_data