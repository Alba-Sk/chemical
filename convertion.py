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

def gal_to_liter(qty):
    # Gallons to Liters conversion
    return qty * 3.785411784

# Streamlit Interface
st.title("Chemical Caustic Soda Quantity Conversion App")
st.write("This app converts quantities of chemicals from one unit to another.")

# Input fields
qty = st.number_input("Enter Quantity (in Liter):", min_value=0.0, step=0.1)
from_unit = st.selectbox("Select the unit to convert from:", ['Liter', 'Gal'])
to_unit = st.selectbox("Select the unit to convert to:", ['Pound', 'Gal', 'Kg', 'DST', 'LMT', 'Liter'])

# Conversion logic
if qty > 0:
    if from_unit == 'Liter':
        if to_unit == 'Pound':
            converted_qty = liter_to_pound(qty)
        elif to_unit == 'Gal':
            converted_qty = liter_to_gal(qty)
        elif to_unit == 'Kg':
            converted_qty = liter_to_kg(qty)
        elif to_unit == 'DST':
            converted_qty = liter_to_dst(qty)
        elif to_unit == 'LMT':
            converted_qty = liter_to_lmt(qty)
        elif to_unit == 'Liter':
            converted_qty = liter_to_liter(qty)
        else:
            converted_qty = None
    elif from_unit == 'Gal':
        if to_unit == 'Liter':
            converted_qty = gal_to_liter(qty)
        else:
            converted_qty = None

    if converted_qty is not None:
        st.write(f"{qty} {from_unit} is equal to {converted_qty:.5f} {to_unit}.")
    else:
        st.write("Conversion not defined for the selected units.")
else:
    st.write("Please enter a valid quantity.")



