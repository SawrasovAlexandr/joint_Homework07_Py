
# возвращаем вырезку из базы
def find_cont(data_base: list, find_str: str, key: str) -> list:
    find_data = []
    if not find_str:
        if key:
            for item in data_base:
                if find_str.lower() in item[key].lower():
                    find_data.append(item)
        else: 
            for item in data_base:
                if find_str.lower() in ' '.join(item.values()).lower():
                    find_data.append(item)
    else: find_data = data_base
    return find_data

def sort_cont(data_base: list, key: str) -> list:
    pass