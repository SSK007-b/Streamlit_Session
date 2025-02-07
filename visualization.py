import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title('Data Visualization')
    st.write('This is the "Data Visualization" page of the Streamlit App.')

    # Load data
    df = pd.read_csv('Salary_dataset.csv')

    # Show dataset
    if st.checkbox('Show dataset'):
        st.write(df)

    # Show summary
    if st.checkbox('Show summary'):
        st.write(df.describe())

    # Show correlation
    if st.checkbox('Show correlation'):
        st.write(df.corr())

    # Show heatmap
    if st.checkbox('Show heatmap'):
        sns.heatmap(df.corr(), annot=True)
        st.pyplot()

    # Show pairplot
    if st.checkbox('Show pairplot'):
        sns.pairplot(x_vars="YearsExperience", y_vars= "Salary", data=df, hue='Salary')
        st.pyplot()

    # Show barplot
    if st.checkbox('Show barplot'):
        sns.barplot(x='YearsExperience', y='Salary', data=df)
        st.pyplot()

    # Show boxplot
    if st.checkbox('Show boxplot'):
        sns.boxplot(x='YearsExperience', y='Salary', data=df)
        st.pyplot()

    # Show scatterplot
    if st.checkbox('Show scatterplot'):
        sns.scatterplot(x='YearsExperience', y='Salary', data=df, hue='Salary')
        st.pyplot()
    

if __name__ == '__main__':
    main()