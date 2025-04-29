n = int(input()) #o(1) -> baca jumlah chunk dari input 
a = list(map(int, input().split())) #o(n) -> membaca dan memetakan n nilai. 

dict_count = {} #o(1) -> dictionary kosong menyimpan peanut bits sum_chunk & index pasangan double chunk 

# jika sum_chunk sudah ada di dict_count : tambah index ke dict 
# jika blm ada : masukan ke dict dengan nilai awal berisi i 

for i in range(n - 1): #o(n-1)= o(n) -> Iterasi semua chunk untuk membuat pasangan double chunk 
    sum_chunk = a[i] + a[i + 1] #o(1) hitung jumlah peanut bits dalam double chunk 

    if sum_chunk in dict_count: #o(1) 
        dict_count[sum_chunk].append(i) #o(1) 
    else: 
        dict_count[sum_chunk] = [i] #o(1) 


max_chunk = 0 #o(1) 

for index in dict_count.values(): #o(m) -> iterasi daftar index di dict_count 

    c= 0 #o(1) -> jml double chunk yang valid 
    last_idx = -2 #o(1) -> simpan index terakhir yang valid (pasangan double chunk tidak boleh bertumpukan)  
    for idx in index: #o(k) 

        if idx > last_idx+1: #o(1) -> Cek apakah pasangan double chunk tidak bertumpuk dengan pasangan sebelumnya. 
            c += 1 #o(1) -> valid maka c+1 
            last_idx = idx #o(1) -> perbarui last idx 

    max_chunk=max(max_chunk,c) #o(1) -> perbarui nilai maximum 