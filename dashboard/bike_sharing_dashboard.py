import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
Day = pd.read_csv('https://raw.githubusercontent.com/YudhaWS13/Bike_Sharing/refs/heads/main/data/day.csv')
Hour = pd.read_csv('https://raw.githubusercontent.com/YudhaWS13/Bike_Sharing/refs/heads/main/data/hour.csv')

# Convert date column
Day['dteday'] = pd.to_datetime(Day['dteday'])
Hour['dteday'] = pd.to_datetime(Hour['dteday'])

# 1. Menghitung rata-rata jumlah penyewaan sepeda per hari
average_rental_per_day = Day['cnt'].mean()

# 2. Menyusun data untuk analisis jumlah penyewaan berdasarkan jam
hourly_rental = Hour.groupby('hr')['cnt'].sum().reset_index()

# 3. Menemukan jam dengan penyewaan terbanyak
peak_hour = hourly_rental.loc[hourly_rental['cnt'].idxmax()]

# 4. Menampilkan hasil rata-rata penyewaan sepeda per hari
st.write(f"### Rata-rata penyewaan sepeda per hari : {average_rental_per_day:.2f}")

# 5. Menampilkan jam puncak penyewaan sepeda
st.write(f"### Penyewaan sepeda paling banyak terjadi pada jam {peak_hour['hr']} dengan jumlah penyewaan {peak_hour['cnt']}.")

# 6. Rata-rata per jam untuk informasi lebih mendetail
average_rental_per_hour = Hour['cnt'].mean()
st.write(f"### Rata-rata penyewaan sepeda per jam: {average_rental_per_hour:.2f}")

# Menampilkan heatmap korelasi
st.header("Korelasi antara Jumlah Penyewaan dan Fitur Lainnya")
plt.figure(figsize=(12, 8))
corr_day = Day.corr()
sns.heatmap(corr_day[['cnt']], annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar=True)
plt.title('Korelasi antara Jumlah Penyewaan dan Fitur Lain (Day Dataset)')
st.pyplot(plt)

# Menampilkan boxplot jumlah penyewaan berdasarkan musim
st.header("Jumlah Penyewaan Sepeda berdasarkan Musim")
plt.figure(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=Day, palette='Set2')
plt.title('Jumlah Penyewaan Sepeda berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewaan')
plt.grid()
st.pyplot(plt)

# Menampilkan scatter plot hubungan antara suhu dan jumlah penyewaan
st.header("Hubungan antara Suhu dan Jumlah Penyewaan")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=Day, color='orange', alpha=0.6)
plt.title('Hubungan antara Suhu dan Jumlah Penyewaan Sepeda')
plt.xlabel('Suhu (normalisasi 0-1)')
plt.ylabel('Jumlah Penyewaan')
plt.grid()
st.pyplot(plt)

# Menampilkan scatter plot hubungan antara kelembapan dan jumlah penyewaan
st.header("Hubungan antara Kelembapan dan Jumlah Penyewaan")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='hum', y='cnt', data=Day, color='blue', alpha=0.6)
plt.title('Hubungan antara Kelembapan dan Jumlah Penyewaan Sepeda')
plt.xlabel('Kelembapan (normalisasi 0-1)')
plt.ylabel('Jumlah Penyewaan')
plt.grid()
st.pyplot(plt)

# Menampilkan boxplot jumlah penyewaan berdasarkan hari dalam seminggu
st.header("Jumlah Penyewaan Sepeda berdasarkan Hari dalam Minggu")
plt.figure(figsize=(10, 6))
sns.boxplot(x='weekday', y='cnt', data=Day, palette='Set2')
plt.title('Jumlah Penyewaan Sepeda berdasarkan Hari dalam Seminggu')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Jumlah Penyewaan')
plt.grid()
st.pyplot(plt)

# Menampilkan line plot jumlah penyewaan per jam
st.header("Jumlah Penyewaan Sepeda per Jam")
hourly_data = Hour.groupby('hr')['cnt'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x='hr', y='cnt', data=hourly_data, marker='o', color='blue')
plt.title('Jumlah Penyewaan Sepeda per Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(range(0, 24), rotation=45)
plt.grid()
st.pyplot(plt)

# Menampilkan boxplot untuk jam 6 pagi hingga 8 malam
st.header("Distribusi Jumlah Penyewaan pada Jam (06:00 - 20:00)")
daytime_hourly_data = Hour[(Hour['hr'] >= 6) & (Hour['hr'] <= 20)]
plt.figure(figsize=(12, 6))
sns.boxplot(x='hr', y='cnt', data=daytime_hourly_data, palette='Set2')
plt.title('Distribusi Jumlah Penyewaan Sepeda pada Jam (06:00 - 20:00)')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(range(6, 21), rotation=45)
plt.grid()
st.pyplot(plt)

# Menampilkan histogram jumlah penyewaan selama siang hari
st.header("Distribusi Jumlah Penyewaan di Siang Hari")
plt.figure(figsize=(12, 6))
sns.histplot(daytime_hourly_data['cnt'], bins=20, kde=True, color='orange')
plt.title('Distribusi Jumlah Penyewaan Sepeda di Siang Hari')
plt.xlabel('Jumlah Penyewaan')
plt.ylabel('Frekuensi')
plt.grid()
st.pyplot(plt)
