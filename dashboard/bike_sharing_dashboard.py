import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
Day = pd.read_csv('https://raw.githubusercontent.com/YudhaWS13/Bike_Sharing/refs/heads/main/data/day.csv')
Hour = pd.read_csv('https://raw.githubusercontent.com/YudhaWS13/Bike_Sharing/refs/heads/main/data/hour.csv')

# Convert 'dteday' to datetime format for better handling of dates
Day['dteday'] = pd.to_datetime(Day['dteday'])
Hour['dteday'] = pd.to_datetime(Hour['dteday'])

# Calculate average rental per day
average_rental_per_day = Day['cnt'].mean()

# Calculate hourly rentals
hourly_rental = Hour.groupby('hr')['cnt'].sum().reset_index()

# Plot hourly rentals using Plotly
hourly_fig = px.line(hourly_rental, x='hr', y='cnt', title="Penyewaan Sepeda per Jam")

# Streamlit app layout
st.title('Dashboard Penyewaan Sepeda')

# Display average rentals per day
st.header(f"Rata-rata Penyewaan Sepeda per Hari: {average_rental_per_day:.2f}")

# Display Plotly figure in Streamlit
st.plotly_chart(hourly_fig)

# Add additional interactive elements (optional)
st.write("Grafik di atas menunjukkan jumlah penyewaan sepeda selama 24 jam dalam sehari.")
