
from cgi import print_environ
from re import A


print('       PROGRAM MENGHITUNG NILAI SISWA        ')
print("===================================================")
nama = input("Masukkan Nama     : ")
Kelas = input("Masukkan Kelas    : ")
Mapel = input("Masukkan Mapel    : ")
nilai = int(input("Masukkan Nilai : "))

if (nilai >= 90) and (nilai <= 100):
     print('Lulus') 
elif (nilai >= 80) and (nilai <= 90 ):
     print('Lulus')
elif (nilai >= 70) and (nilai <= 80):
     print('Lulus')
elif (nilai >= 60) and (nilai <= 70):
     print('Tidak lulus')
elif (nilai >= 50) and (nilai <= 60):
     print('Tidak lulus')
elif (nilai >= 40) and (nilai <= 20):
     print('Tidak lulus')
print("========================================")
print("INILAH HASIL UJIAN ANDA")

class Ayam():
 def __init__(self, nama, umur, warna ):
    self.nama = nama
    self.umur = umur
    self.warna = warna

 def suara(self):
     print("Suara : kuk kruyyuk")

 def jenis_ayam(self):
     print("jenis ayam : ayam jantan")

myAyam = Ayam("miko", 1, "putih")
jago= Ayam("jago", 2, "hitam" )

print(myAyam.nama, myAyam.umur, myAyam.warna)
myAyam.suara()
print(jago.nama, jago.umur, jago.warna)
myAyam.jenis_ayam()


