from typing import Any

from src.masks import get_mask_card_number

# def mask_account_card(nums: str) -> str:
#     """Функция возвращает строку с замаскированным номером карты/счета"""
#
#     if "Счет" in nums:
#         return get_mask_account(nums)
#
#     else:
#         cards = get_mask_card_number(nums[-16:])
#         new_card = nums.replace(nums[-16:], cards)
#         return new_card
#
#
# print(mask_account_card('Maestro 1596837868705199'))



# def mask_account_card(input_number: str) -> Any:
#     """Анализирует принятую строку на наличие информации о счете или карте
#     Формирует строку с Типом карты/Счетом + маска."""
#     if "Счет" in input_number:
#         account_number = int(input_number[-20:])
#         new_text = "Счет " + get_mask_account(account_number)
#     else:
#         card_number = int(input_number[-16:])
#         new_text = input_number[:-16] + get_mask_card_number(card_number)
#     return new_text


def get_data(date: str) -> str:
    """Функция преобразования даты"""

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


# print(get_data('2018-07-11T02:26:18.671407'))
