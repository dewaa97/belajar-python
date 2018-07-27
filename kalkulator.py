def tambah ():
    print ('1. Penjumlahan')
    a = int(input ('Masukkan nilai x = '))
    b = int(input ('Masukkan nilai y = '))
    c = a + b
    print ('x + y = ', c)
    print (' ')
    tanya ()

def kurang ():
    print ('2. Pengurangan')
    a = int(input ('Masukkan nilai x = '))
    b = int(input ('Masukkan nilai y = '))
    c = a-b
    print ('x - y = ', c)
    print (' ')
    tanya ()
    
def kali ():
    print ('3. Kali')
    a = int(input ('Masukkan nilai x = '))
    b = int(input ('Masukkan nilai y = '))
    c = a*b
    print ('x * y = ', c)
    print (' ')
    tanya ()

def bagi ():
    print ('4. Bagi')
    a = int(input ('Masukkan nilai x = '))
    b = int(input ('Masukkan nilai y = '))
    c = a/b
    print ('x / y = ', c)
    print (' ')
    tanya ()

def tanya ():
    choose = input ('Apakah anda ingin mengulang (Y/N)? ')
    if choose == 'Y' or choose == 'y':
        kalkulator()
    elif choose == 'N' or choose == 'n':
        print ('Terima kasih sudah menggunakan program ini')
        exit()
    else:
        print ('Maaf, input yang anda masukkan salah')
        tanya()
    

    print ('Silahkan masukkan Y atau N')
    tanya ()

def kalkulator ():
	print ('Program Kalkulator Sederhana')
	print ('############################')
	print ('1. Penjumlahan')
	print ('2. Pengurangan')
	print ('3. Kali')
	print ('4. Bagi')
	print ('############################')
	print ('Silahkan pilih 1-4')
	print (' ')

	pil = input ('Masukkan pilihan : ')
	if pil == '1':
		tambah ()
	elif pil == '2':
		kurang ()
	elif pil == '3':
		kali ()
	elif pil == '4':
		bagi ()
	else:
		print ('Maaf, input yang anda masukkan salah')
		print ('Coba ulangi lagi')
		tanya()

kalkulator()