# Import libraries if not already done
import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
Day = pd.read_csv('https://raw.githubusercontent.com/YudhaWS13/Bike_Sharing/refs/heads/main/data/day.csv')
Hour = pd.read_csv('https://raw.githubusercontent.com/YudhaWS13/Bike_Sharing/refs/heads/main/data/hour.csv')

# Convert 'dteday' to datetime format for better handling of dates
Day['dteday'] = pd.to_datetime(Day['dteday'])
Hour['dteday'] = pd.to_datetime(Hour['dteday'])

# Sidebar for user interaction
st.sidebar.title("Pilih Visualisasi atau Data")
options = st.sidebar.multiselect(
    "Apa yang ingin Anda lihat?", 
    ["Rata-rata Penyewaan Sepeda per Hari", 
     "Penyewaan Sepeda per Jam", 
     "Waktu Paling Banyak Penyewaan Sepeda", 
     "Penyewaan Sepeda Berdasarkan Waktu (Pagi, Siang, Sore, Malam)", 
     "Penyewaan Sepeda Berdasarkan Musim", 
     "Penyewaan Sepeda Berdasarkan Hari dalam Minggu", 
     "Korelasi antara Suhu dan Penyewaan Sepeda",
     "Korelasi antara Kelembapan dan Penyewaan Sepeda",
     "Faktor-faktor yang Mempengaruhi Penyewaan Harian"]
)

# Plot average rentals per day
if "Rata-rata Penyewaan Sepeda per Hari" in options:
    average_rental_per_day = Day['cnt'].mean()
    st.header(f"Rata-rata Penyewaan Sepeda per Hari: {average_rental_per_day:.2f}")

# Plot hourly rentals
if "Penyewaan Sepeda per Jam" in options:
    hourly_rental = Hour.groupby('hr')['cnt'].sum().reset_index()
    hourly_fig = px.line(hourly_rental, x='hr', y='cnt', title="Penyewaan Sepeda per Jam")
    st.plotly_chart(hourly_fig)

# Plot peak hour for rentals
if "Waktu Paling Banyak Penyewaan Sepeda" in options:
    peak_hour = hourly_rental.loc[hourly_rental['cnt'].idxmax()]['hr']
    st.header(f"Waktu Paling Banyak Penyewaan Sepeda: Jam {int(peak_hour)}:00")

# Plot time of day bike rentals
if "Penyewaan Sepeda Berdasarkan Waktu (Pagi, Siang, Sore, Malam)" in options:
    Hour['time_of_day'] = Hour['hr'].apply(time_of_day)
    time_of_day_rental = Hour.groupby('time_of_day')['cnt'].sum().reset_index()
    time_of_day_fig = px.bar(time_of_day_rental, x='time_of_day', y='cnt', 
                             title="Penyewaan Sepeda Berdasarkan Waktu (Pagi, Siang, Sore, Malam)",
                             labels={'time_of_day': 'Waktu', 'cnt': 'Jumlah Penyewaan'})
    st.plotly_chart(time_of_day_fig)

# Plot bike rentals by season
if "Penyewaan Sepeda Berdasarkan Musim" in options:
    season_rental = Day.groupby('season')['cnt'].sum().reset_index()
    season_rental['season'] = season_rental['season'].map({1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'})
    season_fig = px.bar(season_rental, x='season', y='cnt', 
                        title="Penyewaan Sepeda Berdasarkan Musim",
                        labels={'season': 'Musim', 'cnt': 'Jumlah Penyewaan'})
    st.plotly_chart(season_fig)

# Plot bike rentals by weekday
if "Penyewaan Sepeda Berdasarkan Hari dalam Minggu" in options:
    weekday_rental = Day.groupby('weekday')['cnt'].sum().reset_index()
    weekday_rental['weekday'] = weekday_rental['weekday'].map({0: 'Senin', 1: 'Selasa', 2: 'Rabu', 3: 'Kamis', 4: 'Jumat', 5: 'Sabtu', 6: 'Minggu'})
    weekday_fig = px.bar(weekday_rental, x='weekday', y='cnt', 
                         title="Penyewaan Sepeda Berdasarkan Hari dalam Minggu",
                         labels={'weekday': 'Hari', 'cnt': 'Jumlah Penyewaan'})
    st.plotly_chart(weekday_fig)

# Plot correlation between temperature and bike rentals
if "Korelasi antara Suhu dan Penyewaan Sepeda" in options:
    temp_fig = px.scatter(Day, x='temp', y='cnt', 
                          title="Korelasi antara Suhu dan Penyewaan Sepeda",
                          labels={'temp': 'Suhu', 'cnt': 'Jumlah Penyewaan'})
    st.plotly_chart(temp_fig)

# Plot correlation between humidity and bike rentals
if "Korelasi antara Kelembapan dan Penyewaan Sepeda" in options:
    hum_fig = px.scatter(Day, x='hum', y='cnt', 
                         title="Korelasi antara Kelembapan dan Penyewaan Sepeda",
                         labels={'hum': 'Kelembapan', 'cnt': 'Jumlah Penyewaan'})
    st.plotly_chart(hum_fig)

# Display factors affecting daily rentals
if "Faktor-faktor yang Mempengaruhi Penyewaan Harian" in options:
    factors = ['temp', 'atemp', 'hum', 'windspeed', 'season', 'weekday']
    factors_corr = Day[factors + ['cnt']].corr()
    st.header("Faktor-faktor yang Mempengaruhi Penyewaan Sepeda Harian")
    st.write("Korelasi antara faktor-faktor seperti suhu, kelembapan, kecepatan angin, dan jumlah penyewaan:")
    st.dataframe(factors_corr)
    
    st.write("""
    - **Suhu**: Korelasi positif antara suhu dan jumlah penyewaan sepeda.
    - **Kelembapan**: Korelasi negatif dengan jumlah penyewaan sepeda.
    - **Musim**: Musim semi dan musim panas cenderung memiliki penyewaan yang lebih tinggi.
    - **Kecepatan Angin**: Korelasi negatif dengan jumlah penyewaan.
    - **Hari dalam Minggu**: Penyewaan lebih tinggi pada akhir pekan.
    """)
