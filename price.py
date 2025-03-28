# price.py

def convert_price(price, from_currency, to_currency):
    exchange_rates = {
        "USD": {"EUR": 0.91, "GBP": 0.78},
        "EUR": {"USD": 1.1, "GBP": 0.86},
        "GBP": {"USD": 1.28, "EUR": 1.16},
    }
    if from_currency == to_currency:
        return price
    try:
        return price * exchange_rates[from_currency][to_currency]
    except KeyError:
        return None
