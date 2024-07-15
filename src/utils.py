import json
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="/Users/maksbolomoznov/PycharmProjects/pythonProjectHw/logs/utils.log",
    encoding="utf8",  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске

logger = logging.getLogger("utils.py")


def get_operations(path: str) -> list[dict]:
    """Функция возвращает данные о финансовых транзакциях"""

    logger.info(f"Получаем путь {path}")
    try:
        with open(path, encoding="utf-8") as operat:
            data = json.load(operat)
            logger.info("Открыли файл")

        if isinstance(data, list):
            logger.info("Если файл типа list то вернули его")
            return data

        else:
            logger.info("это не тот тип и возвращаю пустой список")
            return []

    except json.decoder.JSONDecodeError:
        print("Error decoding file")
        logger.warning("Ошибка декодирования вернул пустой список")
        return []
    except FileNotFoundError:
        print("File not found")
        logger.warning("Ошибка файл не найдет вернул пустой список")
        return []


if __name__ == "__main__":
    transactions = get_operations("../data/operations.json")

    if transactions:
        print("Список транзакций:")
        for transaction in transactions:
            print(transaction)
    else:
        print("Файл не найден, пустой или содержит некорректный JSON.")
