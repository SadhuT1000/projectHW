# from typing import Union, Any, Optional
def filter_by_state(inform: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращающая список словарей с ключом который введешь"""

    new_list = []

    for k in inform:
        if k["state"] == state:
            new_list.append(k)

    return new_list


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "CANCELED",
    )
)


def sort_by_date(info: list[dict], date: bool = True) -> list[dict]:
    """Функция возврата отсортированных словарей по дате"""

    newlist = []

    if date is True:
        newlist = sorted(info, key=lambda d: d["date"], reverse=True)
    elif date is False:
        newlist = sorted(info, key=lambda d: d["date"], reverse=False)

    return newlist


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        False,
    )
)
