
# возвращаем вырезку из базы
def find_cont(find_str: str, data_base: list, key: str = '') -> list:
    find_data = []
    if key:
        for i, item in enumerate(data_base):
            if find_str.lower() in item[key].lower():
                item['ID'] = i
                find_data.append(item)
    else: 
        for i, item in enumerate(data_base):
            if find_str.lower() in ' '.join(item.values()).lower():
                item['ID'] = i
                find_data.append(item)
    return find_data

def sort_cont():
    pass