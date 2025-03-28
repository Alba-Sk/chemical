#!/usr/bin/env python
# coding: utf-8

# Step 1: Set Up Your Environment
# Install necessary libraries

# In[1]:





# Step 2: Define the Conversion Logic
# Since pound to liter depends on density, we need a dictionary of densities for different chemicals.

# In[2]:


#!/usr/bin/env python
# coding: utf-8

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
st.title("Chemical Quantity Conversion App")
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
        st.write(f"{qty} {from_unit} is equal to {converted_qty:.3f} {to_unit}.")
    else:
        st.write("Conversion not defined for the selected units.")
else:
    st.write("Please enter a valid quantity.")
# Conversion functions
def convert_units(qty, from_unit, to_unit):
    """Convert quantity from one unit to another using conversion factors."""
    if from_unit == to_unit:
        return qty  # No conversion needed if the units are the same

    conversion_key = f"{from_unit}_to_{to_unit}"
    if conversion_key in conversion_factors:
        return qty * conversion_factors[conversion_key]
    else:
        return None  # Conversion not defined

# Streamlit Interface
st.title("Chemical Quantity Conversion App")
st.write("This app converts quantities of chemicals from one unit to another.")

# Input fields
qty = st.number_input("Enter Quantity:", min_value=0.0, step=0.1)
from_unit = st.selectbox("Select the unit to convert from:", ['DST', 'Liter', 'Kg', 'Gal', 'Pound', 'LMT'])
to_unit = st.selectbox("Select the unit to convert to:", ['DST', 'Liter', 'Kg', 'Gal', 'Pound', 'LMT'])

# Conversion logic
if qty > 0:
    converted_qty = convert_units(qty, from_unit, to_unit)
    
    if converted_qty is not None:
        st.write(f"{qty} {from_unit} is equal to {converted_qty:.3f} {to_unit}.")
    else:
        st.write("Conversion not defined for the selected units.")
else:
    st.write("Please enter a valid quantity.")

# Step 4: Build a Simple UI with Streamlit
# Now that we have the logic, we’ll create a Streamlit UI with dropdowns and input fields.

# Step 2: Initialize Git in Your Local Folder
# Open VS Code Terminal (Jupyter Notebook is fine, but Git commands are easier in the terminal).
# 
# Navigate to your project folder:

# In[ ]:


# import os

# Set the working directory to your project folder
# os.chdir(r"C:\Users\Albana\OneDrive\Desktop\dc\DS\chemical")


# In[ ]:


# on the terminal run:
# Initialize Git:
# git init
# git add .
# Connect GitHub Repo
# git commit -m "Initial commit - Streamlit Unit Converter"
# git remote add origin https://github.com/alba-sk/chemical.git
# git push -u origin main
import streamlit as st

st.title("Chemical Caustic soda Streamlit App")
st.write("Welcome!")


