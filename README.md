# Sistem Rekomendasi Film
---
## 📌Deskripsi Proyek
Proyek ini bertujuan untuk membangun sistem rekomendasi film menggunakan tiga pendekatan algoritma: Collaborative Filtering (CF), Content-Based Filtering (CBF), dan Hybrid Filtering. Sistem ini bertujuan untuk merekomendasikan film secara akurat berdasarkan preferensi pengguna.

---

## 🎯Tujuan
1. Menghasilkan sistem rekomendasi film yang akurat dan relevan berdasarkan preferensi pengguna.
2. Menggabungkan algoritma CF dan CBF dalam pendekatan Hybrid Filtering untuk menghasilkan rekomendasi yang lebih bervariasi.
3. Membandingkan performa algoritma CF, CBF, dan Hybrid Filtering menggunakan metrik evaluasi Precision, Recall, dan F1.
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
| Goals                                                | Evaluasi Model                         | Dampak terhadap Business Understanding           |
|------------------------------------------------------|----------------------------------------|--------------------------------------------------|
| Menyediakan rekomendasi film dengan akurasi tinggi   | Precision tinggi (1.00)                | ✅ Meningkatkan kepuasan & retensi pengguna       |
| Fokus pada top picks yang benar-benar relevan        | Rekomendasi relevan & tepat sasaran    | ✅ Memperkuat kualitas rekomendasi                |


**Hasil evaluasi menunjukkan bahwa model Collaborative Filtering, Content-Based Filtering, dan Hybrid Filtering memiliki precision yang tinggi, walau recall masih rendah. Artinya, sistem mampu memberikan rekomendasi yang sangat akurat (film yang direkomendasikan memang disukai pengguna), walau belum mampu menjangkau semua film relevan yang mungkin disukai oleh pengguna.**

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
