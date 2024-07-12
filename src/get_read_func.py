import csv

import pandas as pd


def get_csv(file: str) -> list[dict]:
    """Функция чтения CSV файла и превобразование его в список словарей"""

    with open(file, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        result = []
        for row in reader:
            result.append(row)

    return result


def get_exel(file: str) -> list[dict]:
    """Функция тения EXCEL файла и превобразование его в список словарей"""

    df = pd.read_excel(file)
    df_dict = df.to_dict("records")

    return df_dict


if __name__ == "__main__":

    print(get_csv("../data/transactions.csv"))
    print(get_exel("../data/transactions_excel.xlsx"))
