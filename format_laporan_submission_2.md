# 📚Laporan Proyek Machine Learning - Tsamarah Muthi'ah Abdullah

## 💡Project Overview
---
**Latar Belakang :**
> Sistem rekomendasi adalah salah satu aplikasi machine learning yang banyak digunakan dalam berbagai sektor, seperti e-commerce, layanan streaming, dan media sosial. Sistem ini dirancang untuk memberikan rekomendasi produk, layanan, atau konten kepada pengguna berdasarkan preferensi atau perilaku mereka. Pentingnya sistem rekomendasi terletak pada kemampuannya untuk meningkatkan pengalaman pengguna, memperkuat keterlibatan, serta mendorong peningkatan penjualan atau penggunaan layanan.

> Menurut penelitian oleh Ricci et al. (2015), sistem rekomendasi dapat meningkatkan pendapatan hingga 20% pada platform e-commerce. Selain itu, layanan streaming seperti Netflix melaporkan bahwa sekitar 80% dari penayangan didorong oleh algoritma rekomendasi (Gomez-Uribe & Hunt, 2015). Oleh karena itu, implementasi sistem rekomendasi merupakan aspek penting dalam dunia digital saat ini.

> Pada proyek ini, akan dikembangkan sistem rekomendasi menggunakan berbagai algoritma untuk membandingkan performa dan efektivitasnya. Fokus utama proyek ini adalah menyelesaikan permasalahan rekomendasi konten pada platform layanan media dengan menggunakan algoritma Collaborative Filtering dan Content-Based Filtering. Selain itu, dilakukan pendekatan Hybrid Filtering untuk menggabungkan kekuatan dari kedua metode tersebut guna menghasilkan rekomendasi yang lebih bervariasi dan mempertimbangkan baik popularitas maupun kesamaan konten.

**Referensi:**

1. Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender Systems Handbook. Springer.

2. Gomez-Uribe, C. A., & Hunt, N. (2015). The Netflix Recommender System: Algorithms, Business Value, and Innovation. ACM Transactions on Management Information Systems.
---
## 🎯Business Understanding

### Problem Statements

1. Bagaimana cara merekomendasikan konten yang sesuai dengan preferensi pengguna secara akurat?

2. Bagaimana menggabungkan algoritma Collaborative Filtering dan Content-Based Filtering guna menghasilkan rekomendasi yang lebih bervariasi dan mempertimbangkan baik popularitas maupun kesamaan konten?

3. Bagaimana membandingkan performa antara algoritma Collaborative Filtering ,Content-Based Filtering, dan Hybrid-Filtering dalam memberikan rekomendasi?

### Goals

1. Menghasilkan sistem rekomendasi film yang akurat dan relevan berdasarkan preferensi pengguna.

2. Menggabungkan kedua algoritma (CF dan CBF) dalam pendekatan Hybrid Filtering untuk memberikan rekomendasi yang lebih bervariasi dengan mempertimbangkan popularitas pengguna dan kesamaan konten.

3. Membandingkan performa algoritma Collaborative Filtering (CF), Content-Based Filtering (CBF), dan Hybrid-Filtering menggunakan metrik evaluasi seperti MSE, RMSE, dan MAE.

### Solution Approach
**1. Menggunakan 2 algoritma utama, yaitu:**
```
A. Collaborative Filtering

- Menggunakan pendekatan berbasis pengguna dan item untuk mengidentifikasi kesamaan antara pengguna atau film.

- Menggunakan teknik Singular Value Decomposition (SVD) untuk memprediksi rating film yang belum ditonton oleh pengguna.

- Menghasilkan rekomendasi film dengan memilih film dengan peringkat tertinggi dalam hasil prediksi.

B. Content-Based Filtering

- Menggunakan fitur konten film (judul, genre) untuk menghasilkan rekomendasi.

- Menggunakan teknik TF-IDF (Term Frequency-Inverse Document Frequency) dan Cosine Similarity untuk mengukur kemiripan antar film.

- Memberikan rekomendasi film serupa dengan film tertentu yang dipilih pengguna.
```
**2. Menggabungkan kedua algoritma dengan metode Hybrid Filtering (CF + CBF)**
Menggabungkan hasil rekomendasi dari Collaborative Filtering dan Content-Based Filtering.

