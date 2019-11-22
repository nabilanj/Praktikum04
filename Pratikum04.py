#Praktikum04
print ("\\----------------------------------TUGAS PRAKTIKUM 04---------------------------------/")
print ("****************************************************************************************")
print ("       \DAFTAR NILAI AKHIR MAHASISWA TEKNIK INFORMATIKA SEMESTER 1 TAHUN 2019/")
print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print ()
Nama  = []
Nim   = []
TGS   = []
UTS   = []
UAS   = []
Akhir = []
grade = []
KET   = []

tanya = "y"
while tanya == "y" :
    NAMA = input (" Masukkan Nama        : ")
    NIM = input (" Masukkan NIM         : ")
    TUGAS = int(input (" Masukkan Nilai Tugas : "))
    UTS1 = int(input (" Masukkan Nilai UTS   : "))
    UAS1 = int(input (" Masukkan Nilai UAS   : "))
    AKHIR = float((TUGAS)*30/100 + (UTS1)*35/100 + (UAS1)*35/100)

    if AKHIR >= 85 :
        indeks = "A"
    elif AKHIR >= 75 and AKHIR < 85 :
        indeks = "B"
    elif AKHIR >= 65 and AKHIR < 75 :
        indeks = "C"
    elif AKHIR >= 50 and AKHIR < 65 :
        indeks = "D"
    elif AKHIR >= 0 and AKHIR < 50  :
        indeks = "E"

    if AKHIR >= 60 :
        Ket = "LULUS"
    else :
        Ket = "TIDAK LULUS"
        
    
    Nama.append(NAMA)
    Nim.append(NIM)
    TGS.append(TUGAS)
    UTS.append(UTS1)
    UAS.append(UAS1)
    Akhir.append(AKHIR)
    grade.append(indeks)
    KET.append(Ket)
    tanya = input(" Input Data Selanjutnya ? (y/t) : ")
    if tanya == "t" :
        print ("\\-------------------------DATA NILAI AKHIR MAHASISWA----------------------------------/")
        print ("****************************************************************************************")
        print ()
        print ()
        print ("========================================================================================")
        print (" |  No |   Nama   |     NIM     |  Tugas |   UTS  |   UAS  |  NILAI | GRADE |   KET  |" )
        print ("========================================================================================")
        for i in range (len (Nama)):
            print (" | " ,i+1," | " , Nama[i] ," | " , Nim[i]," | " , TGS[i] ,"   |  " , UTS[i] ,"  | " , UAS[i] ,"   | " , Akhir[i]," | " , grade[i] ,"   | " , KET[i]
                   ,"| ")
    
