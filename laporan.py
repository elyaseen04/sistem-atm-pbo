# Class untuk mengelola riwayat transaksi

class Laporan:
    def __init__(self):
        self.__daftar_transaksi = []

    def tambah_transaksi(self, transaksi):
        self.__daftar_transaksi.append(transaksi)

    def tampilkan_laporan(self):
        if not self.__daftar_transaksi:
            return "Belum ada transaksi."
        hasil = "\n========== RIWAYAT TRANSAKSI ==========\n"
        for i, t in enumerate(self.__daftar_transaksi, 1):
            hasil += f"{i}. {t.ringkasan()}\n"
        return hasil.strip()

    def total_transaksi(self):
        return sum(t.jumlah for t in self.__daftar_transaksi)

    @property
    def daftar_transaksi(self):
        return self.__daftar_transaksi