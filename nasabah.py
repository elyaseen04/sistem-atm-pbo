# Class untuk menyimpan data nasabah dengan enkapsulasi dan validasi

class Nasabah:
    def __init__(self, nama, nik, no_hp):
        self.nama = nama
        self.nik = nik
        self.no_hp = no_hp

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nilai):
        if not nilai.strip():
            raise ValueError("Nama tidak boleh kosong.")
        self.__nama = nilai.strip()

    @property
    def nik(self):
        return self.__nik

    @nik.setter
    def nik(self, nilai):
        if not nilai.isdigit() or len(nilai) != 16:
            raise ValueError("NIK harus berupa 16 digit angka.")
        self.__nik = nilai

    @property
    def no_hp(self):
        return self.__no_hp

    @no_hp.setter
    def no_hp(self, nilai):
        if not nilai.isdigit() or len(nilai) < 10:
            raise ValueError("Nomor HP tidak valid.")
        self.__no_hp = nilai

    def tampilkan_data(self):
        return f"Nama: {self.__nama} | NIK: {self.__nik} | No. HP: {self.__no_hp}"