#!/usr/bin/env python
# coding: utf-8

# Step 1: Set Up Your Environment
# Install necessary libraries


# Step 2: Define the Conversion Logic

import pandas as pd
import streamlit as st

# Define conversion functions for different units
def liter_to_pound(qty):
    # Example conversion for Liter to Pound based on custom formula
    return (qty / 3.785411784) * 12.76

def liter_to_gal(qty):
    # Liter to Gallons conversion
    return qty / 3.785411784

def liter_to_kg(qty):
    # Liter to Kg based on the formula provided
    return ((qty / 3.78541) * 12.76) / 2.2046

def liter_to_dst(qty):
    # Liter to DST conversion
    return ((qty / 3.78541) * 12.76) / 2000

def liter_to_lmt(qty):
    # Liter to LMT conversion
    return ((qty / 3.78541) * 12.76) / 2204.62

def liter_to_liter(qty):
    # Liter to Liter conversion (no change, just return the same quantity)
    return qty
 # Gallons conversion
def gal_to_liter(qty):   
    return qty * 3.785411784
def gal_to_pound(qty):
    return qty * 12.76
def gal_to_kg(qty):
    return (qty * 12.76 ) / 2.20462
def gal_to_dst(qty):
    return qty * (12.76/2000)
def gal_to_lmt(qty):
    return (qty * 12.76 ) / 2204.62
def gal_to_gal(qty):
    return qty
 # DST conversion
def dst_to_liter(qty):   
    return ((qty * 2000)/12.76)*3.785411784
def dst_to_pound(qty):
    return qty * 2000
def dst_to_kg(qty):
    return qty * (2000/2.20462)
def dst_to_dst(qty):
    return qty
def dst_to_lmt(qty):
    return (qty * 2000)/2204.62
def dst_to_gal(qty):
    return qty *(2000/12.76)

 # DST conversion
def kg_to_liter(qty):   
    return qty *(2.20462/12.76)*3.785411784
def kg_to_pound(qty):
    return qty *2.20462
def kg_to_kg(qty):
    return qty
def kg_to_dst(qty):
    return (qty *2.20462)/2000
def kg_to_lmt(qty):
    return (qty * 2.20462)/2204.62
def kg_to_gal(qty):
    return (qty *2.20462)/12.76


 # Pound conversion
def pound_to_liter(qty):   
    return ((qty /12.76)*3.785411784)
def pound_to_pound(qty):
    return qty
def pound_to_kg(qty):
    return qty /2.20462    
def pound_to_dst(qty):
    return qty /2000
def pound_to_lmt(qty):
    return qty /2204.62
def pound_to_gal(qty):
    return qty / 12.76

 # Pound conversion
def lmt_to_liter(qty):   
    return ((qty *2204.62)/12.76)*3.785411784
def lmt_to_pound(qty):
    return qty * 2204.62    
def lmt_to_kg(qty):
    return qty *(2204.62/2.20462)
def lmt_to_dst(qty):
    return (qty *2204.62)/2000
def lmy_to_lmt(qty):
    return qty 
def lmt_to_gal(qty):
    return (qty * 2204.62)/12.76




# Conversion function that uses the above-defined functions
def convert_units(qty, from_unit, to_unit):
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

        ('LMT', 'Liter'): lmt_to_liter,
        ('LMT', 'Pound'): lmt_to_pound,
        ('LMT', 'Kg'): lmt_to_kg,
        ('LMT', 'DST'): lmt_to_dst,
        ('LMT', 'LMT'): lmt_to_lmt,
        ('LMT', 'Gal'): lmt_to_gal,
    }

    # Get the conversion function based on the provided units
    conversion_func = conversion_map.get((from_unit, to_unit))

    # If conversion function exists, apply it
    if conversion_func:
        return conversion_func(qty)
    else:
        return None  # Invalid conversion


# Streamlit Interface
st.title("Chemical Quantity Conversion App")
st.write("This app converts quantities of chemicals from one unit to another.")

# Input fields
qty = st.number_input("Enter Quantity:", min_value=0.0, step=0.1)
from_unit = st.selectbox("Select the unit to convert from:", ['Liter', 'Gal', 'DST', 'Kg', 'Pound', 'LMT'])
to_unit = st.selectbox("Select the unit to convert to:", ['Liter', 'Gal', 'DST', 'Kg', 'Pound', 'LMT'])

# Conversion logic
if qty > 0:
    converted_qty = convert_units(qty, from_unit, to_unit)

    if converted_qty is not None:
        st.write(f"{qty} {from_unit} is equal to {converted_qty:.3f} {to_unit}.")
    else:
        st.write("Conversion not defined for the selected units.")
else:
    st.write("Please enter a valid quantity.")