**3. Evaluasi Performa**
Menggunakan metrik seperti MSE, RMSE, dan MAE.

---
## 🔎Data Understanding
```
Dataset yang digunakan pada proyek ini berasal dari MovieLens 100K (https://grouplens.org/datasets/movielens/100k/), yang berisi data rating film oleh pengguna.

Dataset ini terdiri dari beberapa file utama, yaitu:
1. u.data: berisi data rating pengguna terhadap film.
2. u.item: berisi informasi mengenai judul film dan genre.
3. u.user: berisi informasi pengguna.
4. u.genre: berisi daftar genre.
```
**Dataset ini berisi 100.000 rating dari 943 pengguna terhadap 1.682 film. Data ini mencakup informasi mengenai ID pengguna, ID film, rating, dan timestamp.**

Berikut adalah uraian variabel-variabel atau fitur pada tiap dataset:
```
1. Dataset Ratings
userId: Merupakan ID unik dari pengguna yang memberikan rating terhadap film.
movieId: Merupakan ID unik dari film yang diberi rating oleh pengguna.
rating: Merupakan nilai penilaian yang diberikan oleh pengguna terhadap film, dengan rentang 1 hingga 5.
timestamp: Merupakan waktu saat pengguna memberikan rating, disimpan dalam format Unix timestamp.

2. Dataset Movies
movieId: Merupakan ID unik dari film.
video_release_date: Tanggal rilis video dari film tersebut (tidak ada data pada contoh).
unknown: Variabel biner yang menunjukkan apakah genre film tidak diketahui (1 jika ya, 0 jika tidak).
Action: Variabel biner yang menunjukkan apakah film bergenre aksi (1 jika ya, 0 jika tidak).
Adventure: Variabel biner yang menunjukkan apakah film bergenre petualangan (1 jika ya, 0 jika tidak).
Animation: Variabel biner yang menunjukkan apakah film bergenre animasi (1 jika ya, 0 jika tidak).
Children: Variabel biner yang menunjukkan apakah film ditujukan untuk anak-anak (1 jika ya, 0 jika tidak).
Comedy: Variabel biner yang menunjukkan apakah film bergenre komedi (1 jika ya, 0 jika tidak).
Crime: Variabel biner yang menunjukkan apakah film bergenre kriminal (1 jika ya, 0 jika tidak).
Documentary: Variabel biner yang menunjukkan apakah film bergenre dokumenter (1 jika ya, 0 jika tidak).
Drama: Variabel biner yang menunjukkan apakah film bergenre drama (1 jika ya, 0 jika tidak).
Fantasy: Variabel biner yang menunjukkan apakah film bergenre fantasi (1 jika ya, 0 jika tidak).
Film-Noir: Variabel biner yang menunjukkan apakah film bergenre noir (1 jika ya, 0 jika tidak).
Horror: Variabel biner yang menunjukkan apakah film bergenre horor (1 jika ya, 0 jika tidak).
Musical: Variabel biner yang menunjukkan apakah film bergenre musikal (1 jika ya, 0 jika tidak).
Mystery: Variabel biner yang menunjukkan apakah film bergenre misteri (1 jika ya, 0 jika tidak).
Romance: Variabel biner yang menunjukkan apakah film bergenre romantis (1 jika ya, 0 jika tidak).
Sci-Fi: Variabel biner yang menunjukkan apakah film bergenre fiksi ilmiah (1 jika ya, 0 jika tidak).
Thriller: Variabel biner yang menunjukkan apakah film bergenre thriller (1 jika ya, 0 jika tidak).
War: Variabel biner yang menunjukkan apakah film bergenre perang (1 jika ya, 0 jika tidak).
Western: Variabel biner yang menunjukkan apakah film bergenre barat atau koboi (1 jika ya, 0 jika tidak).

3. Dataset Users
userId: Merupakan ID unik dari pengguna dalam dataset.
age: Merupakan usia pengguna dalam satuan tahun.

4. Dataset Genres
genreId: Merupakan ID unik dari genre film.
```

