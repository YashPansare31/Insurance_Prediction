import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('models/model.pkl')

# Streamlit page config
st.set_page_config(page_title="Insurance Prediction", layout="centered")

st.title("Insurance Prediction App")

# Input fields
Gender = st.selectbox("Gender", ["Male", "Female"])
Age = st.number_input("Age", min_value=18, max_value=100, step=1)
HasDrivingLicense = st.selectbox("Has Driving License", [0, 1])
RegionID = st.number_input("Region ID", step=1.0)
Switch = st.selectbox("Switch", [0, 1])
PastAccident = st.selectbox("Past Accident", ["Yes", "No"])
AnnualPremium = st.number_input("Annual Premium", step=100.0)

# Predict button
if st.button("Predict"):
    # Construct input data
    input_data = {
        "Gender": Gender,
        "Age": Age,
        "HasDrivingLicense": HasDrivingLicense,
        "RegionID": RegionID,
        "Switch": Switch,
        "PastAccident": PastAccident,
        "AnnualPremium": AnnualPremium
    }
    
    df = pd.DataFrame([input_data.values()], columns=input_data.keys())
    pred = model.predict(df)

    st.success(f"Predicted Class: {int(pred[0])}")
