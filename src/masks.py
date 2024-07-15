import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="/Users/maksbolomoznov/PycharmProjects/pythonProjectHw/logs/utils.log",
    encoding="utf8",  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске

auth_logger = logging.getLogger("app.masks")


def get_mask_card_number(card_number: str) -> str | None:
    """
    Функция принимает на вход номер кредитной карты в виде строки и возвращает строку с маскированным номером.
    """
    auth_logger.info(f"Воод номера карты или счёта {card_number}")

    card_number = str(card_number)
    if "Visa Classic" in card_number:
        masked_number = card_number[:17] + " " + card_number[18:20] + "** **** " + card_number[-4:]
        auth_logger.debug("Карта Visa Classic успешно")
        return masked_number
    elif "Visa Platinum" in card_number:
        masked_number = card_number[:18] + " " + card_number[19:21] + "** **** " + card_number[-4:]
        auth_logger.debug("Карта Visa Platinum успешно")
        return masked_number
    elif "Visa Gold" in card_number:
        masked_number = card_number[:14] + " " + card_number[15:17] + "** **** " + card_number[-4:]
        auth_logger.debug("Карта Visa Gold успешно")
        return masked_number
    elif "Maestro" in card_number:
        masked_number = card_number[:12] + " " + card_number[13:15] + "** **** " + card_number[-4:]
        auth_logger.debug("Карта Maestro успешно")
        return masked_number
    elif "MasterCard" in card_number:
        masked_number = card_number[:16] + " " + card_number[16:18] + "** **** " + card_number[-4:]
        auth_logger.debug("Карта MasterCard успешно")
        return masked_number
    elif "Maestro" in card_number:
        masked_number = card_number[:12] + " " + card_number[13:15] + "** **** " + card_number[-4:]
        auth_logger.debug("Карта Maestro успешно")
        return masked_number
    elif "Счет" in card_number:
        masked_account = card_number[:4] + " " + "**" + card_number[-4:]
        auth_logger.debug("Ввод счёта, успешно")
        return masked_account
    elif card_number == "":
        raise ValueError
        auth_logger.warning("Ошибка ввода")
    return None


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))

    print(get_mask_card_number(70007922896063615674))

    get_mask_card_number(654583)
