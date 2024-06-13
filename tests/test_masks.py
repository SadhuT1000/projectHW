import pytest
from typing import List, Dict, Any
from src.masks import get_mask_card_number
from src.widget import mask_account_card,  get_data


@pytest.fixture
def cards():
    return 'Visa Platinum 7000 7922 8960 6361'

@pytest.fixture
def users():
    return 'Счет 73654108430135874305'


@pytest.fixture
def dates():
    return '2018-07-11T02:26:18.671407'

# def test_mask_account_card(cards):
#     assert mask_account_card(cards) == 'Visa Platinum 7000 79** **** 6361'



# def test_get_mask(cards):
#     assert get_mask_card_number(cards) == 'Visa Platinum 7000 79** **** 6361'
#     #assert get_mask_account(users) == 'Счет **4305'


@pytest.mark.parametrize('card, expected', [('Visa Platinum 7000 7922 8960 6361' ,'Visa Platinum 7000 79** **** 6361')])
def test_mask_card(card, expected):
    assert mask_account_card(card) == expected


# @pytest.mark.parametrize('date, expected', '2018-07-11T02:26:18.671407', '11.07.2018')
# def test_get_data(dates, expected):
#     assert get_data(dates) == expected