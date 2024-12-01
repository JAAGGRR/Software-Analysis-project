# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

## Reporting a Vulnerability

 
Haavoittuvuusraportti 
 
Löysin testisovelluksen mahdollisia tietoturva-aukkoja. Olen sitoutunut työskentelemään kanssasi näiden ongelmien ratkaisemiseksi. Tästä raportista löydät kaiken, mitä tarvitset ongelmien ratkaisemiseksi tehokkaasti. 
Jos sinulla on kysyttävää tästä prosessista, ota yhteyttä minuun osoitteessa [hikimiehet@laurea.fi]. 
 
 Jos et ole oikea yhteyshenkilö tälle raportille, ilmoita minulle! 
Muoto 
Yhteenveto 
 
Sovelluksessa on useita tietoturvahaavoittuvuuksia, jotka liittyvät muun muassa SQL-injektioihin, salasanojen käsittelyyn, tiedostojen käsittelyyn ja henkilötietojen suojaamiseen. Nämä ongelmat voivat mahdollistaa luvattoman pääsyn järjestelmään, arkaluontoisten tietojen varastamisen ja sovelluksen tietokannan vahingoittamisen. 
Muoto 
Tuote 
 
Opiskelijahallintasovellus (testisovellus) 
Muoto 
Testattu versio 
 
Ensimmäinen versio (ei julkisesti jaossa) 
Muoto 
Yksityiskohdat 
1. SQL-injektio 
 
Ongelma: Sovelluksen SQL-kyselyissä käytetään käyttäjän syötettä ilman riittävää tarkastusta, vaikka parametrisoituja kyselyjä hyödynnetään joissain tapauksissa. Esimerkiksi login()-funktiossa seuraava SQL-koodi on altis injektiohyökkäyksille: 
 
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)) 
 
Riski: Hyökkääjä voi syöttää haitallista SQL-koodia esimerkiksi ohittamalla kirjautumisen tai manipuloimalla tietokantaa. 
 
2. Salasanojen suojaus 
 
Ongelma: Käyttäjien salasanat tallennetaan selväkielisinä tietokantaan: 
 
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "password")) 
 
Riski: Jos tietokanta vaarantuu, kaikki salasanat voidaan lukea suoraan. Tämä vaarantaa sekä käyttäjien että järjestelmän tietoturvan. 
 
3. Tiedostojen käsittely 
 
Ongelma: Käyttäjän antamiin tiedostonimiin luotetaan ilman tarkistusta tai rajoituksia. Esimerkiksi upload_image()-funktio voi käsitellä tiedostoja, kuten ../../etc/passwd, ja näin mahdollistaa luvattoman pääsyn järjestelmätiedostoihin. 
 
image_path = os.path.join("images", image_file) 
 
Riski: Hyökkääjä voi käyttää tiedostojen käsittelyä järjestelmän kompromettoimiseen. 
 
4. Henkilötietojen suojaus 
 
Ongelma: Henkilötunnukset (SSN) tallennetaan tietokantaan suojaamattomassa muodossa. 
 
cursor.execute("INSERT INTO students (student_number, name, contact, ssn, image_path) VALUES (?, ?, ?, ?, ?)", ...) 
 
Riski: Arkaluontoiset tiedot voivat vuotaa luvattomalle osapuolelle tietomurron sattuessa. 
 
5. Validoinnin puute 
 
Ongelma: Syötteille, kuten opiskelijanumerolle tai kurssinimelle, ei tehdä minkäänlaista tarkastusta tai muokkausta. 
 
student_number = input("Enter student number: ") 
 
Riski: Haitallinen syöte voi vahingoittaa tietokantaa tai aiheuttaa sovellusvirheitä. 
 
6. Virheenkäsittelyn puute 
 
Ongelma: Useat toiminnot eivät tarkista, onko käyttäjän syöte jo olemassa tietokannassa, esimerkiksi add_student()-funktio: 
 
cursor.execute("INSERT INTO students (student_number, name, contact, ssn, image_path) VALUES (?, ?, ?, ?, ?)", ...) 
 
Riski: Tämä voi johtaa tietojen yliajoihin tai sovellusvirheisiin. 
Muoto 
PoC (Proof of Concept) 
SQL-injektio (kirjautumisen ohittaminen): 
Syötä kirjautumiseen seuraavat tiedot: 
Käyttäjänimi: admin 
Salasana: password' OR '1'='1 
 
Tulos: Kirjautuminen onnistuu, vaikka salasana olisi väärä. 
 
Tiedostojen käsittely: 
upload_image()-funktiossa syötä tiedostonimeksi ../../etc/passwd. 
Tulos: Jos järjestelmä antaa pääsyn, sovellus voi vahingossa avata järjestelmätiedostoja. 
 
Arkaluontoisten tietojen vuoto: 
Käynnistä search_student() ja syötä minkä tahansa olemassa olevan opiskelijan numero. 
Tulos: Henkilötunnus näkyy suojaamattomana tulosteessa. 
Muoto 
Vaikutus 
 
SQL-injektio mahdollistaa tietokannan manipuloinnin tai arkaluontoisten tietojen vuotamisen. 
Selväkieliset salasanat ja SSN voivat vuotaa tietomurrossa. 
Tiedostonimiin luottaminen voi johtaa luvattomaan tiedostojen käsittelyyn. 
Validoinnin ja virheenkäsittelyn puute voi aiheuttaa järjestelmän epävakautta ja tietojen yliajoja. 
Muoto 
Korjaus 
 
SQL-injektioiden estäminen: 
Varmista, että kaikki SQL-kyselyt käyttävät parametrisoituja kyselyjä. 
Tarkista ja puhdista kaikki käyttäjän syötteet. 
Salasanojen suojaus: 
Hashaa salasanat käyttäen turvallista algoritmia, kuten bcrypt. 
Poista selväkieliset salasanat tietokannasta. 
Tiedostojen käsittely: 
Tarkista tiedostonimet ja salli vain sovelluksen määrittelemät polut. 
Käytä tiedostonimeä validoivia kirjastoja, kuten os.path. 
Henkilötunnusten suojaus: 
Salakirjoita arkaluontoiset tiedot tietokannassa. 
Näytä SSN(hetut) vain valtuutetuille käyttäjille ja tarvittaessa osittain peitettynä esim muodossa ***1234. 
Validointi ja virheenkäsittely: 
Lisää syötteiden validointi ja tarkista, ettei tietokannassa ole ristiriitaisia tietoja. 
Lisää virheenkäsittely, joka estää sovelluksen kaatumisen. 
Muoto 
 
Jos tarvitset lisätietoja tai apua korjauksessa, ota yhteyttä! 
 
