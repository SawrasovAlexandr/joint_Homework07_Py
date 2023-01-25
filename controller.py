import view
import find
import mod_imp
import mod_exp
import edit_db


def click_button():
    path = 'database.csv'
    exit_db = True
    view.show_database(main_data)
    while exit_db:
        num_menu = view.main_menu()
        if num_menu == '1':
            find_str = view.second_menu('Введите строку поиска: ')
            colomn_rey = view.select_key('Введите номер столбца: ')
            main_data = find.find_cont(main_data, find_str, colomn_rey)
            view.show_database(main_data)
        elif num_menu == '2':
            # colomn_rey = view.select_key('Введите номер столбца: ')
            # temp_data = find.sort_cont(temp_data, colomn_rey)
            view.show_database(main_data)
        elif num_menu == '3':
            main_data = edit_db.add_cont(main_data, view.data_cont())
            view.show_database(main_data)
        elif num_menu == '4':
            num_cont = view.second_menu('Введите номер редактируемого контакта: ')
            main_data = edit_db.edit_cont(main_data, int(num_cont))
            view.show_database(main_data)
        elif num_menu == '5':
            num_cont = view.second_menu('Введите номер удаляемого контакта: ')
            main_data = edit_db.del_cont(main_data, int(num_cont))
            view.show_database(main_data)
        elif num_menu == '6':
            path_file = view.second_menu('Введите имя файл для импорта: ')
            main_data = mod_imp.load_file(path_file, main_data)
            view.show_database(main_data)
        elif num_menu == '7':
            file_name = view.second_menu('Выберите имя файла для экспорта: ')
            mod_exp.unload_file(file_name, main_data)
            view.show_database(main_data)
        elif num_menu == '8':
            mod_exp.unload_file(path, main_data)
            view.show_database(main_data)
        elif num_menu == '9':
            main_data = mod_imp.load_file(path)
            view.show_database(main_data)
        elif num_menu == '0':
            exit_db = False
        
