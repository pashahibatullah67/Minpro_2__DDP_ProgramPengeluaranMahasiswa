import pwinput
import os
import time
from prettytable import PrettyTable

pengeluaran = [
    {"Nama": "Nasi Goreng", "Kategori": "Makanan", "Harga": 17000},
    {"Nama": "Bensin", "Kategori": "Transportasi", "Harga": 50000}
]


def hapus_layar():
    os.system('cls')


def tambah_pengeluaran():
    hapus_layar()
    print("=== TAMBAH PENGELUARAN ===")
    nama_barang = input("Masukkan nama barang: ")

    while nama_barang == "":
        print("Nama barang tidak boleh kosong bosku.")
        nama_barang = input("Apa lagi yang dibeli nih: ")

    kategori_barang = input("Buat apa kamu beli itu: ")

    while kategori_barang == "":
        print("Kategori barang tidak boleh kosong bosku.")
        kategori_barang = input("Buat apa kamu beli itu: ")

    while True:
        try:
            harga_barang = int(input("Berapa harganya bos: Rp"))

            if harga_barang <= 0:
                print("Dapat gratis atau maling bos? Kok bisa dapat 0? Masukkan yang betul bos, harus lebih dari 0")
            else:
                pengeluaran.append({
                    "Nama": nama_barang,
                    "Kategori": kategori_barang,
                    "Harga": harga_barang
                })
                break

        except ValueError:
            print("Masukkan harganya yang betul bos, harus pake angka bukan huruf")

    print("Nambah lagi nih pengeluarannya bos, yaudah deh")


def tampilkan_pengeluaran():
    hapus_layar()

    print("=== DAFTAR PENGELUARAN ===")

    if len(pengeluaran) == 0:
        print("Belum ada pengeluaran bos, lagi kere kah? Coba tambahin dulu")
        input("Tekan enter untuk kembali ke menu utama bos...")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Barang", "Kategori", "Harga (Rp)"]

    total_pengeluaran = 0

    for i, data in enumerate(pengeluaran, start=1):
        tabel.add_row([i, data["Nama"], data["Kategori"], data["Harga"]])
        total_pengeluaran += data["Harga"]

    print(tabel)
    print(f"\nTotal pengeluaran bos: Rp{total_pengeluaran} bos")
    input("Tekan enter untuk kembali ke menu utama bos...")


def ubah_pengeluaran():
    hapus_layar()

    print("=== UBAH PENGELUARAN ===")

    if len(pengeluaran) == 0:
        print("Belum ada pengeluaran bos, lagi kere kah? Coba tambahin dulu")
        time.sleep(3)
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Barang", "Kategori", "Harga (Rp)"]

    for i, data in enumerate(pengeluaran, start=1):
        tabel.add_row([i, data["Nama"], data["Kategori"], data["Harga"]])

    print(tabel)

    while True:
        try:
            nomor_barang = int(input("Masukkan nomor barang yang ingin anda ubah: "))

            if 1 <= nomor_barang <= len(pengeluaran):
                break
            else:
                print("Gaada nomornya bosku.")
        except ValueError:
            print("Nomor barang harus berupa angka bos.")

    index_barang = nomor_barang - 1
    nama_barang_baru = input("Masukkan nama barang yang baru bos: ")
    while nama_barang_baru == "":
        print("Jangan sampai kosong ya bos.")
        nama_barang_baru = input("Masukkan nama barang anda yang baru bos: ")

    kategori_barang_baru = input("Masukkan kategori barang yang baru bos: ")
    while kategori_barang_baru == "":
        print("Kategori gaboleh kosong bosku.")
        kategori_barang_baru = input("Masukkan kategori barang anda yang baru bos: ")

    while True:
        try:
            nominal_barang_baru = int(input("Masukkan harganya berapa bosku: Rp "))

            if nominal_barang_baru > 0:
                break
            else:
                print("Dapat gratis bos? Harga harus lebih dari 0 bos")

        except ValueError:
            print("Masukan harus pake angka ya bos")

    yakin = input(
        "Yakin mau mengubah barang ini bos? Ketik ya jika ingin mengubah dan no jika tidak ya bos. "
    ).lower()

    if yakin == "ya":
        pengeluaran[index_barang] = {
            "Nama": nama_barang_baru,
            "Kategori": kategori_barang_baru,
            "Harga": nominal_barang_baru
        }
        print("Data berhasil diubah nih bos, awas aja sampe salah.")
    else:
        print("Barang tidak jadi diubah ya bos.")

    time.sleep(3)


