import init


def find_cont(data_base: list, find_str: str, find_key: str) -> None:
    data_base.pop(0)
    find_data = []
    if find_str:
        if find_key:
            for item in data_base:
                if find_str.lower() in item[find_key].lower():
                    find_data.append(item)
        else: 
            for item in data_base:
                if find_str.lower() in ' '.join(item.values()).lower():
                    find_data.append(item)
    else: find_data = data_base
    key = init.get_main_db_keys()
    id = 'ID'
    print(f'\033[1m\033[4m{id:>4} | {key[0]:13} | {key[1]:10} | {key[2]:18} | {key[3]}\033[0m')
    for item in find_data:
        i = data_base.index(item)
        print(f'{i + 1:>4} | {item[key[0]]:13} | {item[key[1]]:10} | {item[key[2]]:18} | {item[key[3]]}')
    print()
    

