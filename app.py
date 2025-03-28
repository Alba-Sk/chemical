# app.py
import streamlit as st
from convertion import convert_units  # Import unit conversion function
from price import convert_price      # Import price conversion function

# Streamlit Interface
st.title("Chemical Quantity and Price Conversion App")
st.write("This app converts quantities and prices from one unit to another.")

# Quantity Conversion Section
st.header("Quantity Conversion")
qty = st.number_input("Enter Quantity:", min_value=0.0, step=0.1)
from_unit = st.selectbox("Select the unit to convert from:", ['Liter', 'Gal', 'DST', 'Kg', 'Pound', 'LMT'])
to_unit = st.selectbox("Select the unit to convert to:", ['Liter', 'Gal', 'DST', 'Kg', 'Pound', 'LMT'])

if qty > 0:
    converted_qty = convert_units(qty, from_unit, to_unit)
    if converted_qty is not None:
        st.write(f"{qty} {from_unit} is equal to {converted_qty:.3f} {to_unit}.")
    else:
        st.write("Conversion not defined for the selected units.")
else:
    st.write("Please enter a valid quantity.")
    
--------------
# Price Conversion Section
st.header("Price Conversion $/UOM")

price_per_unit = st.number_input("Enter price per unit:", min_value=0.0)

# Input for units
from_unit_price = st.selectbox("Select the unit of the price you're entering:", ["Pound", "Gal", "Kg", "DST", "LMT", "Liter"])
to_unit_price = st.selectbox("Select the unit to convert to:", ["Pound", "Gal", "Kg", "DST", "LMT", "Liter"])

# Check if price is greater than 0 and perform conversion
if price_per_unit > 0:
    converted_price = convert_price(price_per_unit, from_unit_price, to_unit_price)
    if converted_price is not None:
        st.write(f"{price_per_unit} {from_unit_price} per unit is equal to {converted_price:.3f} {to_unit_price} per unit.")
    else:
        st.write("Price conversion not defined for the selected units.")
else:
    st.write("Please enter a valid price.")
