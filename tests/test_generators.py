from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


def test_filter_by_currency():
    gen = filter_by_currency(transactions, "USD")
    assert next(gen) == 939719570
    assert next(gen) == 142264268


def test_transaction_descriptions():

    gen2 = transaction_descriptions(transactions)
    assert next(gen2) == "Перевод организации"
    assert next(gen2) == "Перевод со счета на счет"
    assert next(gen2) == "Перевод со счета на счет"
    assert next(gen2) == "Перевод с карты на карту"
    assert next(gen2) == "Перевод организации"


def test_card_number_generator():

    gen3 = card_number_generator(start=1, end=5)
    assert next(gen3) == "0000 0000 0000 0001"
    assert next(gen3) == "0000 0000 0000 0002"
    assert next(gen3) == "0000 0000 0000 0003"
    assert next(gen3) == "0000 0000 0000 0004"
    assert next(gen3) == "0000 0000 0000 0005"
