# Lokalizované názvy a popisy — 116

Čte `tools/lokalizace.py` a nahrává přes `videos.update(part="localizations")`.
Anglický titul a popis jsou v `youtube.md` a posílají se zpátky beze změny.

**Pořadí sekcí je podle YouTube Studia** (bajtově podle ČESKÉHO názvu jazyka):
fi, fr, id, it, de, pl, pt-BR, tr, uk, vi, cs, es, sv.

## Co se NEPŘEKLÁDÁ

- vlastní jména: NATO (fi, sv *Nato*; fr, es, pt-BR *OTAN*; uk *НАТО*;
  jinde NATO — jako v titulcích), Alan Wilson, Vyacheslav Argenberg,
  Wikimedia Commons, Musée de l'air et de l'espace, Le Bourget.
  Moskva/Moskau/Moscou… a Vostok (de, pl *Wostok*, uk *«Восток-1»*) se
  píšou podle zvyklosti jazyka.
- časy kapitol na vteřinu (ze `youtube.md`, scény S01, S06, S10, S13,
  S20, S26, S29, S32, S40, S44, S49, S57, S63, S68, S75, S78).
- citace zdrojů: autoři, názvy dokumentů, studií a instituce zůstávají
  v originále (Address by the President…, IMF, World Economic Outlook,
  MTS and EVA surveys…, Herz, Krivosheev, Rosstat, Federal Law No. 121-FZ,
  EUAA, Gaidar Institute, REPowerEU…, MERICS…). Přeložené je jen slovo
  „Sources" a data (24. 2. 2022, květen 2022 u Yle, 21. 2. 2022).
- licence (CC BY-SA 2.0, CC BY 4.0) a URL; popisné názvy snímků (maketa
  Vostoku 1, Kremelská zeď) se překládají, jména autorů ne.
- tagy — YouTube je per-jazyk nemá.

