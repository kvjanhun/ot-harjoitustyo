# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellusta voi käyttää pienen yhdistyksen jäsenrekisterinä ja laskutuksen apuvälineenä.
## Käyttäjät
Sovellukseen ei välttämättä toteuteta erillisiä käyttäjärooleja. Harkinnassa on tarve evätä peruskäyttäjältä esimerkiksi oikeus poistaa jäseniä rekisteristä.
## Suunnitellut toiminnallisuudet
* Sovelluksessa on graafinen käyttöliittymä
* Sovellus lukee .csv-tiedostosta rekisteriin lisättävät jäsenet
  * Luettavan .csv-tiedoston formaatin voi määritellä sovellukseen
* Rekisteriin voi lisätä ja rekisteristä voi poistaa jäseniä yksitellen
* Sovellus laskee jokaiselle lisättävälle jäsenelle jäsennumeron, joka samalla toimii suomalaisen tilisiirron viitenumerona
  * Sovellus luo aiemmin rekisterissä esiintymättömiä jäsennumeroita joko järjestyksessä tai satunnaisesti
  * Käyttäjä voi määritellä jäsennumeron juoksevan osan alku- ja loppukohdan, kuitenkin niin että viitenumeron ehdot säilyvät (3-19 merkkiä)
* Käyttäjä voi generoida yksilöityjä sähköpostiviestejä jäsenlaskutukseen
  * Joko koko jäsenrekisterille, yksittäiselle jäsenelle tai juuri lisätyille jäsenille
  * Viestin pohjan voi määritellä itse ja sovellus täydentää jäsenen nimen, sähköpostiosoitteen ja jäsennumeron

### Jatkokehitys
Mikäli aika sallii...
* Jäsenten tietoja voi muokata graafisen käyttöliittymän avulla
* Jäsenrekisterin tallennus tietoturvallisessa muodossa
* Sovelluksella voi lähettää sähköpostiviestejä turvallisesti

