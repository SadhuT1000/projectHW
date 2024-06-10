def get_mask_card_number(num: str) -> str:
    """Функция принимающая номер карты и возвращающаяя ее маску"""
    # num_str = str(num)
    new = num[:4] + " " + num[4:6] + "**" + " " + "****" + " " + num[-4:]

    return new


# print(get_mask_card_number(str(7000792289606361)))


def get_mask_account(num2: str) -> str:
    """Функция принимающая номер карты и возвращающаяя ее маску"""

    # num2_str = str(num2)
    new2 = "**" + num2[-4:]

    return new2


# print(get_mask_account(str(73654108430135874305)))
