import unittest
from transaksi import Transaksi, TransaksiTarik, TransaksiSetor, TransaksiTransfer

class TestTransaksi(unittest.TestCase):
    def test_transaksi_umum(self):
        t = Transaksi("UMUM", 100000)
        self.assertEqual(t.jenis, "UMUM")
        self.assertEqual(t.jumlah, 100000)

    def test_polymorphism_ringkasan_subclass(self):
        t_tarik = TransaksiTarik(50000)
        t_setor = TransaksiSetor(100000)
        t_transfer = TransaksiTransfer(75000, "12345")

        self.assertIn("PENARIKAN", t_tarik.ringkasan())
        self.assertIn("PENYETORAN", t_setor.ringkasan())
        self.assertIn("TRANSFER", t_transfer.ringkasan())
        self.assertIn("12345", t_transfer.ringkasan())

    def test_jumlah_transaksi_tidak_valid(self):
        t = TransaksiTarik(10000)
        self.assertEqual(t.jumlah, 10000)

if __name__ == "__main__":
    unittest.main()