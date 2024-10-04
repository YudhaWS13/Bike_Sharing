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

# Determine peak hour for bike rentals
peak_hour = hourly_rental.loc[hourly_rental['cnt'].idxmax()]['hr']

# Categorize hours into morning, afternoon, evening, and night
def time_of_day(hour):
    if 6 <= hour < 12:
        return 'Pagi'
    elif 12 <= hour < 17:
        return 'Siang'
    elif 17 <= hour < 21:
        return 'Sore'
    else:
        return 'Malam'

Hour['time_of_day'] = Hour['hr'].apply(time_of_day)
time_of_day_rental = Hour.groupby('time_of_day')['cnt'].sum().reset_index()

# Plot hourly rentals using Plotly
hourly_fig = px.line(hourly_rental, x='hr', y='cnt', title="Penyewaan Sepeda per Jam")

# Factors affecting daily rentals (weather, temp, humidity, etc.)
factors = ['temp', 'atemp', 'hum', 'windspeed', 'season', 'weekday']
factors_corr = Day[factors + ['cnt']].corr()

# Streamlit app layout
st.title('SELAMAT DATANG DI PENYEWAAAN SEPEDA')
st.write("Ini adalah program untuk melihat data penyewaan sepeda dan faktor-faktor yang mempengaruhinya.")

# Sidebar for user interaction
st.sidebar.title("Pilih Visualisasi atau Data")
options = st.sidebar.multiselect(
    "Apa yang ingin Anda lihat?", 
    ["Rata-rata Penyewaan Sepeda per Hari", 
     "Penyewaan Sepeda per Jam", 
     "Waktu Paling Banyak Penyewaan Sepeda", 
     "Penyewaan Sepeda Berdasarkan Waktu (Pagi, Siang, Sore, Malam)", 
     "Faktor-faktor yang Mempengaruhi Penyewaan Harian"]
)

# Display average rentals per day
if "Rata-rata Penyewaan Sepeda per Hari" in options:
    st.header(f"Rata-rata Penyewaan Sepeda per Hari: {average_rental_per_day:.2f}")

# Display hourly rentals
if "Penyewaan Sepeda per Jam" in options:
    st.plotly_chart(hourly_fig)

# Display peak hour for rentals
if "Waktu Paling Banyak Penyewaan Sepeda" in options:
    st.header(f"Waktu Paling Banyak Penyewaan Sepeda: Jam {int(peak_hour)}:00")

# Display time-of-day bike rentals
if "Penyewaan Sepeda Berdasarkan Waktu (Pagi, Siang, Sore, Malam)" in options:
    time_of_day_fig = px.bar(time_of_day_rental, x='time_of_day', y='cnt', 
                             title="Penyewaan Sepeda Berdasarkan Waktu (Pagi, Siang, Sore, Malam)",
                             labels={'time_of_day': 'Waktu', 'cnt': 'Jumlah Penyewaan'})
    st.plotly_chart(time_of_day_fig)

# Display correlation of factors affecting daily rentals
if "Faktor-faktor yang Mempengaruhi Penyewaan Harian" in options:
    st.header("Faktor-faktor yang Mempengaruhi Penyewaan Sepeda Harian")
    st.write("Korelasi antara faktor-faktor seperti suhu, kelembapan, kecepatan angin, dan jumlah penyewaan:")
    st.dataframe(factors_corr)

    st.write("""
    - **Suhu**: Suhu rata-rata memiliki korelasi positif dengan jumlah penyewaan sepeda.
    - **Kelembapan**: Kelembapan menunjukkan korelasi negatif dengan penyewaan sepeda, artinya pada kelembapan tinggi, penyewaan cenderung menurun.
    - **Musim**: Penyewaan sepeda bervariasi menurut musim, dengan musim semi dan musim panas menjadi waktu puncak.
    - **Windspeed**: Kecepatan angin juga menunjukkan pengaruh negatif terhadap jumlah penyewaan sepeda.
    - **Hari dalam Minggu**: Penyewaan cenderung lebih tinggi pada akhir pekan.
    """)

# Additional explanation
st.write("Pilih opsi di sidebar untuk menampilkan grafik atau informasi yang relevan sesuai dengan minat Anda.")
