import streamlit as st
import pandas as pd
import pickle

st.title('Diabetes Prediction App')
st.write("Enter the following details to predict the outcome:")

preg = st.number_input("Pregnancies", min_value=0, step=1)
glucose = st.number_input("Glucose", min_value=0)
bp = st.number_input("Blood Pressure")
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
age = st.number_input("Age", min_value=0, step=1)

model = pickle.load(open('clf.pkl', 'rb'))

if st.button("Predict"):
    features = pd.DataFrame([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("The patient is likely to have diabetes.")
    else:
        st.success("The patient is unlikely to have diabetes.")