Odstavec o titulcích a americké stopě je **doslova** z tabulky
v `docs/zverejneni.md` („Popis NEJMENUJE počet jazyků titulků").

Terminologie podle titulků téhož videa: *pattern* = toimintamalli, schéma
(fr), pola, schema (it), Muster, wzorzec, padrão, örüntü, сценарій,
khuôn mẫu, vzorec, patrón, mönster; *confrontation* = vastakkainasettelu,
confrontation, konfrontasi, scontro, Konfrontation, konfrontacja,
confronto, çatışma, конфронтація, đối đầu, konfrontace, confrontación,
konfrontation; *security dilemma* a *sphere of influence* jako S25 a S45;
*the bill* jako S68 (lasku, facture, tagihan, conto, Rechnung, rachunek,
conta, fatura, рахунок, cái giá, účet, factura, notan). Pointa (vzorec
slouží systému, který potřebuje nepřítele) se neprozrazuje — popis končí
otázkou jako anglický.

Registr podle titulků tohoto videa: vykání cs, uk, tr, id, de (Sie),
fr (vous); tykání es, it, pl, sv, fi; pt-BR *você*, vi *bạn*. Popis
diváka přímo neoslovuje, takže se registr projeví jen ve volbě slov.

**Kontrola Codexem (2026-10-19): 13 nálezů, 11 zapracováno.** Část C (vynechané
věty, kapitoly, zdroje, atribuce) všude OK. Opraveno: fi *Italian kokoinen*
(srovnával s velikostí Itálie, ne její ekonomiky), fr přístavek u Švédska,
id *harganya dibayar*, de *eine so kleine Wirtschaft*, pl *zbliżanie się NATO*,
vi *biên giới Nga* (zvratné „của mình“ mohlo ukazovat na NATO), cs úvodní věta
a *doplácí*. Většinový nález: kapitola 01:13 *„Is it just one man?“* přeložená
jako otázka na počet (cs, pt-BR, sv) — je to elipsa *[behind it]*, opraveny
překlady, angličtina zůstává. Odmítnuto: vi *khuôn mẫu* → *lối hành xử*
(drží termín z titulků), fr věta o audiostopě (kanonické znění
z `docs/zverejneni.md`). Parser `bloky_z_podkladu()`: 13 jazyků po dvou blocích.

## suomi (`fi`)

```
Miksi Venäjä valitsee yhä uudelleen vastakkainasettelun?
```

```
Vuonna 2022 yksi Moskovan esittämistä syistä hyökkäykselle Ukrainaan oli se, että Nato hiipii sen rajoille. Vähän yli vuotta myöhemmin Suomi liittyi Natoon, ja Venäjän ja Naton välinen maaraja suunnilleen kaksinkertaistui. Sitten myös Ruotsi liittyi – maa, joka ei ollut käynyt sotaa sitten vuoden 1814.

Venäjä on maailman suurin maa, ja sillä on runsaasti öljyä, kaasua, metsiä, viljelysmaata ja mineraaleja. Silti sen talous on suunnilleen yhtä suuri kuin Italian talous. Miksi siis maa, jolla on niin paljon, valitsee yhä uudelleen vastakkainasettelun naapuriensa kanssa, joiden kanssa se voisi käydä kauppaa, silloinkin kun hinnan maksaa Venäjä itse? Helpoin vastaus on yksi mies. Mutta toimintamalli on vanhempi kuin yksikään presidentti. Tämä video seuraa sitä viiden vuosisadan laajentumisesta ja avoimesta tasangosta, jolla ei ole luonnollisia puolustusesteitä, Neuvostoliiton hajoamisen ja kaoottisen 1990-luvun kautta siihen, miten Moskovassa tehdään päätöksiä nykyään, ja kysyy, ketä toimintamalli oikeasti palvelee.

Lähteet: Address by the President of the Russian Federation, 24. helmikuuta 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (toukokuu 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21. helmikuuta 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

LUVUT
00:00 Suomi liittyy Natoon
00:38 Niin paljon maata, niin pieni talous
01:13 Onko kyse vain yhdestä miehestä?
01:39 Viisi vuosisataa laajentumista
02:37 Turvallisuusdilemma
03:14 Suomi muuttaa kantaansa
03:33 Neuvostoliitto
03:55 Romahdus ja 1990-luku
04:51 Järjestys ja vahva valtio
05:33 Menetetty etupiiri
06:23 Miten päätöksiä tehdään
07:25 Kolmas mekanismi
08:06 Ketä toimintamalli palvelee?
08:43 Lasku
09:34 Onko se vain kohtalo?
10:00 Mitä sen muuttaminen vaatisi?

KUVALÄHTEET
Vostok 1 -kapselin täysikokoinen malli, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Kremlin muuri talvella, Moskova — Vyacheslav Argenberg, CC BY 4.0
Wikimedia Commonsin kautta
Lisenssit: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

## français (`fr`)

```
Pourquoi la Russie choisit-elle sans cesse la confrontation ?
```

```
En 2022, l'une des raisons avancées par Moscou pour envahir l'Ukraine était l'OTAN qui se rapprochait peu à peu de ses frontières. Un peu plus d'un an plus tard, la Finlande a rejoint l'OTAN, et la frontière terrestre entre la Russie et l'OTAN a à peu près doublé. Puis la Suède, un pays qui n'avait pas fait la guerre depuis 1814, l'a rejointe à son tour.

La Russie est le plus grand pays du monde, riche en pétrole, en gaz, en forêts, en terres agricoles et en minerais. Pourtant, son économie a à peu près la taille de celle de l'Italie. Alors pourquoi un pays qui a tant choisit-il sans cesse la confrontation avec des voisins avec qui il pourrait commercer, même quand c'est la Russie elle-même qui en paie le prix ? La réponse facile, c'est un seul homme. Mais ce schéma est plus ancien que n'importe quel président. Cette vidéo le suit à travers cinq siècles d'expansion et une plaine ouverte sans défenses naturelles, puis l'effondrement de l'Union soviétique et le chaos des années 1990, jusqu'à la manière dont les décisions se prennent aujourd'hui à Moscou, et se demande à qui ce schéma profite vraiment.

Sources : Address by the President of the Russian Federation, 24 février 2022 (kremlin.ru) ; NATO, Relations with Finland and Sweden ; IMF, World Economic Outlook (2026) ; World Bank, World Development Indicators ; MTS and EVA surveys on NATO membership ; Yle / Taloustutkimus (mai 2022) ; J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950) ; G. F. Krivosheev, Soviet Casualties and Combat Losses (1993) ; Rosstat ; V. Putin, Russia at the Turn of the Millennium (1999) ; V. Putin, Address to the Federal Assembly (2005) ; V. Putin, On the Historical Unity of Russians and Ukrainians (2021) ; Kremlin, Security Council meeting transcript (21 février 2022) ; RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022) ; Federal Law No. 121-FZ (2012) ; EUAA, Russia: Foreign agents (2025) ; Ministry of Finance of the Russian Federation ; Gaidar Institute, Monitoring (2026) ; European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025) ; The Bell (2023) ; MERICS, China–Russia Dashboard (2026).

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

