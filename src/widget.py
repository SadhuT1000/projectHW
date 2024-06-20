def get_data(date: str) -> str:
    """Функция преобразования даты"""

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


# print(get_data('2018-07-11T02:26:18.671407'))
