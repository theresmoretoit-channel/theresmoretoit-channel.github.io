# 128 — fact check (scénář 0.1, 2026-10-31)

Scény podle `script.md` (= `script 0.1.md`). Závěr: ✅ doloženo,
✏️ **OPRAVIT**, 🔸 **ZMÍRNIT**, ❓ **NEDOLOŽENO**, 💬 úvaha / zjednodušení
(není faktické tvrzení, jen nesmí lhát). Návrhy znění jsou na konci,
v „Souhrn nálezů".

Primární zdroje (staženo do scratchpadu, čteno `pdftotext -layout`):

- **3GPP TS 23.038 V18.0.0** (ETSI TS 123 038, 2024-05), *Alphabets and
  language-specific information* —
  <https://www.etsi.org/deliver/etsi_ts/123000_123099/123038/18.00.00_60/ts_123038v180000p.pdf>
- **3GPP TS 23.040 V18.0.0** (ETSI TS 123 040), *Technical realization of
  the Short Message Service (SMS)* —
  <https://www.etsi.org/deliver/etsi_ts/123000_123099/123040/18.00.00_60/ts_123040v180000p.pdf>
- **OMA MMS Conformance Document 1.3** (OMA-TS-MMS_CONF-V1_3-20110913-A) —
  <https://www.openmobilealliance.org/release/MMS/V1_3-20110913-A/OMA-TS-MMS_CONF-V1_3-20110913-A.pdf>
