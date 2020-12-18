import random
import datetime
from random import Random
from costumer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan Pin Anda : "))
    trial = 0
    
    while (id != int(atm.cekPin()) and trial < 3 ):
        id = int(input("Pin Anda Salah, Silahkan Masukkan Lagi : "))
        trial += 1
        
        if trial == 3:
            print("Error. Silahkan Ambil kartu dan coba lagi....")
            exit()
    print('\n Selamat Datang di ATM Progate')
    print(' 1. - Cek Saldo. \n 2. - Debet. \n 3. - Simpan. \n 4. - Ganti Pin. \n 5. - Keluar.')
    selectMenu = int(input('\n Silahkan Pilih Menu : '))
    
    if selectMenu == 1:
        print('Saldo Anda Sekarang Rp' + str(atm.cekBalance()) + '\n')
    elif selectMenu == 2:
        nominal = float(input('Masukkan Nominal Saldo : Rp. '))
        verify_withdraw = input('Konfirmasi : Apakah Anda akan melakukan Debet dengan nominal berikut ? Rp. ' + str(nominal) + '\nPilih : y/n : ' )

        if verify_withdraw == 'y':
            print('Saldo Awal Anda Adalah : Rp.' + str(atm.cekBalance()) + '')
        else:
            exit('Terimakasih !')

        if nominal < atm.cekBalance():
            atm.withdrawBalance(nominal)
            print('Transaksi Debet Sukses!')
            print('Saldo Anda Sekarang : Rp.' + str(atm.cekBalance()) + '')
        else:
            print('Maaf Saldo Anda Tidak Mencukupi untuk melakukan debet! \n Silahkan Lakukan Pengisian Saldo!')
    elif selectMenu == 3:
        nominal = float(input('Masukkan Nominal Saldo : Rp. '))
        verify_deposit  = input('Konfirmasi : Apakah Anda akan melakukan penyimpanan dengan nominal Rp. ' + str(nominal) + '\nPilih : y/n : ')

        if verify_deposit == 'y':
            atm.depositBalance(nominal)
            print('Saldo Anda Sekarang Adalah : Rp. ' + str(atm.cekBalance()) + '\n')
        else:
            exit('Terimakasih !')
    elif selectMenu == 4 :
        verify_pin = int(input('Masukkan Pin Anda : '))

        while verify_pin != int(atm.cekPin()):
            print('Pin Anda Salah!. Coba Lagi!')
            exit('Status : '+ str(atm.Error))
        update_pin = int(input('Masukkan Pin Baru Anda : '))
        print('Sukses! \n Pin Telah Berhasil Diganti!')

        newPin = int(input('Masukkan Pin Baru Anda : '))
        
        if newPin == update_pin:
            print('Sukses! \n Pin Telah Berhasil Diganti!')
        else:
            print('Pin Anda Salah!. Coba Lagi!')
            break

    elif selectMenu == 5 :
        print('Resi Tercetak Ketika Anda Keluar. Harap Menyimpan resi tersebut Sebagai Bukti Transaksi Anda!')
        print('\nNo. Record : ', random.randint(10000, 1000000))
        print('Tanggal : ', datetime.datetime.now())
        print('Saldo Akhir : Rp. ', atm.cekBalance())
        exit(" \nTerimakasih Telah Menggunakan ATM Progate! ")
    else:
        print('Input Salah. Silahkan Coba Lagi!')
