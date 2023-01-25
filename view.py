def main_menu():
    print('1. Показать справочник\n'
          '2. Поиск контактов\n'
          '3. Импорт базы данных\n'
          '4. Экспорт базы данных\n'
          '5. Добавить контакт\n'
          '6. Удалить контакт\n'
          '7. Редактировать контакт\n'
          '8. Выход')
    menu = input('Выберите пункт меню: ')
    return menu

def show_database(data_base):
    for item in data_base:
        item = list(item.values())
        print(f'{item[0]:4} | {item[1]:13} | {item[2]:10} | {item[3]:12} | {item[4]}')  
    


def second_menu(text):
    a = input(text)
    return(a)



def add_user():
    f_name = input('Введите имя: ')
    l_name = input('Введите фамилию: ')
    phonenum = input('Введите номер телефона: ')
    coment = input('Введите комментарий: ')
    user_dict = {'Фамилия': l_name, 'Имя': f_name,'Телефон': phonenum, 'Комментарий': coment}
    return user_dict
