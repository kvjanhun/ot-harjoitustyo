# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellusta voi käyttää pienen yhdistyksen jäsenrekisterinä ja laskutuksen apuvälineenä.
## Käyttäjät
Sovellukseen ei välttämättä toteuteta erillisiä käyttäjärooleja. Harkinnassa on tarve evätä peruskäyttäjältä esimerkiksi oikeus poistaa jäseniä rekisteristä.
## Suunnitellut toiminnallisuudet
* Sovelluksessa on graafinen käyttöliittymä
* Sovelluksella voi lukea .csv-tiedostosta rekisteriin lisättävät jäsenet
  * Luettavan .csv-tiedoston formaatin voi määritellä sovellukseen
* Sovelluksella voi lisätä rekisteriin ja poistaa rekisteristä jäseniä yksitellen
* Jäsentä tai jäseniä lisätessä tietyt tiedot ovat pakollisia eikä lisäyksiä voida tehdä ilman niitä (nimi, kotikunta, sähköpostiosoite)
  * .csv-tiedostosta luettaessa puutteellisista tiedoista saa käyttäjä virheilmoituksen, jossa puutteellisen jäsenen tietoja on mahdollista täydentää tai kyseinen jäsen on mahdollista jättää lisäämättä, muiden lisäysten tapahtuessa normaalisti
  * Yksittäin lisätessä käyttäjä saa virheilmoituksen. 
* Sovellus laskee jokaiselle lisättävälle jäsenelle jäsennumeron, joka samalla toimii suomalaisen tilisiirron viitenumerona
  * Sovellus luo aiemmin rekisterissä esiintymättömiä jäsennumeroita joko järjestyksessä tai satunnaisesti
  * Käyttäjä voi määritellä jäsennumeron juoksevan osan alku- ja loppukohdan, kuitenkin niin että viitenumeron ehdot säilyvät (3-19 numeroa)
* Käyttäjä voi generoida yksilöityjä sähköpostiviestejä jäsenlaskutukseen
  * Joko koko jäsenrekisterille, yksittäiselle jäsenelle tai juuri lisätyille jäsenille
  * Viestin pohjan voi määritellä itse ja sovellus täydentää jäsenen nimen, sähköpostiosoitteen ja jäsennumeron

### Jatkokehitys
Mikäli aika sallii...
* Jäsenten tietoja voi muokata graafisen käyttöliittymän avulla
* Jäsenrekisterin tallennus tietoturvallisessa muodossa
* Sovelluksella voi lähettää sähköpostiviestejä tietoturvallisesti Gmail-tilin kautta
