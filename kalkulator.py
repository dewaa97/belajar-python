def kalkulator ():
    def tambah ():
        print '1. Penjumlahan'
        a = input ('Masukkan nilai x = ')
        b = input ('Masukkan nilai y = ')
        c = a+b
        print 'x + y = ', c
        print (' ')
        tanya ()

    def kurang ():
        print '2. Pengurangan'
        a = input ('Masukkan nilai x = ')
        b = input ('Masukkan nilai y = ')
        c = a-b
        print 'x - y = ', c
        print (' ')
        tanya ()
        
    def kali ():
        print '3. Kali'
        a = input ('Masukkan nilai x = ')
        b = input ('Masukkan nilai y = ')
        c = a*b
        print 'x * y = ', c
        print (' ')
        tanya ()

        
    def bagi ():
        print '4. Bagi'
        a = input ('Masukkan nilai x = ')
        b = input ('Masukkan nilai y = ')
        c = a/b
        print 'x / y = ', c
        print (' ')
        tanya ()

    def tanya ():
        choose = raw_input ('Apakah anda ingin mengulang (Y/N)? ')
        if choose == 'Y' or choose == 'y':
            kalkulator()
            elif choose == 'N' or choose == 'n':
                print 'Terima kasih sudah menggunakan program ini'
                else:
                    print 'Maaf, input yang anda masukkan salah'
    
    print 'Silahkan masukkan Y atau N'
    tanya ()

    print ('Program Kalkulator Sederhana')
    print ('############################')
    print ('1. Penjumlahan')
    print ('2. Pengurangan')
    print ('3. Kali')
    print ('4. Bagi')
    print ('############################')
    print ('Silahkan pilih 1-4')
    print (' ')

    pil = raw_input ('Masukkan pilihan : ')
    if pil = '1':
        tambah ()
        elif pil = '2':
            kurang ()
            elif pil = '3':
                kali ()
                elif pil = '4':
                    bagi ()
                    else:
                        print ('Maaf, input yang anda masukkan salah')
                        print ('Coba ulangi lagi')
                        tanya()
                        kalkulator ()