CHAPITRES
00:00 La Finlande rejoint l'OTAN
00:38 Tant de terres, une si petite économie
01:13 Tout tient-il à un seul homme ?
01:39 Cinq siècles d'expansion
02:37 Le dilemme de sécurité
03:14 La Finlande change d'avis
03:33 L'Union soviétique
03:55 L'effondrement et les années 1990
04:51 L'ordre et un État fort
05:33 Une sphère d'influence perdue
06:23 Comment les décisions se prennent
07:25 Le troisième mécanisme
08:06 À qui profite ce schéma ?
08:43 La facture
09:34 Est-ce simplement le destin ?
10:00 Que faudrait-il pour le changer ?

CRÉDITS DES IMAGES
Maquette grandeur nature de la capsule Vostok 1, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Mur du Kremlin en hiver, Moscou — Vyacheslav Argenberg, CC BY 4.0
via Wikimedia Commons
Licences : creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

## Bahasa Indonesia (`id`)

```
Mengapa Rusia terus memilih konfrontasi?
```

```
Pada 2022, salah satu alasan yang dikemukakan Moskow untuk menginvasi Ukraina adalah NATO yang perlahan merayap mendekati perbatasannya. Sedikit lebih dari setahun kemudian, Finlandia bergabung dengan NATO, dan perbatasan darat antara Rusia dan NATO menjadi kira-kira dua kali lipat. Lalu Swedia ikut bergabung, negara yang tidak pernah berperang sejak 1814.

Rusia adalah negara terbesar di Bumi, kaya akan minyak, gas, hutan, lahan pertanian, dan mineral. Namun ekonominya kira-kira sebesar ekonomi Italia. Jadi, mengapa negara yang punya begitu banyak terus memilih konfrontasi dengan tetangga yang sebenarnya bisa diajak berdagang, bahkan ketika Rusia sendiri harus menanggung akibatnya? Jawaban yang paling gampang adalah satu orang. Tetapi pola ini lebih tua daripada presiden mana pun. Video ini menelusurinya dari lima abad ekspansi dan dataran terbuka tanpa pertahanan alami, melalui runtuhnya Uni Soviet dan kekacauan tahun 1990-an, hingga cara keputusan diambil di Moskow saat ini, lalu bertanya siapa yang sebenarnya diuntungkan oleh pola ini.

Sumber: Address by the President of the Russian Federation, 24 Februari 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (Mei 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21 Februari 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

BAB
00:00 Finlandia bergabung dengan NATO
00:38 Wilayah seluas itu, ekonomi sekecil itu
01:13 Hanya soal satu orang?
01:39 Lima abad ekspansi
02:37 Dilema keamanan
03:14 Finlandia berubah pikiran
03:33 Uni Soviet
03:55 Keruntuhan dan tahun 1990-an
04:51 Ketertiban dan negara yang kuat
05:33 Lingkup pengaruh yang hilang
06:23 Bagaimana keputusan diambil
07:25 Mekanisme ketiga
08:06 Siapa yang diuntungkan pola ini?
08:43 Tagihannya
09:34 Apakah ini sekadar takdir?
10:00 Apa yang dibutuhkan untuk mengubahnya?

KREDIT GAMBAR
Replika kapsul Vostok 1 berukuran asli, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Tembok Kremlin di musim dingin, Moskow — Vyacheslav Argenberg, CC BY 4.0
melalui Wikimedia Commons
Lisensi: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

## italiano (`it`)

```
Perché la Russia continua a scegliere lo scontro?
```

```
Nel 2022, tra le ragioni addotte da Mosca per invadere l'Ucraina c'era la NATO che si avvicinava sempre più ai suoi confini. Poco più di un anno dopo, la Finlandia è entrata nella NATO e il confine terrestre tra Russia e NATO è più o meno raddoppiato. Poi è entrata anche la Svezia, un paese che non combatteva una guerra dal 1814.

La Russia è il paese più grande della Terra, ricco di petrolio, gas, foreste, terreni agricoli e minerali. Eppure la sua economia è più o meno grande quanto quella italiana. Allora perché un paese che ha così tanto continua a scegliere lo scontro con vicini con cui potrebbe commerciare, anche quando il prezzo lo paga la Russia stessa? La risposta facile è un uomo solo. Ma lo schema è più vecchio di qualsiasi presidente. Questo video lo ripercorre attraverso cinque secoli di espansione e una pianura aperta senza difese naturali, il crollo dell'Unione Sovietica e il caos degli anni Novanta, fino al modo in cui oggi si prendono le decisioni a Mosca, e si chiede a chi serva davvero questo schema.

