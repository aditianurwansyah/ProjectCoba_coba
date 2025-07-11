# from sklearn import tree 

# # Data training [berat, tekstur(0=halus, 1=kasar)]
# features = [[150, 0],[130,0],[180,1],[190,1]]
# labels = [0, 0, 1, 1] # => 0= Apel, 1= jeruk 

# #Buat Model 
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features, labels) 

# #Prediksi data baru 
# print(clf.predict([[140,0]])) ==> Project I 

# from sklearn.linear_model import LinearRegression 

# ukuran = [[50],[70],[100],[120]] 
# harga = [500, 700, 1000, 1200]  
# model = LinearRegression( )
# model.fit(ukuran, harga)
# print(model.predict([[80]]))   ==> Project II

# from sklearn.cluster import KMeans 
# import matplotlib.pyplot as plt 

# #Data: Pengeluaran pelanggan 
# data = [[100],[200],[220],[800],[850],[870]]
# kmeans = KMeans(n_clusters=2, random_state=0)
# kmeans.fit(data)
# print(kmeans.labels_)  ==> Project III 

# from sklearn.datasets import load_digits
# from sklearn.linear_model import LogisticRegression 
# from sklearn.model_selection import train_test_split 
# from sklearn.metrics import accuracy_score

# digits = load_digits( )
# X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=0)
# model = LogisticRegression(max_iter=6000)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(f"Akurasi: {accuracy_score(y_test, y_pred) * 100:.2f}%") ==> Project IV 

# Import library yang dibutuhkan
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB

# # 1. Data Email dan Label
# emails = [
#     "Dapatkan hadiah gratis sekarang",
#     "Meeting jam 3 sore di kantor",
#     "Diskon besar untuk Anda",
#     "Laporan penjualan bulan ini",
#     "Anda memenangkan lotre",
#     "Jadwal rapat besok"
# ]

# # Label: 1 = Spam, 0 = Bukan Spam
# labels = [1, 0, 1, 0, 1, 0]

# # 2. Konversi Teks ke Representasi Angka
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(emails)

# # 3. Membuat dan Melatih Model Naive Bayes
# model = MultinomialNB()
# model.fit(X, labels)

# # 4. Contoh Email Baru untuk Diprediksi
# email_baru = [
#     "Undangan meeting siang ini",
#     "Dapatkan pinjaman mudah tanpa jaminan",
#     "Penawaran hadiah eksklusif untuk Anda",
#     "Jangan lupa jadwal rapat hari ini",
# ]

# # 5. Proses Prediksi
# X_baru = vectorizer.transform(email_baru)
# prediksi = model.predict(X_baru)

# # 6. Tampilkan Hasil
# print("\nHasil Prediksi Email Baru:\n")
# for teks, hasil in zip(email_baru, prediksi):
#     status = "SPAM" if hasil == 1 else "BUKAN SPAM"
#     print(f"'{teks}' => {status}") ==> Project V 
 