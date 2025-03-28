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
density_dict = {
    "Water": 1.0,      # 1 kg/L
    "Ethanol": 0.789,  # kg/L
    "Oil": 0.92,       # kg/L
    "Mercury": 13.6    # kg/L
}

# Conversion functions
def pound_to_kg(pounds):
    return pounds * 0.453592

def kg_to_liter(kg, substance):
    """Convert kg to liter using substance density"""
    if substance in density_dict:
        return kg / density_dict[substance]
    else:
        return None  # Density not found

# Streamlit Interface
st.title("Chemical Caustic Soda Conversion App")
st.write("This app converts pounds of a substance into liters based on its density.")

# User Input
substance = st.selectbox("Select a substance:", list(density_dict.keys()))
pounds = st.number_input("Enter weight in pounds:", min_value=0.0, step=0.1)

# Conversion Logic
if pounds > 0:
    kg = pound_to_kg(pounds)
    liters = kg_to_liter(kg, substance)
    
    if liters is not None:
        st.write(f"{pounds} pound(s) of {substance} is equal to {liters:.3f} liters.")
    else:
        st.write(f"Density for {substance} not found.")
else:
    st.write("Please enter a valid weight.")


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


