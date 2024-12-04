import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title('Simple Data')
    uploaded_file = st.file_uploader("Pilih File CSV",type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("Data Preview")
        st.write(df.head())

        st.subheader("Data Summary")
        st.write(df.tail())
        
        st.subheader("Filter Data")
        columns = df.columns.tolist()
        selected_column = st.selectbox("Select columns to filter by", columns)
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox("Select value", unique_values)

        filtered_df = df[df[selected_column] == selected_value]
        st.write(filtered_df)