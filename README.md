Dasbor Berbagi Sepeda dengan Streamlit
Repositori ini berisi Dasbor Berbagi Sepeda sederhana yang dibuat dengan Streamlit. Dasbor menampilkan wawasan utama seperti jumlah rata-rata penyewaan sepeda harian dan waktu puncak penyewaan di siang hari, berdasarkan himpunan data yang disediakan.

Fitur
Tampilkan jumlah rata-rata penyewaan sepeda per hari.
Tampilkan grafik garis penyewaan sepeda per jam untuk mengidentifikasi jam sibuk penggunaan sepeda.
Prasyarat
Sebelum menjalankan aplikasi Streamlit, pastikan Anda telah menginstal yang berikut ini:

Python 3.x
Pip (pengelola paket Python)
Instalasi
Ikuti langkah-langkah di bawah ini untuk menyiapkan dan menjalankan dasbor di komputer lokal Anda:

1. Mengkloning Repositori
Anda dapat mengkloning repositori ini dengan menjalankan:
git clone <repository-url>
cd <repository-folder>

2. Instal Paket Python yang Diperlukan
Instal paket Python yang diperlukan. Anda dapat melakukannya dengan menggunakan dengan menjalankan perintah berikut:streamlit pandas plotly pip
pip install -r requirements.txt

Atau, Anda dapat menginstalnya secara manual menggunakan:
pip install streamlit pandas plotly

3. Jalankan Aplikasi Streamlit
Untuk menjalankan aplikasi Streamlit, gunakan perintah berikut di terminal atau prompt perintah Anda:
streamlit run app.py

Pastikan Anda mengganti dengan nama sebenarnya dari skrip Python Anda jika berbeda.app.py

4. Lihat Dasbor
Setelah aplikasi Streamlit dimulai, Anda dapat melihat dasbor dengan membuka browser web Anda dan menavigasi ke:
http://localhost:8501

Ini akan membuka dasbor interaktif tempat Anda dapat menjelajahi visualisasi dan wawasan.

Struktur Proyek
app.py: Skrip Python utama yang menjalankan dasbor Streamlit.
requirements.txt: File yang mencantumkan semua paket Python yang diperlukan untuk menjalankan proyek.
README.md: File ini dengan instruksi tentang cara menyiapkan dan menjalankan dasbor.
Dataset
Dasbor menggunakan himpunan data berbagi sepeda yang dapat diambil langsung dari URL berikut:

Himpunan data hari
Himpunan data jam
Contoh Visualisasi
Sewa Sepeda Rata-rata per Hari: Menampilkan jumlah rata-rata penyewaan sepeda selama himpunan data.
Sewa Per Jam: Grafik garis yang menunjukkan tren penyewaan sepeda per jam untuk mengidentifikasi waktu penggunaan puncak.
Pemecahan masalah
Jika Anda mengalami kesalahan, pastikan Streamlit diinstal dan ditambahkan dengan benar ke PATH sistem Anda. Anda dapat mengikuti petunjuk penginstalan di atas untuk mengatasinya.'streamlit' is not recognized as an internal or external command

Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT - lihat file LISENSI untuk detailnya.

Opsional: Buat requirements.txt
Anda dapat membuat file dengan menjalankan:requirements.txt
pip freeze > requirements.txt
Ini akan menangkap semua paket yang diinstal di lingkungan virtual Anda.

