# Sistem Rekomendasi Film
---
## 📌Deskripsi Proyek
Proyek ini bertujuan untuk membangun sistem rekomendasi film menggunakan tiga pendekatan algoritma: Collaborative Filtering (CF), Content-Based Filtering (CBF), dan Hybrid Filtering. Sistem ini bertujuan untuk merekomendasikan film secara akurat berdasarkan preferensi pengguna.

---

## 🎯Tujuan
1. Menghasilkan sistem rekomendasi film yang akurat dan relevan berdasarkan preferensi pengguna.
2. Menggabungkan algoritma CF dan CBF dalam pendekatan Hybrid Filtering untuk menghasilkan rekomendasi yang lebih bervariasi.
3. Membandingkan performa algoritma CF, CBF, dan Hybrid Filtering menggunakan metrik evaluasi MSE, RMSE, dan MAE.
---
## 📚Dataset
Dataset yang digunakan terdiri dari beberapa file CSV:
- `movies.csv`: Berisi informasi tentang film.
- `ratings.csv`: Berisi data rating dari pengguna.
- `genres.csv`: Berisi informasi tentang genre film.
- `users.csv`: Berisi data pengguna.
---
## 🪢Algoritma yang Digunakan
1. **Collaborative Filtering (CF)**: Menggunakan interaksi pengguna untuk merekomendasikan film.
2. **Content-Based Filtering (CBF)**: Menggunakan kesamaan konten film untuk memberikan rekomendasi.
3. **Hybrid Filtering**: Menggabungkan CF dan CBF untuk mendapatkan rekomendasi yang lebih akurat dan bervariasi.
---
## 💡Evaluasi Model
Evaluasi dilakukan dengan tiga metrik:
- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Squared Error)**
- **MAE (Mean Absolute Error)**
---
### Hasil Evaluasi
| Algoritma          | MSE    | RMSE   | MAE   |
|-------------------|--------|--------|-------|
| Collaborative Filtering (CF) | 0.3370 | 0.5805 | 0.2707 |
| Content-Based Filtering (CBF) | 32.1889 | 5.6735 | 3.4283 |
| Hybrid Filtering  | 8.1317 | 2.8516 | 1.7434 |

**Dari hasil evaluasi, algoritma Collaborative Filtering menunjukkan performa terbaik dengan nilai MSE, RMSE, dan MAE terendah. Sementara itu, Hybrid Filtering memberikan rekomendasi yang lebih bervariasi dibandingkan CF murni.**

---
## ⚙️Instalasi
Pastikan Anda telah menginstal semua dependensi yang dibutuhkan:
```
pip install -r requirements.txt
```
---
## 🎞️Menjalankan Proyek
1. Jalankan notebook Jupyter atau Google Colab:
   ```
   jupyter notebook Proyek_System_Recommendation_Tsamarah_Muthi'ah_A.ipynb
   ```
2. Ikuti langkah-langkah di dalam notebook untuk melakukan pelatihan dan evaluasi model.

## 🗝️Kesimpulan
> Algoritma Collaborative Filtering merupakan pilihan terbaik untuk akurasi rekomendasi dalam proyek ini. Namun, Hybrid Filtering tetap memiliki nilai tambah dalam hal keragaman rekomendasi.
