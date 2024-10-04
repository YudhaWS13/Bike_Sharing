import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
@st.cache_data
def load_data():
    Day = pd.read_csv('https://raw.githubusercontent.com/YudhaWS13/Bike_Sharing/refs/heads/main/data/day.csv')
    Hour = pd.read_csv('https://raw.githubusercontent.com/YudhaWS13/Bike_Sharing/refs/heads/main/data/hour.csv')
    Day['dteday'] = pd.to_datetime(Day['dteday'])
    Hour['dteday'] = pd.to_datetime(Hour['dteday'])
    return Day, Hour

Day, Hour = load_data()

# Function to categorize time of day
def time_of_day(hour):
    if 6 <= hour < 12:
        return 'Pagi'
    elif 12 <= hour < 17:
        return 'Siang'
    elif 17 <= hour < 21:
        return 'Sore'
    else:
        return 'Malam'

# Add column to categorize time of day
Hour['time_of_day'] = Hour['hr'].apply(time_of_day)

# Function to display correlation matrix
def display_correlation_matrix(df, factors):
    factors_corr = df[factors + ['cnt']].corr()
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

# Function to display a chart
def plot_chart(df, x, y, title, kind="line", labels=None):
    if kind == "line":
        fig = px.line(df, x=x, y=y, title=title, labels=labels)
    elif kind == "bar":
        fig = px.bar(df, x=x, y=y, title=title, labels=labels)
    elif kind == "scatter":
        fig = px.scatter(df, x=x, y=y, title=title, labels=labels)
    st.plotly_chart(fig)

# Main title and introduction
st.title('📊 Analisis Penyewaan Sepeda 🚴')
st.write("""
Selamat datang di aplikasi analisis penyewaan sepeda. Anda bisa menelusuri berbagai visualisasi data penyewaan sepeda berdasarkan waktu, cuaca, dan faktor lainnya. Gunakan **sidebar** untuk memilih visualisasi yang ingin Anda lihat!
""")

# Sidebar for user interaction
st.sidebar.title("🔍 Pilih Visualisasi")
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
     "Faktor-faktor yang Mempengaruhi Penyewaan Harian",
     "Line Plot Penyewaan Sepeda per Jam"]  # Opsi baru
)

# Menampilkan Line Plot untuk Penyewaan Sepeda per Jam
if "Line Plot Penyewaan Sepeda per Jam" in options:
    st.header("Jumlah Penyewaan Sepeda per Jam")
    plot_chart(hourly_data, x='hr', y='cnt', title="Line Plot Penyewaan Sepeda per Jam", kind="line")

# Plot average rentals per day
if "Rata-rata Penyewaan Sepeda per Hari" in options:
    average_rental_per_day = Day['cnt'].mean()
    st.header(f"🚴‍♂️ Rata-rata Penyewaan Sepeda per Hari: {average_rental_per_day:.2f}")

# Plot hourly rentals
if "Penyewaan Sepeda per Jam" in options:
    hourly_rental = Hour.groupby('hr')['cnt'].sum().reset_index()
    plot_chart(hourly_rental, x='hr', y='cnt', title="Penyewaan Sepeda per Jam")

# Plot peak hour for rentals
if "Waktu Paling Banyak Penyewaan Sepeda" in options:
    peak_hour = Hour.groupby('hr')['cnt'].sum().idxmax()
    st.header(f"⏰ Waktu Paling Banyak Penyewaan Sepeda: Jam {int(peak_hour)}:00")

# Plot time of day bike rentals
if "Penyewaan Sepeda Berdasarkan Waktu (Pagi, Siang, Sore, Malam)" in options:
    time_of_day_rental = Hour.groupby('time_of_day')['cnt'].sum().reset_index()
    plot_chart(time_of_day_rental, x='time_of_day', y='cnt', title="Penyewaan Sepeda Berdasarkan Waktu", kind="bar")

# Plot bike rentals by season
if "Penyewaan Sepeda Berdasarkan Musim" in options:
    season_rental = Day.groupby('season')['cnt'].sum().reset_index()
    season_rental['season'] = season_rental['season'].map({1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'})
    plot_chart(season_rental, x='season', y='cnt', title="Penyewaan Sepeda Berdasarkan Musim", kind="bar")

# Plot bike rentals by weekday
if "Penyewaan Sepeda Berdasarkan Hari dalam Minggu" in options:
    weekday_rental = Day.groupby('weekday')['cnt'].sum().reset_index()
    weekday_rental['weekday'] = weekday_rental['weekday'].map({0: 'Senin', 1: 'Selasa', 2: 'Rabu', 3: 'Kamis', 4: 'Jumat', 5: 'Sabtu', 6: 'Minggu'})
    plot_chart(weekday_rental, x='weekday', y='cnt', title="Penyewaan Sepeda Berdasarkan Hari dalam Minggu", kind="bar")

# Plot correlation between temperature and bike rentals
if "Korelasi antara Suhu dan Penyewaan Sepeda" in options:
    plot_chart(Day, x='temp', y='cnt', title="Korelasi antara Suhu dan Penyewaan Sepeda", kind="scatter")

# Plot correlation between humidity and bike rentals
if "Korelasi antara Kelembapan dan Penyewaan Sepeda" in options:
    plot_chart(Day, x='hum', y='cnt', title="Korelasi antara Kelembapan dan Penyewaan Sepeda", kind="scatter")

# Display correlation of factors affecting daily rentals
if "Faktor-faktor yang Mempengaruhi Penyewaan Harian" in options:
    factors = ['temp', 'atemp', 'hum', 'windspeed', 'season', 'weekday']
    display_correlation_matrix(Day, factors)

# Footer message
st.write("""
**Pilih opsi di sidebar untuk menampilkan grafik yang lebih spesifik!**
""")
