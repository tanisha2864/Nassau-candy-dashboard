import streamlit as st
import pandas as pd

st.title("Nassau Candy Shipping Dashboard")

df = pd.read_csv("Nassau Candy Distributor.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Information")
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])








st.write("Columns:", df.shape[1])






st.write("Columns:", df.shape[1])

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${df['Sales'].sum():,.2f}")
col2.metric("Total Profit", f"${df['Gross Profit'].sum():,.2f}")
col3.metric("Total Units", int(df['Units'].sum()))


st.subheader("Sales by Region")

region_sales = df.groupby("Region")["Sales"].sum()

st.bar_chart(region_sales)


st.subheader("Top 10 Products")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_products)



st.sidebar.header("Filters")

selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["Region"].unique())
)

if selected_region != "All":
    filtered_df = df[df["Region"] == selected_region]
else:
    filtered_df = df

st.subheader("Filtered Data")
st.dataframe(filtered_df.head())


st.subheader("Sales by Region")

region_sales = df.groupby("Region")["Sales"].sum()

st.bar_chart(region_sales)



st.subheader("Top 10 Products by Sales")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_products)