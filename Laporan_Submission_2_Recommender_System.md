# 📚Laporan Proyek Machine Learning - Tsamarah Muthi'ah Abdullah

## 💡Project Overview
---
**Latar Belakang :**
> Sistem rekomendasi telah menjadi bagian penting dalam industri film digital, terutama dengan semakin populernya platform layanan streaming seperti Netflix, Disney+, dan Amazon Prime Video. Dalam konteks dunia film, sistem rekomendasi berperan penting untuk membantu pengguna menemukan film atau serial yang sesuai dengan preferensi mereka, tanpa harus mencarinya secara manual di antara ribuan judul yang tersedia. Hal ini tidak hanya meningkatkan kenyamanan pengguna, tetapi juga memperpanjang waktu keterlibatan pengguna di platform dan mendorong loyalitas terhadap layanan tersebut.

> Sistem rekomendasi diperlukan dalam bidang film karena tingginya volume konten yang terus bertambah setiap harinya. Tanpa sistem yang cerdas, pengguna bisa mengalami overload informasi, kesulitan menemukan film yang sesuai dengan selera mereka, atau bahkan berhenti menggunakan layanan karena merasa kebingungan dalam memilih. Dengan memberikan saran yang dipersonalisasi, sistem rekomendasi mampu meningkatkan pengalaman menonton, membuat pengguna merasa dipahami, dan mendorong eksplorasi konten yang lebih luas.

> Menurut penelitian oleh Ricci et al. (2015), sistem rekomendasi dapat meningkatkan pendapatan hingga 20% pada platform digital. Sementara itu, Netflix melaporkan bahwa sekitar 80% dari total penayangan berasal dari saran yang diberikan oleh sistem rekomendasi mereka (Gomez-Uribe & Hunt, 2015). Hal ini menunjukkan betapa besar pengaruh algoritma rekomendasi terhadap perilaku pengguna dalam mengakses konten film.

> Pada proyek ini, akan dikembangkan sistem rekomendasi khusus untuk konten film dengan menggunakan berbagai pendekatan algoritma, seperti Collaborative Filtering dan Content-Based Filtering. Selain itu, pendekatan Hybrid Filtering juga akan diterapkan untuk menggabungkan keunggulan dari kedua metode guna menghasilkan rekomendasi yang lebih beragam. Tujuan akhir dari proyek ini adalah menciptakan sistem yang dapat memberikan rekomendasi film yang relevan berdasarkan minat serta riwayat tontonan pengguna.

**Referensi:**

1. Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender Systems Handbook. Springer.

2. Gomez-Uribe, C. A., & Hunt, N. (2015). The Netflix Recommender System: Algorithms, Business Value, and Innovation. ACM Transactions on Management Information Systems.
---
## 🎯Business Understanding

### Problem Statements

1. Bagaimana menyediakan rekomendasi film yang relevan dan tepat sasaran, meskipun cakupan item yang direkomendasikan masih terbatas?

2. Bagaimana membangun sistem rekomendasi yang efisien untuk membantu pengguna menemukan film-film berkualitas tinggi yang sesuai dengan selera mereka?

### Goals

1. Menyediakan rekomendasi film dengan akurasi tinggi (high precision), agar pengalaman pengguna lebih menyenangkan dan terpercaya.

2. Fokus pada top picks yang benar-benar relevan, meskipun jumlah film yang terjangkau masih terbatas.

### Solution Approach
**1. Menggunakan 2 algoritma utama, yaitu:**
```
A. Collaborative Filtering

- Menggunakan SVD untuk memprediksi rating berdasarkan interaksi pengguna.

- Efektif menghasilkan rekomendasi yang sangat sesuai untuk pengguna aktif.

- Memiliki precision tinggi, cocok untuk menyajikan film yang "pasti disukai".

B. Content-Based Filtering

- Menggunakan kemiripan konten (judul & genre) untuk membuat rekomendasi berdasarkan film yang sudah disukai.

- Menggunakan teknik TF-IDF (Term Frequency-Inverse Document Frequency) dan Cosine Similarity untuk mengukur kemiripan antar film.

- Memberikan rekomendasi film serupa dengan film tertentu yang dipilih pengguna.
```
**2. Menggabungkan kedua algoritma dengan metode Hybrid Filtering (CF + CBF)**

