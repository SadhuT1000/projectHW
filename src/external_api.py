
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_transaction(transaction: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    """

    amount = float(transaction["amount"])
    currency = transaction["currency"]

    if currency == "RUB":
        return amount

    elif currency == "USD" or currency == "EUR":

        api_key = os.getenv("API_KEY")

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        return float(data["result"])

    else:
        raise ValueError(f"Я не в курсе такой валюты' {currency}.")


if __name__ == "__main__":
    transaction1 = {"amount": 150, "currency": "RUB"}
    transaction2 = {"amount": 300, "currency": "USD"}
    transaction3 = {"amount": 100, "currency": "EUR"}

    amount_in_rubles1 = get_transaction(transaction1)
    amount_in_rubles2 = get_transaction(transaction2)
    amount_in_rubles3 = get_transaction(transaction3)

    print(f"Сумма в рублях (RUB): {amount_in_rubles1}")
    print(f"Сумма в рублях (USD): {amount_in_rubles2}")
    print(f"Сумма в рублях (EUR): {amount_in_rubles3}")
#