Fonti: Address by the President of the Russian Federation, 24 febbraio 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (maggio 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21 febbraio 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

CAPITOLI
00:00 La Finlandia entra nella NATO
00:38 Tanta terra, un'economia così piccola
01:13 Dipende tutto da un uomo solo?
01:39 Cinque secoli di espansione
02:37 Il dilemma della sicurezza
03:14 La Finlandia cambia idea
03:33 L'Unione Sovietica
03:55 Il crollo e gli anni Novanta
04:51 Ordine e uno Stato forte
05:33 Una sfera d'influenza perduta
06:23 Come si prendono le decisioni
07:25 Il terzo meccanismo
08:06 A chi serve lo schema?
08:43 Il conto
09:34 È semplicemente destino?
10:00 Cosa servirebbe per cambiarlo?

CREDITI DELLE IMMAGINI
Modello a grandezza naturale della capsula Vostok 1, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Mura del Cremlino in inverno, Mosca — Vyacheslav Argenberg, CC BY 4.0
tramite Wikimedia Commons
Licenze: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

## Deutsch (`de`)

```
Warum setzt Russland immer wieder auf Konfrontation?
```

```
2022 war einer der Gründe, die Moskau für die Invasion in die Ukraine anführte, das Heranrücken der NATO an seine Grenzen. Etwas mehr als ein Jahr später trat Finnland der NATO bei, und die Landgrenze zwischen Russland und der NATO verdoppelte sich ungefähr. Dann trat auch Schweden bei, ein Land, das seit 1814 keinen Krieg mehr geführt hatte.

Russland ist das größte Land der Erde, reich an Öl, Gas, Wäldern, Ackerland und Bodenschätzen. Doch seine Wirtschaft ist ungefähr so groß wie die Italiens. Warum also setzt ein Land, das so viel hat, immer wieder auf Konfrontation mit Nachbarn, mit denen es Handel treiben könnte, selbst wenn Russland den Preis dafür selbst bezahlt? Die einfache Antwort ist ein einziger Mann. Doch das Muster ist älter als jeder einzelne Präsident. Dieses Video verfolgt es von fünf Jahrhunderten Expansion und einer offenen Ebene ohne natürliche Verteidigungslinien über den Zerfall der Sowjetunion und die chaotischen 1990er-Jahre bis zu der Art, wie heute in Moskau Entscheidungen fallen, und fragt, wem das Muster wirklich nützt.

Quellen: Address by the President of the Russian Federation, 24. Februar 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (Mai 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21. Februar 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

KAPITEL
00:00 Finnland tritt der NATO bei
00:38 So viel Land, eine so kleine Wirtschaft
01:13 Liegt es nur an einem Mann?
01:39 Fünf Jahrhunderte Expansion
02:37 Das Sicherheitsdilemma
03:14 Finnland ändert seine Meinung
03:33 Die Sowjetunion
03:55 Zerfall und die 1990er
04:51 Ordnung und ein starker Staat
05:33 Eine verlorene Einflusssphäre
06:23 Wie Entscheidungen fallen
07:25 Der dritte Mechanismus
08:06 Wem nützt das Muster?
08:43 Die Rechnung
09:34 Ist es einfach Schicksal?
10:00 Was wäre nötig, um es zu ändern?

BILDNACHWEISE
Modell der Wostok-1-Kapsel in Originalgröße, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Kremlmauer im Winter, Moskau — Vyacheslav Argenberg, CC BY 4.0
über Wikimedia Commons
Lizenzen: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

## polski (`pl`)

```
Dlaczego Rosja wciąż wybiera konfrontację?
```

```
W 2022 roku jednym z powodów, którymi Moskwa uzasadniała inwazję na Ukrainę, było zbliżanie się NATO do jej granic. Nieco ponad rok później Finlandia wstąpiła do NATO, a granica lądowa między Rosją a NATO mniej więcej się podwoiła. Potem dołączyła też Szwecja, kraj, który nie prowadził wojny od 1814 roku.

Rosja jest największym krajem na Ziemi, bogatym w ropę, gaz, lasy, ziemię uprawną i surowce mineralne. A jednak jej gospodarka jest mniej więcej wielkości gospodarki Włoch. Dlaczego więc kraj, który ma tak wiele, wciąż wybiera konfrontację z sąsiadami, z którymi mógłby handlować, nawet gdy cenę płaci sama Rosja? Najprostsza odpowiedź to jeden człowiek. Ale ten wzorzec jest starszy niż którykolwiek prezydent. Ten film śledzi go od pięciu stuleci ekspansji i otwartej równiny bez naturalnych osłon, przez rozpad Związku Radzieckiego i chaotyczne lata 90., aż po to, jak dziś zapadają decyzje w Moskwie, i pyta, komu ten wzorzec naprawdę służy.

Źródła: Address by the President of the Russian Federation, 24 lutego 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (maj 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21 lutego 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

ROZDZIAŁY
00:00 Finlandia wstępuje do NATO
00:38 Tyle ziemi, tak mała gospodarka
01:13 Czy chodzi tylko o jednego człowieka?
01:39 Pięć stuleci ekspansji
02:37 Dylemat bezpieczeństwa
03:14 Finlandia zmienia zdanie
03:33 Związek Radziecki
03:55 Rozpad i lata 90.
04:51 Porządek i silne państwo
05:33 Utracona strefa wpływów
06:23 Jak zapadają decyzje
07:25 Trzeci mechanizm
08:06 Komu służy ten wzorzec?
08:43 Rachunek
09:34 Czy to po prostu los?
10:00 Co musiałoby się stać, żeby to zmienić?

ŹRÓDŁA ZDJĘĆ
Pełnowymiarowa makieta kapsuły Wostok 1, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Mur Kremla zimą, Moskwa — Vyacheslav Argenberg, CC BY 4.0
przez Wikimedia Commons
Licencje: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

## português (Brasil) (`pt-BR`)

```
Por que a Rússia continua escolhendo o confronto?
```

```
Em 2022, um dos motivos que Moscou apresentou para invadir a Ucrânia foi o avanço gradual da OTAN rumo às suas fronteiras. Pouco mais de um ano depois, a Finlândia entrou na OTAN, e a fronteira terrestre entre a Rússia e a OTAN praticamente dobrou. Depois a Suécia também entrou, um país que não entrava em guerra desde 1814.

A Rússia é o maior país da Terra, rico em petróleo, gás, florestas, terras agrícolas e minerais. Mesmo assim, sua economia tem mais ou menos o tamanho da italiana. Então por que um país que tem tanto continua escolhendo o confronto com vizinhos com quem poderia fazer comércio, mesmo quando quem paga o preço é a própria Rússia? A resposta fácil é um homem só. Mas o padrão é mais antigo do que qualquer presidente. Este vídeo o acompanha desde cinco séculos de expansão e uma planície aberta sem defesas naturais, passando pelo colapso da União Soviética e pelos caóticos anos 1990, até a forma como as decisões são tomadas hoje em Moscou, e pergunta a quem esse padrão realmente serve.

Fontes: Address by the President of the Russian Federation, 24 de fevereiro de 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (maio de 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21 de fevereiro de 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

CAPÍTULOS
00:00 A Finlândia entra na OTAN
00:38 Tanta terra, uma economia tão pequena
01:13 Tudo se resume a um só homem?
01:39 Cinco séculos de expansão
02:37 O dilema de segurança
03:14 A Finlândia muda de ideia
03:33 A União Soviética
03:55 O colapso e os anos 1990
04:51 Ordem e um Estado forte
05:33 Uma esfera de influência perdida
06:23 Como as decisões são tomadas
07:25 O terceiro mecanismo
08:06 A quem esse padrão serve?
08:43 A conta
09:34 É simplesmente o destino?
10:00 O que seria preciso para mudá-lo?

CRÉDITOS DAS IMAGENS
Maquete em tamanho real da cápsula Vostok 1, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Muralha do Kremlin no inverno, Moscou — Vyacheslav Argenberg, CC BY 4.0
via Wikimedia Commons
Licenças: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

## Türkçe (`tr`)

```
Rusya neden durmadan çatışmayı seçiyor?
```

```
2022'de Moskova'nın Ukrayna'yı işgal etmek için öne sürdüğü gerekçelerden biri NATO'nun adım adım sınırlarına yaklaşmasıydı. Bir yıldan biraz fazla bir süre sonra Finlandiya NATO'ya katıldı ve Rusya ile NATO arasındaki kara sınırı kabaca iki katına çıktı. Ardından İsveç de katıldı: 1814'ten beri hiç savaşa girmemiş bir ülke.

Rusya dünyanın en büyük ülkesi; petrol, gaz, orman, tarım arazisi ve maden bakımından zengin. Ama ekonomisi kabaca İtalya'nınki kadar. Peki bu kadar çok şeye sahip bir ülke neden ticaret yapabileceği komşularıyla durmadan çatışmayı seçiyor, hem de bedelini bizzat Rusya ödediği hâlde? Kolay cevap tek bir adam. Ama bu örüntü herhangi bir devlet başkanından daha eski. Bu video onu beş yüzyıllık genişlemeden ve doğal savunması olmayan açık bir ovadan başlayarak, Sovyetler Birliği'nin dağılması ve kaotik 1990'lar üzerinden, bugün Moskova'da kararların nasıl alındığına kadar izliyor ve bu örüntünün aslında kimin işine yaradığını soruyor.

Kaynaklar: Address by the President of the Russian Federation, 24 Şubat 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (Mayıs 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21 Şubat 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

BÖLÜMLER
00:00 Finlandiya NATO'ya katılıyor
00:38 Bu kadar toprak, bu kadar küçük bir ekonomi
01:13 Mesele tek bir adam mı?
01:39 Beş yüzyıllık genişleme
02:37 Güvenlik ikilemi
03:14 Finlandiya fikrini değiştiriyor
03:33 Sovyetler Birliği
03:55 Çöküş ve 1990'lar
04:51 Düzen ve güçlü bir devlet
05:33 Kaybedilmiş bir nüfuz alanı
06:23 Kararlar nasıl alınıyor
07:25 Üçüncü mekanizma
08:06 Bu örüntü kimin işine yarıyor?
08:43 Fatura
09:34 Bu sadece kader mi?
10:00 Bunu değiştirmek için ne gerekir?

GÖRSEL KAYNAKLARI
Vostok 1 kapsülünün gerçek boyutlu maketi, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Kışın Kremlin duvarı, Moskova — Vyacheslav Argenberg, CC BY 4.0
Wikimedia Commons aracılığıyla
Lisanslar: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

## українська (`uk`)

```
Чому Росія раз у раз обирає конфронтацію?
```

```
У 2022 році однією з причин, якими Москва пояснювала вторгнення в Україну, було те, що НАТО підкрадається до її кордонів. Трохи більше ніж за рік Фінляндія вступила до НАТО, і сухопутний кордон між Росією та НАТО приблизно подвоївся. Потім приєдналася і Швеція — країна, яка не воювала з 1814 року.

Росія — найбільша країна на Землі, багата на нафту, газ, ліси, сільськогосподарські землі та корисні копалини. Проте її економіка приблизно такого ж розміру, як італійська. То чому країна, яка має так багато, раз у раз обирає конфронтацію із сусідами, з якими могла б торгувати, навіть коли ціну платить сама Росія? Найпростіша відповідь — одна людина. Але цей сценарій старший за будь-якого президента. Це відео простежує його від п'яти століть експансії та відкритої рівнини без природних рубежів оборони, через розпад Радянського Союзу й хаотичні 1990-ті, до того, як сьогодні ухвалюють рішення в Москві, і запитує, кому цей сценарій насправді служить.

Джерела: Address by the President of the Russian Federation, 24 лютого 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (травень 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21 лютого 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

РОЗДІЛИ
00:00 Фінляндія вступає до НАТО
00:38 Стільки землі, така мала економіка
01:13 Чи все через одну людину?
01:39 П'ять століть експансії
02:37 Дилема безпеки
03:14 Фінляндія змінює думку
03:33 Радянський Союз
03:55 Розпад і 1990-ті
04:51 Порядок і сильна держава
05:33 Втрачена сфера впливу
06:23 Як ухвалюють рішення
07:25 Третій механізм
08:06 Кому служить цей сценарій?
08:43 Рахунок
09:34 Це просто доля?
10:00 Що знадобиться, щоб це змінити?

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Повнорозмірний макет капсули «Восток-1», Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Кремлівська стіна взимку, Москва — Vyacheslav Argenberg, CC BY 4.0
через Wikimedia Commons
Ліцензії: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

## Tiếng Việt (`vi`)

```
Tại sao Nga cứ mãi chọn đối đầu?
```

```
Năm 2022, một trong những lý do Moskva đưa ra để xâm lược Ukraine là NATO đang lấn dần tới sát biên giới Nga. Chỉ hơn một năm sau, Phần Lan gia nhập NATO, và đường biên giới trên bộ giữa Nga và NATO tăng lên gần gấp đôi. Rồi Thụy Điển cũng gia nhập, một đất nước đã không tham chiến kể từ năm 1814.

Nga là quốc gia lớn nhất trên Trái Đất, giàu dầu mỏ, khí đốt, rừng, đất nông nghiệp và khoáng sản. Thế nhưng nền kinh tế Nga chỉ xấp xỉ nền kinh tế Ý. Vậy tại sao một đất nước có nhiều thứ như vậy lại cứ chọn đối đầu với những láng giềng mà lẽ ra có thể buôn bán cùng, ngay cả khi chính nước Nga phải trả giá? Câu trả lời dễ nhất là một người. Nhưng khuôn mẫu này có từ trước bất kỳ vị tổng thống nào. Video này lần theo nó từ năm thế kỷ bành trướng và một đồng bằng trống trải không có phòng tuyến tự nhiên, qua sự sụp đổ của Liên Xô và thập niên 1990 hỗn loạn, đến cách các quyết định được đưa ra ở Moskva ngày nay, và đặt câu hỏi khuôn mẫu này thực sự phục vụ ai.

Nguồn: Address by the President of the Russian Federation, 24 tháng 2 năm 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (tháng 5 năm 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21 tháng 2 năm 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

CHƯƠNG
00:00 Phần Lan gia nhập NATO
00:38 Đất rộng đến thế, kinh tế nhỏ đến thế
01:13 Chỉ vì một người?
01:39 Năm thế kỷ bành trướng
02:37 Thế lưỡng nan an ninh
03:14 Phần Lan đổi ý
03:33 Liên Xô
03:55 Sụp đổ và thập niên 1990
04:51 Trật tự và một nhà nước mạnh
05:33 Một vùng ảnh hưởng đã mất
06:23 Các quyết định được đưa ra thế nào
07:25 Cơ chế thứ ba
08:06 Khuôn mẫu này phục vụ ai?
08:43 Cái giá phải trả
09:34 Chỉ là số phận?
10:00 Cần gì để thay đổi nó?

NGUỒN HÌNH ẢNH
Mô hình kích thước thật của khoang tàu Vostok 1, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Tường thành Kremlin vào mùa đông, Moskva — Vyacheslav Argenberg, CC BY 4.0
qua Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

## čeština (`cs`)

```
Proč Rusko stále volí konfrontaci?
```

```
V roce 2022 zdůvodňovala Moskva invazi na Ukrajinu mimo jiné tím, že se k jejím hranicím plíživě blíží NATO. O něco víc než rok později vstoupilo do NATO Finsko a pozemní hranice mezi Ruskem a NATO se zhruba zdvojnásobila. Pak se přidalo i Švédsko, země, která nevedla válku od roku 1814.

Rusko je největší zemí na světě, bohatou na ropu, plyn, lesy, zemědělskou půdu a nerostné suroviny. Přesto je jeho ekonomika zhruba stejně velká jako italská. Proč tedy země, která má tolik, stále volí konfrontaci se sousedy, se kterými by mohla obchodovat, i když na to doplácí samo Rusko? Nejsnazší odpověď je jeden člověk. Jenže ten vzorec je starší než kterýkoli prezident. Video ho sleduje od pěti století rozpínání a otevřené roviny bez přirozené obrany přes rozpad Sovětského svazu a chaotická devadesátá léta až k tomu, jak se dnes v Moskvě rozhoduje, a ptá se, komu ten vzorec doopravdy slouží.

Zdroje: Address by the President of the Russian Federation, 24. února 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (květen 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21. února 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

KAPITOLY
00:00 Finsko vstupuje do NATO
00:38 Tolik území, tak malá ekonomika
01:13 Je to všechno kvůli jednomu člověku?
01:39 Pět století rozpínání
02:37 Bezpečnostní dilema
03:14 Finsko mění názor
03:33 Sovětský svaz
03:55 Rozpad a devadesátá léta
04:51 Pořádek a silný stát
05:33 Ztracená sféra vlivu
06:23 Jak se rozhoduje
07:25 Třetí mechanismus
08:06 Komu ten vzorec slouží?
08:43 Účet
09:34 Je to prostě osud?
10:00 Co by bylo potřeba, aby se to změnilo?

ZDROJE OBRÁZKŮ
Maketa kabiny lodi Vostok 1 ve skutečné velikosti, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Kremelská zeď v zimě, Moskva — Vyacheslav Argenberg, CC BY 4.0
přes Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

## español (`es`)

```
¿Por qué Rusia sigue eligiendo la confrontación?
```

```
En 2022, una de las razones que dio Moscú para invadir Ucrania fue que la OTAN se iba acercando a sus fronteras. Poco más de un año después, Finlandia entró en la OTAN, y la frontera terrestre entre Rusia y la OTAN más o menos se duplicó. Luego se sumó también Suecia, un país que no había librado una guerra desde 1814.

Rusia es el país más grande de la Tierra, rico en petróleo, gas, bosques, tierras de cultivo y minerales. Sin embargo, su economía tiene más o menos el tamaño de la de Italia. Entonces, ¿por qué un país que tiene tanto sigue eligiendo la confrontación con vecinos con los que podría comerciar, incluso cuando el precio lo paga la propia Rusia? La respuesta fácil es un solo hombre. Pero el patrón es más antiguo que cualquier presidente. Este vídeo lo sigue desde cinco siglos de expansión y una llanura abierta sin defensas naturales, pasando por el colapso de la Unión Soviética y los caóticos años noventa, hasta la forma en que hoy se toman las decisiones en Moscú, y se pregunta a quién sirve de verdad este patrón.

Fuentes: Address by the President of the Russian Federation, 24 de febrero de 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (mayo de 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21 de febrero de 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

CAPÍTULOS
00:00 Finlandia entra en la OTAN
00:38 Tanta tierra, una economía tan pequeña
01:13 ¿Es solo cosa de un hombre?
01:39 Cinco siglos de expansión
02:37 El dilema de seguridad
03:14 Finlandia cambia de opinión
03:33 La Unión Soviética
03:55 El colapso y los años noventa
04:51 Orden y un Estado fuerte
05:33 Una esfera de influencia perdida
06:23 Cómo se toman las decisiones
07:25 El tercer mecanismo
08:06 ¿A quién sirve el patrón?
08:43 La factura
09:34 ¿Es simplemente el destino?
10:00 ¿Qué haría falta para cambiarlo?

CRÉDITOS DE LAS IMÁGENES
Maqueta a tamaño real de la cápsula Vostok 1, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Muralla del Kremlin en invierno, Moscú — Vyacheslav Argenberg, CC BY 4.0
vía Wikimedia Commons
Licencias: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

## svenska (`sv`)

```
Varför väljer Ryssland gång på gång konfrontation?
```

```
2022 var ett av skälen som Moskva angav för invasionen av Ukraina att Nato kröp allt närmare dess gränser. Drygt ett år senare gick Finland med i Nato, och landgränsen mellan Ryssland och Nato blev ungefär dubbelt så lång. Sedan gick även Sverige med, ett land som inte hade varit i krig sedan 1814.

Ryssland är världens största land, rikt på olja, gas, skog, jordbruksmark och mineraler. Ändå är dess ekonomi ungefär lika stor som Italiens. Så varför väljer ett land med så mycket gång på gång konfrontation med grannar som det skulle kunna handla med, även när det är Ryssland självt som betalar priset? Det enkla svaret är en enda man. Men mönstret är äldre än någon enskild president. Den här videon följer det från fem sekler av expansion och en öppen slätt utan naturliga försvarslinjer, via Sovjetunionens sammanbrott och det kaotiska 1990-talet, till hur besluten fattas i Moskva i dag, och frågar vem mönstret egentligen tjänar.

Källor: Address by the President of the Russian Federation, 24 februari 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (maj 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21 februari 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

KAPITEL
00:00 Finland går med i Nato
00:38 Så mycket land, så liten ekonomi
01:13 Beror allt på en enda man?
01:39 Fem sekler av expansion
02:37 Säkerhetsdilemmat
03:14 Finland ändrar sig
03:33 Sovjetunionen
03:55 Sammanbrottet och 1990-talet
04:51 Ordning och en stark stat
05:33 En förlorad intressesfär
06:23 Hur beslut fattas
07:25 Den tredje mekanismen
08:06 Vem tjänar mönstret?
08:43 Notan
09:34 Är det helt enkelt ödet?
10:00 Vad skulle krävas för att förändra det?

BILDKÄLLOR
Fullskalig modell av kapseln Vostok 1, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Kremlmuren på vintern, Moskva — Vyacheslav Argenberg, CC BY 4.0
via Wikimedia Commons
Licenser: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```
