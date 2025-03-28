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

# Define densities for different substances (example values)
conversion_factors = {
    'Liter_to_Pound': ((1/3.785411784)*12.76),    # DST to Kg (assuming DST is equivalent to Liters for now)
    'Liter_to_Gal':1/3.785411784,  # Pounds to Kilograms
    'Liter_to_Kg': ((1/3.78541)*12.76)/2.2046,  # Gallons to Liters
    'Liter_to_DST': ((1/3.78541)*12.76)/2000,  # Assume 1 Kg is equivalent to 1 Liter for simplicity, adjust based on substance
    'Liter_to_LMT': (((1/3.78541)*12.76))/2204.62,  # Pounds to Liters based on density of water (adjust for other chemicals)
    'Liter_to_Liter': 1*1,    # LMT to Kg (for example purposes, adjust as per the substance)
    'Gal_to_Liter':1*3.785411784
    
    
}
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


