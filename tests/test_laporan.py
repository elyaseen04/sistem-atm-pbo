import unittest
from laporan import Laporan
from transaksi import TransaksiSetor, TransaksiTarik

class TestLaporan(unittest.TestCase):
    def setUp(self):
        self.laporan = Laporan()

    def test_laporan_awal_kosong(self):
        self.assertEqual(len(self.laporan.daftar_transaksi), 0)
        self.assertEqual(self.laporan.tampilkan_laporan(), "Belum ada transaksi.")

    def test_tambah_transaksi(self):
        t1 = TransaksiSetor(100000)
        self.laporan.tambah_transaksi(t1)
        self.assertEqual(len(self.laporan.daftar_transaksi), 1)

    def test_total_dan_isi_laporan(self):
        self.laporan.tambah_transaksi(TransaksiSetor(200000))
        self.laporan.tambah_transaksi(TransaksiTarik(50000))
        self.assertEqual(self.laporan.total_transaksi(), 250000)
        
        output = self.laporan.tampilkan_laporan()
        self.assertIn("PENYETORAN", output)
        self.assertIn("PENARIKAN", output)

if __name__ == "__main__":
    unittest.main()