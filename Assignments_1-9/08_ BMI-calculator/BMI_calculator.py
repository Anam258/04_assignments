import streamlit as st
import pandas as pd

# Title of the app
st.title("BMI Calculator")

# Input sliders for height and weight
height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

# Calculate BMI
bmi = weight / ((height / 100) ** 2)

# Display BMI result
st.write(f"**Your BMI is:** {bmi:.2f}")

# BMI Category Guide
st.markdown("### BMI Categories")
st.markdown("""
- **Underweight**: BMI less than 18.5  
- **Normal weight**: BMI between 18.5 and 24.9  
- **Overweight**: BMI between 25 and 29.9  
- **Obesity**: BMI 30 or greater
""")
