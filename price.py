# price.py

# Example static currency conversion rates (you can update these as needed)
currency_rates = {
    'USD': {'EUR': 0.85, 'GBP': 0.75},
    'EUR': {'USD': 1.18, 'GBP': 0.88},
    'GBP': {'USD': 1.33, 'EUR': 1.14},
}

def convert_price(price_per_unit, from_unit, to_unit):
    # Check if conversion rate exists between the selected currencies
    if from_unit in currency_rates and to_unit in currency_rates[from_unit]:
        conversion_rate = currency_rates[from_unit][to_unit]
        converted_price = price_per_unit * conversion_rate
        return converted_price
    else:
        return None  # Invalid conversion
