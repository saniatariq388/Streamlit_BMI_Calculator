import streamlit as st
import pandas as pd
import random
import time

st.title("BMI Calculator")

height = st.slider("Enter your height  (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight  (in kg):", 40, 200, 70)

bmi = weight / ((height/100) ** 2)


# # Show confetti effect if the BMI is calculated
if bmi:
#     st.balloons()  # Display the party popper effect (confetti)
    st.snow()      # Snowfall effect (optional) 
    with st.spinner('Calculating BMI...'):
       time.sleep(2)  # Simulate some delay (e.g., complex calculations)
    st.success('Done!')



st.write(f"Your BMI is {bmi:.2f}")

# Provide suggestion based on BMI categories
if bmi < 18.5:
    st.write("### Suggestion: You are underweight. It's important to maintain a healthy weight for your well-being.")
elif 18.5 <= bmi < 24.9:
    st.write("### Suggestion: Your weight is normal. Keep up the good work!")
elif 25 <= bmi < 29.9:
    st.write("### Suggestion: You are overweight. Consider adopting a healthier diet and exercise routine.")
else:
    st.write("### Suggestion: You are in the obesity category. It's important to seek guidance from a healthcare provider for a personalized health plan.")




st.write("### BMI Categories ###")
st.write("- Underweight: BMI less than 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity:BMI 30 or greater")