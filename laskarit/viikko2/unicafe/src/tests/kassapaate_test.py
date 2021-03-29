import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        
    # konstruktorin testit
    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
        
    def test_luodussa_kassassa_oikea_summa_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_luodussa_kassassa_ei_myytyja_edullisia(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_luodussa_kassassa_ei_myytyja_maukkaita(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    # edullisesti käteisellä -testit
    def test_edullisesti_kateisella_kasvattaa_kassaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        
    def test_edullisesti_kateisella_antaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        
    def test_edullisesti_kateisella_kasvattaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_edullisesti_riittamaton_kateinen_ei_muuta_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_edullisesti_riittamaton_kateinen_ei_muuta_myytyja(self):
        self.kassapaate.syo_edullisesti_kateisella(1)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_edullisesti_riittamaton_kateinen_palauttaa_rahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(1), 1)
        
    # maukkaasti käteisellä -testit
    def test_maukkaasti_kateisella_kasvattaa_kassaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        
    def test_maukkaasti_kateisella_antaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        
    def test_maukkaasti_kateisella_kasvattaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_maukkaasti_riittamaton_kateinen_ei_muuta_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_maukkaasti_riittamaton_kateinen_ei_muuta_myytyja(self):
        self.kassapaate.syo_maukkaasti_kateisella(1)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_maukkaasti_riittamaton_kateinen_palauttaa_rahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1), 1)
        
    # edullisesti kortilla -testit
    def test_edullisesti_kortilla_ei_kasvata_kassan_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(1000))
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisesti_veloittaa_korttia_oikein(self):
        mk = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(mk)
        self.assertEqual(str(mk), "saldo: 7.6")
        
    def test_edullisesti_kortilla_palauttaa_rahan_riittaessa_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(240)), True)
            
    def test_edullisesti_kortilla_kasvattaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(240))
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullisesti_riittamaton_saldo_ei_vahene_kortilta(self):
        mk = Maksukortti(1)
        self.kassapaate.syo_edullisesti_kortilla(mk)
        self.assertEqual(str(mk), "saldo: 0.01")
        
    def test_edullisesti_riittamaton_saldo_ei_muuta_myytyja(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(1))
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_edullisesti_kortilla_palauttaa_riittamattomalle_rahalle_false(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(1)), False)
        
    # maukkaasti kortilla -testit
    def test_maukkaasti_kortilla_ei_kasvata_kassan_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(1000))
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukkaasti_veloittaa_korttia_oikein(self):
        mk = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(mk)
        self.assertEqual(str(mk), "saldo: 6.0")
        
    def test_maukkaasti_kortilla_palauttaa_rahan_riittaessa_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(400)), True)
            
    def test_maukkaasti_kortilla_kasvattaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(400))
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukkaasti_riittamaton_saldo_ei_vahene_kortilta(self):
        mk = Maksukortti(1)
        self.kassapaate.syo_maukkaasti_kortilla(mk)
        self.assertEqual(str(mk), "saldo: 0.01")
        
    def test_maukkaasti_riittamaton_saldo_ei_muuta_myytyja(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(1))
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_maukkaasti_kortilla_palauttaa_riittamattomalle_rahalle_false(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(1)), False)
        
    # kortinlataustestit
    def test_negatiivista_summaa_ei_ladata_kortille(self):
        mk = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(mk, -50)
        self.assertEqual(str(mk), "saldo: 5.0")
        
    def test_negatiivista_summaa_ei_lisata_kassaan(self):
        self.kassapaate.lataa_rahaa_kortille(Maksukortti(500), -50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kortille_ladattava_summa_siirtyy_kortin_saldoon(self):
        mk = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(mk, 5000)
        self.assertEqual(str(mk), "saldo: 55.0")
        
    def test_kortille_ladattava_summa_siirtyy_kassaan(self):
        self.kassapaate.lataa_rahaa_kortille(Maksukortti(500), 5000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 105000)
