import os
import time
import pandas as pd

def header_view():
    block_text = """
▓▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓  ▓▓▓▓▓▓  ▓▓▓▓▓▓▓ ▓▓   ▓▓ ▓▓▓▓▓▓  ▓▓▓▓▓▓  ▓▓    ▓▓   ▓▓
▓▓   ▓▓ ▓▓       ▓▓   ▓▓ ▓▓    ▓▓ ▓▓      ▓▓   ▓▓ ▓▓   ▓▓ ▓▓   ▓▓ ▓▓    ▓▓   ▓▓
▓▓▓▓▓▓▓ ▓▓  ▓▓▓  ▓▓▓▓▓▓  ▓▓    ▓▓ ▓▓▓▓▓▓▓ ▓▓   ▓▓ ▓▓▓▓▓▓  ▓▓▓▓▓▓  ▓▓     ▓▓▓▓▓
▓▓   ▓▓ ▓▓   ▓▓  ▓▓   ▓▓ ▓▓    ▓▓      ▓▓ ▓▓   ▓▓ ▓▓      ▓▓      ▓▓      ▓▓
▓▓   ▓▓ ▓▓▓▓▓▓▓  ▓▓   ▓▓ ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓ ▓▓      ▓▓      ▓▓▓▓▓▓  ▓▓
"""
    print(block_text)

def menu_utama():
    try:
        while True:
            clear()
            header_view()
            print("===========================================================================")
            print("================== W E L C O M E  T O  A G R O S U P P L Y ================")
            print("===========================================================================")
            print("1. Menu Admin")
            print("2. Menu User")
            print("0. Keluar dari Program")
            pilihan = input("Pilih opsi yang ingin dipilih: ")
            if pilihan == "1":
                admin()
                time.sleep(1)
            elif pilihan == "2":
                menu_user()
                time.sleep(1)
            elif pilihan == "0":
                time.sleep(1)
                print("Terima kasih telah menggunakan aplikasi ini!")
                break
            else:
                print("Pilihan tidak valid!")
                time.sleep(1)
    except:
        print("Menu yang anda masukkan tidak ada.")

# ========================================== M O D E  A D M I N ==========================================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def admin():
    try:
        while True:
            clear()
            print("=====================================================================")
            print("============================== A D M I N ============================")
            print("=====================================================================")
            print("-----------------------------")
            print("1. Login Admin")
            print("-----------------------------")
            print("2. Register Akun Admin")
            print("-----------------------------")
            print("0. Keluar dari Program")
            print("-----------------------------")
            pilihan = input("Pilih opsi yang ingin dipilih: ")
            if pilihan == "1":
                login()
                time.sleep(1)
            elif pilihan == "2":
                register()
                time.sleep(1)
            elif pilihan == "0":
                time.sleep(1)
                break
            else:
                print("Pilihan tidak valid!")
                time.sleep(1)
    except:
        print("Menu yang anda masukkan tidak ada.")

def menu_admin():
    try:
        while True:
            clear()
            print("=====================================================")
            print("=============== M E N U  A D M I N =================")
            print("=====================================================")
            print("\n--- Menu Admin ---")
            print("1. Kelola Produk")
            print("2. Lihat Akun")
            print("3. voucher")
            print("0. Logout")
            pilihan = input("Pilihan: ")
            if pilihan == "1":
                menu_produk()
                time.sleep(1)
            elif pilihan == "2":
                tampilkan_akun()
                time.sleep(1)
            elif pilihan == "3":
                kelola_voucher()
                time.sleep(1)   
            elif pilihan == "0":
                time.sleep(1)
                break
            else:
                print("Pilihan tidak valid!")
    except:
        print("Menu yang anda masukkan tidak ada.")

def register():
    clear()
    try:
        validasi = input("Apakah anda adalah admin baru Agrosupply? (y/n): ").lower()
        if validasi != 'y':
            print("Anda tidak dapat mendaftar sebagai admin baru.")
            input("Tekan Enter untuk kembali...")
            return
        
        validasi2 = input("Masukkan kode verifikasi anda: ")
        if validasi2 != 'agrosupplyadmin':
            print("Kode verifikasi salah!")
            input("Tekan Enter untuk kembali...")
            return

        clear()
        print("=====================================================")
        print("============ R E G I S T E R  A D M I N ============")
        print("=====================================================")

        user_baru = input("Username Baru Admin: ").strip()
        pass_baru = input("Password Baru Admin: ").strip()
        konfirmasi_pass = input("Konfirmasi password: ").strip()

        if pass_baru != konfirmasi_pass:
            print("Password tidak sesuai!")
            input("Tekan Enter untuk kembali...")
            return

        file = "akun_admin.csv"
        kolom = ["Username", "Password"]

        if os.path.exists(file):
            df = pd.read_csv(file, dtype=str)
        else:
            df = pd.DataFrame(columns=kolom)

        if len(df[df["Username"] == user_baru]) > 0:
            print("Username sudah dipakai, gunakan yang lain.")
            input("Tekan Enter...")
            return

        if len(df[df["Password"] == pass_baru]) > 0:
            print("Password sudah digunakan, buat yang lain.")
            input("Tekan Enter...")
            return

        df.loc[len(df)] = [user_baru, pass_baru]
        df.to_csv(file, index=False)

        print("Akun berhasil dibuat!")
        input("Tekan Enter untuk kembali...")

    except Exception as e:
        print(f"Terjadi error saat register: {e}")
        input("Enter...")

