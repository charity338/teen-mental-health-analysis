# app.py
import streamlit as st
import pandas as pd
import joblib

# Load model and label encoder
model = joblib.load("model.pkl")
le = joblib.load("label_encoder.pkl")

st.title("🧠 Teen Stress Predictor")
st.markdown("Enter behavioral inputs to predict stress level (Low / Medium / High).")

# Input sliders
age = st.slider("Age", 13, 19, 16)
screen_time = st.slider("Screen Time (hrs/day)", 0.0, 12.0, 4.0)
sleep = st.slider("Sleep Hours", 0.0, 12.0, 7.0)
exercise = st.slider("Exercise Hours", 0.0, 5.0, 1.0)
social_media = st.slider("Social Media Hours", 0.0, 10.0, 3.0)
survey_stress = st.slider("Survey Stress Score (1-10)", 1, 10, 5)

# Predict button
if st.button("Predict Stress Level"):
    input_df = pd.DataFrame([[
    age,
    social_media,
    exercise,
    sleep,
    screen_time,
    survey_stress
]], columns=[
    "age",
    "social_media_hours",
    "exercise_hours",
    "sleep_hours",
    "screen_time_hours",
    "survey_stress_score"
])

    
    prediction = model.predict(input_df)[0]
    stress_label = le.inverse_transform([prediction])[0]
    
    st.success(f"Predicted Stress Level: **{stress_label}** 🧠")


