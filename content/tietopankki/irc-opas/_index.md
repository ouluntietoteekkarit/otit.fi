---
title: IRC opas
date: 2021-15-5
authorbox: false
sidebar: true
menu:
---

### IRC-OPAS

#### **Mikä IRC, miksi IRC?**

Wikipedia luonnehtii aihetta näin:

”IRC (Internet Relay Chat, puhekielessä irkki) mahdollistaa reaaliaikaisen keskustelun Internet-käyttäjien välillä. IRC on vanhin Internetin pikaviestipalvelu (instant messenger).”

Sillä siis voi viestitellä interwebsin välityksellä toisten ihmisten kanssa ja ryhmien kesken. Vaikka IRC onkin internet-ajassa vanha keksintö, sillä on silti paljon käyttäjiä esimerkiksi opiskelijoiden seurassa. IRC:ssä eli _irkissä_ pysyt ajan tasalla pienryhmäsi, vuosikurssisi ja koko killan menoista, löydät äkkiä apua tai seuraa opiskeluun, tai löydät jopa töitä. Irkin etu on myös että serverit eivät tallenna keksusteluita kuten WhatsApp ja muut valtavat viestisovellukset käyttääkseen materiaalia mainostukseen ja muihin foliohattutarpeisiin.

Plus fuksipisteitä, mutta ne ovat enemmänkin syötti kuin itsetarkoitus. Vanhat ja väsyneetkin vielä irkkaavat ja hyvistä syistä.

#### **Miten sinne pääsee?**

Kaikista paras tapa irkata on laittaa jollekin käytössäsi olevalle palvelimelle IRC-klientti **Irssi** pyörimään. Näin pystyt seuraamaan keskusteluita 24/7, vaikket konettasi pitäisikkään koko aikaa päällä. Samalla pääset näppärästi irkkiin myös kiltahuoneen koneilta, kirjastosta tai omalta koneelta.

Mahdollisesti käytössäsi olevat palvelimet:

*   otitsunii.oulu.fi – Killan ylläpitämä, jäsenille tarkoitettu palvelin, **suositeltava vaihtoehto.** Täytä hakemus ja toimita se hallituslaiselle tai pienryhmäohjaajalle.
*   tuomi.oulu.fi – Yliopiston palvelin, periaatteessa ei salli Irssin pitkäaikaista käyttöä mutta välttää ennen kuin saat tunnukset muualle. Tänne kirjaudutaan samoilla lyhennetyillä Paju-tunnuksilla kuin muihin yliopiston palveluihin.
*   Kotipalvelin, jos sellaisen ylläpitämistä harrastat (tällöin et tosin varmaan tarvitse näitä ohjeita…)

#### 1\. Palvelimelle yhdistäminen SSH:lla

Windows:

