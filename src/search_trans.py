import re
import os
from collections import Counter
from src.utils import get_operations

list_transactions = get_operations(os.path.join("../data/operations.json"))
def search_transactions(file: list[dict], input_user: str) -> list[dict]:

    '''Функция, которая принимает список словарей с данными о банковских операциях
    и строку поиска, а возвращает список словарей, у которых в описании есть данная строка'''
    new_list = []
    for i in file:
        if 'description' in i and re.findall(input_user, i['description']):
            new_list.append(i)
    return new_list






def sort_transactions(file: list[dict], category: list) -> dict:

    '''Функция, которая возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории'''

    new = []
    for j in file:
        if 'description' in j and j['description'] in category:
            new.append(j['description'])

    return Counter(new)




if __name__ == "__main__":
    categories_operations = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
        "Перевод со счета на счет",
        "Открытие вклада",
    ]

    print(sort_transactions(list_transactions, categories_operations))

    input_user = input("Введите слово для поиска: ")
    print(search_transactions(list_transactions, input_user))
