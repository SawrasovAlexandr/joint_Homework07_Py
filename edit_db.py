def add_cont(database, user_dict):
    database.append(user_dict)
    return database
    
def del_cont(database, num_str):
    print(f'Контакт: {database.pop(int(num_str))} удален')
    return database

def edit_cont(database, num_str):
    pass
    return database