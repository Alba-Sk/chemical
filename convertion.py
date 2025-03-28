#!/usr/bin/env python
# coding: utf-8

# Step 1: Set Up Your Environment
# Install necessary libraries

# In[1]:





# Step 2: Define the Conversion Logic
# Since pound to liter depends on density, we need a dictionary of densities for different chemicals.

# In[2]:


import pandas as pd

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


# Step 3: Test the Conversion Logic in Jupyter

# In[3]:


pounds = 1
substance = "Water"

kg = pound_to_kg(pounds)
liters = kg_to_liter(kg, substance)

print(f"{pounds} pound(s) of {substance} = {liters:.3f} liters")


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


