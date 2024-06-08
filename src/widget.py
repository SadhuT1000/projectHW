import masks


def mask_account_card(nums: str) -> str:
    """Функция возвращает строку с замаскированным номером карты/счета"""

    if "Счет" in nums:
        return masks.get_mask_account(nums)

    else:
        cards = masks.get_mask_card_number(nums[-16:])
        new_card = nums.replace(nums[-16:], cards)
        return new_card


#print(mask_account_card('Maestro 1596837868705199'))


def get_data(date: str) -> str:
    """Функция преобразования даты"""

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


#print(get_data('2018-07-11T02:26:18.671407'))
