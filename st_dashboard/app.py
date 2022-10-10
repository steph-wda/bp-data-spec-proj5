import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

st.title('Data Supermart Dashboard')

super_df = pd.read_csv('supermarket.csv')

total_store_sales = super_df['store_sales'].sum()
avg_store_sales = round(super_df['store_sales'].mean(),2)

top_stores = super_df.sort_values(by='store_sales', ascending=False).head(10)
bottom_stores = super_df.sort_values(by='store_sales').head(10)



col1,col2 = st.columns(2)
col1.metric(label="Total Store Sales", value=total_store_sales)
col2.metric(label="Average Store Sales", value=avg_store_sales)

st.header("Top 10 Performing Stores In Sales")
st.bar_chart(data=top_stores, x='store_id', y='store_sales')

st.header("Top 10 Least Performing Stores In Sales")
st.bar_chart(data=bottom_stores, x='store_id', y='store_sales')


total_daily_customer_count = super_df['daily_customer_count'].sum()
avg_daily_customer_count = int((super_df['daily_customer_count'].sum()/ len(super_df['store_sales'])))
avg_spent_per_customer = round((super_df['store_sales'].sum() / super_df['daily_customer_count'].sum()),2)

col1,col2,col3 = st.columns(3)
col1.metric(label="Total Daily Customer Count", value=total_daily_customer_count)
col2.metric(label="Average Daily Customer Count", value=avg_daily_customer_count)
col3.metric(label="Average Customer Spend", value=avg_spent_per_customer)