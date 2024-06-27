import json
from unittest.mock import patch

from src.utils import get_operations


@patch("builtins.open")
def test_get_operations(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value

    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_operations("test.json") == [{"test": "test"}]

    mock_file.read.return_value = json.dumps({})
    assert get_operations("test.json") == []

    mock_file.read.return_value = json.dumps("test")
    assert get_operations("test.json") == []

    mock_file.read.return_value = ""
    assert get_operations("test.json") == []
