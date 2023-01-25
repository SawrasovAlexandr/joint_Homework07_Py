import view

def add_cont(database: list, contact: dict) -> list: 
    contact['ID'] = len(database)
    database.append(contact)
    return database
    
def del_cont(database: list, num_cont: int) -> list:
    print(f'Контакт: {database.pop(int(num_cont))} удален')
    return database

def edit_cont(database: list, num_cont: int) -> list:
    contact = view.data_cont()
    contact['ID'] = num_cont
    database[num_cont] = contact
    return database