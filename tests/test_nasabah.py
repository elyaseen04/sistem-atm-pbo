import unittest
from nasabah import Nasabah

class TestNasabah(unittest.TestCase):
    def setUp(self):
        self.nasabah = Nasabah("m.umar yain", "3326123456789012", "081234567890")

    def test_data_nasabah_tersimpan(self):
        self.assertEqual(self.nasabah.nama, "m.umar yain")
        self.assertEqual(self.nasabah.nik, "3326123456789012")
        self.assertEqual(self.nasabah.no_hp, "081234567890")

    def test_setter_nama(self):
        self.nasabah.nama = "Umar Yasin"
        self.assertEqual(self.nasabah.nama, "Umar Yasin")

    def test_nik_tidak_valid(self):
        with self.assertRaises(ValueError):
            self.nasabah.nik = "123"

if __name__ == "__main__":
    unittest.main()