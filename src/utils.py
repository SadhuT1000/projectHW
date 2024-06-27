import json


def get_operations(path: str) -> list[dict]:
    """Функция возвращает данные о финансовых транзакциях"""

    try:
        with open(path, encoding="utf-8") as operat:
            data = json.load(operat)

        if isinstance(data, list):
            return data

        else:
            return []

    except json.decoder.JSONDecodeError:
        print("Error decoding file")
        return []
    except FileNotFoundError:
        print("File not found")
        return []


if __name__ == "__main__":
    transactions = get_operations("../data/operations.json")

    if transactions:
        print("Список транзакций:")
        for transaction in transactions:
            print(transaction)
    else:
        print("Файл не найден, пустой или содержит некорректный JSON.")