1.  Lataa haluamasi SSH-klientti, vaikkapa [PuTTYTray](https://puttytray.goeswhere.com/). SSH-klientti löytyy asennettuna yliopiston käytännössä kaikilta Windows-koneilta.
2.  Avaa PuTTYTray ja säädä Translating-asetuksista utf-8 päälle
3.  Kirjoita ”Host name”-kenttään käyttämäsi palvelimen osoite (esim. `otitsunii.oulu.fi`). Käytä jatkossa samaa palvelinta, kunnes vaihdat parempaan. PuTTY:lla voi myös tallentaa yhteyden asetukset niin seuraavalla kerralla ei tarvitse kirjoittaa niin paljon.
4.  Hyväksy yhteys kysyttäessä, ja syötä käyttäjänimi ja salasana

Linux/Mac OSX/Unix yms:

1.  Avaa konsoli/terminaali/komentorivi ja yhdistä komennolla `**ssh käyttäjä@palvelin**`. Esimerkiksi **`ssh loilollo@otitsunii.oulu.fi`**.
2.  Hyväksy yhteys kysyttäessä, ja syötä käyttäjäsi salasana

Nykyaikaisiin puhelimiin löytyy myös SSH-klienttejä, esimerkiksi Androidille [Irssi ConnectBot](https://play.google.com/store/apps/details?id=org.woltage.irssiconnectbot&hl=fi) tai [JuiceSSH](https://play.google.com/store/apps/details?id=com.sonelli.juicessh&hl=fi). JuiceSSH on näistä parempi vaihtoehto, koska sillä pääsee paljon nopeammin sisään ja siitä löytyy pikanäppäimiä. Irkin käyttämisessä puhelimen viestittelykanavana on monia etuja, joista tärkeimpänä voisi mainita sen olevan hyvin vaikeaa autoa ajaessa. Näin sitä ei tule tehtyä ja liikenteessä olo on turvallisempaa.

Palvelimen sisältöjä voit tutkia tavallisilla unix-komennoilla.

#### 2\. Screenin käyttö

**Screen** on ohjelma, jonka sisälle voi jättää muita ohjelmia ajamaan taustalle, silloinkin kun et ole yhteydessä palvelimeen. Irkkaamisessa screenistä on se hyöty, että voit jättää Irssisession taustalle, ja avata sen myöhemmin uudestaan missä tahansa, ilman että yhtään keskustelua menee sivu suun. Screenin käytön oppii äkkiä, vaikkapa näitä ohjeita seuraamalla.

Ensimmäinen avauskerta:

Ruudulla pitäisi nyt olla joitain palvelimen viestejä. Eka kerta on aina jotain uutta ja poikkeavaa, niin on irssinkin käytön tapauksessa. Komento **`screen irssi`** avaa Irssin screenin sisään. Tämä sinun tarvitsee tehdä **vain tämän ekan kerran**. Oikeasti, jos kirjoitat tämän komennon kaksi kertaa ilman että tiedät syyn miksi, olet todennäköisesti tehnyt virheen. Kun olet kerran avannut irssin screenin sisään se pysyy siellä turvassa tallentaen viestejä vaikka katkaisisit oman yhteytesi tai sammuttaisit tietokoneesi välillä. Kun seuraavan kerran otat yhteyden palvelimeen esimerkiksi Puttylla, ja epähuomiossa kirjoitat ”screen irssi”, sinä aukaisetkin uuden irssin screenin sisään, ja huomaat että se ei ole sama asia (katso alta kohta ”Jos käy vahinko”). Lue alempi huolella niin näin ei pääse käymään.

Seuraavat kerrat eli aina jatkossa:

Komento **`screen -dr`** sulkee (-d, _detach_) mahdollisesti muualla auki olevan yhteyden screeniin, ja avaa (-r, _reattach_) sen uudestaan koneelle jolla syötit komennon. Jos et tee palvelimella muuta kuin irkkaat, tämän pitäisi olla ainut komento mitä ikinä tulet käyttämään.

#### Jos (tai no, kun) käy vahinko:

Jos kaikesta huolimatta onnistut avaamaan usean session kirjoittamalla screen irssin useammin kuin kerran (eli näet kanavalla oman nikkisi useampaan kertaan listattuna) ja `screen -dr` ei tahdo toimia, saat listattua auki olevat screenit komennolla **`screen -ls`**. Katso listauksesta mikä screeni on ylimääräinen (yleensä viimeisimpänä luotu), ja sulje se komennolla **`kill [viisinumeroinen prosessi-ID]`**, viisinumeroisen prosessi-ID:n saat listauksesta. Kun saat ylimääräiset screenit suljettua, voit taas yhdistää alkuperäiseen normaalisti screen -dr:llä.

Screenistä poistuminen turvallisesti:

Kun haluat poistua auki olevasta screenistä (Irssistä) palvelimen komentoriville, jättäen sessien taustalle, käytä näppäinyhdistelmää `**Ctrl-A, D**`. Eli ensin Ctrl-A, jota seuraa kirjain D. Ikkunan sulkeminen on myös turvallista jos laiskottaa.

#### 3\. Irssin käyttöönotto

Avatessasi Irssin ensimmäistä kertaa, se ei tee vielä mitään. Irssiin voi syöttää sanallisia komentoja, joita aina edeltää merkki **`/`**. Apua komennoista saat kirjoittamalla **`/help`**.

Ensimmäisenä haluamme yhdistää IRC-verkkoon, jotta voisimme liittyä eri kanaville. Yleisimmin käytetty verkko, jolta löytyy mm. killan ja kurssien kanavat, on **IRCnet**. IRCnet koostuu monesta palvelimesta, joista meille kätevin on paikallinen **irc.oulu.fi**. Asetetaan se vakioverkoksi komennolla: **(komento saattaa viedä minuutin, älä hätäänny jos serveri ei sekunnissa yhdistä)**

**`/server add -auto -network IRCnet irc.oulu.fi 6667`**

**`/connect irc.oulu.fi`**

_HUOM! Jos yhdistät palvelimelta joka ei ole yliopiston verkossa, joudut selvittämään itse mikä IRCnetin palvelin on paras._

Vieläkään emme ole yhdelläkään kanavalla, joten liitytäänpä vuosikurssin kanavalle #otit.2019:

**`/join #otit.2019`**

Nyt voimme jo huutaa maailmalle ”hei” niin että joku kuulee.

#### **Mitä sisällä tehdään?**

#### Nikki

Jos ei halua niin ei ole pakko käyttää hallituksen kovalla vaivalla juuri sinulle miettimää otitsunii-tunnusta muille näkyvänä nikkinä. Sen voi vaihtaa ihan vain komennolla **`/nick uusinikki`**.

#### Kanavat

Voit liittyä uusille kanaville komennolla **`/join #kanavan-nimi`**. Kun liityt uudelle kanavalle jolle aiot jäädä pitemmäksi aikaa, kannattaa syöttää komento **`/channel add -auto #kanavan-nimi IRCnet`**. Näin sinun ei tarvitse liittyä manuaalisesti uudestaan joka kanavalle jos palvelin sattuu kaatumaan tai vahingossa suljet Irssin.

Tärkeitä kanavia lisätä ovat:

**#otit.n**, missä `n` on oma vuosikurssisi (esim. `#otit.2019`). Tämä on vuosikurssin n kanava, joka on fukseille hyvä paikka olla fukseja, keskustella keskenään vaikka videopeleistä ja kysyä asioita. Paikalla on myös hallituslaisia, PROita ja muita aktiiveja jotka vastaavat kysymyksiin salamannopeasti.

**#otit,** Oulun Tietoteekkareiden pääkanava, iso osa irkin kautta tapahtuvasta tiedotuksesta tapahtuu täällä. Paljon vanhoja naamoja.

**#oty,** kaikkien Oulun irkkaavien Teekkareiden kattokanava. Aktiiviset keskustelijat saattavat olla jostain syystä aika pitkälti myös Tietoteekkareita.

**#oman-pienryhmäsi-kanava** jonka nimen PROsi sinulle kertoo.

On hyvin todennäköistä, että löydät liityttäviä kanavia paljon lisääkin. Eri hyvillä hommilla on omansa, monilla kursseilla on omansa ja lisäksi monilla harrastuksilla, joukkueilla ja puheenaiheilla on omansa.

Lähettääksesi salaisia kuumia yksityisviestejä toiselle nickille voit käyttää komentoa **`/q nick`** (_q_ niinkuin _query_). Tämä avaa uuden ikkunan, kuten kanavalle liittyminen.

#### Liikkuminen

Irssin ikkunoita voi selata näppäimillä: **Alt+\[numero 0-9 tai kirjain q-u\]** tai **Esc, \[numero 0-9 tai kirjain q-u\]**. **Alt+\[vasen nuolinäppäin tai oikea nuolinäppäin\]** siirtää viereiselle kanavalle. **Alt+a** siirtää kanavalle jossa on tapahtunut jotain. Myös komento **`/window goto _numero_`** ja **`/window goto _nimi_`** toimivat tarvittaessa. Ikkuna numero 1 on status-ruutu, jossa näkyy serveriin liittyvät viestit, sekä useimpien komentojen tulosteita. Muut ikkunat ovat kanavia joille olet liittynyt, tai yksityiskeskusteluita muiden ihmisten kanssa.

Itse kanavalla olevissa viesteissä pääsee rullaamaan ylös ja alas **Page up** ja **Page down** -näppäimillä. Nuolinäppäimillä liikutaan omissa teksteissä.

**Puhelimella** Irssi ConnectBotissa ylös ja alas liikutaan vetämällä viestejä kellonajoista ylös tai alas, kanavalta toiselle vetämällä vasemmalle tai oikealle. Tuplatökkäämällä liikutaan kanavalle jossa on uusia viestejä. JuiceSSH:ssä on PageUp- ja PageDown-näppäimet, joita käytetään.

#### Topikeista ja @-merkeistä

Monella kanavalla tärkeimmät asiat jotka käyttäjien on hyvä tietää (esim. seuraavien bileiden ajankohta), ja jotka helposti hukkuisivat keskustelun sekaan, on nostettu otsikkoon eli topikkiin **/topic** -käskyllä. Tämän tekee kulloisenkin kanavan pääasiallinen tiedottaja tai pomo tai sitten (demokraattisimilla kanavilla) kenellä on niin polttavaa asiaa. Nykyistä topikkia saa muutettua helpoiten **/topic <tab>**\-käskyllä, jolloin vanha topikki ilmaantuu syöttöriville muokattavaksi.

Topikkeja pystyvät vaihtamaan käyttäjät joiden nimien edessä on @. He ovat kanavaoperaattoreita (ei tule sekoittaa killan operaattoreihin) eli heillä on ”oppeja”. He voivat myös muun muassa potkia ihmisiä ulos kanavilta. Yleensä hyvän tavan mukaista on jakaa oppeja (komennolla **/mode <#kanava> +o <nikki>**) kaikille keihin luottaa siltä varalta että kanavalle tulee botteja joita pitää potkia ulos.

#### Kopiointi ja liittäminen

Irssissä kopiointi toimii niin, että riittää kun maalaa kopioitavan tekstin. Se kopioi sen automaagisesti samalla, ja tekstin voi sitten liittää mihin haluaa. Liittäminen irssissä toimii oikealla klikillä. Näin voi käydä hassusti, jos luulee kopioinnin toimivan niin, että ensin maalataan ja sitten kopioidaan oikealla klikillä. Se kun ei toimi niin, vaan nyt sinä jo liitit kopioimasi tekstinpätkän viestiisi ja todennäköisesti lähetitkin sen. Ei se mitään. Linkkejä saa klikkailtua suoraan ilman kopiointeja kun on hyvä SSH-clientti, esimerkiksi [Putty-tray](https://puttytray.goeswhere.com/) (Puttyn kehittyneempi muoto). Puhelimella linkkien kopiointi on pyllystä.

#### Hilightit

ovat määrittelemiäsi avainsanoja joista Irssi ilmoittaa sinulle kun joku niitä mainitsee millä tahansa kanavalla. Voit lisätä sanan hilighteihin komennolla **`/hilight`** `_sana_`. Poistaaksesi hilightin syötä vastaavasti **`/dehilight`** `_sana_`. Hyviä hilighteja ovat esimerkiksi oma etunimesi, nimimerkkisi eri variaatiot, ja muut kiinnostuksen kohteet joita et halua missata kuten _tissit_. Tissit on Oulun Tietoteekkareiden yleisesti tiedotuksessa käytettävä hilight, eli kun jollakulla on asiaa aivan kaikille kanavalla olijoille, hän mainitsee tissit, mikä herättää kaikkien huomion (esimerkiksi ”tissit: tapahtuma alkaa kello 18”). Laita se siis ehdottomasti hilightteihin niin tiedät mitä tapahtuu.

Parhaiten hilightit ovat hyödyksi kun puhelimessasi on IrssiNotifier, joka sitten kivasti värisee kun joku huutaa tissejä tai sinua (tai molempia), sekä näyttää viestin jossa hilight mainittiin ilman sisäänkirjautumista.

#### Logit

Erittäin kätevä toiminto irkissä on se, että halutessasi saat kaikki viestit talteen mahdollista myöhempää kiristyskäyttöä varten. Logien tallennus ei ole automaattisesti päällä, mutta sen saa päälle ihan vain komennolla **/SET autolog ON** . Logeja voi mennä sitten lukemaan lähtemällä ensin irssin sisältä pois ctrl+a+d:llä (mutta ei katkaise koko yhteyttä, on siis tilassa jossa normaalisti kirjoitetaan screen -dr) ja sitten avaa haluamansa login komennolla **less ~/irclogs/IRCnet/\[#kanavannimi tai querykaverinnimi\].log** . Pois logista lähdetään painamalla **q**.

#### Skriptit

Irssiin voi tuoda lisäominaisuuksia skripteillä, eli ohjelmanpätkillä jotka toteuttavat tiettyjä lisätoimintoja taustalla. Skriptejä voit asentaa kopiomalla niitä kotikansioosi kansioon: ~/.irssi/scripts mutta kannattaa ensin tarkistaa löytyykö kyseistä skriptiä jo valmiiksi kansiosta /usr/share/irssi/scripts

(Eli **kun olet sisällä palvelimessa mutta et vielä irssissä** (et ole kirjoittanut **screen -dr**) niin voit hypellä kansioissa peruskomentorivikomennoilla. Ne kannattaa opetella vaikkei niitä juuri irkkikäytössä tarvitsekaan, tällä alalla kun olet.)

Kun skripti on kansiossa paikallaan, mene irssiin sisään (**screen -dr**, muista) ja lataa skripti käyttöön komennolla: **/script load \[nimi\]** Irssi lataa skriptin käyttövalmiiksi.

**Muutama näppärä skripti:**

*   [Title](http://scripts.irssi.org/scripts/title.pl) – Näyttää terminaalin otsikkopalkissa fiksumman otsikon.
*   [Trackbar](http://scripts.irssi.org/scripts/trackbar.pl) – Näyttää viivan viimeisimmän lukemasi rivin jälkeen. Äärimmäisen näppärä kanavasurffailun apu.
*   [Hilight window](http://scripts.irssi.org/scripts/hilightwin.pl) – Kopioi hilighttaavat rivit erilliseen ikkunaan. Näet onko asia tärkeää – vaihtamatta kanavaa. (Setup: Laita kansioon _~/.irssi/scripts/autorun_ ja komenna irssiin **`/run hilightwin ; /window new split ; /window name hilight ; /window size 6`**)
    
*   [IrssiNotifier](https://irssinotifier.appspot.com/) – Ilmoittaa hilighteista ja yksityisviesteistä suoraan Android-puhelimeesi, ja näyttää viestit ilman että tarvitsee edes yhdistää palvelimelle.
*   [Splitlong](https://scripts.irssi.org/scripts/splitlong.pl) – Jos tykkäät kirjoittaa romaaneja irkkiin niin ikäviä uutisia: se pätkäisee ylipitkän viestisi tietyn merkkimäärän kohdalla eikä edes kerro sinulle, toiset vain näkevät pätkäistyn viestin. Tällä skriptillä viestisi lähtevät useammassa pompsissa ja vastaanottajatkin saavat joka merkin.

Lisää skriptejä löytyy [täältä](http://scripts.irssi.org/).

#### Hyödyllisiä komentoja

*   **/help** listaa kaikki komennot, **/help \[komento\]** kertoo mitä komento tekee
*   **Page up** ja **Page down** -näppäimillä liikutaan keskustelussa vanhempiin ja uudempiin viesteihin. Nuolinäppäimillä näin ei tapahdu, ja hiirtä on turha yrittäkään käyttää
*   **Alt+\[numero\]** -komennolla liikutaan numerolla merkitylle kanavalle. Viereiselle kanavalle pääsee komennolla **Alt+\[vasen nuolinäppäin tai oikea nuolinäppäin\]**. Pitämällä nuolinäppäintä pohjassa voi kanavasurffata vauhdilla.
*   **Alt+a** siirtää kanavalle jossa on tapahtunut jotain
*   **/win move \[numero\]** siirtää kanavan haluamallesi paikalle. Käytetyimmät kanavat saa näin likimmäs toisiaan ja helpoimmille Alt+# -paikoille
*   **/ignore \[ignorattavat\]** jättää huomioimatta haluamasi asiat, kuten kanavalle liittymiset ja poistumiset. Vähentää huomattavasti isojen kanavien (#otit, #oty) kohinaa  
    (Esim: /ignore -channels #chan1,#chan2,#chan3 \* JOINS PARTS QUITS)
*   **/FORMAT timestamp {timestamp %%H:%%M:%%S}** muutetaan kellonajat näyttämään myös sekunnit. Näkee helposti onko yhteys katkennut (kun sekunnit eivät enää liiku), ja näkee tarkemman ajan milloin joku on laittanut viestiä
*   **/whois \[nikki\]** tai **/wii \[nikki\]** kertoo tiedot nikin omistajasta, muun muassa oikean nimen jos sen haluaa tietää

Google on myös kiva apu, avainsana joka kannattaa lisätä hakuun on irssi.

#### Etiketti

Kaikilla kanavilla arvostetaan [IRC-etiketin](https://www.pulina.fi/irc-etiketti) mukaista käytöstä, vaikka osa siitä voikin olla käytännössä enemmänkin suuntaviivoja kuin oikeita sääntöjä. Perussääntö on että tulet näkemään näitä ihmisiä kasvotusten opiskelu- tai jopa työurasi aikana hyvin paljon, joten ei kannata käyttäytyä kuin idiootti ja huudella oikeasti typeriä asioita. Asia erikseen ovat kilta- tai koulujutuista tietämättömyys sekä komennoissa möhliminen, niistä ei kukaan suutu vaan todennäköisemmin antaa neuvoja.

Olisiko muitakin tapoja irkata?

On huonompia. Jos kumminkin hankkisit ne otitsuniin tunnukset ja käyttäisit ylläolevia ohjeita.

Mutta toinen tapa irkata on asentaa jokin IRC-ohjelma omalle koneellesi ja yhdistää sillä palveluntarjoajasi IRC-palvelimelle.

#### IRC-ohjelmia

*   [Bersirc](http://www.bersirc.com/)
*   [Irssi](http://irssi.org/)
*   [mIRC](http://www.mirc.com/)
*   [XChat](http://xchat.org/)

#### IRC-palvelimia

*   irc.oulu.fi – Toimii vain yliopiston verkosta
*   irc.cs.hut.fi – Toimii useimmilla yhteyksillä, jos palveluntarjoajallasi ei ole omaa palvelinta.

Liian pitkä; et lukenut?

1.  Yhdistä vapaa-valintaisella ssh-klientillä palvelimelle josta löytyy Irssi
2.  Ekakerta: Kirjoita **screen irssi**
3.  Syötä irssiin seuraavat komennot:
    1.  **/server add -auto -network IRCnet irc.oulu.fi 6667**
    2.  **/connect irc.oulu.fi**
    3.  **/channel add -auto #otit.2019** (toista mm. kanavalle **#otit** ja muille haluamillesi)
    4.  **/hilight tissit**
4.  Poistu screenistä näppäimillä **Ctrl-A, D**, ja (nyt ja **aina jatkossa**) avaa se komennolla **screen -dr** (ei screen irssi)
5.  ???
6.  Profit