# E-Commerce Performance Dashboard ✨

## Deskripsi
Dashboard ini merupakan proyek akhir dari analisis data yang bertujuan untuk memberikan *insight* mengenai performa penjualan produk dan preferensi metode pembayaran pada platform e-commerce. Dashboard ini dibangun menggunakan Python dan library Streamlit.

**Fitur Utama:**
- **Best & Worst Performing Products:** Menampilkan top 3 produk dengan penjualan tertinggi dan 3 produk dengan penjualan terendah.
- **Payment Type Usage:** Visualisasi persentase penggunaan berbagai jenis metode pembayaran oleh pelanggan.
- **Identity Sidebar:** Informasi pengembang dashboard.

## Struktur Proyek
- `dashboard/`: Folder utama untuk dashboard.
  - `dashboard.py`: File utama kode Streamlit.
  - `main_data.csv`: Dataset yang telah dibersihkan.
  - `farhan.png`: Foto profil pengembang.
- `requirements.txt`: Daftar library yang dibutuhkan.
- `README.md`: Dokumentasi proyek.

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Streamlit App
```streamlit run dashboard.py```