def login():
    clear()
    print("=====================================================")
    print("============ L O G I N  K E  A D M I N ==============")
    print("=====================================================")

    file = "akun_admin.csv"

    if not os.path.exists(file):
        print("Belum ada akun admin. Silakan register dulu.")
        input("Tekan Enter untuk kembali...")
        return

    df = pd.read_csv(file, dtype=str)              

    username = input("Masukkan Username Admin Anda: ").strip()
    password = input("Masukkann Password Admin Anda: ").strip()

    cek = df[(df["Username"] == username) & (df["Password"] == password)]

    if not cek.empty:
        print(f"Selamat datang, {username}!")
        time.sleep(1)
        menu_admin()
    else:
        print("Username atau password salah!")
        input("Tekan Enter untuk kembali...")
    
def kelola_voucher():
    file_voucher = "voucher.csv"
    kolom = ["Kode", "Diskon"]

    if not os.path.exists(file_voucher):
        df = pd.DataFrame(columns=kolom)
        df.to_csv(file_voucher, index=False)

    while True:
        clear()
        print("========================================")
        print("------ K E L O L A  V O U C H E R ------")
        print("========================================")

        df = pd.read_csv(file_voucher)

        print("\nDaftar Voucher:")
        print("Index | Kode Voucher | Diskon")
        print("-----------------------------------")

        if df.empty:
            print("Belum ada voucher.")
        else:
            for i in range(len(df)):
                kode = df["Kode"][i]
                diskon = int(float(df["Diskon"][i]) * 100)
                print(f"{i+1}. {kode} - {diskon}%")

        print("\n1. Tambah Voucher")
        print("2. Edit Voucher")
        print("3. Hapus Voucher")
        print("0. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            clear()
            print("=== Tambah Voucher ===")

            kode = input("Kode voucher: ").strip().upper()
            diskon = input("Diskon (contoh 0.30 untuk 30%): ").strip()

            try:
                diskon = float(diskon)
            except:
                print("Diskon harus angka desimal.")
                input("Enter...")
                continue

            if not (0 < diskon < 1):
                print("Diskon harus antara 0.1 - 0.9")
                input("Enter...")
                continue

            if len(df[df["Kode"] == kode]) > 0:
                print("Kode voucher sudah ada.")
                input("Enter...")
                continue

            df.loc[len(df)] = [kode, diskon]
            df.to_csv(file_voucher, index=False)

            print("Voucher berhasil ditambahkan!")
            input("Enter...")

        elif pilihan == "2":
            clear()
            print("=== Edit Voucher ===")

            idx = input("Masukkan index voucher: ")

            if not idx.isdigit():
                print("Index harus angka.")
                input("Enter...")
                continue

            idx = int(idx) - 1

            if idx < 0 or idx >= len(df):
                print("Index tidak ditemukan.")
                input("Enter...")
                continue

            data_lama = df.loc[idx]
            print(f"Kode lama  : {data_lama['Kode']}")
            print(f"Diskon lama: {float(data_lama['Diskon'])*100:.0f}%")

            kode_baru = input("Kode baru (enter = tidak ubah): ").strip().upper()
            diskon_baru = input("Diskon baru (enter = tidak ubah): ").strip()

            if kode_baru == "":
                kode_baru = data_lama["Kode"]

            if diskon_baru == "":
                diskon_baru = float(data_lama["Diskon"])
            else:
                try:
                    diskon_baru = float(diskon_baru)
                except:
                    print("Diskon harus angka.")
                    input("Enter...")
                    continue

                if not (0 < diskon_baru < 1):
                    print("Diskon harus antara 0.1 - 0.9")
                    input("Enter...")
                    continue

            df.at[idx, "Kode"] = kode_baru
            df.at[idx, "Diskon"] = diskon_baru

            df.to_csv(file_voucher, index=False)

            print("Voucher berhasil diperbarui!")
            input("Enter...")

        elif pilihan == "3":
            clear()
            print("=== Hapus Voucher ===")

            idx = input("Masukkan index voucher: ")

            if not idx.isdigit():
                print("Index harus angka.")
                input("Enter...")
                continue

            idx = int(idx) - 1

            if idx < 0 or idx >= len(df):
                print("Index tidak ditemukan.")
                input("Enter...")
                continue

            konfirmasi = input(f"Hapus voucher {df.loc[idx, 'Kode']}? (y/n): ")

            if konfirmasi.lower() == "y":
                df = df.drop(idx).reset_index(drop=True)
                df.to_csv(file_voucher, index=False)
                print("Voucher berhasil dihapus!")
            else:
                print("Dibatalkan.")

            input("Enter...")

        elif pilihan == "0":
            return

        else:
            print("Pilihan tidak valid.")
            input("Enter...")

def menu_produk():
    try:
        while True:
            clear()
            print("=====================================================")
            print("============== M E N U  P R O D U K ================")
            print("=====================================================")
            print("1. Tambah Produk")
            print("2. Tampilkan Produk")
            print("3. Hapus Produk")
            print("4. Ubah Produk")
            print("5. Status Pembeli")
            print("0. Kembali")
            pilihan = input("Masukkan pilihan anda (0/1/2/3/4/5): ")
            if pilihan == "1":
                time.sleep(1)
                tambah_produk()
            elif pilihan == "2":
                time.sleep(1)
                tampilkan_produk()
            elif pilihan == "3":
                time.sleep(1)
                hapus_produk()
            elif pilihan == "4":
                time.sleep(1)
                ubah_produk()
            elif pilihan == "5":
                time.sleep(1)
                status_pembeli()
            elif pilihan == "0":
                time.sleep(1)
                break
            else:
                print("Pilihan tidak valid!")
    except:
        print("Menu yang anda masukkkan tidak valid! Mohon kembali ke Menu Admin")


def tambah_produk():
    clear()
    print("=====================================================")
    print("----------- [ T A M B A H  P R O D U K ] -----------")
    print("=====================================================")

    if os.path.exists("daftar_produk.csv"):
        df = pd.read_csv("daftar_produk.csv")
    else:
        df = pd.DataFrame(columns=["Index", "Produk", "Harga", "Stok"])

    nama = input("Nama produk   : ").strip()

    if nama == "":
        print("Nama tidak boleh kosong!")
        input("Enter...")
        return

    huruf_valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

    for c in nama:
        if c not in huruf_valid:
            print("Nama produk cuma boleh huruf dan spasi!")
            input("Enter...")
            return

    if not df.empty:
        df_filter = df[df["Produk"].str.lower() == nama.lower()]
        if not df_filter.empty:
            idx = df_filter.iloc[0]["Index"]
            print("Produk sudah ada di index", idx)
            input("Enter...")
            return

    harga = input("Harga produk  : ").strip()

    if not harga.isdigit():
        print("Harga harus angka!")
        input("Enter...")
        return

    harga = int(harga)

    if harga < 500:
        print("Harga minimal 500!")
        input("Enter...")
        return

    stok = input("Stok produk   : ").strip()

    if not stok.isdigit():
        print("Stok harus angka!")
        input("Enter...")
        return

    stok = int(stok)

    index_baru = len(df) + 1  
    df.loc[len(df)] = [index_baru, nama, harga, stok]
    df.to_csv("daftar_produk.csv", index=False)

    print("Produk berhasil ditambahkan dengan index", index_baru)
    input("Enter...")

def tampilkan_produk():
    clear()
    try:
        file = "daftar_produk.csv"
        print("=====================================================")
        print("-------- [ T A M P I L K A N  P R O D U K ] --------")
        print("=====================================================")

        if not os.path.exists(file):
            print("Belum ada produk.")
            input("\nTekan Enter untuk kembali...")
            return
        
        df = pd.read_csv(file)

        clear()
        print("=" * 60)
        print("DAFTAR PRODUK AGROSUPPLY".center(60))
        print("=" * 60)
        print(f"{'Index':<6} | {'Produk':<20} | {'Harga':<10} | {'Stok':<5}")
        print("-" * 60)

        if df.empty:
            print("Belum ada produk.")
            input("\nTekan Enter untuk kembali...")
            return

        for i in range(len(df)):
            idx  = str(df.iloc[i]["Index"])
            prod = str(df.iloc[i]["Produk"])
            hrg  = str(df.iloc[i]["Harga"])
            stk  = str(df.iloc[i]["Stok"])
            print(f"{idx:<6} | {prod:<20} | {hrg:<10} | {stk:<5}")

        input("\nTekan Enter untuk kembali...")

    except Exception as e:
        print("Terjadi kesalahan saat membuka file.")
        input("Tekan Enter untuk kembali...")

def hapus_produk():
    clear()
    file = "daftar_produk.csv"

    print("=" * 60)
    print("DAFTAR PRODUK AGROSUPPLY".center(60))
    print("=" * 60)
    print(f"{'Index':<6} | {'Produk':<20} | {'Harga':<10} | {'Stok':<5}")
    print("-" * 60)

    if not os.path.exists(file):
        print("Belum ada produk.")
        input("Enter...")
        return
    
    df = pd.read_csv(file)

    if df.empty:
        print("Belum ada produk.")
        input("Enter...")
        return
    
    for i in range(len(df)):
        idx  = str(df.iloc[i]["Index"])
        prod = str(df.iloc[i]["Produk"])
        hrg  = str(df.iloc[i]["Harga"])
        stk  = str(df.iloc[i]["Stok"])
        print(f"{idx:<6} | {prod:<20} | {hrg:<10} | {stk:<5}")
    
    print("=" * 60)
    print(" HAPUS PRODUK ".center(60))
    print("=" * 60)

    try:
        idx_hapus = int(input("Index produk yang ingin dihapus: "))

        index_list = list(df["Index"])
        if idx_hapus not in index_list:
            print("Index tidak ditemukan!")
            input("Enter...")
            return

        for i in range(len(df)):
            if df.at[i, "Index"] == idx_hapus:
                nama_produk = df.at[i, "Produk"]
                break

        yakin = input(f"Yakin ingin menghapus '{nama_produk}'? (y/n): ").lower()
        if yakin != "y":
            print(f"Produk '{nama_produk}' tidak jadi dihapus.")
            input("Enter...")
            return
        
        df = df[df["Index"] != idx_hapus]

        df = df.reset_index(drop=True)
        df["Index"] = df.index + 1

        df.to_csv(file, index=False)

        print("Produk berhasil dihapus!")
        input("Enter...")

    except:
        print("Input tidak valid!")
        input("Enter...")

def ubah_produk():
    clear()
    print("=====================================================")
    print("-------------- [ U B A H  P R O D U K ] -------------")
    print("=====================================================")

    file = "daftar_produk.csv"

    if not os.path.exists(file):
        print("Belum ada produk.")
        input("Enter...")
        return

    try:
        df = pd.read_csv(file)
    except:
        print("File CSV rusak atau format salah!")
        input("Enter...")
        return

    if df.empty:
        print("Belum ada produk.")
        input("Enter...")
        return

    print("Index | Produk               | Harga     | Stok")
    print("-" * 55)

    for i in range(len(df)):
        print(f"{df.at[i, 'Index']:<5} | {df.at[i, 'Produk']:<20} | {df.at[i, 'Harga']:<9} | {df.at[i, 'Stok']}")

    try:
        idx = int(input("\nMasukkan index produk yang ingin diubah: "))
    except:
        print("Index harus angka!")
        input("Enter...")
        return

    index_list = list(df["Index"])
    if idx not in index_list:
        print("Index tidak ditemukan!")
        input("Enter...")
        return

    target = None
    for i in range(len(df)):
        if df.at[i, "Index"] == idx:
            target = i
            break

    lama_nama  = df.at[target, 'Produk']
    lama_harga = str(df.at[target, 'Harga'])
    lama_stok  = str(df.at[target, 'Stok'])

    print("\nData Lama Produk:")
    print(f"Nama  : {lama_nama}")
    print(f"Harga : {lama_harga}")
    print(f"Stok  : {lama_stok}")

    print("\n--- Masukkan data baru (Enter = tidak mengubah) ---")

    nama_baru = input("Nama baru  : ").strip()
    if nama_baru != "":
        if not all(c.isalpha() or c == " " for c in nama_baru):
            print("Nama produk hanya boleh huruf dan spasi!")
            input("Enter...")
            return
    else:
        nama_baru = lama_nama

    harga_baru = input("Harga baru : ").strip()
    if harga_baru != "":
        if not harga_baru.isdigit():
            print("Harga harus angka!")
            input("Enter...")
            return

        harga_int = int(harga_baru)
        if harga_int < 1000:
            print("Harga minimal 4 digit (>= 1000)!")
            input("Enter...")
            return

        harga_baru = harga_int
    else:
        harga_baru = int(lama_harga)

    stok_baru = input("Stok baru  : ").strip()
    if stok_baru != "":
        if not stok_baru.isdigit():
            print("Stok harus berupa angka!")
            input("Enter...")
            return
        stok_baru = int(stok_baru)
    else:
        stok_baru = int(lama_stok)

    print("\n=== PERUBAHAN DATA ===")
    print(f"Nama  : {lama_nama}  →  {nama_baru}")
    print(f"Harga : {lama_harga} →  {harga_baru}")
    print(f"Stok  : {lama_stok}  →  {stok_baru}")

    yakin = input("\nYakin ingin menyimpan perubahan? (y/n): ").lower()
    if yakin != "y":
        print("Perubahan dibatalkan.")
        input("Enter...")
        return

    df.at[target, 'Produk'] = nama_baru
    df.at[target, 'Harga']  = harga_baru
    df.at[target, 'Stok']   = stok_baru

    df.to_csv(file, index=False)

    print("\nProduk berhasil diperbarui!")
    input("Enter...")

def tampilkan_akun():
    clear()
    try:
        print("\n========= T A M P I L K A N  A K U N ==========")
        file = "akun_admin.csv"

        if not os.path.exists(file):
            print("Belum ada akun admin.")
            input("Tekan Enter untuk kembali...")
            return
        
        try:
            df = pd.read_csv(file)
        except:
            print("File akun rusak atau tidak bisa dibaca!")
            input("Tekan Enter untuk kembali...")
            return

        if df.empty:
            print("Belum ada akun admin.")
            input("Tekan Enter untuk kembali...")
            return

        for i in range(len(df)):
            if 'Username' in df.columns:
                username = df.at[i, 'Username']
            else:
                username = df.iloc[i, 0]

            print(f"{i+1}. Username: {username}")

        input("Tekan Enter untuk kembali...")

    except Exception as e:
        print("Terjadi kesalahan saat membaca akun.")
        input("Tekan Enter untuk kembali...")

def status_pembeli():
    clear()
    file = "rekap_penjualan.csv"

    if not os.path.exists(file):
        print("Belum ada data penjualan.")
        input("Tekan Enter untuk kembali...")
        return

    print("=====================================================")
    print("======== S T A T U S  P E N J U A L A N ============")
    print("=====================================================")

    try:
        df = pd.read_csv(file)
    except:
        print("File tidak bisa dibaca.")
        input("Enter...")
        return
        
    if df.empty:
        print("Tidak ada data.")
        input("Enter...")
        return

    if df.shape[1] < 4:
        print("Format file tidak sesuai.")
        input("Enter...")
        return

    df_ok = df[df.iloc[:, 3].astype(str).str.strip() != ""]

    if df_ok.empty:
        print("Tidak ada pesanan yang valid.")
        input("Enter...")
        return

    print(f"{'No':<4} | {'Nama':<15} | {'Produk':<20} | {'Status':<15}")
    print("-" * 60)

    for i in range(len(df_ok)):
        nama = str(df_ok.iloc[i, 0])
        produk = str(df_ok.iloc[i, 3])

        if df.shape[1] > 6:
            isi = str(df_ok.iloc[i, 6]).strip()
            status = isi if isi not in ["", "nan"] else "Belum Diproses"
        else:
            status = "Belum Diproses"

        print(f"{i+1:<4} | {nama:<15} | {produk:<20} | {status:<15}")

    pilih = input("\nMasukkan nomor pesanan (atau 'n' untuk kembali): ").strip()

    if pilih.lower() == "n":
        return

    if not pilih.isdigit():
        print("Input harus angka!")
        input("Enter...")
        return

    pilih = int(pilih)

    if pilih < 1 or pilih > len(df_ok):
        print("Nomor tidak ada!")
        input("Enter...")
        return

    idx = df_ok.index[pilih - 1]

    if df.shape[1] > 6 and str(df.at[idx, df.columns[6]]).strip() != "":
        status_lama = str(df.at[idx, df.columns[6]])
    else:
        status_lama = "Belum Diproses"

    clear()
    print(f"Pesanan milik : {df.at[idx, df.columns[0]]}")
    print(f"Status sekarang : {status_lama}")

    print("\nPilih status baru:")
    print("1. Dikemas")
    print("2. Dikirim")
    print("3. Sampai")

    pilih_status = input("Masukkan pilihan (1/2/3): ")

    if pilih_status == "1":
        status_baru = "Dikemas"
    elif pilih_status == "2":
        status_baru = "Dikirim"
    elif pilih_status == "3":
        status_baru = "Sampai"
    else:
        print("Pilihan tidak valid!")
        input("Enter...")
        return

    while df.shape[1] <= 6:
        df[f"col{df.shape[1]}"] = ""

    df.at[idx, df.columns[6]] = status_baru

    df.to_csv(file, index=False)

    print("Status pesanan berhasil diperbarui!")
    input("Enter...")

# ========================================== M O D E  U S E R ==========================================

def menu_user():
    try:
        while True:
            user = login_user()
            if not user:
                return

            while True:
                clear()
                print("=====================================================================")
                print("=============== W E L C O M E  T O  A G R O S U P P L Y =============")
                print("=====================================================================")
                print("1. Lihat Produk")
                print("2. Beli Produk")
                print("3. Cek Status Pesanan")
                print("0. Keluar dari Program")
                pilihan = input("Pilih opsi yang ingin dipilih: ")

                if pilihan == "1":
                    lihat_produk()
                elif pilihan == "2":
                    beli_produk(user)
                elif pilihan == "3":
                    status_penjualan(user)
                elif pilihan == "0":
                    print("Keluar dari program. Terima kasih!")
                    return
                else:
                    print("Pilihan tidak valid!")
                    time.sleep(1)
    except Exception as e:
        print("Terjadi kesalahan:", e)
        input("Tekan enter untuk kembali.")

def login_user():
    clear()
    print("=====================================================")
    print("=============== L O G I N  U S E R ==================")
    print("=====================================================")

    file_akun = "akun_user.csv" 

    if not os.path.exists(file_akun): 
        df_kosong = pd.DataFrame(columns=["username", "alamat", "password"]) 
        df_kosong.to_csv(file_akun, index=False) 

    df = pd.read_csv(file_akun) 

    while True:
        nama = input("Masukkan username: ").strip() 

        if not nama.isalpha(): 
            print("Username harus huruf semua tanpa angka/spasi!")
            continue

        df_user = df[df["username"].str.lower() == nama.lower()] 

        if not df_user.empty:
            data = df_user.iloc[0] 

            print(f"Anda sudah terdaftar.")
            print(f"Nama   : {data['username']}") 
            print(f"Alamat : {data['alamat']}")

            pw = input("Masukkan password: ").strip()

            if pw != str(data["password"]): 
                print("Password salah! Kembali ke menu utama.")
                return None

            return {  
                "username": data["username"].strip(),
                "alamat": data["alamat"].strip().lower(),
                "password": data["password"]
            }

        print("Username belum terdaftar, silakan registrasi.")

        alamat = input("Masukkan alamat (jawa / luar jawa): ").strip().lower()
        if alamat not in ["jawa", "luar jawa"]:
            print("Alamat tidak valid! Kembali ke menu utama.")
            return None 

        pw = input("Buat password: ").strip()

        akun_baru = pd.DataFrame([{
            "username": nama,
            "alamat": alamat,
            "password": pw
        }])

        df = pd.concat([df, akun_baru], ignore_index=True) 
        df.to_csv(file_akun, index=False) 

        print(f"Akun berhasil dibuat. Selamat datang, {nama}!")
        return { 
            "username": nama,
            "alamat": alamat,
            "password": pw
        }

def lihat_produk():
    clear()
    file_produk = "daftar_produk.csv" 

    if not os.path.exists(file_produk): 
        print("Belum ada produk.")
        input("Tekan Enter untuk kembali...")
        return 
    
    try:
        df = pd.read_csv(file_produk)
    except:
        print("File produk rusak atau format tidak valid.")
        input("Tekan Enter untuk kembali...")
        return

    if df.empty: 
        print("Belum ada produk.")
        input("Tekan Enter...")
        return

    print("=" * 50)
    print("DAFTAR PRODUK AGROSUPPLY".center(50))
    print("=" * 50)
    print(f"{'Index':<6} | {'Produk':<20} | {'Harga':<10} | {'Stok':<5}")
    print("-" * 50)

    for i in range(len(df)): 
        baris = df.iloc[i] 
        print(f"{baris['Index']:<6} | {baris['Produk']:<20} | {baris['Harga']:<10} | {baris['Stok']:<5}") 

    print("-" * 50)
    input("Tekan Enter untuk kembali...")

def beli_produk(user):
    clear()

    file_produk = "daftar_produk.csv"
    if not os.path.exists(file_produk):
        print("Belum ada produk.")
        input("Tekan Enter untuk kembali...")
        return {} 

    df = pd.read_csv(file_produk)
    df["Index"] = df["Index"].astype(int)
    df["Harga"] = df["Harga"].astype(int)
    df["Stok"] = df["Stok"].astype(int)

    keranjang = {}

    while True: 
        clear()
        print("=" * 50)
        print("DAFTAR PRODUK AGROSUPPLY".center(50))
        print("=" * 50)
        print(f"{'Index':<6} | {'Produk':<20} | {'Harga':<10} | {'Stok':<5}")
        print("-" * 50)

        for i in range(len(df)): 
            print(f"{df.iloc[i]['Index']:<6} | "
                f"{df.iloc[i]['Produk']:<20} | "
                f"{df.iloc[i]['Harga']:<10} | "
                f"{df.iloc[i]['Stok']:<5}")
            
        pilih = input("\nMasukkan index produk atau 'n' untuk selesai: ").strip().lower()
        if pilih == "n":
            if not keranjang:
                print("Keranjang kosong. Pembelian dibatalkan.")
                input("Enter...")
                return {} 
            break 

        produk_cocok = df[df["Index"] == int(pilih)]
        if len(produk_cocok) == 0: 
            print("Index tidak ditemukan!")
            input("Enter...")
            continue 

        idx = produk_cocok.index[0]  
        stok = df.loc[idx, "Stok"] 

        try:
            jumlah = int(input("Jumlah dibeli: "))
        except:
            print("Jumlah harus angka!")
            input("Enter...")
            continue

        if jumlah <= 0:
            print("Jumlah harus > 0")
            input("Enter...")
            continue

        if jumlah > stok:
            print(f"Stok tidak cukup. Sisa stok: {stok}")
            input("Enter...")
            continue

        df.loc[idx, "Stok"] = stok - jumlah
        if pilih not in keranjang:
            keranjang[pilih] = jumlah
        else:
            keranjang[pilih] += jumlah

        print("Berhasil ditambahkan!")

        total_sementara = 0
        for index_produk in keranjang:
            jumlah = keranjang[index_produk]
            data_produk = df[df["Index"] == int(index_produk)]
            harga = int(data_produk["Harga"].iloc[0])
            total_sementara += harga * jumlah

        print(f"\nTotal sementara (belum diskon & ongkir): Rp {total_sementara}")
        input("Enter...")


    total = 0
    for index_produk in keranjang:                     
        jumlah_beli = keranjang[index_produk]          
        produk = df[df["Index"] == int(index_produk)]  
        harga = int(produk["Harga"].iloc[0])         
        total += harga * jumlah_beli                  

    clear()
    file_voucher = "voucher.csv"
    daftar_voucher = {} 

    if os.path.exists(file_voucher):
        df_voucher = pd.read_csv(file_voucher) 
        for i in range(len(df_voucher)):
            kode = df_voucher.iloc[i]["Kode"].strip().upper() 
            diskon = float(df_voucher.iloc[i]["Diskon"]) 
            daftar_voucher[kode] = diskon 

    while True:
        kode = input("Punya voucher? (enter untuk skip): ").strip().upper()
        if kode == "":
            diskon = 0
            break 
        if kode in daftar_voucher: 
            diskon = daftar_voucher[kode]
            print(f"Voucher valid! Diskon {int(diskon*100)}%")
            input("Enter...")
            break 
        else:
            ulang = input("Kode salah. Coba lagi? (y/n): ").strip().lower()
            if ulang != "y":
                diskon = 0
                break 

    potongan = int(total * diskon)
    total_setelah_diskon = total - potongan

    print("="*40)
    print("RINGKASAN SETELAH VOUCHER")
    print(f"Total awal         : Rp {total}")
    print(f"Diskon voucher     : Rp {potongan}")
    print(f"Total setelah diskon: Rp {total_setelah_diskon}")
    print("="*40)
    input("Enter...")

    clear()
    alamat = user["alamat"] 
    if alamat == "jawa":
        ongkir = 3000
    else:
        ongkir = 5000

    print("Metode pengiriman:")
    print("1. Ekspres (+20000)")
    print("2. Standar (+10000)")
    while True:
        pilih = input("Pilih (1/2): ").strip()
        if pilih == "1":
            metode = "Ekspres"
            biaya_kirim = 20000
            break
        elif pilih == "2":
            metode = "Standar"
            biaya_kirim = 10000
            break

    print("\n=== RINGKASAN ONGKIR ===")
    print(f"Ongkir dasar wilayah : Rp {ongkir}")
    print(f"Metode {metode}       : Rp {biaya_kirim}")
    print(f"Subtotal setelah ongkir: Rp {total_setelah_diskon + ongkir + biaya_kirim}")
    input("Enter...")

    total_ongkir = total_setelah_diskon + ongkir + biaya_kirim

    clear()
    print("Metode Pembayaran:")
    print("1. QRIS (0 admin)")
    print("2. BCA")

    while True:
        bayar = input("Pilih (1/2): ").strip()
        if bayar == "1":
            admin = 0
            break
        elif bayar == "2":
            sesama = input("Sesama BCA? (y/n): ").lower()
            if sesama == "y":
                admin = 2000
            else:
                admin = 6500
            
            break

    total_akhir = total_ongkir + admin

    while True:
        yakin = input("Anda yakin ingin konfirmasi pembayaran? (y/n): ").strip().lower()
        if yakin in ["y", "n"]:
            break
        print("Input harus 'y' atau 'n' saja!")

    if yakin == "n":
        clear()
        print("Pembayaran dibatalkan.")
        df = pd.read_csv(file_produk) 
        input("Tekan Enter untuk kembali...")
        return {}  
    
    clear()
    while True:
        rek = input("Masukkan nomor rekening (8 digit): ").strip()
        if rek.isdigit() and len(rek) == 8:
            break 
        print("Rekening harus 8 angka!")

    df.to_csv(file_produk, index=False)

    file_rekap = "rekap_penjualan.csv"

    produk_list_final = []
    for idx in keranjang: 
        jumlah_beli = keranjang[idx]   
        baris = df[df["Index"] == int(idx)].iloc[0]  
        nama_produk = baris["Produk"] 
        produk_list_final.append(f"{nama_produk} {jumlah_beli}x") 

    data_rekap = {
        "Nama": user["username"],
        "Alamat": user["alamat"],
        "Tanggal": time.strftime("%Y-%m-%d %H:%M:%S"),
        "Produk": "; ".join(produk_list_final),       
        "TotalBelanja": total_akhir,
        "Rekening": rek,
        "StatusPesanan": "Belum Diproses"
    }

    if not os.path.exists(file_rekap):
        df_r = pd.DataFrame([data_rekap]) 
    else:
        df_lama = pd.read_csv(file_rekap)
        df_r = pd.concat([df_lama, pd.DataFrame([data_rekap])], ignore_index=True)

    df_r.to_csv(file_rekap, index=False) 

    clear()
    print("===== NOTA PEMBELIAN =====")
    print(f"Nama     : {user['username']}")
    print(f"Alamat   : {user['alamat']}")
    print(f"Rekening : {rek}")
    print("-" * 40)
    print("Rincian:")

    for idx in keranjang:
        jumlah_beli = keranjang[idx]
        baris = df[df["Index"] == int(idx)].iloc[0] 
        nama = baris["Produk"]
        harga = int(baris["Harga"])
        print(f"{nama} x{jumlah_beli} = Rp {harga * jumlah_beli}")

    print("-" * 40)
    print(f"Total awal     : Rp {total}")
    print(f"Diskon         : Rp {potongan}")
    print(f"Ongkir         : Rp {ongkir}")
    print(f"{metode}       : Rp {biaya_kirim}")
    print(f"Admin          : Rp {admin}")
    print(f"TOTAL BAYAR    : Rp {total_akhir}")
    print("-" * 40)
    pull_gacha()
    input("Tekan Enter untuk kembali...")

    return keranjang

def pull_gacha():
    try:
        diskon = pd.read_csv('voucher.csv')

        if diskon.empty:
            print("=====================================================")
            print("       Belum ada voucher untuk hari ini :(           ")
            print("=====================================================")
            return

        random_row = diskon.sample(n=1).iloc[0] 
        kode_voucher = random_row['Kode'] 
        diskon = random_row['Diskon'] 

        print("=======================================================================================")
        print(f"Coba Voucher {kode_voucher} untuk diskon {int(diskon * 100)}% di pembelian selanjutnya")
        print("=======================================================================================")

    except:
        print("=====================================================")
        print("Gagal melakukan gacha voucher! Cek file voucher.csv")
        print("=====================================================")

def status_penjualan(user):
    clear()
    file = "rekap_penjualan.csv"

    if not os.path.exists(file):
        print("Belum ada data penjualan.")
        input("Tekan Enter untuk kembali...")
        return

    try:
        df = pd.read_csv(file)

        if "Nama" not in df.columns or "Produk" not in df.columns:
            print("Format file penjualan tidak sesuai.")
            input("Tekan Enter untuk kembali...")
            return 
        
        nama_user = user["username"].lower() 
        df_user = df[
            (df["Nama"].str.lower() == nama_user) & 
            (df["Produk"].str.strip() != "") 
        ]

        if df_user.empty:
            print("Belum ada pesanan untuk Anda.")
            input("Tekan Enter untuk kembali...")
            return 

        print("=====================================================")
        print("========== S T A T U S  P E N J U A L A N ==========")
        print("=====================================================")
        print(f"{'No':<4} | {'Produk':<30} | {'Status':<15} | {'Tanggal':<20}")
        print("-" * 65)

        nomor = 1 
        for idx in range(len(df_user)): 
            produk = str(df_user.iloc[idx]["Produk"])
            if "StatusPesanan" in df_user.columns:
                status = str(df_user.iloc[idx]["StatusPesanan"])  
            else:
                status = "Belum Diproses"
                
            if "Tanggal" in df_user.columns:
                tanggal = str(df_user.iloc[idx]["Tanggal"])  
            else:
                tanggal = "-"

            print(f"{nomor:<4} | {produk:<30} | {status:<15} | {tanggal:<20}")
            nomor += 1

        input("\nTekan Enter untuk kembali ke menu...")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        input("Tekan Enter untuk kembali...")

if __name__ == "__main__":
    menu_utama()


    