- **Rozhovor s Hillebrandem**: Milian, *LA Times* Technology blog, 2009-05
  (originál na latimes.com nejde stáhnout; doslovný přetisk v archivu
  konference Link: <https://mailman.anu.edu.au/pipermail/link/2009-May/015590.html>).
  Doplňkově profil Hans-Böckler-Stiftung „Mister SMS"
  (<https://www.boeckler.de/de/alumni-portraits-18574-mister-sms-5578.htm>)
  a Hillebrand (ed.), *Short Message Service (SMS): The Creation of Personal
  Global Text Messaging*, Wiley 2010 — kniha sama dostupná není, cituje se
  přes abstrakt („the maximum message length in SMS in the beginning was
  128 bytes carrying 146 characters … later enlarged to 140 bytes as
  160 characters").

Výpočty jsou počítané, ne opsané.

## S01–S07 Úvod: cena dat

| | tvrzení | ověření | |
|---|---|---|---|
| S01 | na počátku 2000. let prodávali operátoři data za absurdní cenu | viz S04; v USA 2005 typicky **10 c za zprávu odeslanou i přijatou**, 2008 **20 c** (dopis senátora H. Kohla čtyřem operátorům, 9/2008: „text messages in 2005 were commonly priced at 10 cents per message sent or received… by the end of August 2008… 20 cents on all four", přes [Fierce Wireless](https://www.fierce-network.com/wireless/verizon-at-t-defend-text-messaging-price-policies) a [RCR Wireless](https://www.rcrwireless.com/article/20081013/WIRELESS/810139983)). Doložená 10c cena je z poloviny dekády, „early 2000s" je na hraně, ale 2001–2004 ceny nebyly nižší | ✅ 💬 |
| S02 | nešlo o mobilní internet, ale o SMS | rámování | 💬 |
| S03 | jedna SMS nesla nejvýš 140 bajtů | TS 23.040, kap. 3: „The text messages to be transferred by means of the SM MT or SM MO contain **up to 140 octets**." | ✅ |
| S04 | při 10 c za zprávu by 1 MB stál přes 700 USD | 10⁶ B / 140 B = **7 142,9 zpráv** × 0,10 = **714 USD**; při MiB (1 048 576 B) 7 490 zpráv = 749 USD. Při 20 c (USA 2008) **1 429 USD**. Předpoklad: každá zpráva plně využitá (u kratších textů je cena za bajt ještě vyšší) | ✅ |
| S05 | lidé to platili, miliardykrát denně | ITU *The World in 2010*: SMS celosvětově **1,8 bil. (2007) → 6,1 bil. (2010)** ([ITU press, 2010](https://www.itu.int/net/pressoffice/press_releases/2010/39-fr.aspx); [New Atlas](https://newatlas.com/itu-tracks-the-decade-that-transformed-the-world/18016/)). 1,8×10¹²/365 = **4,9 mld./den**, 6,1×10¹²/365 = **16,7 mld./den**. Pro rok 2002 udává Wikipedie 366 mld./rok = **1,0 mld./den** — „billions" (množné) tedy platí asi od poloviny dekády | ✅ |
| S06 | malá vedlejší funkce sítě se stala zlatým dolem | viz S52–S64 | ✅ |
| S07 | každá zpráva omezena na přesně 160 znaků | 140 × 8 / 7 = **160** znaků GSM 7bit (TS 23.038 kap. 6.1.2.1); platí jen pro 7bitovou abecedu, viz S28–S29 | ✅ |

## S08–S24 Dva „rodiče" čísla 160

| | tvrzení | ověření | |
|---|---|---|---|
| S08 | číslo má dva rodiče | rámování; viz S24 | 💬 |
| S09 | 1985, německý inženýr Friedhelm Hillebrand, psací stroj | LA Times 2009: „Alone in a room in his home in Bonn, Germany, Friedhelm Hillebrand sat at his typewriter"; „he recalled thinking during that epiphany of **1985**". Byl ve vedoucích funkcích u Deutsche Bundespost v Bonnu, později Telekomu (Böckler). Předseda skupiny GSM pro neřečové služby; první návrh SMS Německo + Francie (s **Bernardem Ghillebaertem**, France Télécom) na zasedání GSM v Oslu v únoru 1985 (Wikipedie *SMS*, odkaz na GSM doc 19/85). „Engineer" drží (vzděláním inženýr telekomunikací) | ✅ |
| S10 | psal běžné věty a otázky a počítal znaky | „tapping out random sentences and questions on a sheet of paper… counted the number of letters, numbers, punctuation marks and spaces" (LA Times) | ✅ |
| S11 | skoro všechny se vešly do 160 | „nearly always clocked in under 160 characters" (LA Times) | ✅ |
| S12 | prověřil i pohlednice a telexy, i ty byly většinou kratší než 160 | „they found that postcards often contained fewer than 150 characters… Telex transmissions were usually about the same length as postcards" (LA Times; dělal to Hillebrandův tým/výbor, ne on sám). Böckler: „Friedhelm Hillebrand hat die Texte vieler Postkarten ausgezählt." | ✅ |
| S13 | první rodič je lidský: 160 stačí na většinu toho, co lidé říkají | Hillebrandův závěr „This is perfectly sufficient" | ✅ |
| S14–S15 | druhý rodič je síť; inženýři navrhovali GSM, nový evropský standard digitálních mobilů | Groupe Spécial Mobile (CEPT) od 1982, první sítě 1991–92 | ✅ |
| S16–S17 | telefon neustále vyměňuje se sítí malé zprávy: jsem tady, přesunul jsem se do jiné buňky, přichází hovor | location update (periodický i při změně oblasti), paging. **Drobnost:** v klidovém stavu telefon přechod do jiné **buňky** síti nehlásí, jen změnu **lokalizační oblasti** (skupiny buněk); handover za hovoru řídí síť. Popularizační zkratka, smysl drží | ✅ 💬 |
| S18 | tomu se říká signalizace a ty kanály většinu času stojí skoro prázdné | LA Times: „harness a secondary radio channel that already existed… This smaller data lane had been used only to alert a cellphone about reception strength"; TechCrunch 2009: „a barely used radio channel". SMS jde v klidu přes SDCCH, za hovoru přes SACCH | ✅ |
| S19 | myšlenka: krátké texty by se svezly ve volné kapacitě | dtto | ✅ |
| S20 | signalizační zpráva je malá, na text zbylo 140 bajtů | 140 oktetů je konečná hodnota (TS 23.040). **Ale nebyla daná od začátku:** viz S24 | ✅ (viz S24) |
| S21 | 140 bajtů = 1 120 bitů | 140 × 8 = **1 120** | ✅ |
| S22 | jednoduchý text nepotřebuje 8 bitů na znak, GSM použilo 7 | TS 23.038 kap. 6.2.1 „GSM 7 bit default alphabet" | ✅ |
| S23 | 1 120 / 7 = přesně 160 | 1 120 / 7 = **160,0** | ✅ |
| S24 | odhad inženýra a mez sítě „landed on the same number" | **Takhle to nebylo.** 160 bylo **cílem** od Hillebranda a síť se k němu **natahovala**: „Initially, Hillebrand's team could fit only **128 characters** into that space… they squeezed out room for another 32 characters" (LA Times); Wiley 2010 (abstrakt): „in the beginning was **128 bytes carrying 146 characters**… later **enlarged to 140 bytes** as 160 characters". Kontrola: 128 × 8 / 7 = 146,3 → **146** ✔. Věta „landed on the same number" navozuje náhodnou shodu dvou nezávislých čísel, kdežto ve skutečnosti se 140 B vybralo, aby se do něj 160 vešlo. Rámování „dvou rodičů" (S08) může zůstat — lidská potřeba určila číslo, síť a 7bitové kódování ho umožnily | ✏️ |

## S25–S31 Abeceda

Tabulka GSM 7bit default alphabet podle TS 23.038 V18.0.0, kap. 6.2.1
(vypsáno z PDF): 128 pozic, z toho 1 escape do rozšiřující tabulky
(`€ [ ] { } \ ~ ^ |`). Písmena mimo A–Z: **è é ù ì ò Ç Ø ø Å å Æ æ ß É
Ä Ö Ñ Ü ä ö ñ ü à** (23) a řecké verzálky **Δ Φ Γ Λ Ω Π Ψ Σ Θ Ξ**.

| | tvrzení | ověření | |
|---|---|---|---|
| S25 | 7 bitů dává jen 128 znaků | 2⁷ = **128** ✔ (jeden z nich je escape; přes něj dalších 10 znaků za cenu 2 pozic) | ✅ |
| S26 | to pokryje angličtinu a hrstku písmen s diakritikou | viz výpis: 16 písmen s akcentem + 7 skandinávských/německých (Ø, Å, Æ, ß…) — „a handful" je na hraně, ale drží (francouzština, němčina, španělština, italština, skandinávské jazyky z velké části ano) | ✅ |
| S27 | ne české ř, polské ł, turecké ş ani cyrilice | **ř, ł, ş ani žádné cyrilské písmeno v základní tabulce nejsou** ✔. **Ale ş:** od **Release 8 (2008)** existuje turecká národní tabulka (*National Language Locking Shift Table*, TS 23.038 příl. A.3.1, pozice 1/13 = ş, 1/12 = Ş; i single shift A.2.1). Change history: „CP-080138 … Rel-8 … SMS-addition of turkish national language locking shift table". S telefonem a sítí, které to podporují, jde turečtina **7bitově** za cenu 3 oktetů hlavičky (155 znaků místo 160; TS 23.038 příl. C). Národní tabulky existují jen pro **turečtinu, španělštinu, portugalštinu a 10 indických jazyků + urdštinu** (tab. 6.2.1.2.4.1) — **čeština, polština ani cyrilice ne**. Pro ř, ł a cyrilici tvrzení i S28 platí bez výhrad; pro ş jen do zavedení Rel-8 tabulek | 🔸 |
| S28 | použij jedno takové písmeno a telefon přepne na 16bitové kódování | UCS-2 (TS 23.038 kap. 5/6.2.3) — platí pro ř, ł, cyrilici; pro ş viz S27. (Část telefonů místo přepnutí diakritiku sama odstraňovala nebo nahrazovala — „the phone switches" je typický, ne jediný případ) | ✅ (s výhradou S27) |
| S29 | stejných 140 bajtů pojme jen 70 znaků | 140 / 2 = **70** ✔ | ✅ |
| S30 | jedno písmeno zkrátí zprávu o víc než polovinu | 160 → 70: zbude 43,75 %, **úbytek 56 %** ✔. (U složené SMS je to 153 → 67, tj. (140−6)×8/7 = 153,1 a (140−6)/2 = 67; TS 23.040 kap. 9.2.3.24.1: „maximum length… is 67" pro UCS2) | ✅ |
| S31 | proto léta miliony lidí psaly SMS bez diakritiky | mechanismus doložený (Svět Androida 2014: <https://www.svetandroida.cz/sms-zpravy-diakritika-odstraneni/>; Noviny.sk: „Slováci pozor! Písanie SMS s diakritikou je drahšie"; android.com.pl „brak polskich znaków w SMS"). Kvantifikaci („millions") nikdo neměří, ale jen Česko, Slovensko a Polsko mají přes 50 mil. obyvatel a psaní bez háčků bylo pravidlem; ruský *translit* totéž. Řádově drží | ✅ 💬 |

## S32–S38 SMS a první zpráva

| | tvrzení | ověření | |
|---|---|---|---|
| S32 | služba se jmenovala SMS, Short Message Service | TS 23.040, název | ✅ |
| S33 | nikdo ji nenavrhl jako messenger | **Příliš silné.** Hillebrandův vlastní vzorový případ je zpráva **člověku**: elektrikář, který po zakázce „im Autotelefon einen neuen Auftrag vorfindet" (Böckler); LA Times: „originally devised as a **portable paging system** for craftsmen using their cars as a mobile office". A test na psacím stroji (S10–S13) byl právě o tom, co lidé **říkají** — S33 tak odporuje S13. Doložené je, že **nikdo nečekal masové posílání mezi lidmi**: LA Times — Hillebrand říká, že nikdo nepředpověděl, jak rychle to vezmou mladí; Böckler: „Massenhaft durchgesetzt haben den Dienst freilich die jungen User" | 🔸 |
| S34 | malý doplněk sítě; hodí se na notifikace, možná pro pagery | „portable paging system" (LA Times) — tedy **jako** pager, ne **pro** pagery; „Maybe for pagers" zní, jako by se SMS posílala na pagery | 🔸 |
| S35 | 3. 12. 1992 poslána první SMS přes britskou síť | Neil Papworth (Sema Group) z PC v Newbury na Orbitel 901 Richarda Jarvise, síť **Vodafone UK** ([NPR 2017](https://www.npr.org/2017/12/04/568393428/the-first-text-messages-celebrates-25-years); [Smithsonian](https://www.smithsonianmag.com/smart-news/the-first-text-message-sent-twenty-years-ago-was-merry-christmas-152311567/); Wikipedie *Neil Papworth*, odkaz na BBC 2002) | ✅ |
| S36 | text: „Merry Christmas" | tamtéž | ✅ |
| S37 | napsaná na počítači, ne na telefonu | „Mobile phones did not yet have keyboards, so he typed the message out on a PC" (tamtéž) | ✅ |
| S38 | telefon ji zobrazil, ale odpovědět neuměl | BBC 2002: Orbitel 901 „had no method of inputting text"; Jarvis neodpověděl | ✅ |

## S39–S51 Store and forward, rozšíření

| | tvrzení | ověření | |
|---|---|---|---|
| S39–S40 | doručení jako pošta: telefon předá text serveru v síti, SMS centru | TS 23.040 kap. 3: „The provision of SMS makes use of a **Service Centre, which acts as a store and forward centre** for short messages" | ✅ |
| S41–S43 | vypnutý telefon / mimo signál → zpráva čeká; když se vrátí, síť to zkusí znovu | TS 23.040: Messages-Waiting, *alert SC* po opětovném přihlášení (kap. 10.2 / 9.1.2.2). Čeká jen do konce doby platnosti (validity period) — zjednodušení přijatelné | ✅ |
| S44 | inženýři tomu říkají store and forward; bez internetu, účtu, aplikace, jen signál | tamtéž | ✅ |
| S45 | pak se telefony naučily SMS posílat a lidé objevili něco, s čím autoři moc nepočítali | první komerční P2P služba Radiolinja (Finsko) 1993; Nokia jediná v 1993 s odesíláním v celé řadě (Wikipedie *SMS*). „hadn't really planned for" drží (LA Times, Böckler, viz S33) | ✅ |
| S46–S49 | hovor potřebuje oba současně, text ne | asynchronnost — popis | 💬 |
| S50 | na klávesnici se **třemi písmeny na každé klávese** byli lidé neuvěřitelně rychlí | ITU-T E.161: 2 ABC, 3 DEF, 4 GHI, 5 JKL, 6 MNO, **7 PQRS**, 8 TUV, **9 WXYZ** — dvě klávesy mají čtyři písmena (a 0, 1 žádné). „Every key" tedy neplatí | ✏️ (drobnost) |
| S51 | telefon se stal osobním zařízením na zprávy | interpretace | 💬 |

## S52–S64 Zlatý důl

| | tvrzení | ověření | |
|---|---|---|---|
| S53–S54 | věže i signalizační kanály už stály | mezní náklad zprávy je malý (SMSC, propojení, signalizace SS7 nejsou zadarmo, ale vůči ceně zanedbatelné) — zjednodušení | ✅ 💬 |
| S55 | každá zpráva byla 140 bajtů | **nejvýš** 140 bajtů (TS 23.040); běžná zpráva kratší. Formulace z S03 („at most") se tu ztratila | 🔸 (drobnost) |
| S56 | zákazníci platili za zprávu, ne za bajty | ✔ (Kohl 2008; české ceníky) | ✅ |
| S57 | nebo za balík pár set zpráv měsíčně | balíčky běžné (USA „bulk texting plans", RCR 2008) | ✅ |
| S58 | ceny se mezi zeměmi hodně lišily | ✔ | ✅ |
| S59 | v mnoha evropských zemích se platilo za každou zprávu | předplacené karty a tarify s cenou za SMS byly v Evropě normou (ČR: Eurotel/Paegas/Oskar, ceníky 2003–2005 na Měšec.cz, <https://www.mesec.cz/clanky/kolik-ted-stoji-smsky>) | ✅ |
| S60 | v USA texting přišel později a neomezené tarify dřív | **„texting caught on later" ✔**: mezioperátorské SMS v USA až od listopadu 2001 (AT&T Wireless první) a jaro 2002 (Cingular březen 2002): [RCR Wireless 2002-04-08](https://www.rcrwireless.com/20020408/archived-articles/interoperability-success-requires-cooperating-with-the-competition), [Light Reading 2002-02](https://www.lightreading.com/cable-technology/real-sms-comes-to-the-us); v UK mezisíťové SMS od 1999. **„unlimited plans arrived sooner" ❓**: nenašel jsem doklad, že neomezené SMS přišly v USA dřív než v Evropě (v USA kolem 2007–2008, v UK v balících od poloviny dekády); a „sooner" nemá jasné srovnání. Doložitelná americká zvláštnost je jiná: **platil i příjemce** („10 cents per message **sent or received**", Kohl 2008) | ❓ |
| S61–S63 | stejná aritmetika téměř všude; malá data prodaná jako zvláštní služba, miliardykrát denně | viz S04, S05 (2010 ≈ 16,7 mld./den) | ✅ |
| S64 | pro operátory jedna z nejziskovějších věcí, jaké kdy prodávali | In-Stat: SMS „the **most profitable** value-added data service" ([The Media Leader](https://uk.themedialeader.com/text-messaging-remains-most-profitable-mobile-data-service/)); „messaging still cash cow for operators" ([Fierce](https://www.fierce-network.com/europe/messaging-still-cash-cow-for-operators)); SMS tržby 2010 **114,6 mld. USD** (Portio, přes Wikipedii *SMS*). ITU 2010 při 0,07 USD/SMS: 14 000 USD za sekundu. „One of the most profitable things they had ever sold" je superlativ, ale hedgovaný („one of") a v rámci operátorů | ✅ |

## S65–S69 Webové brány

| | tvrzení | ověření | |
|---|---|---|---|
| S66 | někteří operátoři nabízeli SMS zdarma ze svých webů | ČR: Eurotel (do 17. 3. 2003 bez omezení, pak 60 znaků + 99 znaků reklamy), Oskar, Paegas (T-Mobile bránu zpoplatnil), Vodafone CZ s ověřovacím kódem 2006; v zahraničí např. orange.net (30 SMS/měsíc). [Novinky.cz 2003-03-11](https://www.novinky.cz/clanek/internet-a-pc-co-noveho-u-operatoru-eurotel-omezuje-sms-z-internetu-251813), [Lupa 2003-10-22](https://www.lupa.cz/clanky/sms-zdarma-podruhe/), [Lupa: ověřovací kód Vodafonu](https://www.lupa.cz/clanky/uzivatele-si-stezuji-na-overovaci-kod-sms-brany-vodafonu/). **Bonus:** Eurotel v roce 2002 odeslal přes 2 mld. SMS, z toho **278 mil. přes bezplatné internetové brány** (= 13,9 %) | ✅ |
| S67–S68 | programátoři si všimli; vznikly aplikace, které posílaly SMS z počítače přes brány operátorů | program **Gatekeeper** (běží na PC, „dosud tento program odesílal SMS zprávy skrze veřejné SMS brány příslušných operátorů", [Lupa: Jak funguje Mobilem.cz](https://www.lupa.cz/clanky/jak-funguje-mobilem-cz/)); operátoři kvůli automatům zaváděli opisovací kódy (Vodafone 2006: kód nesmí být čitelný „automatickým čtečkám") | ✅ |
| S69 | placená služba byla někdy zdarma o okno vedle | ✔ | ✅ |

## S70–S81 MMS

| | tvrzení | ověření | |
|---|---|---|---|
| S72 | MMS, Multimedia Messaging Service | 3GPP TS 22.140/23.140, OMA MMS | ✅ |
| S73 | obrázky, zvuk, krátká videa, delší text | OMA MMS CONF 1.3, tab. 1: třídy Text, Image Basic/Rich, Video Basic/Rich | ✅ |
| S74–S76 | MMS necestuje jako SMS: napřed přijde malá skrytá zpráva „čeká na tebe obrázek", pak se telefon připojí a stáhne ho | MMSC pošle **M-Notification.ind** jako WAP Push (v GSM běžně přes SMS), s URL zprávy; klient ji stáhne WSP/HTTP GET (**M-Retrieve.conf**) přes paketová data (OMA MMS Encapsulation, kap. 6.3; 3GPP TS 23.140; [NowSMS](https://nowsms.com/doc/submitting-sms-messages/sending-mms-notifications-and-content)). Notifikaci uživatel nevidí, zpracuje ji MMS klient ✔ | ✅ |
| S77–S78 | proto MMS potřebovala mobilní data a správné nastavení od operátora | APN, URL MMSC, WAP proxy — konfigurace OTA nebo ručně (OMA MMS CONF 1.3 zmiňuje konfiguraci „in particular via OTA") | ✅ |
| S79 | limity velikosti mačkaly fotky do rozmazaného obdélníčku | OMA MMS CONF 1.3, tab. 1: **Image Basic 30 kB / 160×120**, **Image Rich 100 kB / 640×480**, Video Rich 300 kB; Megapixel 300 nebo 600 kB (příl. D). Klient/MMSC zmenšuje rozlišení a kvalitu, když zpráva přesáhne 30/100/300 kB (kap. 9.3) | ✅ |
| S80 | často drahá a někdy prostě nedorazila | ceny MMS řádově násobek SMS; nedoručení při chybějícím nastavení / mezioperátorském propojení — obecně známé, nijak kvantifikováno | 💬 |
| S81 | MMS jako „neohrabaný teenager" | metafora | 💬 |

## S82–S89 Internet v telefonu

| | tvrzení | ověření | |
|---|---|---|---|
| S83–S84 | s datovým připojením zpráva nepotřebuje službu operátora, jede jako běžná data | OTT messaging | ✅ |
| S85 | WhatsApp a Messenger posílaly texty, obrázky, hlasové zprávy a videa stejně | WhatsApp 2009, Messenger 2011; obojí přes IP | ✅ |
| S86–S88 | ekonomika se obrátila; tisíce zpráv jsou zaokrouhlovací chyba datového tarifu | textová zpráva v aplikaci má jednotky kB; 1 000 zpráv × ~1 kB ≈ 1 MB | ✅ |
| S89 | zlatý důl nevyschl, jen ho obešli | Informa: za 2012 **chatovací aplikace 19 mld. zpráv/den vs. SMS 17,6 mld./den** — první předstižení ([The Register 2013-04-29](https://www.theregister.com/2013/04/29/sms_im/); [TechRadar](https://www.techradar.com/news/phone-and-communications/mobile-phones/beginning-of-the-end-for-sms-as-whatsapp-and-co-take-over-1147661)). Tržby SMS ale **klesaly** (Ovum: >15 mld. £ ztraceno v 2012; Indie −94 % 2010–2022, Hindustan Times 2023) — „didn't run dry" je obraz pro to, že SMS jako kanál existuje dál (S90+), ne že tržby vydržely | ✅ 💬 |

## S90–S96 SMS přežívá

| | tvrzení | ověření | |
|---|---|---|---|
| S90–S93 | bez Wi-Fi a mobilních dat, jen se signálem SMS pořád funguje | SMS nepotřebuje datové spojení uživatele (v 2G/3G CS doména, ve 4G SMS over SGs nebo IMS — i s vypnutými daty) | ✅ |
| S94 | proto nese věci, které nemůžou čekat na dobré připojení | ✔ | ✅ |
| S95 | přihlašovací kódy, upozornění z banky, **nouzová varování** | kódy a bankovní upozornění ✔. **Nouzová varování** jdou většinou přes **Cell Broadcast** (EU-Alert, NL-Alert, UK Emergency Alerts, USA WEA), což není SMS — jiná služba GSM (TS 23.041), bez SMSC, bez adresáta. **Location-based SMS** ale existuje jako druhá uznaná cesta: EECC čl. 110(1) a BEREC BoR (20) 115 hodnotí právě „Cell Broadcast and Location-based SMS" ([BEREC](https://berec.europa.eu/sites/default/files/files/document_register_store/2020/6/BoR_%2820%29_115_BEREC_Guidelines_on_PWS.pdf); [EENA](https://eena.org/press-releases/the-majority-of-eu-countries-are-still-not-complying-with-the-eecc/)). Tvrzení tedy není nepravdivé, ale divák si pod „emergency warning" vybaví pípající celoplošné varování, které je Cell Broadcast | 🔸 |
| S96 | občas „Call me." | 💬 | 💬 |

## S97–S109 RCS

| | tvrzení | ověření | |
|---|---|---|---|
| S97–S98 | průmysl zkusil dát systému moderního nástupce: RCS, Rich Communication Services | GSMA RCS (od 2008), Universal Profile od 2016 | ✅ |
| S99 | indikátor psaní, potvrzení přečtení, skupinové chaty, pořádné fotky, reakce | GSMA Universal Profile; **reakce** byly napřed rozšířením Googlu, do standardu přišly s **UP 2.7 (červen 2024)** ([SamMobile](https://www.sammobile.com/?p=16587710), [Tom's Guide](https://www.tomsguide.com/phones/major-rcs-update-will-improve-messaging-between-iphone-and-android-users-heres-how)). V praxi je RCS uživatelé měli od ~2020 | ✅ 💬 |
| S100 | v podstatě vše, co lidé měli z aplikací léta | ✔ | ✅ |
| S101 | RCS potřebuje internetové připojení | běží přes IP (mobilní data nebo Wi-Fi) | ✅ |
| S102 | když data nejsou, telefon spadne zpět na SMS | Google Messages / iOS: odeslat jako SMS/MMS, když RCS není dostupné | ✅ |
| S103 | zpráva navržená v 80. letech, vtěsnaná do mezer signalizačního kanálu, 160 znaků | 1985 (Oslo), první návrh GSM 03.40 listopad 1987 (Wikipedie *SMS*) | ✅ |
| S104 | stala se jednou z nejziskovějších služeb, jaké kdy kdo prodal | viz S64 — doklad je v rámci **operátorů** („most profitable data service"), ne napříč všemi odvětvími. „Ever sold" bez podmětu zní jako superlativ přes celé hospodářství | 🔸 |
| S105 | internet ji obešel | viz S89 | ✅ |
| S106 | pořád je to to, po čem telefon sáhne, když nic jiného nejde | viz S102 | ✅ |
| S107–S108 | nejznámější telefon světa RCS léta neuměl | iPhone podporuje RCS od **iOS 18, září 2024** ([PhoneArena](https://www.phonearena.com/news/rcs-message-reactions-from-android-are-finally-being-displayed-properly-on-ios_id164586); Wikipedie *SMS*, odkaz CNET 2024). Universal Profile od 2016 → „for years" ✔ | ✅ |
| S109–S110 | odkaz na další video, otázka do komentářů | 💬 | 💬 |

## Souhrn nálezů

Ověřeno **81 řádků tvrzení** (skupinové řádky jako S14–S15 počítány
jako jeden). OK nebo 💬 72, k opravě 9:

| scéna | závěr | problém | návrh znění |
|---|---|---|---|
| **S24** | ✏️ OPRAVIT | 160 nebyla náhodná shoda dvou nezávislých čísel: byla **cílem** a místo pro text se zvětšovalo, až se vešla (napřed 128 B ≈ 146 znaků, pak 140 B = 160) | „It wasn't a coincidence. / The first design had room / for only about 146 characters. / So the engineers stretched it / until 160 fitted." — kratší varianta: „The engineer picked the number. / The network was stretched / until it fitted." |
| **S27** | 🔸 ZMÍRNIT | turecké ş má od Release 8 (2008) národní 7bitovou tabulku (TS 23.038 A.3.1), takže S28 pro něj neplatí vždy | vyměnit za jazyk bez národní tabulky: „But not the Czech ř. / Not the Polish ł, / the Hungarian ő, / or the Cyrillic alphabet." (ő v tabulce není, ö ano — hezký kontrast). Alternativa: „the Romanian ș" |
| **S33** | 🔸 ZMÍRNIT | Hillebrand počítal se zprávami mezi lidmi (S10–S13, elektrikář v autě); nedoložené je jen to, že by někdo čekal masové chatování | „And nobody expected it / to become the way people talk." |
| **S34** | 🔸 ZMÍRNIT | „Maybe for pagers" zní, jako by se posílalo na pagery; zdroj říká „portable paging system" | „It was a small extra / built into the network. / Something like a pager: / a short note for someone on the move." |
| **S50** | ✏️ OPRAVIT (drobnost) | klávesy 7 (PQRS) a 9 (WXYZ) mají čtyři písmena | „And on a keypad / with three or four letters on each key, / people got astonishingly fast." |
| **S55** | 🔸 ZMÍRNIT (drobnost) | zpráva má **nejvýš** 140 bajtů | „And each message was / at most a hundred and forty bytes." |
| **S60** | ❓ NEDOLOŽENO | „unlimited plans arrived sooner" — nenašel jsem doklad a srovnání je nejasné; doložená zvláštnost USA je, že **platil i příjemce** | „In the United States, texting caught on later, / and you often paid to receive a text, too." |
| **S95** | 🔸 ZMÍRNIT | nouzová varování jdou většinou přes Cell Broadcast, ne SMS (location-based SMS existuje, ale menšinově) | „Login codes. / Bank alerts. / Delivery updates." — nebo ponechat a nepřidávat do obrazu celoplošné varování |
| **S104** | 🔸 ZMÍRNIT | superlativ doložený jen v rámci operátorů | „It became one of the most profitable / services operators ever sold." |

Drobné poznámky bez nutnosti opravy: S01 „early 2000s" — doložená 10c
cena je z roku 2005 (2008 už 20 c); S16–S17 „I've moved to another cell"
— v klidu telefon hlásí změnu oblasti, ne buňky; S89 „didn't run dry" —
tržby SMS ve skutečnosti padaly, obraz platí pro SMS jako kanál.

**Zapracováno do `script 0.2.md` (2026-10-31)**: všech devět návrhů
z tabulky v uvedeném znění (S24 delší varianta, S27 maďarské ő, S95
„Delivery updates"), navíc S102 „the phone can fall back". Čísla scén
beze změny.

**V0.3 (2026-10-31):** S104 je teď „It became a gold mine.“, metafora,
která odkazuje na S52–S64, a ne superlativ. Nález 🔸 u S104 tím odpadá,
doklad k zisku operátorů zůstává u S64.
