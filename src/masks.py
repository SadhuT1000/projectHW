def get_mask_card_number(card_number: str) -> str | None:
    """
    Функция принимает на вход номер кредитной карты в виде строки и возвращает строку с маскированным номером.
    """

    #   Проверяем тип карты
    if "Visa Classic" in card_number:
        masked_number = card_number[:17] + " " + card_number[18:20] + "** **** " + card_number[-4:]
        return masked_number
    elif "Visa Platinum" in card_number:
        masked_number = card_number[:18] + " " + card_number[19:21] + "** **** " + card_number[-4:]
        return masked_number
    elif "Visa Gold" in card_number:
        masked_number = card_number[:14] + " " + card_number[15:17] + "** **** " + card_number[-4:]
        return masked_number
    elif "Maestro" in card_number:
        masked_number = card_number[:12] + " " + card_number[13:15] + "** **** " + card_number[-4:]
        return masked_number
    elif "MasterCard" in card_number:
        masked_number = card_number[:16] + " " + card_number[16:18] + "** **** " + card_number[-4:]
        return masked_number
    elif "Maestro" in card_number:
        masked_number = card_number[:12] + " " + card_number[13:15] + "** **** " + card_number[-4:]
        return masked_number
    elif "Счет" in card_number:
        masked_account = card_number[:4] + " " + "**" + card_number[-4:]
        return masked_account
    elif " ":
        raise ValueError
    return None
