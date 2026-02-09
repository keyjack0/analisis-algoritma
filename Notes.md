catatan tanggal 27 desember 2025
- tambahkan persen pada data kategorikal
- belum ada pemeriksaan outlier pada EDA
- analisis pada 1 per 1 algoritma 
- testing analisis memperkuat prediksi SVM dengan gridsearch

1. visualisasi 
- tampilan pengetahuan dan opini responden sebelum di preprocessing h1n1 dan seasonal vacsinez`
- tampilkan penerimaan vaksin sebelum di preprocessing
- 

BAB 1 PENDAHULUAN
LATAR BELAKANG MASALAH
1.1 point-point latar belakang masalah per-paragraf
    - membahas tentang latar belakang topik utama skripsi
    - membahas kenapa topik utama bisa di ambil dan seberapa penting (ambil menurut data)
    - membahas solusi apa yang di tawarkan 
    - membahas tentang teknologi yang akan di pakai (machine learning, algoritma svm, naive bayes, random forest ) 
    - membahas hasil penelitian 
1.2 rumusan masalah
    - buat pertanyaan tentang acuracy perbandingan dari ke 3 algoritma dalam klasifikasi penerimaan vaksin influenza
1.3 batasan masalah
    - dataset terbatas bersumber dari kaggle
    - hanya berfokus pada 3 algoritma
    - hanya melakukan analisis algoritma
    - hanya berfokus klasifikasi dengan 2 label, (pernerimaan vaksin [1], tidak menerima vaksin [0])
    - hanye berfokus pada metode crips-dm
1.4 tujuan penelitian
    - menganalisis dan membandingkan ke 3 algoritma dalam menentukan algoritma terbaik untuk kalsifikasi penerimaan vaksin influenza
    - ...
1.5 manfaat penelitian
    - mengetahui kinerja perbandingan dari 3 algoritma 
    - menjadi referensi bagi peneliti selanjutnya dalam penggunaan machine learning klasifikasi penerimaan vaksin influenza
    - menjadi referensi dalam membantu instansi terkait menentukan penerimaan vaksin influenza
1.6 sistematika penulisan
    - 

BAB 2 TINJAUAN PUSTAKA
2.1 studi literatur
2.2 dasar teori 
    - Virus Influenza
    - Vaksin Influenza
    - Klasifikasi
    - Mahcine Learning
    - Suport Vector Machine (SVM)
    - Naive Bayes
    - Random Forest
    - CRIPS-DM
    - SMOTE
    - Confusion Matrix
        - akurasi
        - presisi
        - recall
        - F1
        - ROC AUC

BAB 3 METODE PENELTIAN
3.1 object penelitian
3.2 alur penelitian
    - 
3.3 alat dan bahan
    - deskripsi dataset (menjelaskan arti dari dataset dan tipe dataset berbentuk tabel )
    - perangkat lunak
    - perangkat keras

BAB 4 HASIL DAN PEMBAHASAN
4.2 Eksplorasi Data
4.3 Preprocessing Data
4.4 Pemodelan Data
4.5 Evaluasi Data
4.6 Deployment



Referensi jurnal, publikasi yang akan di cari, 
1. CRIP-DM (done) [2]
2. Support Vector Machine (done) [2]
3. Naive Bayes (done) [2]
4. Random Forest (done) [2]
5. Vaksin Influnza (primary) (done) [4]
6. Klasifikasi Machine Learning (pending, belum di butuhkan)'

referensi jurnal untuk studi literatur yang berkaitan dengan:
perbandingan 
perbandingan klasifikasi algoritma


URUTAN LENGKAP PROSES ANALISIS (DIMULAI DARI EDA)
1. Exploratory Data Analysis (EDA)

Tujuan: memahami karakteristik data sebelum diproses

Yang dilakukan:

Menampilkan jumlah data dan jumlah fitur

Melihat tipe data (numerik & kategorikal)

Analisis distribusi target (h1n1_vaccine)

Mengecek ketidakseimbangan kelas

Mengecek missing value per kolom

Analisis statistik deskriptif (mean, median, std)

Visualisasi awal:

Distribusi target

Distribusi fitur penting

Korelasi fitur numerik (jika perlu)

📌 Catatan skripsi:
EDA dilakukan sebelum pembersihan data agar kondisi asli data tetap terlihat.

2. Data Cleaning & Preparation

Tujuan: menyiapkan data agar layak untuk pemodelan

Langkah:

Menghapus kolom yang tidak relevan

ID responden

Label lain yang tidak digunakan (misal seasonal_vaccine)

Memisahkan fitur numerik & kategorikal

Menangani missing value:

Numerik → mean / median

Kategorikal → modus

Encoding data kategorikal

Label Encoding / One-Hot Encoding

Menggabungkan kembali semua fitur

📌 Dilakukan setelah EDA

3. Feature Scaling

Tujuan: menormalkan skala data

Langkah:

Standarisasi fitur numerik

Scaling diterapkan hanya pada data training

Data testing menggunakan scaler yang sama

📌 Penting untuk SVM

4. Data Splitting

Tujuan: memastikan evaluasi model adil

Langkah:

Membagi data menjadi:

Data training

Data testing

Proporsi umum: 80% : 20%

Gunakan random state tetap

📌 Dilakukan sebelum HPO

5. Handling Class Imbalance

Tujuan: meningkatkan performa kelas minoritas


HPO pada data training

📌 Jangan diterapkan ke data testing

6. Pembuatan Model (Modeling)

Tujuan: membangun model klasifikasi

Langkah:

Melatih model:

Naive Bayes

Support Vector Machine

Random Forest

Menggunakan parameter awal (default)

(Opsional) Hyperparameter tuning ringan

📌 Setiap model dilatih dengan data yang sama

7. Evaluasi Model

Tujuan: mengukur performa model

Metode evaluasi:

Confusion Matrix

Accuracy

Precision

Recall

F1-score

(Opsional) ROC & AUC

📌 Fokus pada kelas penerima vaksin

8. Analisis Perbandingan Algoritma

Tujuan: menjawab rumusan masalah

Langkah:

Membandingkan metrik evaluasi

Menyusun tabel perbandingan

Analisis kelebihan & kelemahan tiap algoritma

Menjelaskan penyebab perbedaan performa


9. Visualisasi Hasil

Tujuan: memperjelas hasil analisis

Visualisasi:

Grafik perbandingan metrik

Confusion matrix heatmap

ROC curve (opsional)

📌 Visual mendukung narasi, bukan sekadar hiasan

10. Interpretasi & Kesimpulan

Tujuan: menarik makna dari hasil penelitian

Langkah:

Menentukan algoritma terbaik

Menjawab tujuan penelitian

Menyebutkan keterbatasan penelitian

Memberikan rekomendasi penelitian lanjutan

📌 Ini masuk Bab V

RINGKASAN URUTAN (VERSI CEPAT)

EDA
→ Data Cleaning
→ Encoding
→ Scaling
→ Split Data
→ Handling Imbalance
→ Modeling
→ Evaluation
→ Comparison
→ Conclusion