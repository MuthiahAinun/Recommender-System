# -*- coding: utf-8 -*-
"""Proyek_System_Recommendation_Tsamarah_Muthi'ah_A.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/MuthiahAinun/Recommender-System/blob/main/Proyek_System_Recommendation_Tsamarah_Muthi'ah_A.ipynb

# 📚Proyek Machine Learning- System Recommendation: [Movielens-dataset]
- **Nama:** [Tsamarah Muthi'ah Abdullah]
- **Email:** [a135xaf486@devacademy.id]
- **ID Dicoding:** [a135xaf48]

# Project Overview

Sistem rekomendasi adalah salah satu aplikasi machine learning yang banyak digunakan dalam berbagai sektor, seperti e-commerce, layanan streaming, dan media sosial. Sistem ini dirancang untuk memberikan rekomendasi produk, layanan, atau konten kepada pengguna berdasarkan preferensi atau perilaku mereka. Pentingnya sistem rekomendasi terletak pada kemampuannya untuk meningkatkan pengalaman pengguna, memperkuat keterlibatan, serta mendorong peningkatan penjualan atau penggunaan layanan.

Menurut penelitian oleh Ricci et al. (2015), sistem rekomendasi dapat meningkatkan pendapatan hingga 20% pada platform e-commerce. Selain itu, layanan streaming seperti Netflix melaporkan bahwa sekitar 80% dari penayangan didorong oleh algoritma rekomendasi (Gomez-Uribe & Hunt, 2015). Oleh karena itu, implementasi sistem rekomendasi merupakan aspek penting dalam dunia digital saat ini.

Pada proyek ini, akan dikembangkan sistem rekomendasi menggunakan berbagai algoritma untuk membandingkan performa dan efektivitasnya. Fokus utama proyek ini adalah menyelesaikan permasalahan rekomendasi konten pada platform layanan media dengan menggunakan algoritma Collaborative Filtering dan Content-Based Filtering. Selain itu, dilakukan pendekatan Hybrid Filtering untuk menggabungkan kekuatan dari kedua metode tersebut guna menghasilkan rekomendasi yang lebih bervariasi dan mempertimbangkan baik popularitas maupun kesamaan konten.

**Referensi:**

- Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender Systems Handbook. Springer.

- Gomez-Uribe, C. A., & Hunt, N. (2015). The Netflix Recommender System: Algorithms, Business Value, and Innovation. ACM Transactions on Management Information Systems.

# Business Understanding

### **Problem Statements**

1. Bagaimana cara merekomendasikan konten yang sesuai dengan preferensi pengguna secara akurat?

2. Bagaimana menggabungkan algoritma Collaborative Filtering dan Content-Based Filtering guna menghasilkan rekomendasi yang lebih bervariasi dan mempertimbangkan baik popularitas maupun kesamaan konten?

3. Bagaimana membandingkan performa antara algoritma Collaborative Filtering ,Content-Based Filtering, dan Hybrid-Filtering dalam memberikan rekomendasi?

### **Goals**

1. Menghasilkan sistem rekomendasi film yang akurat dan relevan berdasarkan preferensi pengguna.

3. Menggabungkan kedua algoritma (CF dan CBF) dalam pendekatan Hybrid Filtering untuk memberikan rekomendasi yang lebih bervariasi dengan mempertimbangkan popularitas pengguna dan kesamaan konten.

2. Membandingkan performa algoritma Collaborative Filtering (CF), Content-Based Filtering (CBF), dan Hybrid-Filtering menggunakan metrik evaluasi seperti MSE, RMSE, dan MAE.

### **Solution Approach**

1. Menggunakan 2 algoritma utama, yaitu:

  **A. Collaborative Filtering**

  - Menggunakan pendekatan berbasis pengguna dan item untuk mengidentifikasi kesamaan antara pengguna atau film.

  - Menggunakan teknik Singular Value Decomposition (SVD) untuk memprediksi rating film yang belum ditonton oleh pengguna.

  - Menghasilkan rekomendasi film dengan memilih film dengan peringkat tertinggi dalam hasil prediksi.

 **B. Content-Based Filtering**

  - Menggunakan fitur konten film (judul, genre) untuk menghasilkan rekomendasi.

  - Menggunakan teknik TF-IDF (Term Frequency-Inverse Document Frequency) dan Cosine Similarity untuk mengukur kemiripan antar film.

  - Memberikan rekomendasi film serupa dengan film tertentu yang dipilih pengguna.

2. Menggabungkan kedua algoritma dengan metode Hybrid Filtering (CF + CBF)

  - Menggabungkan hasil rekomendasi dari Collaborative Filtering dan Content-Based Filtering.

3. Evaluasi Performa

  - Menggunakan metrik seperti MSE, RMSE, dan MAE.

# **Import Library**
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse.linalg import svds
import os

"""# **Data Understanding**

