import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("mutual_funds_india.csv")  # Adjust path as needed
    df.columns = df.columns.str.replace(" ", "")
    return df

df = load_data()

# Dropdown for Category
categories = df['category'].dropna().unique()
cat = st.selectbox("Select Mutual Fund Category", sorted(categories))

# Filter by selected category
filtered_df = df[df['category'] == cat]

# Dropdown for AMC Name
amc_names = filtered_df['AMC_name'].dropna().unique()
mf = st.selectbox("Select AMC Name", sorted(amc_names))

# Filter further by selected AMC
selected_data = filtered_df[filtered_df['AMC_name'] == mf]

# Show plot only if there is data
if not selected_data.empty:
    st.subheader("1-Year Return of Mutual Funds")
    plt.figure(figsize=(12, 6))
    sb.barplot(x=selected_data['MutualFundName'], y=selected_data['return_1yr'], palette='ocean')
    plt.xticks(rotation=90)
    st.pyplot(plt)
else:
    st.warning("No data available for the selected AMC in this category.")

