# Menerapkan Algoritma Dsatur dalam Meminimalisasi Potensi Kecurangan Seleksi Nasional Berbasis Tes (SNBT)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![NetworkX](https://img.shields.io/badge/NetworkX-3.4.2-red)
![Matplotlib](https://img.shields.io/badge/matplotlib-3.10.0-green)

Selamat datang di **Menerapkan Algoritma Dsatur dalam Meminimalisasi Potensi Kecurangan Seleksi Nasional Berbasis Tes (SNBT)** oleh Kaindra. Proyek ini bertujuan untuk mengimplementasikan algoritma Dsatur dalam mengoptimalkan distribusi paket soal ujian untuk memastikan keadilan dan mengurangi risiko kecurangan dalam SNBT.

## 📖 Deskripsi

Seleksi Nasional Berbasis Tes (SNBT) adalah ujian penting untuk penerimaan mahasiswa baru di perguruan tinggi negeri di Indonesia. Penelitian ini memodelkan ruang ujian sebagai graf, dengan peserta sebagai simpul dan kedekatan tempat duduk sebagai sisi. Algoritma Dsatur digunakan untuk pewarnaan graf guna memastikan bahwa peserta yang duduk berdekatan tidak menerima paket soal yang sama.

Penelitian ini memanfaatkan **Python** dengan pustaka seperti `NetworkX` dan `Matplotlib` untuk pemodelan graf dan visualisasi. Dengan pendekatan ini, penelitian memberikan solusi berbasis matematika diskrit yang efisien untuk meningkatkan integritas ujian.

---

## 💻 Fitur

1. **Pembuatan Graf Ruang Ujian**:
   - Representasi ruang ujian dalam dua tipe dengan model graf.
   - Memastikan model sesuai dengan kondisi SNBT (20-30 peserta per ruangan).

2. **Pewarnaan Graf Menggunakan Algoritma Dsatur**:
   - Pewarnaan simpul dengan memprioritaskan derajat saturasi.
   - Mendapatkan jumlah paket soal minimum yang diperlukan untuk setiap sesi.

3. **Visualisasi Pewarnaan Graf**:
   - Menampilkan hasil pewarnaan dalam bentuk graf persegi panjang sesuai layout ruangan.

---

## 🛠️ Teknologi yang Digunakan

- **Python 3.x**
- **NetworkX**: Pemodelan dan manipulasi graf.
- **Matplotlib**: Visualisasi graf dan hasil pewarnaan.

---

## 📂 Struktur Direktori

```
├── src/
│   ├── dsatur_algorithm.py             # Implementasi algoritma Dsatur
│   ├── insert_room_type.py             # Model graf ruang ujian
│   ├── visualization.py                # Visualisasi hasil pewarnaan
├── data/
│   ├── pictures/                       # Gambar
│   ├── references/                     # File-file referensi
├── docs/
├── README.md
```

---

## 🚀 Cara Penggunaan

1. **Clone Repositori**:
   ```bash
   git clone https://github.com/username/dsatur-snbt.git
   cd dsatur-snbt
   ```

2. **Instalasi Dependensi**:
   Pastikan Anda memiliki Python 3.x, lalu install modul yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

3. **Menjalankan Program**:
   - Pilih tipe ruangan dan masukkan dimensi ruangan (m x n).
   - Algoritma akan menghitung jumlah warna (paket soal) yang dibutuhkan.
   ```bash
   python src/main.py
   ```

---

## 📊 Contoh Hasil

### Pewarnaan Graf (Tipe Ruangan 1, 5x6):
Graf dengan 30 peserta:
- **Jumlah paket soal**: 4 warna

### Pewarnaan Graf (Tipe Ruangan 2, 5x6):
Graf dengan 30 peserta:
- **Jumlah paket soal**: 2 warna

---

## 🧑‍💻 Kontributor

- **Maheswara Bayu Kaindra**  
  - [LinkedIn](https://www.linkedin.com/in/maheswarakaindra/)  
  - [Email](mailto:2kaindramaheswara11@gmail.com)

---

## 📝 Lisensi
Proyek ini bersifat **open-source** dan bebas digunakan untuk keperluan penelitian dan edukasi. Kritik dan saran sangat diharapkan untuk pengembangan lebih lanjut.
