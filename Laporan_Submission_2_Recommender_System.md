# 📚Laporan Proyek Machine Learning - Tsamarah Muthi'ah Abdullah

## 💡Project Overview
---
**Latar Belakang :**
> Sistem rekomendasi telah menjadi bagian penting dalam industri film digital, terutama dengan semakin populernya platform layanan streaming seperti Netflix, Disney+, dan Amazon Prime Video. Dalam konteks dunia film, sistem rekomendasi berperan penting untuk membantu pengguna menemukan film atau serial yang sesuai dengan preferensi mereka, tanpa harus mencarinya secara manual di antara ribuan judul yang tersedia. Hal ini tidak hanya meningkatkan kenyamanan pengguna, tetapi juga memperpanjang waktu keterlibatan pengguna di platform dan mendorong loyalitas terhadap layanan tersebut.

> Sistem rekomendasi diperlukan dalam bidang film karena tingginya volume konten yang terus bertambah setiap harinya. Tanpa sistem yang cerdas, pengguna bisa mengalami overload informasi, kesulitan menemukan film yang sesuai dengan selera mereka, atau bahkan berhenti menggunakan layanan karena merasa kebingungan dalam memilih. Dengan memberikan saran yang dipersonalisasi, sistem rekomendasi mampu meningkatkan pengalaman menonton, membuat pengguna merasa dipahami, dan mendorong eksplorasi konten yang lebih luas.

> Menurut penelitian oleh Ricci et al. (2015), sistem rekomendasi dapat meningkatkan pendapatan hingga 20% pada platform digital. Sementara itu, Netflix melaporkan bahwa sekitar 80% dari total penayangan berasal dari saran yang diberikan oleh sistem rekomendasi mereka (Gomez-Uribe & Hunt, 2015). Hal ini menunjukkan betapa besar pengaruh algoritma rekomendasi terhadap perilaku pengguna dalam mengakses konten film.

> Pada proyek ini, akan dikembangkan sistem rekomendasi khusus untuk konten film dengan menggunakan berbagai pendekatan algoritma, seperti Collaborative Filtering dan Content-Based Filtering. Selain itu, pendekatan Hybrid Filtering juga akan diterapkan untuk menggabungkan keunggulan dari kedua metode guna menghasilkan rekomendasi yang lebih beragam. Tujuan akhir dari proyek ini adalah menciptakan sistem yang dapat memberikan rekomendasi film yang relevan dan memuaskan berdasarkan minat serta riwayat tontonan pengguna.

**Referensi:**

1. Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender Systems Handbook. Springer.

2. Gomez-Uribe, C. A., & Hunt, N. (2015). The Netflix Recommender System: Algorithms, Business Value, and Innovation. ACM Transactions on Management Information Systems.
---
## 🎯Business Understanding

### Problem Statements

1. Bagaimana meningkatkan keterlibatan pengguna dengan menyediakan rekomendasi film yang lebih personal dan sesuai dengan preferensi mereka?

2. Bagaimana menciptakan sistem rekomendasi yang mampu meningkatkan loyalitas pelanggan dengan mempertimbangkan popularitas dan relevansi konten?

3. Bagaimana mengembangkan strategi rekomendasi yang dapat mengoptimalkan pengalaman pengguna sekaligus meningkatkan potensi pendapatan bisnis melalui langganan atau iklan?

### Goals

1. Meningkatkan retensi pelanggan dengan menyediakan rekomendasi yang lebih akurat dan relevan untuk meningkatkan kepuasan pengguna.

2. Mengembangkan sistem rekomendasi yang tidak hanya mempertimbangkan kesukaan pengguna tetapi juga memperhitungkan tren pasar dan popularitas konten untuk mendorong pertumbuhan bisnis.

3. Mengevaluasi efektivitas strategi rekomendasi dalam meningkatkan keterlibatan pengguna dan konversi pelanggan, dengan tujuan mendukung pertumbuhan bisnis dan monetisasi platform secara optimal.

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

- Menggabungkan hasil rekomendasi dari Collaborative Filtering dan Content-Based Filtering.
- Memastikan rekomendasi lebih bervariasi dan mempertimbangkan baik popularitas pengguna maupun kesamaan konten.

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

**Pada tahap ini langkah yang dilakukan yaitu mengubah .u file menjadi csv file, pengecekan dan penanganan data hilang, transformasi data, penggabungan dataset ratings dan movies untuk mempermudah pembuatan matriks user-item yang mengandung informasi rating dan judul film pembagian data, serta Menggunakan TF-IDF Vectorizer untuk algoritma CBF untuk mengubah judul film menjadi representasi vektor numerik yang bermakna.** 
```
Mengapa Tahap Data Preparation Diperlukan:
- Mengatasi data yang hilang agar tidak mengganggu proses analisis dan model.
- Melakukan transformasi agar data lebih terstruktur dan dapat digunakan oleh model.
- Menghasilkan data yang lebih konsisten dan bebas dari error yang dapat mempengaruhi hasil prediksi.
- Meningkatkan akurasi dan kinerja model dengan data yang bersih dan terstruktur.
```
Berikut detail tahapannya :

**A. Data Cleaning**

