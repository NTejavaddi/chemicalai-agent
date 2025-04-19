import streamlit as st
import numpy as np

st.title("🧪 ChemicalAI Yield Predictor")

temp = st.slider("Temperature (K)", 300, 600)
press = st.slider("Pressure (atm)", 1, 20)
cat = st.slider("Catalyst Concentration (%)", 0.01, 0.1)
time = st.slider("Residence Time (h)", 1.0, 10.0)

if st.button("Predict Yield"):
    yield_pred = 0.3 * np.log(temp) + 0.5 * np.sqrt(press) - 2 * cat + 0.2 * time
    st.success(f"Predicted Yield: {round(yield_pred, 2)}%")