Dataset yang digunakan pada proyek ini berasal dari MovieLens 100K (https://grouplens.org/datasets/movielens/100k/), yang berisi data rating film oleh pengguna. Dataset ini terdiri dari beberapa file utama, yaitu:

- u.data: berisi data rating pengguna terhadap film.

- u.item: berisi informasi mengenai judul film dan genre.

- u.user: berisi informasi pengguna.

- u.genre: berisi daftar genre.

Dataset ini berisi 100.000 rating dari 943 pengguna terhadap 1.682 film. Data ini mencakup informasi mengenai ID pengguna, ID film, rating, dan timestamp.

**Berikut adalah uraian variabel-variabel atau fitur pada tiap dataset:**

**1. Dataset Ratings**
- userId: Merupakan ID unik dari pengguna yang memberikan rating terhadap film.

- movieId: Merupakan ID unik dari film yang diberi rating oleh pengguna.

- rating: Merupakan nilai penilaian yang diberikan oleh pengguna terhadap film, dengan rentang 1 hingga 5.

- timestamp: Merupakan waktu saat pengguna memberikan rating, disimpan dalam format Unix timestamp.

**2. Dataset Movies**
- movieId: Merupakan ID unik dari film.

- video_release_date: Tanggal rilis video dari film tersebut (tidak ada data pada contoh).

- unknown: Variabel biner yang menunjukkan apakah genre film tidak diketahui (1 jika ya, 0 jika tidak).

- Action: Variabel biner yang menunjukkan apakah film bergenre aksi (1 jika ya, 0 jika tidak).

- Adventure: Variabel biner yang menunjukkan apakah film bergenre petualangan (1 jika ya, 0 jika tidak).

- Animation: Variabel biner yang menunjukkan apakah film bergenre animasi (1 jika ya, 0 jika tidak).

- Children: Variabel biner yang menunjukkan apakah film ditujukan untuk anak-anak (1 jika ya, 0 jika tidak).

- Comedy: Variabel biner yang menunjukkan apakah film bergenre komedi (1 jika ya, 0 jika tidak).

- Crime: Variabel biner yang menunjukkan apakah film bergenre kriminal (1 jika ya, 0 jika tidak).

- Documentary: Variabel biner yang menunjukkan apakah film bergenre dokumenter (1 jika ya, 0 jika tidak).

- Drama: Variabel biner yang menunjukkan apakah film bergenre drama (1 jika ya, 0 jika tidak).

- Fantasy: Variabel biner yang menunjukkan apakah film bergenre fantasi (1 jika ya, 0 jika tidak).

- Film-Noir: Variabel biner yang menunjukkan apakah film bergenre noir (1 jika ya, 0 jika tidak).

- Horror: Variabel biner yang menunjukkan apakah film bergenre horor (1 jika ya, 0 jika tidak).

- Musical: Variabel biner yang menunjukkan apakah film bergenre musikal (1 jika ya, 0 jika tidak).

- Mystery: Variabel biner yang menunjukkan apakah film bergenre misteri (1 jika ya, 0 jika tidak).

- Romance: Variabel biner yang menunjukkan apakah film bergenre romantis (1 jika ya, 0 jika tidak).

- Sci-Fi: Variabel biner yang menunjukkan apakah film bergenre fiksi ilmiah (1 jika ya, 0 jika tidak).

- Thriller: Variabel biner yang menunjukkan apakah film bergenre thriller (1 jika ya, 0 jika tidak).

- War: Variabel biner yang menunjukkan apakah film bergenre perang (1 jika ya, 0 jika tidak).

- Western: Variabel biner yang menunjukkan apakah film bergenre barat atau koboi (1 jika ya, 0 jika tidak).

**3. Dataset Users**
- userId: Merupakan ID unik dari pengguna dalam dataset.

- age: Merupakan usia pengguna dalam satuan tahun.

**4. Dataset Genres**
- genreId: Merupakan ID unik dari genre film.
"""

# Fungsi untuk mengubah .u file to CSV
def convert_u_to_csv(file_path, delimiter, columns, csv_name, encoding='ISO-8859-1'):
    df = pd.read_csv(file_path, delimiter=delimiter, header=None, engine='python', encoding=encoding)
    df.columns = columns
    csv_path = csv_name
    df.to_csv(csv_path, index=False)
    print(f'File {file_path} successfully converted to {csv_path}')
    return csv_path

# Mengubah u.data file to CSV
ratings_path = convert_u_to_csv('u.data', '	', ['userId', 'movieId', 'rating', 'timestamp'], 'ratings.csv')

# Mengubah u.item file to CSV
movies_path = convert_u_to_csv('u.item', '|', ['movieId', 'title', 'release_date', 'video_release_date', 'IMDb_URL', 'unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'], 'movies.csv')

# Mengubah u.user file to CSV
users_path = convert_u_to_csv('u.user', '|', ['userId', 'age', 'gender', 'occupation', 'zip_code'], 'users.csv')

# Mengubah u.genre file to CSV
genre_path = convert_u_to_csv('u.genre', '|', ['genre', 'genreId'], 'genres.csv')

# Memuat dataset
ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")
users = pd.read_csv("users.csv")
genres = pd.read_csv("genres.csv")

# Melihat informasi umum tentang dataset
print("\nInfo Dataset Ratings:")
print(ratings.info())

"""**✨Dataset Ratings**
- Jumlah Data: 100.000 entri

- Jumlah Kolom: 4 kolom (userId, movieId, rating, timestamp)

- Tipe Data: Seluruh kolom bertipe int64

- Ukuran Memori: 3.1 MB

- **Insight:** Dataset ini merepresentasikan data rating film dari pengguna. Setiap entri berisi informasi tentang ID pengguna, ID film, rating yang diberikan, dan timestamp kapan rating diberikan. Data lengkap tanpa ada nilai kosong.
"""

print("\nInfo Dataset Movies:")
print(movies.info())

"""**📹Dataset Movies**
- Jumlah Data: 1.682 entri

- Jumlah Kolom: 24 kolom

- Kolom Penting: movieId, title, release_date, IMDb_URL, dan 19 kolom genre

- Tipe Data:

  - int64 pada ID dan genre

  - object pada judul, tanggal rilis, dan URL

  - float64 pada video_release_date (seluruhnya kosong)

- Ukuran Memori: 315.5 KB

- **Insight:** Dataset ini menyimpan informasi detail tentang film, termasuk judul, tanggal rilis, URL IMDb, dan genre. Kolom video_release_date tidak memiliki data sama sekali, sehingga dapat diabaikan. Setiap film memiliki 19 kolom genre dengan nilai biner (0 atau 1) yang menunjukkan genre film tersebut.
"""

print("\nInfo Dataset Users:")
print(users.info())

"""**👥Dataset Users**
- Jumlah Data: 943 entri

- Jumlah Kolom: 5 kolom (userId, age, gender, occupation, zip_code)

- Tipe Data:

  - int64 pada ID dan usia

  - object pada gender, pekerjaan, dan kode pos

- Ukuran Memori: 37.0 KB

- **Insight:** Dataset ini berisi informasi demografi pengguna, termasuk usia, jenis kelamin, pekerjaan, dan kode pos. Data lengkap tanpa ada nilai kosong.
"""

print("\nInfo Dataset Genres:")
print(genres.info())

"""**🎞️Dataset Genres**
- Jumlah Data: 19 entri

- Jumlah Kolom: 2 kolom (genre, genreId)

- Tipe Data:

  - object pada nama genre

  - int64 pada ID genre

- Ukuran Memori: 436 bytes

- **Insight:** Dataset ini mendefinisikan genre film dengan ID unik untuk setiap genre.
"""

# Statistik Deskriptif
print("\nStatistik Deskriptif Ratings:")
print(ratings.describe())

"""**Insight Statistik Deskriptif Ratings:**

1. Sebagian besar rating berada di kisaran 3 hingga 4, dengan nilai rata-rata 3.53.

2. Rating minimum adalah 1 dan maksimum adalah 5, menunjukkan adanya variasi pendapat pengguna terhadap film.

3. User ID tersebar secara merata dari 1 hingga 943, menunjukkan banyaknya pengguna yang memberikan rating.

4. Waktu pemberian rating berkisar dalam rentang waktu yang cukup luas.
"""

print("\nStatistik Deskriptif Movies:")
print(movies.describe())

"""**Insight Statistik Deskriptif Movies:**

1. Terdapat 1.682 film dengan berbagai genre.

2. Genre paling umum adalah Comedy (30%), diikuti Action (15%) dan Romance (14.7%).

3. Beberapa genre sangat jarang muncul, seperti Fantasy (1.3%), Film-Noir (1.4%), dan Western (1.6%).
"""

print("\nStatistik Deskriptif Users:")
print(users.describe())

"""**Insight Statistik Deskriptif Users:**

1. Terdapat 943 pengguna dengan rentang usia dari 7 hingga 73 tahun.

2. Rata-rata usia pengguna adalah sekitar 34 tahun, menunjukkan dominasi pengguna dewasa muda.

3. Mayoritas pengguna berusia antara 25 hingga 43 tahun, yang merupakan segmen pengguna paling aktif.
"""

print("\nStatistik Deskriptif Genres:")
print(genres.describe())

"""**Insight Statistik Deskriptif Genres:**

1. Terdapat 19 genre film dalam dataset.

2. Genre dengan ID maksimum adalah 18, sementara ID minimum adalah 0, menandakan adanya berbagai macam kategori film.

3. Genre rata-rata memiliki ID di sekitar angka 9, dengan variasi yang cukup besar.

# **Data Preparation**

Pada tahap ini, dilakukan pengecekan dan penanganan data hilang, serta transformasi data.
Mengapa Tahap Data Preparation Diperlukan:
1. Mengatasi data yang hilang agar tidak mengganggu proses analisis dan model.
2. Melakukan transformasi agar data lebih terstruktur dan dapat digunakan oleh model.
3. Menghasilkan data yang lebih konsisten dan bebas dari error yang dapat mempengaruhi hasil prediksi.
4. Meningkatkan akurasi dan kinerja model dengan data yang bersih dan terstruktur.
"""

# Mengecek nilai hilang pada setiap kolom
def check_missing_values(df):
    print("\nJumlah nilai hilang per kolom:")
    print(df.isnull().sum())

print("\nPengecekan Nilai Hilang pada Ratings:")
check_missing_values(ratings)

print("\nPengecekan Nilai Hilang pada Movies:")
check_missing_values(movies)

print("\nPengecekan Nilai Hilang pada Users:")
check_missing_values(users)

print("\nPengecekan Nilai Hilang pada Genres:")
check_missing_values(genres)

# Informasi Statistik untuk Kolom dengan Nilai Hilang pada Movies
print('\nInformasi Statistik pada Kolom dengan Nilai Hilang pada Movies:')
print(movies[['release_date', 'video_release_date', 'IMDb_URL']].describe(include='all'))

"""## Insight :
**Kolom release_date:**

- Terdapat 1 nilai hilang dari total 1682 data.

- Format tanggal yang digunakan adalah DD-MMM-YYYY.

- Tanggal yang paling sering muncul adalah 01-Jan-1995, sebanyak 215 kali.

**Kolom video_release_date:**

- Seluruh nilai pada kolom ini hilang (1682 nilai hilang), sehingga tidak memberikan informasi apapun.

- Kolom ini akan dihapus karena tidak berkontribusi terhadap analisis.

**Kolom IMDb_URL:**

1. Terdapat 3 nilai hilang.

2. URL yang paling sering muncul adalah "http://us.imdb.com/M/title-exact?That%20Darn%20Cat!%20(1997)", sebanyak 2 kali.

# A. Data Cleaning

### **Mengatasi permasalahan nilai hilang agar model tidak mengalami error atau bias.**
"""

# Menghapus kolom dengan seluruh nilai hilang (video_release_date)
movies.drop(columns=['video_release_date'], inplace=True)

# Menghapus baris dengan nilai hilang pada release_date dan IMDb_URL
movies.dropna(subset=['release_date', 'IMDb_URL'], inplace=True)

"""# B. Transformasi Data

### **Melakukan transformasi data sehingga lebih mudah diolah pada tahap modeling.**
"""

# Transformasi timestamp ke datetime
ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')

# Mengecek Kembali Nilai Hilang pada Dataset Movies
print("\nPengecekan Nilai Hilang pada Movies:")
check_missing_values(movies)

# Mengecek Kembali Informasi Statistik untuk Kolom dengan Nilai Hilang pada Movies
print('\nInformasi Statistik pada Kolom dengan Nilai Hilang pada Movies:')
print(movies[['release_date', 'IMDb_URL']].describe(include='all'))

"""# C. Penggabungan Dataset

### **Dataset ratings dan movies digabungkan berdasarkan kolom movieId. Hal ini dilakukan untuk mempermudah pembuatan matriks user-item yang mengandung informasi rating dan judul film.**
"""

# Penggabungan data ratings dan movies
data = pd.merge(ratings, movies, on='movieId')

"""# D. Data Splitting

### **Pada Tahap ini data dibagi menjadi 80/20 untuk data training dan data testing.**
"""

# Data splitting
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

"""# **Modeling**

1. Kelebihan: CF dapat memanfaatkan interaksi pengguna, sedangkan CBF dapat merekomendasikan item baru.

2. Kekurangan: CF membutuhkan data yang cukup banyak dan padat, sementara CBF bergantung pada informasi konten.
"""

# Collaborative Filtering (User-Item Matrix)
from scipy.sparse import csr_matrix

user_item_matrix = data.pivot(index='userId', columns='movieId', values='rating').fillna(0)
user_item_matrix_sparse = csr_matrix(user_item_matrix)
U, sigma, Vt = svds(user_item_matrix_sparse, k=50)
sigma = np.diag(sigma)
pred_ratings = np.dot(np.dot(U, sigma), Vt)
pred_ratings_df = pd.DataFrame(pred_ratings, columns=user_item_matrix.columns)

# Content-Based Filtering (TF-IDF)
# Menghitung TF-IDF langsung dari judul film pada dataset movies
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['title'].fillna(''))

# Menghitung similaritas menggunakan cosine similarity
content_sim = cosine_similarity(tfidf_matrix)

"""# **Evaluasi**

- MSE (Mean Squared Error): Rata-rata kuadrat selisih antara nilai aktual dan nilai prediksi.
- RMSE (Root Mean Squared Error): Akar kuadrat dari MSE, memberikan ukuran seberapa besar kesalahan.
- MAE (Mean Absolute Error): Rata-rata dari nilai absolut selisih antara prediksi dan nilai aktual.
"""

# Fungsi evaluasi model
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Fungsi evaluasi metrik: MSE, RMSE, dan MAE
def evaluate_model(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    print(f'MSE: {mse:.4f}')
    print(f'RMSE: {rmse:.4f}')
    print(f'MAE: {mae:.4f}')

actual_ratings = user_item_matrix.values.flatten()
predicted_ratings = pred_ratings.flatten()
evaluate_model(actual_ratings, predicted_ratings)

# Evaluasi Collaborative Filtering (SVD)
def evaluate_cf():
    actual_ratings = user_item_matrix.values.flatten()
    predicted_ratings = pred_ratings.flatten()
    evaluate_model(actual_ratings, predicted_ratings)

# Evaluasi Content-Based Filtering (CBF)
def evaluate_cbf():
    # Menyesuaikan ukuran content_sim dengan user_item_matrix
    valid_movie_ids = user_item_matrix.columns
    content_sim_filtered = content_sim[:len(valid_movie_ids), :len(valid_movie_ids)]

    # Menghitung prediksi CBF
    cbf_pred = np.dot(user_item_matrix.values, content_sim_filtered)
    actual_ratings = user_item_matrix.values.flatten()
    predicted_ratings = cbf_pred.flatten()
    evaluate_model(actual_ratings, predicted_ratings)

# Evaluasi Hybrid (gabungan CF dan CBF)
def evaluate_hybrid(alpha=0.5):
    # Menyesuaikan ukuran content_sim dengan user_item_matrix
    valid_movie_ids = user_item_matrix.columns
    content_sim_filtered = content_sim[:len(valid_movie_ids), :len(valid_movie_ids)]

    # Menghitung prediksi CBF
    cbf_pred = np.dot(user_item_matrix.values, content_sim_filtered)

    # Menggabungkan prediksi CF (SVD) dan CBF
    hybrid_pred = alpha * pred_ratings + (1 - alpha) * cbf_pred
    actual_ratings = user_item_matrix.values.flatten()
    predicted_ratings = hybrid_pred.flatten()
    evaluate_model(actual_ratings, predicted_ratings)

print("\nEvaluasi Collaborative Filtering (CF):")
evaluate_cf()

print("\nEvaluasi Content-Based Filtering (CBF):")
evaluate_cbf()

print("\nEvaluasi Hybrid:")
evaluate_hybrid(alpha=0.5)

"""Berdasarkan hasil evaluasi:
1. **Model Collaborative Filtering (CF)** menunjukkan performa terbaik dengan nilai MSE sebesar 0.3370, RMSE sebesar 0.5805, dan MAE sebesar 0.2707, mengindikasikan bahwa CF mampu memberikan rekomendasi dengan tingkat kesalahan yang rendah.
2. Sebaliknya, **Content-Based Filtering (CBF)** memiliki performa yang lebih rendah dengan MSE sebesar 32.1889, RMSE sebesar 5.6735, dan MAE sebesar 3.4283, yang menunjukkan bahwa model ini kurang akurat dalam memprediksi rating pengguna.
3. Sementara itu, **Hybrid Filtering** yang menggabungkan CF dan CBF menghasilkan nilai MSE sebesar 8.1317, RMSE sebesar 2.8516, dan MAE sebesar 1.7434, yang lebih baik daripada CBF tetapi masih lebih rendah dibandingkan dengan CF.

**Dari hasil tersebut, dapat disimpulkan bahwa Collaborative Filtering (CF) merupakan pilihan terbaik dalam hal akurasi rekomendasi pada kasus ini.**

# Example of Usage

**1. Metode Tunggal ( CF dan CBF)**
"""

# Fungsi rekomendasi dengan Collaborative Filtering (CF)
def recommend_cf(user_id, num_recommendations=10):
    user_ratings = pred_ratings_df.loc[user_id - 1].sort_values(ascending=False)
    recommended_movie_ids = user_ratings.head(num_recommendations).index
    return movies[movies['movieId'].isin(recommended_movie_ids)]['title']

# Content-based Filtering (CBF)
def recommend_cbf(movie_id, num_recommendations=10):
    if movie_id not in movies['movieId'].values:
        print(f'Movie ID {movie_id} tidak ditemukan.')
        return []
    idx = movies[movies['movieId'] == movie_id].index[0]
    sim_scores = list(enumerate(content_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    movie_indices = [i[0] for i in sim_scores[1:num_recommendations+1]]
    return movies['title'].iloc[movie_indices].tolist()

# Example of usage
user_id = 1
print("Recommendations for User (CF):")
print(recommend_cf(user_id))

"""**Hasil :**
1. Rekomendasi film untuk pengguna dengan ID 1 didasarkan pada kemiripan rating dengan pengguna lain.

2. Beberapa film yang direkomendasikan antara lain:

- Toy Story (1995): Film animasi keluarga dengan cerita persahabatan mainan.

- Star Wars (1977): Film fiksi ilmiah klasik tentang perjuangan melawan Kekaisaran.

- Blade Runner (1982): Film fiksi ilmiah bertema dystopia dan robot manusia.

- Fargo (1996): Drama kriminal dengan cerita penuh misteri.

- 2001: A Space Odyssey (1968): Film fiksi ilmiah epik karya Stanley Kubrick.

- Aliens (1986) dan Alien (1979): Film horor fiksi ilmiah dengan tema invasi alien.

- Chasing Amy (1997) dan Full Monty, The (1997): Film drama dan komedi romantis.

**Insight:**
Pengguna ini cenderung menyukai film dengan tema fiksi ilmiah, petualangan, dan drama kriminal, serta beberapa film dengan elemen komedi dan animasi.

**Kelebihan:**

1. Mampu memberikan rekomendasi berdasarkan interaksi pengguna lain, sehingga menghasilkan rekomendasi film populer yang disukai banyak orang.

2. Cocok digunakan ketika data interaksi pengguna cukup banyak.

**Kekurangan:**

1. Mengalami masalah Cold Start, terutama jika pengguna baru belum memiliki interaksi.

2. Tidak mempertimbangkan konten film, sehingga bisa kurang relevan jika pengguna menyukai genre atau tipe film tertentu.
"""

movie_id = 1
print("Recommendations for Movie (CBF):")
print(recommend_cbf(movie_id))

"""**Hasil :**

1. Rekomendasi didasarkan pada kesamaan fitur film, seperti genre dan deskripsi.

2. Beberapa film yang direkomendasikan antara lain:

- Pyromaniac's Love Story, A (1995): Drama romantis dengan kisah cinta yang tidak biasa.

- Philadelphia Story, The (1940): Drama komedi romantis klasik.

- NeverEnding Story III, The (1994): Film petualangan fantasi keluarga.

- FairyTale: A True Story (1997): Film drama keluarga dengan unsur fantasi.

- Police Story 4: Project S (1993): Film aksi petualangan dengan elemen seni bela diri.

**Insight:**
Film yang direkomendasikan memiliki genre drama romantis, fantasi keluarga, dan petualangan aksi.

**Kelebihan:**

1. Mampu memberikan rekomendasi berdasarkan kesamaan fitur film (genre, sutradara, dll).

2. Tidak terpengaruh oleh popularitas, sehingga dapat merekomendasikan film dengan karakteristik yang serupa dengan preferensi pengguna.

**Kekurangan:**

1. Rekomendasi bisa kurang bervariasi karena terlalu fokus pada kesamaan.

2. Tidak mampu menangkap pola kompleks dari perilaku pengguna seperti CF.

**2. Metode Hybrid Filtering**

**Hybrid filtering menggabungkan Collaborative Filtering (CF) dan Content-Based Filtering (CBF) untuk memberikan rekomendasi yang lebih variatif dengan memanfaatkan keunggulan dari kedua pendekatan.**
"""

# Rekomendasi Hybrid (CF + CBF)
def recommend_hybrid(user_id, movie_id, num_recommendations=10, alpha=0.5):
    # Mengambil rekomendasi dari CF dan CBF
    cf_recommendations = recommend_cf(user_id, num_recommendations)
    cbf_recommendations = recommend_cbf(movie_id, num_recommendations)

    # Buat dictionary untuk menyimpan skor rekomendasi
    recommendation_scores = {}

    # Menggabungkan skor CF dengan bobot alpha
    for movie in cf_recommendations:
        recommendation_scores[movie] = recommendation_scores.get(movie, 0) + alpha

    # Menggabungkan skor CBF dengan bobot (1 - alpha)
    for movie in cbf_recommendations:
        recommendation_scores[movie] = recommendation_scores.get(movie, 0) + (1 - alpha)

    # Mengurutkan hasil berdasarkan skor (nilai tertinggi ke terendah)
    sorted_recommendations = sorted(recommendation_scores, key=recommendation_scores.get, reverse=True)

    # Mengembalikan rekomendasi teratas sesuai jumlah yang diminta
    return sorted_recommendations[:num_recommendations]

user_id = 1
movie_id = 1
print('\nRekomendasi Hybrid (CF + CBF):')
print(recommend_hybrid(user_id, movie_id))

"""Berdasarkan hasil rekomendasi hybrid yang menggabungkan Collaborative Filtering (CF) dan Content-Based Filtering (CBF), sistem berhasil menghasilkan daftar film yang mencerminkan keseimbangan antara preferensi pengguna dan kesamaan konten. Film-film seperti "Toy Story (1995)", "Usual Suspects, The (1995)", "Star Wars (1977)", dan "Blade Runner (1982)" merupakan film-film populer yang disukai oleh pengguna serupa, sementara film-film seperti "Fargo (1996)" dan "Chasing Amy (1997)" juga dipilih berdasarkan kesamaan genre atau tema. Kombinasi kedua pendekatan ini memungkinkan sistem memberikan rekomendasi yang lebih beragam dan relevan, sehingga dapat meningkatkan kepuasan pengguna dengan menawarkan pilihan film dari berbagai sudut pandang.

# **📌Kesimpulan Akhir :**
1. Dari hasil evaluasi dan perbandingan metode, dapat disimpulkan bahwa pendekatan Collaborative Filtering (CF) memberikan hasil prediksi dengan tingkat kesalahan yang paling rendah dibandingkan metode lainnya, dengan nilai MSE (0.3370), RMSE (0.5805), dan MAE (0.2707). Hal ini menunjukkan bahwa CF mampu menghasilkan rekomendasi dengan akurasi yang sangat baik.

2. Metode Content-Based Filtering (CBF) menunjukkan performa yang kurang optimal dengan nilai kesalahan yang cukup tinggi (MSE: 32.1889, RMSE: 5.6735, MAE: 3.4283). Hal ini menunjukkan bahwa model CBF kurang efektif dalam memberikan rekomendasi yang akurat jika dibandingkan dengan CF.

3. Sementara itu, pendekatan Hybrid Filtering yang menggabungkan kekuatan CF dan CBF menghasilkan performa yang berada di tengah-tengah, dengan nilai MSE (8.1317), RMSE (2.8516), dan MAE (1.7434). Meskipun hasilnya tidak sebaik CF secara murni, pendekatan ini tetap memberikan rekomendasi yang lebih bervariasi dengan mempertimbangkan popularitas pengguna (CF) dan kesamaan konten (CBF).

**Saran**: Pemilihan metode yang tepat bergantung pada tujuan implementasi. Jika mengutamakan akurasi rekomendasi, Collaborative Filtering (CF) lebih unggul. Namun, jika membutuhkan rekomendasi yang lebih bervariasi dan tidak hanya mengandalkan data perilaku pengguna, Hybrid Filtering dapat menjadi pilihan yang lebih seimbang.
"""