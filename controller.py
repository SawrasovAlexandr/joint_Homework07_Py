import init
import view
import find
import mod_imp
import mod_exp
import edit_db
import os
# def quit():
#     input('Нажмите клавишу для выхода в главное меню: ')

def clear() -> None:
    os.system('cls')

def ClickButton():
    path = 'database.csv'
    main_data = init.main_db(path)
    temp_data = init.temp_db(main_data)
    exit_db = True
    view.show_database(temp_data)
    while edit_db:
        num_menu = view.main_menu()
        if num_menu == '1':
            find_str = view.second_menu('Введите строку поиска: ')
            colomn_rey = view.select_key('Введите номер столбца: ')
            temp_data = find.find_cont(temp_data, find_str, colomn_rey)
            clear()
            view.show_database(temp_data)
        elif num_menu == '2':
            # colomn_rey = view.select_key('Введите номер столбца: ')
            # temp_data = find.sort_cont(temp_data, colomn_rey)
            clear()
            view.show_database(temp_data)
        elif num_menu == '3':
            main_data = edit_db.add_cont(main_data, view.add_user())
            clear()
            view.show_database(temp_data)
        elif num_menu == '4':
            num_cont = view.second_menu('Введите номер редактируемого контакта: ')
            main_data = edit_db.edit_cont(main_data, num_cont)
            clear()
            view.show_database(temp_data)
        elif num_menu == '5':
            num_cont = view.second_menu('Введите строку удаляемого контакта: ')
            main_data = edit_db.del_cont(main_data, num_cont)
            quit()
        elif num_menu == '6':
            path_file = view.second_menu('Выберите файл для импорта: ')
            if mod_imp.load_file(path_file):
                print('Ok')
            else:
                print('Not Ok')
            quit()
        elif num_menu == '7':
            file_name = view.second_menu('Выберите имя экспортируемого файла: ')
            mod_exp.unload_file(file_name)
            quit()
        elif num_menu == '8':
            exit_db = False
        

    

        



# def add_contact():
#     pass



