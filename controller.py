import init
import view
import find
import mod_imp
import mod_exp
import edit_db

def quit():
    input('Нажмите клавишу для выхода в главное меню: ')



def ClickButton():
    path = 'database.csv'
    main_data = init.main_db(path)
    temp_data = init.temp_db(main_data)
    exit_db = True
    while edit_db:
        view.show_database(temp_data)
        num_menu = view.main_menu()
        if num_menu == '1':
            find_str = view.second_menu('Введите строку поиска: ')
            
            quit()
        elif num_menu == '2':
            
            find.find_cont(find_str, main_data)
            quit()
        elif num_menu == '3':
            path_file = view.second_menu('Выберите файл для импорта: ')
            if mod_imp.load_file(path_file):
                print('Ok')
            else:
                print('Not Ok')
            quit()
        elif num_menu == '4':
            file_name = view.second_menu('Выберите имя экспортируемого файла: ')
            mod_exp.unload_file(file_name)
            quit()
        elif num_menu == '5':
            main_data = edit_db.add_cont(main_data, view.add_user())
            quit()
        elif num_menu == '6':
            num_user = view.second_menu('Введите строку удаляемого контакта: ')
            main_data = edit_db.del_cont(main_data, num_user)
            quit()
        elif num_menu == '7':
            num_user = view.second_menu('Введите строку редактируемого контакта: ')
            main_data = edit_db.edit_cont(main_data, num_user)
            quit()
        elif num_menu == '8':
            exit_db = False
        

    

        



# def add_contact():
#     pass