**Insight Statistik Deskriptif Ratings:**
```
1. Sebagian besar rating berada di kisaran 3 hingga 4, dengan nilai rata-rata 3.53.
2. Rating minimum adalah 1 dan maksimum adalah 5, menunjukkan adanya variasi pendapat pengguna terhadap film.
3. User ID tersebar secara merata dari 1 hingga 943, menunjukkan banyaknya pengguna yang memberikan rating.
4. Waktu pemberian rating berkisar dalam rentang waktu yang cukup luas.
```
**Insight Statistik Deskriptif Movies:**
```
1. Terdapat 1.682 film dengan berbagai genre.
2. Genre paling umum adalah Comedy (30%), diikuti Action (15%) dan Romance (14.7%).
3. Beberapa genre sangat jarang muncul, seperti Fantasy (1.3%), Film-Noir (1.4%), dan Western (1.6%).
```

**Insight Statistik Deskriptif Users:**
```
1. Terdapat 943 pengguna dengan rentang usia dari 7 hingga 73 tahun.
2. Rata-rata usia pengguna adalah sekitar 34 tahun, menunjukkan dominasi pengguna dewasa muda.
3. Mayoritas pengguna berusia antara 25 hingga 43 tahun, yang merupakan segmen pengguna paling aktif.
```
**Insight Statistik Deskriptif Genres:**
```
1. Terdapat 19 genre film dalam dataset.
2. Genre dengan ID maksimum adalah 18, sementara ID minimum adalah 0, menandakan adanya berbagai macam kategori film.
3. Genre rata-rata memiliki ID di sekitar angka 9, dengan variasi yang cukup besar.
```

## ✨ Data Preparation

**Pada tahap ini, dilakukan pengecekan dan penanganan data hilang, serta transformasi data.** 
```
Mengapa Tahap Data Preparation Diperlukan:
- Mengatasi data yang hilang agar tidak mengganggu proses analisis dan model.
- Melakukan transformasi agar data lebih terstruktur dan dapat digunakan oleh model.
- Menghasilkan data yang lebih konsisten dan bebas dari error yang dapat mempengaruhi hasil prediksi.
- Meningkatkan akurasi dan kinerja model dengan data yang bersih dan terstruktur.
```

**A. Data Cleaning**
Mengatasi permasalahan nilai hilang agar model tidak mengalami error atau bias.

**B. Transformasi Data**
Melakukan transformasi data sehingga lebih mudah diolah pada tahap modeling.

**C. Penggabungan Dataset**
Dataset ratings dan movies digabungkan berdasarkan kolom movieId. Hal ini dilakukan untuk mempermudah pembuatan matriks user-item yang mengandung informasi rating dan judul film.

**D. Data Splitting**
Pada Tahap ini data dibagi menjadi 80/20 untuk data training dan data testing.

## 📹Modeling
```
Kelebihan: CF dapat memanfaatkan interaksi pengguna, sedangkan CBF dapat merekomendasikan item baru.
Kekurangan: CF membutuhkan data yang cukup banyak dan padat, sementara CBF bergantung pada informasi konten.
```
## Evaluation
`Matriks Evaluasi yang digunakan yaitu MSE, RMSE, dan MAE.`

**MSE (Mean Squared Error):**
```
- Mengukur rata-rata kesalahan kuadrat antara nilai prediksi dan nilai aktual. Semakin kecil nilainya, semakin baik model dalam memprediksi nilai sebenarnya.
- Formula: MSE = (1/n) * Σ(actual - predicted)^2
- Metrik ini bekerja dengan menghitung selisih antara nilai aktual dan nilai prediksi, kemudian mengkuadratkan selisih tersebut dan menghitung rata-ratanya.
- MSE sangat sensitif terhadap outlier karena menggunakan kuadrat dari kesalahan.
```

