def ad():
    print"nilai mahasiswa"
    
nm = raw_input("Masukan Nama\n: ")
uts = input("Masukan Nilai UTS\n: ")
uas = input("Masukan Nilai UAS\n: ")
tugas = input("Masukan Nilai TUGAS\n: ")
print "Nama         : ", nm
print "Nilai UTS    : ", uts
print "Nilsi UAS    : ", uas
print "Nilai Tugas  : ", tugas
akhir = (uts+uas+tugas)/3
print "Nilai Akhir  \n: ", akhir

if akhir >= 80:
    print "Nilai Huruf  : A"
    print "Keterangan   : Lulus"
elif akhir >= 70 :
    print "Nilai Huruf  : B"
    print "Keterangan   : Lulus"
elif akhir >= 50 :
    print "Nilai Huruf  : C"
    print "Keterangan   : Tidak Lulus"
elif akhir >= 40:
    print "Nilai Huruf  : D"
    print "Keterangan   : Tidak Lulus"
else :
    print "Nilai Huruf  : E"
    print "Keterangan   : Tidak Lulus"
