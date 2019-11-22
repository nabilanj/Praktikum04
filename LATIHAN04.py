#Latihan01
print ("\\----------------------------------LATIHAN 1---------------------------------/")
print ("*******************************************************************************")
print ("           \DAFTAR SMARTPHONE TERBAIK DI TAHUN 2019 MENURUT NABILA/")
print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print ()

HP = ["Iphone", "Samsung", "Google", "Vivo", "Xiaomi"]
print ("Daftar Smartphone Terbaik : ", HP)
print ()

#AKSES LIST
print ("#AKSES LIST")
print ("Brand Smartphone Terbaik [2]   : ",HP[2])
print ("Brand Smartphone Terbaik [1:4] : ", HP [1:4])
print ("Brand Smartphone Terbaik [4]   : ", HP [4])
print ()

#UBAH ELEMENT
print ("#MENGUBAH ELEMENT")
print ("Daftar Smartphone Terbaik : ", HP)
HP [3] = "Oppo"
print ("Perubahan ke-1 : ", HP)
HP [3:5] = ["Huawei", "Oppo"]
print ("Perubahan ke-2 : ", HP)
print ()

#MENAMBAHKAN ELEMENT
print ("#MENAMBAHKAN ELEMENT")
A = HP
B = A[0:2]
print ("2 Smartphone Terbaik : ",B)
C = ["11 Pro Max" , "Note 10"]
X = B + C
print ("Tipe Smartphone terbaik : ", B[0],C[0], B[1],C[1] )
print ()
print ("Smartphone Terbaik dibulan Oktober  : ",B)
B.append ("Asus")
B.append ("Sony")
B.append ("Vivo")
print ("Smartphone Terbaik dibulan November : ",B)
Y = B + A
print ("Daftar Brand Smartphone Terbaik : " , Y)





