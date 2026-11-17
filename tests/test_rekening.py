import unittest
from nasabah import Nasabah
from rekening import Rekening
from exception import SaldoTidakCukupError, JumlahTidakValidError

class TestRekening(unittest.TestCase):
    def setUp(self):
        self.nasabah = Nasabah("m.umar yain", "3326123456789012", "081234567890")
        self.rekening = Rekening("60225046", self.nasabah, 1000000.0)

    def test_cek_saldo_awal(self):
        self.assertEqual(self.rekening.cek_saldo(), 1000000.0)

    def test_setor_dan_tarik(self):
        self.rekening.setor_tunai(500000.0)
        self.assertEqual(self.rekening.cek_saldo(), 1500000.0)
        
        self.rekening.tarik_tunai(200000.0)
        self.assertEqual(self.rekening.cek_saldo(), 1300000.0)

    def test_jumlah_tidak_valid(self):
        with self.assertRaises(JumlahTidakValidError):
            self.rekening.tarik_tunai(0)
        with self.assertRaises(JumlahTidakValidError):
            self.rekening.setor_tunai(-50000)

    def test_saldo_tidak_cukup(self):
        with self.assertRaises(SaldoTidakCukupError):
            self.rekening.tarik_tunai(2000000.0)

    def test_transfer(self):
        nasabah2 = Nasabah("Diva", "3326987654321098", "089876543210")
        rekening2 = Rekening("99999999", nasabah2, 200000.0)
        
        self.rekening.transfer(rekening2, 300000.0)
        self.assertEqual(self.rekening.cek_saldo(), 700000.0)
        self.assertEqual(rekening2.cek_saldo(), 500000.0)

if __name__ == "__main__":
    unittest.main()