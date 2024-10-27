# TODO Напишите функцию для поиска индекса товара
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


def find_item(lst, item):
    return lst.index(item) if item in lst else None


for good in ['банан', 'груша', 'персик']:
    index_item = find_item(items_list, good)
    if index_item is not None:
        print(f"Первое вхождение товара '{good}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{good}' не найден в списке.")
