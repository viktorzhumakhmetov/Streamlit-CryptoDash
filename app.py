import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('currencies.csv')
df.date = pd.to_datetime(df.date)
df['date'] = df['date'].dt.date

st.header('Cryptocurrency Prices')


with st.sidebar:
    st.header('Options')
    currency = st.selectbox('Select an asset:', df['currency'].unique())
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('Date from:', value=df['date'].min())
    with col2:
        end_date = st.date_input('Date to:', value=df['date'].max())

filtered_data = df[(df['currency'] == currency) & (df['date'] <= end_date) & (df['date'] >= start_date)]

fig = px.line(filtered_data, x='date', y='price')

fig.update_traces(line_color='#4BD964')

fig.update_layout(
    title=f'{currency} price change in USD',
    xaxis_title="Date",
    yaxis_title="Price"
)

st.plotly_chart(fig)

# для запуска приложения в браузере прописать в терминал команду: streamlit run app.py