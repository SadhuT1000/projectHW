import unittest
from unittest.mock import patch

from src.external_api import get_transaction


@patch("requests.get")
def test_get_transaction_amount_in_rubles_rub(mock_get):
    transaction = {"amount": 150, "currency": "RUB"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 100}
    assert get_transaction(transaction) == 150


@patch("requests.get")
def test_get_transaction_amount_in_rubles_usd(mock_get):
    transaction = {"amount": 300, "currency": "USD"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 4340.0814}
    assert get_transaction(transaction) == 26371.2786


@patch("requests.get")
def test_get_transaction_amount_in_rubles_eur(mock_get):
    transaction = {"amount": 100, "currency": "EUR"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 13974.2193}
    assert get_transaction(transaction) == 9540.8066


@patch("requests.get")
def test_get_transaction_amount_in_rubles_unknown_currency(mock_get):
    transaction = {"amount": 100, "currency": "INR"}
    with unittest.TestCase().assertRaises(ValueError) as context:
        get_transaction(transaction)
        assert "Неизвестная валюта INR." in str(context.exception)
