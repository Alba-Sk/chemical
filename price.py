# !/usr/bin/env python
# coding: utf-8

# Step 1: Set Up Your Environment
# Install necessary libraries

# Step 2: Define the Conversion Logic

# Define conversion functions for different units
def liter_to_pound(price):
    return (1 * price) / (((1 / 3.78541) * 12.76))

def liter_to_gal(price):  # Liter to Gallons conversion
    return (1 * price) / (1 / 3.785411784)

def liter_to_kg(price):    
    return (1 * price) / (((1 / 3.78541) * 12.76) / 2.2046)

def liter_to_dst(price):  # Liter to DST conversion
    return (((1 * price)) / (((1 / 3.78541) * 12.76) / 2000)) * 2  

def liter_to_lmt(price):  # Liter to LMT conversion
    return (((1 * price)) / (((1 / 3.78541) * 12.76) / 2204.62)) * 2

def liter_to_liter(price):  # Liter to Liter conversion (no change, just return the same quantity)
    return price

# Gallons conversion
def gal_to_liter(price):   
    return (1 * price) / (1 * 3.785411784)

def gal_to_pound(price):
    return (1 * price) / (1 * 12.76)

def gal_to_kg(price):
    return (1 * price) / ((1 * 12.76) / 2.20462)

def gal_to_dst(price):
    return (1 * price) / (1 * (12.76 / 2000)) * 2

def gal_to_lmt(price):
    return ((1 * price) / (1 * (12.76 / 2204.62))) * 2

def gal_to_gal(price):
    return price

# DST conversion
def dst_to_liter(price):   
    return (1 * price) / (((1 * 2000) / 12.76) * 3.785411784) * 0.5

def dst_to_pound(price):
    return (1 * price) / (1 * 2000) * 0.5

def dst_to_kg(price):
    return (1 * price) / (1 * (2000 / 2.20462)) * 0.5   

def dst_to_dst(price):
    return price

def dst_to_lmt(price):
    return (1 * price) / ((1 * 2000) / 2204.62)

def dst_to_gal(price):
    return (1 * price) / (1 * (2000 / 12.76)) * 0.5

# Kg conversion- need to check
def kg_to_liter(price):   
    return 0

def kg_to_pound(price):
    return 0

def kg_to_kg(price):
    return price

def kg_to_dst(price):
    return 0

def kg_to_lmt(price):
    return 0

def kg_to_gal(price):
    return 0

# Pound conversion
def pound_to_liter(price):   
    return (1 * price) / ((1 / 12.76) * 3.785411784)

def pound_to_pound(price):
    return price

def pound_to_kg(price):
    return (1 * price) / (1 / 2.20462)

def pound_to_dst(price):
    return ((1 * price) / (1 / 2000)) * 2  # Fixed missing parenthesis

def pound_to_lmt(price):
    return ((1 * price) / (1 / 2204.62)) * 2  # Fixed missing parenthesis

def pound_to_gal(price):
    return (1 * price) / (1 / 12.76)


# Conversion function that uses the above-defined functions
def convert_price(price, from_unit, to_unit):
    # Define a dictionary to map the units to their respective conversion functions
    conversion_map = {
        ('Liter', 'Pound'): liter_to_pound,
        ('Liter', 'Gal'): liter_to_gal,
        ('Liter', 'Kg'): liter_to_kg,
        ('Liter', 'DST'): liter_to_dst,
        ('Liter', 'LMT'): liter_to_lmt,
        ('Liter', 'Liter'): liter_to_liter,

        ('Gal', 'Liter'): gal_to_liter,
        ('Gal', 'Pound'): gal_to_pound,
        ('Gal', 'Kg'): gal_to_kg,
        ('Gal', 'DST'): gal_to_dst,
        ('Gal', 'LMT'): gal_to_lmt,
        ('Gal', 'Gal'): gal_to_gal,

        ('DST', 'Liter'): dst_to_liter,
        ('DST', 'Pound'): dst_to_pound,
        ('DST', 'Kg'): dst_to_kg,
        ('DST', 'DST'): dst_to_dst,
        ('DST', 'LMT'): dst_to_lmt,
        ('DST', 'Gal'): dst_to_gal,

        ('Kg', 'Liter'): kg_to_liter,
        ('Kg', 'Pound'): kg_to_pound,
        ('Kg', 'Kg'): kg_to_kg,
        ('Kg', 'DST'): kg_to_dst,
        ('Kg', 'LMT'): kg_to_lmt,
        ('Kg', 'Gal'): kg_to_gal,

        ('Pound', 'Liter'): pound_to_liter,
        ('Pound', 'Pound'): pound_to_pound,
        ('Pound', 'Kg'): pound_to_kg,
        ('Pound', 'DST'): pound_to_dst,
        ('Pound', 'LMT'): pound_to_lmt,
        ('Pound', 'Gal'): pound_to_gal,

        ('LMT', 'Liter'): kg_to_liter,  # You need to define these LMT conversions if they're used
        ('LMT', 'Pound'): kg_to_pound,
        ('LMT', 'Kg'): kg_to_kg,
        ('LMT', 'DST'): kg_to_dst,
        ('LMT', 'LMT'): kg_to_lmt,
        ('LMT', 'Gal'): kg_to_gal,
    }

    # Get the conversion function based on the provided units
    conversion_func = conversion_map.get((from_unit, to_unit))

    # If conversion function exists, apply it
    if conversion_func:
        return conversion_func(price)
    else:
        return None  # Invalid conversion
