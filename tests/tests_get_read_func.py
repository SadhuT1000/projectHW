import os
from unittest.mock import patch
from src.get_read_func import get_csv, get_exel


@patch("csv.DictReader")
def test_get_data_from_csv(mock_reader):
    mock_reader.return_value = iter(
        [
            ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"],
            [
                "650703",
                "EXECUTED",
                "2023-09-05T11:30:32Z",
                "16210",
                "SoL",
                "PEN",
                "Счет 58803664651298323391",
                "Счет 39746506635466619397",
                "Перевод организации",
            ],
        ]
    )

    result = get_csv(os.path.join("../data/transactions.csv"))
    expected_result = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "SoL",
            "currency_code": "PEN",
            "from": "Счет 58803664651298323391",
            "to": "Счет 39746506635466619397",
            "description": "Перевод организации",
        }
    ]
    assert result == expected_result


@patch("pandas.read_exel")
def test_get_exel(mock_reader_ex):
    mock_reader_ex.return_value = iter(
        [
            ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"],
            [
                "650703",
                "EXECUTED",
                "2023-09-05T11:30:32Z",
                "16210",
                "SoL",
                "PEN",
                "Счет 58803664651298323391",
                "Счет 39746506635466619397",
                "Перевод организации",
            ],
        ]
    )
    result = get_exel(os.path.join("../data/transactions.csv"))
    expected_result = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "SoL",
            "currency_code": "PEN",
            "from": "Счет 58803664651298323391",
            "to": "Счет 39746506635466619397",
            "description": "Перевод организации",
        }
    ]
