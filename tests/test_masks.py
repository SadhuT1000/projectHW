from typing import Any, Dict, List

import pytest

from src.masks import get_mask_card_number
from src.widget import get_data


@pytest.fixture
def cards():
    return "Visa Platinum 7000 7922 8960 6361"


@pytest.fixture
def users():
    return "Счет 73654108430135874305"


@pytest.fixture
def dates():
    return "2018-07-11T02:26:18.671407"


# def test_mask_account_card(cards):
#     assert mask_account_card(cards) == 'Visa Platinum 7000 79** **** 6361'


# def test_get_mask(cards):
#     assert get_mask_card_number(cards) == 'Visa Platinum 7000 79** **** 6361'
#     #assert get_mask_account(users) == 'Счет **4305'


@pytest.mark.parametrize(
    "x, expected",
    [
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000 7922 8960 6361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_card(x, expected):
    assert get_mask_card_number(x) == expected
    # with pytest.raises(ValueError):
    #     assert get_mask_card_number(" ")
    with pytest.raises(ValueError):
        assert get_mask_card_number(card_number="")


# @pytest.mark.parametrize('date, expected', '2018-07-11T02:26:18.671407', '11.07.2018')
# def test_get_data(dates, expected):
#     assert get_data(dates) == expected


def test_dated(dates):
    assert get_data(dates) == "11.07.2018"
