import view
import init

def add_cont(database: list, contact: dict) -> list: 
    database.append(contact)
    
def del_cont(database: list, num_cont: int) -> list:
    print(f'Контакт: {database.pop(int(num_cont))} удален')

def edit_cont(database: list, num_cont: int) -> list:
    key = init.get_main_db_keys()
    contact = view.data_cont()
    for item in key:
        if contact[item]:
            database[num_cont][item] = contact[item]

def sort_cont(data_base: list, sort_key: str):
    if sort_key:
        head = data_base.pop(0)
        data_base.sort(key=lambda item: item[sort_key])
        data_base.insert(0, head)
