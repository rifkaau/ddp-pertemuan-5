#soal 2
# buat proram python dengan match case untuk menghitung luas bangun datar :
# jika pilih 1, maka menghitung luas persegi
# jika pilih 2, maka menghitung luas lingkaran
# jika pilih 3, maka menghitung luas segitiga
# kalau pilihannya tidak ada maka ada keterangan : salah pilih

print('ini adalah progran sederhana untuk menghitung luas bangun datar')
print('pilih menu angka 1-3 : \n1. persegi\n2. lingkaran\n3. segitiga')
pilihMenu = int(input('silahkan pilih menu dengan mengetikan angka 1-3 :'))

match pilihMenu :
    case 1 : 
        print('luas persegi')
        sisi = int(input('silahkan masukkan nilai yang mau dihitung'))
        hitung = sisi*sisi
        print(f'luas persegi adalah : {hitung}')
        print('======')

    case 2 :
        print('luas lingkaran')
        r=int(input('silahkan masukkan nilai yang mau dihitung'))
        hitung= 22/7 * r**2
        print(f'luas lingkaran adalah : {hitung}')
        
    case 3 :
         print('luas segitiga')
         a= int(input('silahkan masukkan nilai yang mau dihitung'))
         t= int(input('silahkan masukkan nilai yang mau dihitung'))
         hitung = 1/2 * a * t
         print (f'luas segitiga adalah : {hitung}')
         print('======')