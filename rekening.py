# Class untuk mengelola rekening, saldo, dan transaksi ATM
from exception import SaldoTidakCukupError, JumlahTidakValidError
from laporan import Laporan
from transaksi import TransaksiTarik, TransaksiSetor, TransaksiTransfer

class Rekening:
    def __init__(self, nomor_rekening, nasabah, saldo_awal=0.0):
        self.__nomor_rekening = nomor_rekening
        self.__nasabah = nasabah
        self.__saldo = float(saldo_awal)
        self.__laporan = Laporan()

    @property
    def nomor_rekening(self):
        return self.__nomor_rekening

    @property
    def nasabah(self):
        return self.__nasabah

    @property
    def saldo(self):
        return self.__saldo

    @property
    def laporan(self):
        return self.__laporan

    def cek_saldo(self):
        return self.__saldo

    def tarik_tunai(self, jumlah):
        if jumlah <= 0:
            raise JumlahTidakValidError("Jumlah penarikan harus lebih besar dari 0.")
        if self.__saldo < jumlah:
            raise SaldoTidakCukupError("Saldo tidak mencukupi untuk penarikan.")
        
        self.__saldo -= jumlah
        transaksi = TransaksiTarik(jumlah)
        self.__laporan.tambah_transaksi(transaksi)

    def setor_tunai(self, jumlah):
        if jumlah <= 0:
            raise JumlahTidakValidError("Jumlah setoran harus lebih besar dari 0.")
        
        self.__saldo += jumlah
        transaksi = TransaksiSetor(jumlah)
        self.__laporan.tambah_transaksi(transaksi)

    def transfer(self, rekening_tujuan, jumlah):
        if jumlah <= 0:
            raise JumlahTidakValidError("Jumlah transfer harus lebih besar dari 0.")
        if self.__saldo < jumlah:
            raise SaldoTidakCukupError("Saldo tidak mencukupi untuk transfer.")
        
        self.__saldo -= jumlah
        rekening_tujuan.setor_eksternal(jumlah)
        transaksi = TransaksiTransfer(jumlah, rekening_tujuan.nomor_rekening)
        self.__laporan.tambah_transaksi(transaksi)

    def setor_eksternal(self, jumlah):
        self.__saldo += jumlah