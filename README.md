**MENENTUKAN NILAI AKHIR DARI SUATU DATA / LIST DARI SUATU PROGRAM**

LANGKAH - LANGKAH 

1) Buat beberapa data list awal dengan mengkosongkan element.

    ![Screenshot (113)](https://user-images.githubusercontent.com/57028453/69423464-c153d000-0d58-11ea-9d4d-72a14e5ba901.png)

2) Lalu, gunakan ***while*** untuk melakukan perulangan pada sebuah data. Sebelumnya, tentukan variabel untuk menentukan kapan              perulangan berhenti , kalau pengguna menjawab tidak maka perulangan akan berhenti. Misal tanya = “y” dan while tanya == “y”.

3) Lalu, dilanjutkan dengan menginput data yang akan dihitung. Misalnya : input Nama, NIM, Nilai Tugas, Nilai UTS, dan nilai UAS.          Gunanya untuk menginput data tersebut untuk menentukan nilai akhir . 

4) Setelah itu, hitung nilai akhir dengan menjumlahkan  nilai tugas, nilai uts dan nilai uas yang sudah di input tadi. Namun sebelum        dijumlahkan nilai tugas x 35% , nilai uts x 30% dan nilai uas x 30%. Gunakan fungsi ***float*** digunakan untuk menyatakan bilangan      desimal atau bilangan yang memiliki koma, atau gunakan fungsi ***round*** untuk membulatkan hasil suatu bilangan.

    ![Screenshot (114)](https://user-images.githubusercontent.com/57028453/69424920-615f2880-0d5c-11ea-832c-38047bf3d05e.png)

5) Gunakan kondisi if, elif dan else. Untuk menentukan hasil grade dari nilai akhir  gunakan kondisi if dan elif karna untuk                lanjutan/percabangan logika dari “kondisi if”. Dengan elif kita bisa membuat kode program yang akan menyeleksi beberapa kemungkinan      yang bisa terjadi. Hampir sama dengan kondisi “else”, bedanya kondisi “elif” bisa banyak dan tidak hanya satu.

6) Sedangan untuk menambahkan keterangan gunakan kondisi if dan else dimana jika pernyataan benar True maka kode dalam if akan              dieksekusi, tetapi jika bernilai salah False maka akan mengeksekusi kode di dalam else.

   ![Screenshot (112)](https://user-images.githubusercontent.com/57028453/69423461-c0bb3980-0d58-11ea-94c1-98b7fac5520e.png)
   
7) Gunakan metode **append()** untuk menambahkan item ke list awal. Misal : List.append(item). Append semua list yang akan dibuat table    dari Nama, Nim, Tugas, Uts, Uas,Nilai akhir, Grade dan Keterangan. 

8) Lalu, input sebuah pertanyaan untuk menambahkan data atau tidak. Misalnya  tanya = “ input data selanjutnya? (y/t) :  “. Gunakan        kondisi if lagi untuk menjawab pertanyaan tersebut (Misal : if tanya == “t” : ).

9) Setelah menginput t cetak tabel yg ingin dibuat .

10) Setelah itu gunakan fungsi for untuk mengulang suatu proses dengan jumlah perulangan yang sudah ditentukan.  Misal for i in range       (len(Nama)) fungsi len(list) untuk memberikan total panjang list.

    ![Screenshot (118)](https://user-images.githubusercontent.com/57028453/69425449-74bec380-0d5d-11ea-8d94-64ea76353c8f.png)

**Berikut contoh hasil program untukmenentukan nilai akhir **
  
  Program ini bisa menampilkan hasil data berapapun yang kalian inginkan.

   ![Screenshot (117)](https://user-images.githubusercontent.com/57028453/69425751-1b0ac900-0d5e-11ea-8677-fc822f2f476c.png)
   