Mengatasi permasalahan nilai hilang agar model tidak mengalami error atau bias.

**Kondisi dataset 'movies' memiliki beberapa nilai hilang, terutama pada kolom release_date (1 nilai hilang), video_release_date (1.682 nilai hilang), dan IMDb_URL (3 nilai hilang). Sementara itu, dataset 'ratings', 'genres', dan 'users' tidak memiliki nilai hilang.**

**B. Transformasi Data**

Melakukan transformasi data timestamp ke datetime sehingga lebih mudah diolah pada tahap modeling. 

**C. Penggabungan Dataset**

Dataset ratings dan movies digabungkan berdasarkan kolom movieId. Hal ini dilakukan untuk mempermudah pembuatan matriks user-item yang mengandung informasi rating dan judul film.

**D. Data Splitting**

Pada Tahap ini data dibagi menjadi 80/20 untuk data training dan data testing.

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

3. Model hybrid dalam proyek ini menggabungkan hasil prediksi dari model Collaborative Filtering dan Content-Based Filtering secara linier, untuk mendapatkan prediksi rating yang lebih beragam.

📌 Konsep Penggabungan:
- CF Prediction (pred_ratings): Hasil dari model SVD.

- CBF Prediction (cbf_pred): Dihitung dari dot product antara user_item_matrix dan content_sim, sehingga mewakili skor preferensi berdasarkan kemiripan konten.

- Hybrid Score: Gabungan linier dari keduanya menggunakan bobot alpha = 0.5 agar kombinasi seimbang.

📈 Keunggulan:

- Menyeimbangkan antara kekuatan CF (menggunakan data interaksi pengguna) dan CBF (menggunakan konten item).
- Mengatasi cold-start item (dari sisi CBF) dan cold-start user (jika punya cukup rating item mirip).
```

### Hasil Top-N Rekomendasi
**Hasil Collaborative Filtering (User ID = 1):**
- Toy Story (1995): Film animasi keluarga dengan cerita persahabatan mainan.
- Star Wars (1977): Film fiksi ilmiah klasik tentang perjuangan melawan Kekaisaran.
- Blade Runner (1982): Film fiksi ilmiah bertema dystopia dan robot manusia.
- Fargo (1996): Drama kriminal dengan cerita penuh misteri.
- 2001: A Space Odyssey (1968): Film fiksi ilmiah epik karya Stanley Kubrick.
- Aliens (1986) dan Alien (1979): Film horor fiksi ilmiah dengan tema invasi alien.
- Chasing Amy (1997) dan Full Monty, The (1997): Film drama dan komedi romantis.

**Hasil Content-Based Filtering (Movie ID = 1):**
- Pyromaniac's Love Story, A (1995): Drama romantis dengan kisah cinta yang tidak biasa.
- Philadelphia Story, The (1940): Drama komedi romantis klasik.
- NeverEnding Story III, The (1994): Film petualangan fantasi keluarga.
- FairyTale: A True Story (1997): Film drama keluarga dengan unsur fantasi.
- Police Story 4: Project S (1993): Film aksi petualangan dengan elemen seni bela diri.


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
1. Model Collaborative Filtering (CF) memberikan hasil prediksi dengan tingkat kesalahan yang paling rendah dibandingkan metode lainnya, dengan nilai MSE (0.3370), RMSE (0.5805), dan MAE (0.2707). Hal ini menunjukkan bahwa CF mampu menghasilkan rekomendasi dengan akurasi yang sangat baik, sehingga dapat meningkatkan pengalaman pengguna dan memperkuat loyalitas pelanggan.

2. Sebaliknya, Content-Based Filtering (CBF) menunjukkan performa yang kurang optimal dengan nilai kesalahan yang cukup tinggi (MSE: 32.1889, RMSE: 5.6735, MAE: 3.4283). Model ini kurang efektif dalam memberikan rekomendasi yang akurat, yang dapat mengurangi kepuasan pengguna serta berpotensi menurunkan retensi pelanggan.

3. Sementara itu, Hybrid Filtering yang menggabungkan CF dan CBF menghasilkan performa yang berada di tengah-tengah, dengan nilai MSE (8.1317), RMSE (2.8516), dan MAE (1.7434). Meskipun hasilnya tidak sebaik CF secara murni, pendekatan ini tetap memberikan rekomendasi yang lebih bervariasi dengan mempertimbangkan popularitas pengguna (CF) dan kesamaan konten (CBF). Dengan demikian, Hybrid Filtering dapat meningkatkan eksplorasi konten pengguna sekaligus menjaga akurasi rekomendasi.
```
---
> **Dari hasil tersebut, dapat disimpulkan bahwa Collaborative Filtering (CF) merupakan pilihan terbaik dalam hal akurasi rekomendasi pada kasus ini.**
---