def hapus_pengeluaran():
    hapus_layar()

    print("=== HAPUS PENGELUARAN ===")

    if len(pengeluaran) == 0:
        print("Gaada yang bisa dihapus bos.")
        time.sleep(3)
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Kategori", "Harga"]

    for i, data in enumerate(pengeluaran, start=1):
        tabel.add_row([
            i,
            data["Nama"],
            data["Kategori"],
            f"Rp {data['Harga']}"
        ])

    print(tabel)

    while True:
         try:
            nomor_barang = int(input("Masukkan nomor barang yang ingin anda hapus bos: "))

            if nomor_barang >= 1 and nomor_barang <= len(pengeluaran):
                break
            else:
                print("Gimana mau dihapus kalo nomornya aja gaada bos.")

         except ValueError:
             print("Harus pake angka bos.")

    index_barang = nomor_barang - 1

    yakin = input("Yakin bos mau dihapus barangnya"
                  "Kalo yakin ketik ya, kalo gak yakin ketik tidak.").lower()

    if yakin == "Ya":
        pengeluaran.pop(index_barang)

        print("Berhasil dihapus nih bos, jangan sampe itu salah hapus ya bos.")

    else:
        print("Barangnya batal dihapus bos.")

    time.sleep(2)

def menu_admin():
    while True:
        hapus_layar()
       
        print("" \
        "=== MENU ADMIN ===" \
        "\n1. Tambah Pengeluaran" \
        "\n2. Lihat Pengeluaran" \
        "\n3. Ubah pengeluaran" \
        "\n4. Hapus pengeluaran" \
        "\n5. Keluar" \
        "")

        pilihan = input("Pilih menu 1-5 wahai admin penguasa: ")

        if pilihan == "1":
            tambah_pengeluaran()
        elif pilihan == "2":
            tampilkan_pengeluaran()
        elif pilihan == "3":
            ubah_pengeluaran()
        elif pilihan == "4":
            hapus_pengeluaran()
        elif pilihan == "5":
            print("Program selesai bos, jangan lupa lebih hemat bos yak.")
            break
        else:
            print("Pilihanmu gak valid bos, pilih yang betul ya bos")
            time.sleep(2)

def menu_user():
    while True:
        hapus_layar
        print("" \
        "=== MENU USER ===" \
        "\n1.Lihat pengeluaran" \
        "\n2. Keluar" \
        "")

        pilihan = input("Pilih antara 1 atau 2 wahai manusia biasa: ")

        if pilihan == "1":
            tampilkan_pengeluaran()
            input("\nTekan enter...")
        elif pilihan == "2":
            print("Selamat tinggal wahai kamu manusia biasa")
            break
        else:
            print("Kamu ini cuma user, pilih yang betul, pilihan gakk valid gitu...")
            time.sleep(2)


def login():
    while True:
        hapus_layar()
        print("=== SISTEM PENGELUARAN HARIAN MAHASISWA ===")

        username = input("username: ")
        password = pwinput.pwinput("password: ")

        if username == "Admin" and password == "AkuAdminKauMember":
            print("Selamat datang wahai admin yang berkuasa")
            time.sleep(2)
            menu_admin()
            break

        elif username == "Member" and password == "AkuMemberSuki":
            print("Yah ada member, bete gw. Welkom.")
            time.sleep(2)
            menu_user
            break

        else:
            print("Ada kesalahan di password atau username nya.")
            time.sleep(3)


login()
