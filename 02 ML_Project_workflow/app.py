import streamlit as st
import numpy as np
import pandas as pd
import pickle

# page config
st.set_page_config(
    page_title="Smartphone Addiction Predictor",
    page_icon="📱",
    layout="wide"
)

# load model
model = pickle.load(open("smartphone_addiction_model.pkl", "rb"))
preprocessor = pickle.load(open("preprocessor.pkl", "rb"))

# title
st.markdown(
    "<h1 style='text-align:center;'>📱 Smartphone Addiction Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Analyze smartphone behaviour patterns</p>",
    unsafe_allow_html=True
)

st.divider()

# layout columns
col1, col2 = st.columns(2)

# ------------ COLUMN 1 ------------ #

with col1:

    st.subheader("User Profile")

    age = st.slider("Age", 10, 80, 25)

    gender = st.radio("Gender", ["Male", "Female"])

    stress_level = st.selectbox(
        "Stress Level",
        ["Low", "Medium", "High"]
    )

    academic_work_impact = st.selectbox(
        "Work Impact",
        ["No", "Yes"]
    )

# ------------ COLUMN 2 ------------ #

with col2:

    st.subheader("Usage Behaviour")

    daily_screen_time_hours = st.slider(
        "Daily screen time (hours)",
        0.0, 15.0, 3.0
    )

    social_media_hours = st.slider(
        "Social media hours",
        0.0, 12.0, 1.5
    )

    gaming_hours = st.slider(
        "Gaming hours",
        0.0, 12.0, 0.5
    )

    work_study_hours = st.slider(
        "Work/study hours",
        0.0, 12.0, 2.0
    )

    sleep_hours = st.slider(
        "Sleep hours",
        0.0, 12.0, 7.0
    )

    weekend_screen_time = st.slider(
        "Weekend screen time",
        0.0, 20.0, 4.0
    )

# ------------ extra inputs ------------ #

st.subheader("Interaction Behaviour")

col3, col4 = st.columns(2)

with col3:

    notifications_per_day = st.slider(
        "Notifications per day",
        0, 500, 50
    )

with col4:

    app_opens_per_day = st.slider(
        "App opens per day",
        0, 500, 60
    )

st.divider()

# ------------ feature engineering ------------ #

entertainment_ratio = (
    (social_media_hours + gaming_hours) /
    daily_screen_time_hours
    if daily_screen_time_hours > 0 else 0
)

weekend_usage_diff = (
    weekend_screen_time -
    daily_screen_time_hours
)

opens_per_notification = (
    app_opens_per_day /
    notifications_per_day
    if notifications_per_day > 0 else 0
)

sleep_deficit = 7 - sleep_hours

# ------------ prediction ------------ #

predict_button = st.button("Predict Addiction Risk", use_container_width=True)

if predict_button:

    input_data = pd.DataFrame({

        "age":[age],

        "daily_screen_time_hours":[daily_screen_time_hours],

        "social_media_hours":[social_media_hours],

        "gaming_hours":[gaming_hours],

        "work_study_hours":[work_study_hours],

        "sleep_hours":[sleep_hours],

        "notifications_per_day":[notifications_per_day],

        "app_opens_per_day":[app_opens_per_day],

        "weekend_screen_time":[weekend_screen_time],

        "entertainment_ratio":[entertainment_ratio],

        "weekend_usage_diff":[weekend_usage_diff],

        "opens_per_notification":[opens_per_notification],

        "sleep_deficit":[sleep_deficit],

        "gender":[gender],

        "stress_level":[stress_level],

        "academic_work_impact":[academic_work_impact]

    })

    input_processed = preprocessor.transform(input_data)

    prediction = model.predict(input_processed)

    probability = model.predict_proba(input_processed)[0][1]

    st.divider()

    if prediction[0] == 1:

        st.error("⚠️ High Risk of Smartphone Addiction")

        st.progress(float(probability))

    else:

        st.success("✅ Low Risk of Smartphone Addiction")

        st.progress(float(probability))

    st.metric(
        label="Addiction Probability",
        value=f"{probability:.2%}"
    )