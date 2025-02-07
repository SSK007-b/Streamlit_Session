import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib as jlb

@st.cache_data
def load_data():
    scaler = jlb.load(r'pkl_Files/scaler.pkl')
    model = jlb.load(r'pkl_Files/model.pkl')
    return scaler, model

def main():
    st.title('Salary Prediction')
    scaler, model = load_data()
    years_experience = st.number_input('Enter years of experience:', min_value=0.0, max_value=100.0, value=0.0)
    salary = model.predict(scaler.transform(np.array([[years_experience]])))[0]
    if st.button('Predict Salary'):
        st.write(f'Predicted Salary: {round(salary, 2)}')
    else:
        st.write('Click the button to predict salary.')

if __name__ == '__main__':
    main()