- Menggabungkan hasil rekomendasi dari Collaborative Filtering dan Content-Based Filtering.
- Memastikan rekomendasi lebih bervariasi dan mempertimbangkan baik popularitas pengguna maupun kesamaan konten.

**3. Evaluasi Performa**

Menggunakan metrik seperti Precision, Recall, dan F1.

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
[Link Dataset](https://grouplens.org/datasets/movielens/100k/)

**Dataset ini berisi 100.000 rating dari 943 pengguna terhadap 1.682 film. Data ini mencakup informasi mengenai ID pengguna, ID film, rating, dan timestamp.**

**Kondisi dataset 'movies' memiliki beberapa nilai hilang, terutama pada kolom release_date (1 nilai hilang), video_release_date (1.682 nilai hilang), dan IMDb_URL (3 nilai hilang). Sementara itu, dataset 'ratings', 'genres', dan 'users' tidak memiliki nilai hilang.**

Berikut adalah uraian variabel-variabel atau fitur pada tiap dataset:
```
1. Dataset Ratings
userId: Merupakan ID unik dari pengguna yang memberikan rating terhadap film.
movieId: Merupakan ID unik dari film yang diberi rating oleh pengguna.
rating: Merupakan nilai penilaian yang diberikan oleh pengguna terhadap film, dengan rentang 1 hingga 5.
timestamp: Merupakan waktu saat pengguna memberikan rating, disimpan dalam format Unix timestamp.

2. Dataset Movies
movieId: Merupakan ID unik dari film.
Title: Merupakan Judul film.
release_date: Merupakan tanggal rilis film.
video_release_date: Tanggal rilis video dari film tersebut (tidak ada data pada contoh).
IMDb_URL: Merupakan kolom yang menyimpan tautan ke halaman film di situs IMDb.
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
gender: Menunjukkan jenis kelamin pengguna.
occupation: Menunjukkan pekerjaan pengguna.
zip_code: Menunjukkan kode pos pengguna sebagai representasi dari lokasi geografis mereka.

4. Dataset Genres
genre: Merupakan genre film.
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

**Data preparation adalah tahap penting sebelum analisis atau modeling, karena bertujuan untuk menghasilkan data yang bersih, terstruktur, dan siap digunakan oleh algoritma. Berikut adalah tahapan-tahapan lengkapnya:**

**1. Mengubah File `.u` Menjadi `.csv`**
- File asli dari dataset MovieLens diubah ke format .csv agar bisa diolah menggunakan Python (pandas).

**2. Transformasi Kolom Timestamp**
`ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')`

**Penjelasan:** Mengubah kolom timestamp dari format Unix time (detik) ke format datetime agar lebih mudah dianalisis.

**3. Pengecekan dan Penanganan Data Hilang**

**Penjelasan:** Kondisi dataset 'movies' memiliki beberapa nilai hilang, terutama pada kolom release_date (1 nilai hilang), video_release_date (1.682 nilai hilang), dan IMDb_URL (3 nilai hilang). Sementara itu, dataset 'ratings', 'genres', dan 'users' tidak memiliki nilai hilang.

`movies.drop(columns=['video_release_date'], inplace=True)`

**Penjelasan:** Menghapus kolom yang seluruhnya kosong karena tidak berguna untuk analisis.

`movies.dropna(subset=['release_date', 'IMDb_URL'], inplace=True)`

**Penjelasan:** Menghapus baris yang memiliki data penting (seperti release_date atau IMDb_URL) yang kosong, agar tidak mengganggu proses selanjutnya.

**4. Penggabungan Data ratings dan movies**

`data = pd.merge(ratings, movies, on='movieId')`
**Penjelasan:** Penggabungan ini menyatukan informasi rating dan informasi film (judul, tanggal rilis, genre, dll.) dalam satu dataframe. Penting untuk membuat fitur gabungan dan membangun matriks user-item yang lengkap.

**5. Transformasi Data ke User-Item Matrix**

`user_item_matrix = data.pivot(index='userId', columns='movieId', values='rating').fillna(0)`

**Penjelasan:** Mengubah data ke bentuk matriks 2D (user x movie) yang berisi nilai rating. Nilai kosong diisi dengan 0 sebagai tanda user belum memberikan rating.

**6. Konversi ke Sparse Matrix**

`user_item_matrix_sparse = csr_matrix(user_item_matrix)`

**Penjelasan:** Menghemat memori dan mempercepat komputasi dengan merepresentasikan matriks besar (dengan banyak nol) dalam format sparse.

**7. Ekstraksi Fitur dari Judul dan Genre Film (TF-IDF)**
`
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined'].fillna(''))
`
**Penjelasan:**

- Mengubah teks judul film menjadi vektor numerik menggunakan metode TF-IDF.
- TF-IDF (Term Frequency-Inverse Document Frequency) mengukur seberapa penting suatu kata dalam dokumen (judul) relatif terhadap keseluruhan dokumen.
- Representasi ini digunakan dalam Content-Based Filtering untuk mencari kemiripan antar film berdasarkan **judul dan genre**.


## 📹Modeling
```
Kelebihan: CF dapat memanfaatkan interaksi pengguna, sedangkan CBF dapat merekomendasikan item baru.
Kekurangan: CF membutuhkan data yang cukup banyak dan padat, sementara CBF bergantung pada informasi konten.

Berikut penjelasan cara kerja setiap algoritma yang digunakan dalam solusi rekomendasi beserta parameter yang digunakan:

1. Collaborative Filtering (CF) - Singular Value Decomposition (SVD)
Collaborative Filtering menggunakan pendekatan berbasis pengguna dan item untuk mengidentifikasi pola preferensi pengguna berdasarkan interaksi sebelumnya. Dalam implementasi ini, digunakan Singular Value Decomposition (SVD) untuk memprediksi rating film yang belum ditonton pengguna.

📌Cara Kerja:

- Membentuk User-Item Matrix, yaitu matriks yang merepresentasikan hubungan antara pengguna (user) dan film (item) berdasarkan rating yang diberikan. Jika pengguna belum memberikan rating, nilai diisi dengan 0. pivot() digunakan untuk membuat matriks pengguna-item.

- Mengubah matriks ini menjadi format sparse matrix menggunakan csr_matrix() dari SciPy, karena sebagian besar nilai dalam matriks ini adalah nol (sparsity).

- Menggunakan SVD (svds()) untuk mendekomposisi matriks menjadi tiga komponen:

  1. U: Matriks fitur pengguna (dimensi: jumlah pengguna × k)

  2. σ (sigma): Matriks diagonal dengan singular values (dimensi: k × k)

  3. Vt: Matriks fitur film (dimensi: k × jumlah film)

- Melakukan perkalian kembali U × sigma × Vt untuk membentuk matriks prediksi rating.

- Hasilnya digunakan untuk merekomendasikan film dengan prediksi rating tertinggi bagi pengguna.

🪢Parameter yang Digunakan:

- k=50 → Menentukan jumlah fitur laten (latent factors) dalam dekomposisi SVD. Default tidak digunakan; angka 50 dipilih untuk keseimbangan antara akurasi dan efisiensi.

- fillna(0) → Mengisi nilai kosong dalam user-item matrix dengan 0 agar bisa diproses oleh SVD.

- csr_matrix(user_item_matrix) → Mengubah user-item matrix menjadi sparse matrix agar lebih efisien dalam penyimpanan dan komputasi.

2. Content-Based Filtering (CBF) - TF-IDF & Cosine Similarity
Content-Based Filtering merekomendasikan film berdasarkan kesamaan atribut film, dalam hal ini menggunakan judul film sebagai fitur untuk menemukan kemiripan antar film dan Cosine Similarity.

📌Cara Kerja:

- Menggunakan TF-IDF (Term Frequency - Inverse Document Frequency) untuk mengubah judul film menjadi representasi vektor yang lebih bermakna.

- Menghitung cosine similarity antar film berdasarkan representasi TF-IDF untuk menemukan film yang mirip satu sama lain.

- Film yang memiliki nilai similarity tertinggi dengan film yang telah ditonton pengguna akan direkomendasikan. Cosine Similarity menghitung kesamaan antar film berdasarkan vektor TF-IDF.

Ket : Nilai cosine similarity berada di rentang 0 hingga 1, dengan 1 berarti sangat mirip.

🪢Parameter yang Digunakan:

- stop_words='english' → Menghilangkan kata-kata umum dalam bahasa Inggris yang tidak relevan untuk analisis.

- fillna('') → Mengisi nilai kosong dalam kolom judul film agar tidak menyebabkan error saat diproses oleh TF-IDF.

- cosine_similarity(tfidf_matrix) → Menghitung kesamaan antar film berdasarkan hasil vektorisasi TF-IDF.

3. Model hybrid dalam proyek ini menggabungkan prediksi dari Collaborative Filtering (CF) dan Content-Based Filtering (CBF) secara linier, untuk menghasilkan rekomendasi yang lebih seimbang antara preferensi pengguna dan kemiripan konten film.

📌 Konsep Penggabungan:

1. CF Prediction (pred_ratings_df):

Prediksi rating yang dihasilkan oleh model Singular Value Decomposition (SVD) berdasarkan pola interaksi pengguna terhadap film.

2. CBF Prediction (user_item_matrix @ content_sim):

Skor preferensi berdasarkan kemiripan konten antar film, dihitung melalui dot product antara user_item_matrix dan matriks kemiripan konten (content_sim).

Hybrid Score: Gabungan linier dari CF dan CBF dengan formula:

[hybrid_score = alpha * cf_score + (1 - alpha) * cbf_score]

Nilai alpha = 0.5 digunakan untuk memberi bobot seimbang antara CF dan CBF.

📈 Keunggulan Model Hybrid:

✅ Mengombinasikan kekuatan dua pendekatan:

- CF memanfaatkan interaksi pengguna-berbasis rating.

- CBF mempertimbangkan fitur konten dari film (misalnya judul, genre).

🔄 Mengurangi masalah cold-start:

- Cold-start item: Film baru tanpa rating tetap bisa direkomendasikan melalui kemiripan konten (CBF).

- Cold-start user: Jika user memiliki beberapa interaksi, CF tetap bisa berkontribusi dalam prediksi.

🎯 Rekomendasi lebih personal dan relevan, karena mempertimbangkan baik preferensi eksplisit pengguna maupun kemiripan film yang pernah disukai.
```

### Hasil Top-N Rekomendasi
**✅ Rekomendasi CF untuk User ID = 1 (Top-10):**
- Toy Story (1995)
- Usual Suspects, The (1995)
- Star Wars (1977)
- Blade Runner (1982)
- Fargo (1996)
- 2001: A Space Odyssey (1968)
- Aliens (1986)
- Alien (1979)
- Chasing Amy (1997)
- Full Monty, The (1997)

**✅ Rekomendasi CBF untuk Movie ID 1 (Top-10):**
- Pyromaniac's Love Story, A (1995)
- Balto (1995)
- Goofy Movie, A (1995)
- NeverEnding Story III, The (1994)
- Pocahontas (1995)
- FairyTale: A True Story (1997)
- Philadelphia Story, The (1940)
- Story of Xinghua, The (1993)
- Gumby: The Movie (1995)
- Aladdin (1992)

**✅ Rekomendasi Hybrid untuk User 1 (Top-10):**
- Star Wars (1977)
- Fargo (1996)
- Empire Strikes Back, The (1980)
- Aliens (1986)
- Alien (1979)
- Terminator, The (1984)
- Star Trek: First Contact (1996)
- Sneakers (1992)
- Men in Black (1997)
- Contact (1997)

## Evaluation

### Collaborative Filtering	
**1. Precision@10: 1.00**

Precision yang mendekati 1 berarti hampir semua rekomendasi yang diberikan relevan (maksudnya, dari 10 film yang direkomendasikan, hampir semuanya adalah film yang disukai oleh pengguna).

**2. Recall@10: 0.06**

Recall yang rendah menunjukkan bahwa meskipun rekomendasi sangat tepat (high precision), hanya sebagian kecil dari total film relevan yang disukai oleh pengguna yang ditemukan di rekomendasi. Ini mungkin disebabkan oleh jumlah film relevan yang lebih sedikit dibandingkan jumlah rekomendasi yang diberikan.

**3. F1 Score@10: 0.12**

F1 Score yang rendah menunjukkan adanya trade-off antara Precision dan Recall, dengan Precision yang baik tetapi Recall yang rendah. Ini bisa jadi karena jumlah film relevan terbatas yang tersedia untuk pengguna, yang membuat recall rendah.

### Content-Based Filtering	
**Precision@10 = 0.70** → Dari 10 film yang direkomendasikan, hanya 7 yang dianggap relevan (disukai oleh user yang juga menyukai Movie ID 1).

**Recall@10 = 0.01** → Dari semua film yang disukai oleh user yang juga menyukai Movie ID 1, hanya 1% yang berhasil ditemukan dalam rekomendasi.

**F1 Score = 0.01** → Meskipun precision tinggi (0.70), recall yang sangat rendah (0.01) membuat F1 score ikut rendah. Ini berarti bahwa meskipun sebagian besar
**Tujuan:** Rekomendasi item

### Hybrid Filtering

**📊 Precision@10: 1.00**

Artinya 10 dari 10 film yang direkomendasikan ternyata disukai user (rating ≥ 4). Ini menunjukkan akurasi rekomendasi sangat tinggi dalam hal kesesuaian.

**📈 Recall@10: 0.06**

Dari semua film yang disukai oleh user, hanya sekitar 6% yang berhasil ditangkap oleh Top-10 rekomendasi. Ini menunjukkan bahwa cakupan rekomendasi masih terbatas terhadap keseluruhan preferensi user.

**🎯 F1 Score@10: 0.12**

Kombinasi dari precision dan recall. Meskipun precision sangat tinggi, recall yang rendah menurunkan F1 Score, artinya model masih bisa ditingkatkan dalam menjangkau lebih banyak film relevan bagi user.

**Penjelasan:**

1. Precision
   **Mengukur seberapa banyak item yang direkomendasikan di Top-K yang benar-benar relevan bagi pengguna.**
   _Precision@K= Jumlah item relevan di Top-K / K_
   > Nilainya antara 0 dan 1. Semakin tinggi, semakin baik.

2. Recall
   **Recall@K mengukur seberapa banyak item yang relevan bagi pengguna yang berhasil direkomendasikan dalam Top-K.**
   _Recall@K= Jumlah item relevan di Top-K / Jumlah total item relevan untuk user_
   > Recall tinggi berarti sistem berhasil "menemukan" sebagian besar item relevan.

3. F1
   **F1@K adalah harmonic mean dari Precision@K dan Recall@K, digunakan untuk menyeimbangkan keduanya.**
   _F1@K=2× Precision@K×Recall@K / Precision@K+Recall@K_
   > Cocok jika ingin sistem yang tidak hanya akurat (precision) tapi juga komprehensif (recall).
​

## 📌Kesimpulan Akhir :
---
> Hasil evaluasi menunjukkan bahwa model **Collaborative Filtering**, **Content-Based Filtering**, dan **Hybrid Filtering** memiliki precision yang tinggi, walau recall masih rendah. Artinya, sistem mampu memberikan rekomendasi yang sangat akurat (film yang direkomendasikan memang disukai pengguna), walau belum mampu menjangkau semua film relevan yang mungkin disukai oleh pengguna.

- Precision tinggi (1.00) → rekomendasi tepat sasaran, meningkatkan kepercayaan dan kenyamanan pengguna.

- Recall rendah (0.06) → sistem belum mampu menjangkau seluruh preferensi pengguna, tetapi tetap menjaga kualitas rekomendasi.

- F1 Score rendah (0.12) → menjadi sinyal bahwa cakupan sistem masih bisa dikembangkan lebih luas untuk memperbaiki keseimbangan akurasi dan jangkauan.

### **💡Analisis Terhadap Business Understanding**
---
1. **Rekomendasi berkualitas tinggi**, meskipun belum mencakup semua kemungkinan preferensi.

  - Ini cocok dengan hasil precision tinggi → sistem sudah efektif untuk menyajikan film yang pasti disukai.

2. **Efisiensi dan kepercayaan pengguna** dalam eksplorasi konten.
---

|Goals                                              | Evaluasi Model                      | Dampak terhadap Business Understanding      |
| Menyediakan rekomendasi film dengan akurasi tinggi | Precision tinggi (1.00)             | ✅ Meningkatkan kepuasan & retensi pengguna |
| Fokus pada top picks yang benar-benar relevan      | Rekomendasi relevan & tepat sasaran | ✅ Memperkuat kualitas rekomendasi          

_Catatan:_
_Semua detail penjelasan setiap tahapan juga sudah ada dalam notebook._

📧 Hubungi saya melalui [GitHub](https://github.com/MuthiahAinun) jika ada pertanyaan.
