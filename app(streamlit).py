import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(r"YouTube_Long_vs_Shorts_Analysis.csv", encoding="ISO-8859-1")
    return df

df = load_data()

# Streamlit App Layout
st.title("Data Analysis Dashboard")
st.write("This is a simple Streamlit app for data analysis.")

# Show Data
if st.checkbox("Show raw data"):
    st.write(df)

# Visualization
st.subheader("Data Visualization")
fig, ax = plt.subplots()
df["Video ID"].hist(ax=ax)
st.pyplot(fig)