def input_data_mahasiswa():
    mahasiswa = []

    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        mahasiswa.append({'NIM': nim, 'Nama': nama})
        tambah_lagi = input("Ingin tambah data lagi? (ya/tidak): ").lower()
        if tambah_lagi != 'ya':
            break
    print("\nData Mahasiswa:")
    for mhs in mahasiswa:
        print(f"NIM: {mhs['NIM']}, Nama: {mhs['Nama']}")

input_data_mahasiswa()