## 📌Kesimpulan Akhir :
---
> Berdasarkan hasil evaluasi yang telah dilakukan, pendekatan **Collaborative Filtering (CF)** terbukti memberikan hasil prediksi paling akurat, dengan nilai **MSE: 0.3370, RMSE: 0.5805, dan MAE: 0.2707**. Ini menunjukkan bahwa CF mampu memberikan rekomendasi yang paling sesuai dengan preferensi pengguna, sehingga secara langsung berdampak pada peningkatan **keterlibatan pengguna (user engagement) dan loyalitas pelanggan**. Model ini juga secara efisien mengisi kekosongan informasi pada film yang belum ditonton pengguna, sehingga membantu pengguna tetap aktif di platform.

> Namun demikian, pendekatan **Hybrid Filtering**, meskipun memiliki tingkat akurasi yang tidak setinggi CF (MSE: 8.1317, RMSE: 2.8516, MAE: 1.7434), tetap memiliki peran strategis dalam konteks **eksplorasi konten dan diversifikasi rekomendasi**. Dengan menggabungkan kekuatan CF (berbasis rating historis) dan CBF (berbasis kemiripan konten), hybrid model mampu memperluas cakupan rekomendasi, mendorong pengguna menemukan film baru, dan meningkatkan **waktu tontonan serta eksposur terhadap berbagai genre**, yang mendukung strategi monetisasi platform berbasis langganan dan iklan.

> Sebaliknya, pendekatan **Content-Based Filtering (CBF)** murni menghasilkan tingkat kesalahan yang tinggi (MSE: 32.1889, RMSE: 5.6735, MAE: 3.4283), yang menunjukkan keterbatasan dalam mempersonalisasi rekomendasi hanya berdasarkan informasi konten. CBF kurang efektif dalam membangun koneksi antar pengguna, dan tidak cukup kuat dalam mempertahankan pengguna jangka panjang.

### **💡Analisis Terhadap Business Understanding**
**🎯Problem Statement 1:**

Bagaimana meningkatkan keterlibatan pengguna dengan menyediakan rekomendasi film yang lebih personal dan sesuai dengan preferensi mereka?

✔️ Terjawab.

> Model CF memberikan rekomendasi yang sangat personal berdasarkan perilaku pengguna lain yang serupa, terbukti dari akurasi tinggi. Hybrid Filtering juga menambah lapisan rekomendasi dengan menyarankan film baru yang masih relevan secara konten.

**🎯Problem Statement 2:**

Bagaimana menciptakan sistem rekomendasi yang mampu meningkatkan loyalitas pelanggan dengan mempertimbangkan popularitas dan relevansi konten?

✔️ Terjawab.

> CF mempertimbangkan popularitas melalui data rating kolektif, sedangkan CBF menilai relevansi konten. Kombinasi keduanya pada hybrid model menciptakan sistem yang seimbang antara popularitas dan relevansi konten, mendorong pengguna untuk kembali dan menjelajahi lebih banyak konten.

**🎯Problem Statement 3:**

Bagaimana mengembangkan strategi rekomendasi yang dapat mengoptimalkan pengalaman pengguna sekaligus meningkatkan potensi pendapatan bisnis melalui langganan atau iklan?

✔️ Terjawab.

> Model rekomendasi yang akurat seperti CF mendorong retensi pengguna, yang merupakan metrik penting dalam monetisasi. Hybrid Filtering meningkatkan waktu jelajah dan variasi tontonan, mendukung peningkatan konsumsi konten dan membuka peluang untuk penempatan iklan serta loyalitas berlangganan jangka panjang.


**🎯 Pencapaian Goals**
Goal 1:

Meningkatkan retensi pelanggan melalui rekomendasi yang relevan dan akurat.
✅ CF berhasil mencapainya secara langsung melalui akurasi tinggi, yang berdampak pada pengalaman pengguna yang lebih personal.

Goal 2:

Mengembangkan sistem yang mempertimbangkan preferensi pengguna dan tren pasar.
✅ Hybrid model menggabungkan keduanya: rating kolektif (tren) dan kesamaan konten (preferensi), sehingga cocok untuk strategi pertumbuhan bisnis.

Goal 3:

Evaluasi strategi dalam mendukung konversi pelanggan dan monetisasi platform.
✅ Melalui metrik evaluasi model, didapatkan bahwa pendekatan CF paling kuat untuk meningkatkan konversi pelanggan karena presisi tinggi. Sementara hybrid mendukung monetisasi melalui peningkatan content discoverability.

**🛠️ Solusi yang Diterapkan dan Dampaknya**
1. Collaborative Filtering (CF)

✅ Dampak: Paling akurat dalam merepresentasikan preferensi pengguna.
🔁 Relevansi terhadap bisnis: Peningkatan engagement dan loyalitas.

2. Content-Based Filtering (CBF)

⚠️ Dampak: Kurang akurat, namun penting untuk cold-start item.
🔁 Relevansi terhadap bisnis: Mendukung eksplorasi konten awal dan pengenalan film baru.

3. Hybrid Filtering (CF + CBF)

✅ Dampak: Lebih bervariasi dan strategis secara bisnis.
🔁 Relevansi terhadap bisnis: Meningkatkan waktu jelajah konten, mendukung eksposur dan iklan.

---

_Catatan:_
_Semua detail penjelasan setiap tahapan juga sudah ada dalam notebook._

📧 Hubungi saya melalui [GitHub](https://github.com/MuthiahAinun) jika ada pertanyaan.
