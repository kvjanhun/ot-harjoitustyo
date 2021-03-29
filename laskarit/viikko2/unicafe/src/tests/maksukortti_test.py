import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
        
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(str(self.maksukortti), "saldo: 35.0")
    
    def test_rahan_ottaminen_saldon_riittaessa_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
        
    def test_rahan_ottaminen_kun_saldo_ei_riita_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5000), False)
    
    def test_rahan_ottaminen_vahentaa_oikein_saldon_riittaessa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")
        
    def test_rahan_ottaminen_ei_muuta_riittamatonta_saldoa(self):
        self.maksukortti.ota_rahaa(5000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