**RMSE (Root Mean Squared Error):**
```
- Akar dari MSE, mengembalikan satuan data asli sehingga lebih mudah diinterpretasikan. Semakin rendah, semakin baik.
- Formula: RMSE = sqrt(MSE)
- Metrik ini bekerja dengan menghitung akar dari MSE, sehingga lebih mudah dipahami dalam konteks satuan aslinya.
```
**MAE (Mean Absolute Error):**
```
- Mengukur rata-rata kesalahan absolut antara nilai prediksi dan aktual. Semakin kecil nilainya, semakin akurat prediksi model.
- Formula: MAE = (1/n) * Σ|actual - predicted|
- Metrik ini bekerja dengan menghitung rata-rata dari nilai absolut kesalahan prediksi.
```

**Berdasarkan hasil evaluasi:**
```
1. Model Collaborative Filtering (CF) menunjukkan performa terbaik dengan nilai MSE sebesar 0.3370, RMSE sebesar 0.5805, dan MAE sebesar 0.2707, mengindikasikan bahwa CF mampu memberikan rekomendasi dengan tingkat kesalahan yang rendah.

2. Sebaliknya, Content-Based Filtering (CBF) memiliki performa yang lebih rendah dengan MSE sebesar 32.1889, RMSE sebesar 5.6735, dan MAE sebesar 3.4283, yang menunjukkan bahwa model ini kurang akurat dalam memprediksi rating pengguna.

3. Sementara itu, Hybrid Filtering yang menggabungkan CF dan CBF menghasilkan nilai MSE sebesar 8.1317, RMSE sebesar 2.8516, dan MAE sebesar 1.7434, yang lebih baik daripada CBF tetapi masih lebih rendah dibandingkan dengan CF.
```
---
> Dari hasil tersebut, dapat disimpulkan bahwa Collaborative Filtering (CF) merupakan pilihan terbaik dalam hal akurasi rekomendasi pada kasus ini.
---

## 📌Kesimpulan Akhir :
---
> Dari hasil evaluasi dan perbandingan metode, dapat disimpulkan bahwa pendekatan Collaborative Filtering (CF) memberikan hasil prediksi dengan tingkat kesalahan yang paling rendah dibandingkan metode lainnya, dengan nilai MSE (0.3370), RMSE (0.5805), dan MAE (0.2707). Hal ini menunjukkan bahwa CF mampu menghasilkan rekomendasi dengan akurasi yang sangat baik.

> Metode Content-Based Filtering (CBF) menunjukkan performa yang kurang optimal dengan nilai kesalahan yang cukup tinggi (MSE: 32.1889, RMSE: 5.6735, MAE: 3.4283). Hal ini menunjukkan bahwa model CBF kurang efektif dalam memberikan rekomendasi yang akurat jika dibandingkan dengan CF.

> Sementara itu, pendekatan Hybrid Filtering yang menggabungkan kekuatan CF dan CBF menghasilkan performa yang berada di tengah-tengah, dengan nilai MSE (8.1317), RMSE (2.8516), dan MAE (1.7434). Meskipun hasilnya tidak sebaik CF secara murni, pendekatan ini tetap memberikan rekomendasi yang lebih bervariasi dengan mempertimbangkan popularitas pengguna (CF) dan kesamaan konten (CBF).
---
---
> **Saran:** Pemilihan metode yang tepat bergantung pada tujuan implementasi. Jika mengutamakan akurasi rekomendasi, Collaborative Filtering (CF) lebih unggul. Namun, jika membutuhkan rekomendasi yang lebih bervariasi dan tidak hanya mengandalkan data perilaku pengguna, Hybrid Filtering dapat menjadi pilihan yang lebih seimbang.
---

_Catatan:_
_Semua detail penjelasan setiap tahapan juga sudah ada dalam notebook._
