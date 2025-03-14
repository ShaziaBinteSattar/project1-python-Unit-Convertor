import streamlit as st

# Title
st.title("🔄 Google Unit Converter")

# Supported conversion categories
categories = {
    "Length": {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254},
    "Weight": {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495, "Ton": 1000},
    "Temperature": {"Celsius": 1, "Fahrenheit": "F", "Kelvin": "K"},
    "Speed": {"Meter/Second": 1, "Kilometer/Hour": 0.277778, "Miles/Hour": 0.44704, "Feet/Second": 0.3048}
}

# Dropdown for category selection
category = st.selectbox("Select Conversion Type", list(categories.keys()))

# Dropdowns for units
units = list(categories[category].keys())
from_unit = st.selectbox("Convert From", units)
to_unit = st.selectbox("Convert To", units)

# Input field for value
value = st.number_input(f"Enter value in {from_unit}")

# Conversion logic
def convert(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        else:
            return value  # Same unit
    else:
        return value * (categories[category][to_unit] / categories[category][from_unit])

# Convert and display result
if st.button("Convert"):
    result = convert(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
