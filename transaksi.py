# Class induk dan subclass transaksi menerapkan inheritance dan polymorphism
from datetime import datetime

class Transaksi:
    def __init__(self, jenis, jumlah):
        self.jenis = jenis
        self.jumlah = jumlah
        self.tanggal = datetime.now()

    def ringkasan(self):
        format_tanggal = self.tanggal.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{format_tanggal}] {self.jenis}: Rp{self.jumlah:,.2f}"


class TransaksiTarik(Transaksi):
    def __init__(self, jumlah):
        super().__init__("PENARIKAN", jumlah)

    def ringkasan(self):
        format_tanggal = self.tanggal.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{format_tanggal}] [PENARIKAN] Rp{self.jumlah:,.2f}"


class TransaksiSetor(Transaksi):
    def __init__(self, jumlah):
        super().__init__("PENYETORAN", jumlah)

    def ringkasan(self):
        format_tanggal = self.tanggal.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{format_tanggal}] [PENYETORAN] Rp{self.jumlah:,.2f}"


class TransaksiTransfer(Transaksi):
    def __init__(self, jumlah, rekening_tujuan):
        super().__init__("TRANSFER", jumlah)
        self.rekening_tujuan = rekening_tujuan

    def ringkasan(self):
        format_tanggal = self.tanggal.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{format_tanggal}] [TRANSFER] Rp{self.jumlah:,.2f} ke Rekening {self.rekening_tujuan}"