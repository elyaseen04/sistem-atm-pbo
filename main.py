# Program Utama Sistem ATM Sederhana (CLI)
from nasabah import Nasabah
from rekening import Rekening
from exception import SaldoTidakCukupError, JumlahTidakValidError

def tampilkan_menu():
    print("\n===== ATM SEDERHANA =====")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Transfer")
    print("5. Lihat Laporan Riwayat")
    print("6. Keluar")
    print("=========================")

def main():
    print("Selamat datang di Sistem ATM Sederhana!")
    nasabah1 = Nasabah("m.umar yain", "3326123456789012", "081234567890")
    rekening1 = Rekening("60225046", nasabah1, 1500000.0)

    nasabah2 = Nasabah("Diva", "3326987654321098", "089876543210")
    rekening2 = Rekening("99999999", nasabah2, 500000.0)

    print(f"Halo, {rekening1.nasabah.nama} (No. Rekening: {rekening1.nomor_rekening})")

    while True:
        tampilkan_menu()
        try:
            pilihan = input("Pilih menu (1-6): ").strip()
            
            if pilihan == "1":
                print(f"\n[INFO] Saldo Anda saat ini: Rp{rekening1.cek_saldo():,.2f}")
            
            elif pilihan == "2":
                jumlah = float(input("Masukkan jumlah penarikan (Rp): "))
                rekening1.tarik_tunai(jumlah)
                print(f"\n[SUKSES] Penarikan berhasil. Saldo sisa: Rp{rekening1.cek_saldo():,.2f}")
            
            elif pilihan == "3":
                jumlah = float(input("Masukkan jumlah setoran (Rp): "))
                rekening1.setor_tunai(jumlah)
                print(f"\n[SUKSES] Setoran berhasil. Saldo sekarang: Rp{rekening1.cek_saldo():,.2f}")
            
            elif pilihan == "4":
                jumlah = float(input("Masukkan jumlah transfer (Rp): "))
                no_tujuan = input("Masukkan nomor rekening tujuan (contoh: 99999999): ").strip()
                if no_tujuan == rekening2.nomor_rekening:
                    rekening1.transfer(rekening2, jumlah)
                    print(f"\n[SUKSES] Transfer sebesar Rp{jumlah:,.2f} ke Rekening {no_tujuan} berhasil!")
                else:
                    print("\n[GAGAL] Rekening tujuan tidak ditemukan!")
            
            elif pilihan == "5":
                print(rekening1.laporan.tampilkan_laporan())
            
            elif pilihan == "6":
                print("\nTerima kasih telah menggunakan ATM Sederhana. Sampai jumpa!")
                break
            else:
                print("\n[PERINGATAN] Pilihan tidak valid, silakan pilih angka 1 sampai 6.")

        except ValueError as e:
            print(f"\n[ERROR INPUT] Input tidak valid: {e}")
        except (SaldoTidakCukupError, JumlahTidakValidError) as e:
            print(f"\n[ERROR TRANSAKSI] {e}")

if __name__ == "__main__":
    main()