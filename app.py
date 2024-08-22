import streamlit as st
import pickle
import numpy as np

# Load the data and model
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title("Laptop Price Predictor")

# Dropdowns for selecting laptop specifications
company = st.selectbox("Brand", df['Company'].unique(), index=0)
laptop_type = st.selectbox("Type", df['TypeName'].unique(), index=0)
cpu = st.selectbox("Processor", df['Cpu'].unique(), index=0)
ram = st.selectbox("RAM (in GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64, 128], index=3)
gpu = st.selectbox("GPU", df['Gpu'].unique(), index=0)
opsys = st.selectbox("Operating System", df['OpSys'].unique(), index=0)
weight = st.number_input("Weight (in kg)", value=1.5, step=0.01)
touchscreen = st.radio("Touchscreen", ['Yes', 'No'])
ips = st.radio("IPS Display", ['Yes', 'No'])
ppi = st.number_input("PPI (Pixels Per Inch)", value=100)

# Convert touchscreen and IPS display to binary
touchscreen = 1 if touchscreen == 'Yes' else 0
ips = 1 if ips == 'Yes' else 0

# Predicting the price when "Predict" button is clicked
if st.button("Predict"):
    input_data = np.array([[company, laptop_type, cpu, ram, gpu, opsys, weight, touchscreen, ips, ppi]])
    predicted_price = pipe.predict(input_data)[0]
    st.success(f"The predicted price of the laptop is ${predicted_price:.2f}")
