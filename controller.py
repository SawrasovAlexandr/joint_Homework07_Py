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
    while exit_db:
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
            temp_data = edit_db.add_cont(temp_data, view.data_cont())
            clear()
            view.show_database(temp_data)
        elif num_menu == '4':
            num_cont = view.second_menu('Введите номер редактируемого контакта: ')
            temp_data = edit_db.edit_cont(temp_data, int(num_cont))
            clear()
            view.show_database(temp_data)
        elif num_menu == '5':
            num_cont = view.second_menu('Введите номер удаляемого контакта: ')
            temp_data = edit_db.del_cont(temp_data, int(num_cont))
            clear()
            view.show_database(temp_data)
        elif num_menu == '6':
            path_file = view.second_menu('Введите имя файл для импорта: ')
            temp_data = mod_imp.load_file(path_file, temp_data)
            clear()
            view.show_database(temp_data)
        elif num_menu == '7':
            file_name = view.second_menu('Выберите имя файла для экспорта: ')
            mod_exp.unload_file(file_name, temp_data)
            clear()
            view.show_database(temp_data)
        elif num_menu == '8':
            exit_db = False
        

    

        



# def add_contact():
#     pass



