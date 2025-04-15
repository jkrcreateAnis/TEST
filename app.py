# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the web app
st.title("Pump Failure Monitoring Dashboard")

# Create a file uploader for CSV files
uploaded_file = st.file_uploader("Upload your CSV file")

# If a file is uploaded, read and process it
if uploaded_file:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the raw data as a table
    st.subheader("Raw Data")
    st.write(df)

    # Let the user select a column to visualize
    col = st.selectbox("Select column to visualize", df.columns)

    # Show a line chart of the selected column
    st.subheader(f"Trend of {col}")
    st.line_chart(df[col])
