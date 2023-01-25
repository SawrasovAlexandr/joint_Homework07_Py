import view

def add_cont(database: list, contact: dict) -> list: 
    database.append(contact)
    return database
    
def del_cont(database: list, num_cont: int) -> list:
    print(f'Контакт: {database.pop(int(num_cont))} удален')
    return database

def edit_cont(database: list, num_cont: int) -> list:
    database[num_cont] = view.data_cont()
    return database