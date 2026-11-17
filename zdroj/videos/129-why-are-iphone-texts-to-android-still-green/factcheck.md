# 129 — fact check (scénář 0.1, 2026-10-31)

Scény podle `script.md`. **Čísla scén jsou přepočítaná na v0.4** (z v0.3 škrtnuty S61 a S63, od S64 vše −2), i ve starších dodatcích. Stav RCS/iMessage ověřen
k 2026-10-31. Závěr: **OK** doloženo · **ZMÍRNIT** jádro sedí, formulace
přestřelí · **OPRAVIT** neplatí, jak stojí · **NEDOLOŽENO** nepodařilo se
doložit · 💬 rétorika / zjednodušení (není faktické tvrzení, jen nesmí lhát).

Primární zdroje, ze kterých je většina dokladů:

- **Žaloba DOJ** *United States v. Apple Inc.*, 2:24-cv-04055 (D.N.J.),
  Document 1, podáno **2024-03-21**,
  <https://www.justice.gov/opa/media/1344546/dl?inline>, čteno přes
  `pdftotext -layout` (¶ 22–23, 83–93).
- **Epic Games v. Apple**, 4:20-cv-05640-YGR, Document 407 (Epic's Proposed
  Findings of Fact and Conclusions of Law), podáno **2021-04-08**, s. 14–15
  (¶ 57–58),
  <https://appliedantitrust.com/16_foreclosure/cases_private/epic_apple2020/1_ndcalif/epic_ndcalif_ffcl_epic_2021_04_08.pdf>.
- **Apple Support** „If your iPhone messages are green",
  <https://support.apple.com/en-us/105087>.
- **Apple Newsroom** 2026-05-11, „End-to-end encrypted RCS messaging begins
  rolling out today in beta",
  <https://www.apple.com/newsroom/2026/05/end-to-end-encrypted-rcs-messaging-begins-rolling-out-today-in-beta/>.

Článek WSJ (Tim Higgins, *Why Apple's iMessage Is Winning: Teens Dread the
Green Text Bubble*, 8.–9. 1. 2022) je za paywallem a WebFetch na wsj.com
nedosáhne; znění je proto **z doslovných citací ve třech nezávislých
textech** (Daring Fireball 2022-01-14, Outside the Beltway 2022-01-10,
The Loop 2022-01-10), ne z článku samotného.

---

## S01–S07 Háček

| | tvrzení | ověření | závěr |
|---|---|---|---|
| S01 | zpráva iPhone → iPhone je v modré bublině | iMessage = modrá; Apple Support 105087: zelená, když „that message was sent using RCS or MMS/SMS instead of iMessage" | OK |
| S02 | iPhone → Android je zelená | Apple Support 105087: zelená, když „The person that you sent the message to doesn't have an Apple device" | OK |
| S03 | stejná aplikace | obojí jde aplikací Messages | OK |
| S04 | léta s tím chodily rozmazaná videa a rozbité skupinové chaty | DOJ ¶ 90: „the conversation is not encrypted, videos are pixelated and grainy, and users cannot edit messages or see typing indicators"; skupiny viz S35 | OK |
| S05 | v roce 2024 se iPhone naučil tentýž moderní standard jako Android | RCS Universal Profile v iOS 18, vydán **2024-09-16**; Google Messages jede na RCS | OK |
| S06 | bubliny jsou pořád zelené | Apple Support 105087: „RCS or MMS/SMS" = zelená | OK |

## S08–S15 Zelená je původní

| | tvrzení | ověření | závěr |
|---|---|---|---|
| S08 | zelená nevznikla kvůli Androidu | Gruber, *Seeing Green* (2022-01-14, <https://daringfireball.net/2022/01/seeing_green>): „The color of SMS messages on iOS was green before iMessage was introduced, and remained green after." Android vyšel až 2008 | OK |
| S09 | iPhone 2007: každá textovka zelená | How-To Geek (<https://www.howtogeek.com/785247/>): v letech 2007–2011 „every chat bubble was green". **Výhrada:** zeleně se kreslily zprávy **odeslané**, přijaté byly šedé — snímek iPhone OS 1 jsem nedohledal, je to z paměti, ale shoduje se to s dnešním chováním (i dnes je modrá/zelená jen vlastní bublina). S01–S02 mluví taky z pohledu odesílatele, takže to divák pochopí; přesnější znění je volitelné | ZMÍRNIT (volitelné) |
| S10 | i mezi dvěma iPhony | do iOS 5 iPhone jinou cestu než SMS neměl | OK |
| S11 | modrá až 2011 s novou službou iMessage | iMessage ohlášen na WWDC 2011-06-06, vydán s **iOS 5, 2011-10-12** | OK |
| S12–S13 | zelená je originál, modrá výjimka | plyne z S09–S11 | OK 💬 |
| S14–S15 | barva popisuje cestu zprávy, ne telefon | Apple Support 105087: zelená i mezi dvěma iPhony, když „iMessage is turned off… or temporarily unavailable"; Gruber: „Messages doesn't render texts from Android green, per se — it renders all SMS messages as green." | OK |

**Návrh S09 (volitelný):**
```
When the iPhone launched in 2007,
every text you sent on it was green.
```

## S16–S32 Dvě cesty

| | tvrzení | ověření | závěr |
|---|---|---|---|
| S17–S18 | stará cesta = mobilní síť, SMS na text, MMS na obrázky a video | DOJ ¶ 83 a pozn. 1: „MMS is a companion protocol to SMS that allows for group messages and messages with basic [media]" | OK |
| S19 | mluví jimi každý telefon, protože je provozují operátoři, ne výrobci | DOJ ¶ 83: „all mobile phones can receive SMS messages". U MMS „every phone" neplatí doslova (první iPhone MMS neuměl do iPhone OS 3, 2009), ale jako obraz drží | OK 💬 |
| S20 | SMS pojme 160 znaků | GSM 03.38, 7bitová abeceda; s diakritikou/UCS-2 jen 70 — scénář o tom nemluví | OK |
| S21 | MMS video se zmáčkne pod limit operátora, „often well under a megabyte" | Telnyx (<https://support.telnyx.com/en/articles/4450150>): „Tier 1 Carriers (Verizon, T-Mobile, AT&T, Sprint): Up to 1 MB", tier 2 „Up to 600 KB", tier 3 „Up to 300 KB". Starší AT&T podmínky ~600 KB, Verizon v různých zdrojích 1,2–1,7 MB. U velkých operátorů je to tedy **kolem jednoho megabajtu**, „well under" platí jen u menších | ZMÍRNIT |
| S22–S23 | nová cesta = internet, iMessage posílá data přes servery Applu | iMessage jde přes Apple Push Notification service; DOJ ¶ 83–84 ho řadí mezi OTT („over the top") služby | OK |
| S24 | žádný operátor, „no size limits from the 1990s" | operátor ano. **Ale limit MMS není z 90. let** — MMS je standard z let 2001–2002 (3GPP/OMA, první komerční služby 2002); z 80./90. let je jen 160 znaků SMS | ZMÍRNIT |
| S25 | potvrzení o přečtení, indikátor psaní, fotky v plné kvalitě, funkční skupiny | DOJ ¶ 90 výčet chybějících funkcí u zelené; Epic FFCL ¶ 57 | OK |
| S26 | servery Applu mluví jen se zařízeními Applu | Epic FFCL ¶ 57: „If an iPhone user attempts to send a text message to the user of a non-Apple device… iMessage transmits the message as a standard cellular text (called an SMS)"; výjimka Beeper Mini viz S78–S79 | OK |
| S27–S28 | jinak spadne zpátky na starou cestu | totéž | OK |
| S29–S30 | modrá = nese Apple, zelená = nese síť | Apple Support 105087 | OK |

**Návrh S21:**
```
And an MMS video is squeezed
until it fits the operator's size limit,
often about a megabyte, or less.
```

**Návrh S24:**
```
No operator in the middle.
No size limits from the flip-phone era.
```

## S33–S44 Dopad v USA

| | tvrzení | ověření | závěr |
|---|---|---|---|
| S33–S34 | horší pro všechny v chatu | DOJ ¶ 90: „the experience of messaging friends and family who do not own iPhones is worse"; WSJ (cit. Gruber): „when an Android user is part of a group chat, the iPhone users see green bubbles rather than blue" | OK |
| S35 | jeden Android ve skupině iPhonů → celá skupina spadne na MMS | před RCS (iOS 18) ano: smíšená skupina je skupinové MMS (DOJ pozn. 1: MMS „allows for group messages"). WSJ: „No longer did her group chats work seamlessly with other peers" | OK |
| S36 | videa jako šmouha, reakce jako text „Liked an image." | video: DOJ ¶ 90 „pixelated and grainy". Reakce: Engadget / 9to5Google 2022-01-31 — Google Messages začal v r. 2022 rozpoznávat textové řetězce, které Messages posílá („Liked", „Loved", „Laughed at"…), a převádět je na emoji; předtím Android dostal popis typu „liked an image". Od 2022 tedy jen v jiných aplikacích než Google Messages — kontext „for years" to drží | OK |
| S37 | vypadalo to, že problém je telefon toho člověka | DOJ ¶ 90: „blame for 'breaking' chats… even though Apple, not the rival smartphone, is the cause" | OK |
| S38 | v USA z toho byla společenská věc | WSJ, DOJ ¶ 90 „social stigma, exclusion" | OK |
| S39 | 2022: WSJ psal, že američtí teenageři se zelené bubliny děsí | Tim Higgins, WSJ, 8. 1. 2022, titul *„Why Apple's iMessage Is Winning: Teens Dread the Green Text Bubble"*; „Teens and college students said they dread the ostracism that comes with a green text." | OK |
| S40 | někteří se cítili vynechaní ze skupinových chatů, někteří se kvůli tomu stali terčem posměchu | WSJ (cit. Outside the Beltway, Daring Fireball): „The social pressure is palpable, with some reporting being **ostracized or singled out** after switching away from iPhones"; podtitul *„Ew, that's gross."*; ve skupině se kdosi ozval „Who's green?". **„Left out of group chats" doslova v dostupných citacích není** — článek píše, že skupiny „didn't work seamlessly". Vyloučení z chatů tvrdí až žaloba DOJ (¶ 90: „social stigma, exclusion, and blame for 'breaking' chats"), ne WSJ. Věta přisuzuje WSJ víc, než doložitelně napsal | ZMÍRNIT |
| S41 | týž rok průzkum amerických teenagerů: 87 % má iPhone | Piper Sandler, *Taking Stock With Teens*, **podzim 2022**, 14 500 respondentů ze 47 států: „87 percent of teenagers surveyed own an iPhone" (MacRumors 2022-10-11). Stejné číslo měl i podzim 2021, které cituje WSJ. DOJ ¶ 90 uvádí 85 % „according to one survey" | OK |
| S42 | 2024: americká vláda zažalovala Apple za monopolizaci smartphonů | DOJ + 16 států, podáno 2024-03-21; žaloba na „monopolization of smartphone markets" (¶ 22: „over 70 percent in the performance smartphone market… over 65 percent for all smartphones" podle tržeb) | OK |
| S43 | zelená bublina je v žalobě | DOJ ¶ 90: „the text appears to the iPhone user as a green bubble and incorporates limited functionality… Many non-iPhone users also experience social stigma, exclusion, and blame for 'breaking' chats" | OK |
| S44 | nebyla to okrajová stížnost, v Americe na barvě záleželo | WSJ + DOJ + otázka na Cooka (S63) + kampaň Googlu „Get the Message" (2022) — čtyři nezávislé doklady | OK |

**Návrh S40** (drží se toho, co WSJ doslova napsal):
```
Some said they'd been singled out,
even ostracised, for switching.
```

## S45–S57 Zlom: jinde to nikoho nezajímalo — NOSNÁ TEZE

Shrnutí napřed: **teze je věrohodná a podložená nepřímo (objemy SMS, ceny,
tarify), ale přímý doklad příčiny „cena SMS → WhatsApp" jsem nenašel.**
Ani jedna mezinárodní studie, která by to měřila, ve výsledcích nebyla;
v odborném tisku se to opakuje jako obecné vysvětlení. Co doložit jde:

- **Američané posílali SMS o řád víc.** CTIA: v USA **2,19 bilionu**
  SMS odeslaných i přijatých v roce 2012 při **326,4 mil.** přípojkách
  (Computerworld,
  <https://www.computerworld.com/article/1397734/>) → **~560 za přípojku
  měsíčně** (odeslané + přijaté, tedy ~280 odeslaných). Německo: **59,8 mld.**
  odeslaných SMS v roce 2012 (Bundesnetzagentur, cit. Macwelt) při ~113 mil.
  SIM → **~44 odeslaných měsíčně**, tedy zhruba šestina. Ofcom (ICMR 2012,
  data 2011, cit. Mobile Europe 2012-12-14): USA „over 600 texts per person
  per month", další země kolem 200.
- **Neomezené SMS jsou v USA standard od roku 2012.** Verizon *Share
  Everything* (ohlášeno 2012-06-12, platí od 28. 6.): „unlimited voice
  minutes, unlimited text, video and picture messaging" ve **všech**
  tarifech; AT&T *Mobile Share* od 2012-08-23 totéž.
- **SMS v Evropě stály za kus.** Doložené jsou ceny **roamingových** SMS:
  průměr EU před regulací 2009 **€0,24–0,27**, po ní ~€0,10 (BEREC BoR (11) 51
  a BoR (12) 24). Domácí ceny po jednotlivých zemích jsem z primárního zdroje
  nedohledal; německé předplacené tarify kolem 2012 účtovaly řádově 9–19 ct
  za SMS (z paměti, nedoloženo).
- **Protipříklady:** Británie měla velké balíky SMS v paušálech (a přesto
  přešla na WhatsApp), Francie má neomezené SMS od Free Mobile (2012).
  **Indie** k tezi o ceně nesedí dobře — WhatsApp se tam masově rozšířil
  s levnými daty (Jio, 2016), a iPhone má v Indii jednotky procent, takže
  zelená bublina tam nemohla vzniknout z čistě demografických důvodů.

| | tvrzení | ověření | závěr |
|---|---|---|---|
| S46 | ve většině světa to skoro nikoho nezajímalo | žádný průzkum napříč zeměmi jsem nenašel. Nepřímo: iPhone má celosvětově zhruba čtvrtinu až třetinu smartphonů (StatCounter, řádově), kde vládne WhatsApp, fallback na SMS nenastává. NPR (2024-03-28) i Android Authority to popisují jako americký jev. „Almost nobody cared" je ale tvrzení o lidech, které změřit nejde | ZMÍRNIT |
| S47 | v Německu, Brazílii nebo Indii nevědí, o čem je řeč | WhatsApp: Německo — 76 % obyvatel ho používá denně (ARD/ZDF-Onlinestudie 2019); Brazílie — přes 95 % uživatelů internetu (Ilumeo/NovaSB); Indie — přes 500 mil. uživatelů (Meta). Výběr zemí drží, „may get a blank look" je dost opatrné | OK |
| S48 | důvod sahá k ceně textovky | viz shrnutí: věrohodné, ale jen **jeden** z důvodů (dále cena MMS, přeshraniční zprávy, nízký podíl iPhonu, u Indie levná data) | ZMÍRNIT |
| S49 | ve velké části Evropy se SMS platily po kusech | často ano (předplacené karty, roaming), ale ne všude (britské balíky, francouzské neomezené SMS) | ZMÍRNIT |
| S50–S51 | se smartphony lidé přešli na aplikace přes data, hlavně WhatsApp | Bundesnetzagentur jako hlavní příčinu propadu SMS (59,8 → 37,9 mld., 2012 → 2013, −37 %) jmenuje messengery, především WhatsApp (cit. Macwelt, Statista) | OK |
| S52–S53 | WhatsApp vypadá na iPhonu i Androidu stejně, žádná modrá, zelená ani fallback | WhatsApp na SMS nepřepadá; barvu bubliny neurčuje druh telefonu protistrany | OK |
| S54 | v USA bylo psaní SMS levné a často neomezené | Verizon/AT&T 2012 (viz výš), objem ~560 SMS na přípojku měsíčně | OK |
| S55 | nebyl důvod opouštět vestavěnou aplikaci | z S54 plyne; úsudek | OK 💬 |
| S56 | Američané psali dál a vestavěná aplikace na **většině** jejich telefonů byla od Applu | iPhone přesáhl **50 % používaných smartphonů v USA až v Q4 2021** (Counterpoint, 2022-04-25) / ve čtvrtletí do června 2022 (Counterpoint přes FT, 2022-09-02). V letech 2011–2020, kdy se zelená bublina stala „social thing", měl většinu Android. Věta v minulém čase tvrdí většinu, která tehdy nebyla. Mezi teenagery ano (70–87 %, WSJ/Piper Sandler) | OPRAVIT |
| S57 | problém zelené bubliny žil hlavně tam, kde byla SMS levná | závěr bloku; „mostly" drží, ale skutečnou podmínkou je **levná SMS A vysoký podíl iPhonu** | OK 💬 |

**Návrhy S46–S56:**
```
<!-- S46 -->
In most of the world,
it barely registered.

<!-- S48 -->
And a big part of the reason
goes back to the price of a text message.

<!-- S49 -->
In much of Europe,
texts often cost money, one by one.

<!-- S56 -->
Americans kept texting,
and more and more of them
did it on an iPhone.
```

(Kdyby S56 chtěl zachovat pointu „built-in app was Apple's", jde to
přes teenagery, kde je to doložené: *„and among teenagers, / that app was
almost always Apple's."*)

## S58–S64 Proč Apple nedal iMessage na Android

| | tvrzení | ověření | závěr |
|---|---|---|---|
| S59 | uvnitř Applu to lidé navrhovali | Epic FFCL ¶ 58b: Cue vypověděl, že Apple „could have made a version on Android that worked with iOS"; Cue v e-mailu z dubna 2013: „We really need to bring iMessage to Android" (výpověď Cue, cit. 9to5Mac 2021-04-27) | OK |
| S60 | e-maily ze soudního sporu ukazují debatu v roce 2013 | Epic FFCL ¶ 58a: „As early as 2013, Apple decided not to develop a version of iMessage for the Android OS. (Cue Dep. 92:22-93:1.)"; e-mail Federighiho PX407 | OK |
| S61 | jeden manažer: iMessage na Androidu by iPhonovým rodinám usnadnil dát dětem Android | Federighi (SVP Software Engineering), 2013, PX407 at '122: „**iMessage on Android would simply serve to remove [an] obstacle to iPhone families giving their kids Android phones**" (Epic FFCL ¶ 58c; totéž DOJ ¶ 91). Parafráze věrná | OK |
| S63 (v0.4 ŠKRT) | 2016 jiný řekl, že by to Applu víc uškodilo než pomohlo | Schiller, 2016, PX416 at '610: „**moving iMessage to Android will hurt us more than help us, this email illustrates why**" — reakce na e-mail bývalého zaměstnance, že „the #1 most difficult [reason] to leave the Apple universe app is iMessage… iMessage amounts to serious lock-in" (Epic FFCL ¶ 58e). DOJ ¶ 91: „In March 2016… forwarded an email to CEO Tim Cook". (The Loop chybně datuje Schillerův e-mail do 2013 — primární zdroj říká 2016.) | OK |
| S62 | iMessage nebyl jen funkce, byl to důvod zůstat | „iMessage amounts to serious lock-in" (týž e-mail); Epic FFCL ¶ 58: „Apple has recognized the power that iMessage has to attract and keep users within its ecosystem" | OK |
| S63 | 2022 se někdo zeptal šéfa Applu, jak poslat videa na matčin Android | Code Conference (Vox Media), 2022-09-07; tazatel LiQuan Hunt. DOJ ¶ 92: „Mr. Cook was asked whether Apple would **fix** iPhone-to-Android messaging. 'It's tough,' the questioner implored Mr. Cook, 'not to make it personal but I can't send my mom certain videos.'" Ptal se tedy, **jestli to Apple opraví** (podporou RCS), ne jak videa poslat | ZMÍRNIT |
| S64 | odpověď: „Buy your mom an iPhone." | DOJ ¶ 92: „Mr. Cook's response? 'Buy your mom an iPhone.'"; NPR 2022-09-08 shodně. Doslovné | OK |

**Návrh S63:**
```
And in 2022, when someone told Apple's CEO
he couldn't send his mother certain videos,
because she had an Android phone,
```

## S65–S72 Google a RCS

| | tvrzení | ověření | závěr |
|---|---|---|---|
| S66 | Android neměl jednu odpověď na iMessage | viz S67 | OK |
| S67 | Google spouštěl aplikaci za aplikací: Talk, Hangouts, Allo | Google Talk 2005-08; Hangouts 2013-05; Allo 2016-09 (vedle toho Duo, Messages, Chat) | OK |
| S68 | a jednu po druhé rušil | Talk nahrazen Hangouts 2013, definitivně vypnut 2022; Allo vypnuto **2019-03-12** (TechSpot; ohlášeno 2018-12-05, 9to5Google); Hangouts vypnuty **listopad 2022** (Android Authority 2022-11-02) | OK |
| S69 | skutečným nástupcem SMS měl být RCS | GSMA RCS; DOJ ¶ 89: RCS „combines aspects of SMS and OTT" | OK |
| S70 | standard mobilního průmyslu z konce 2000s | RCS Initiative operátorů a výrobců 2007, pod GSMA od 2008, první specifikace 2008-09-15; Universal Profile 2016-11-16 | OK |
| S71 | RCS záviselo na operátorech a mnozí ho léta nezapnuli | GSMA/Google ohlásili společný Universal Profile až v únoru 2016, aby operátoři konečně nasazovali jednotně (GSMA newsroom); první nasazení UP Sprint 2016-11 | OK |
| S72 | nakonec ho Google z velké části provozoval na vlastních serverech | Google koupil Jibe Mobile 2015 a nabídl operátorům hostované RCS; od 2019 Google Messages zapíná „chat features" přes Jibe i bez operátora (UK, Francie, USA 2019-11), američtí operátoři v roce 2021 přešli na Google Messages / Jibe | OK |

## S73–S83 Obrat 2023–2026

| | tvrzení | ověření | závěr |
|---|---|---|---|
| S73–S74 | v listopadu 2023 Apple oznámil podporu RCS | prohlášení pro 9to5Mac **2023-11-16**: „Later next year, we will be adding support for RCS Universal Profile, the standard currently published by the GSM Association." (Droid Life, Light Reading, The National 2023-11-16/17) | OK |
| S75 | Apple neřekl proč | **Apple důvod uvedl:** „We believe the RCS Universal Profile will offer a better interoperability experience when compared to SMS or MMS." Neřekl jen, **proč zrovna teď** | OPRAVIT |
| S76 | načasování sedělo s evropským vyšetřováním | Evropská komise zahájila v září 2023 (spolu s označením gatekeeperů 2023-09-06) šetření, zda iMessage označit za základní platformní službu podle DMA; 2024-02-13 rozhodla, že ne (iPhone in Canada 2024-02-18). Je to šetření podle **DMA**, ne klasická soutěžní věc — „competition investigation" je volné, ale přijatelné. Formulováno jako souvislost, ne příčina | OK (drobnost) |
| S77 | jiní ukazovali na Čínu, kde se nové telefony tlačily k podpoře RCS | MIIT v červenci 2023 zveřejnilo návrh, podle kterého by nově certifikované 5G telefony musely po šestiměsíčním přechodném období podporovat „5G messaging", tedy RCS (9to5Google 2024-02-16, IT之家). Hypotézu zveřejnil Gruber v únoru 2024 a sám řekl, že ji jistě vědět nemůže. „Others pointed to" ji správně uvádí jako domněnku; „were being pushed" sedí na **návrh** | OK |
| S78 | o pár týdnů později Beeper Mini umožnil Androidu posílat skutečné iMessage | spuštěn úterý **2023-12-05** (19 dní po ohlášení RCS); protokol iMessage zpětně analyzovaný, připojení přímo na servery Applu (TechCrunch, Tom's Guide) | OK |
| S79 | Apple ho během dnů odstřihl | **2023-12-08**, tři dny po spuštění; Apple: „significant risks to user security and privacy" (TechCrunch 2023-12-08). Beeper pak obnovil provoz přes Apple ID, Apple blokoval znovu, projekt skončil v prosinci 2023 | OK |
| S80 | modrá zůstala Applu, 2024 dorazil RCS | iOS 18, 2024-09-16 | OK |
| S81 | iPhony a Androidy konečně sdílely potvrzení o přečtení, indikátor psaní, fotky v pořádné kvalitě | výčet funkcí RCS v iOS 18 (Apple, WWDC 2024); jen u operátorů, kteří RCS na iPhonu podporují | OK |
| S82 | 2026 začali Apple a Google zavádět šifrování, **pořád v betě** a jen u některých operátorů | Apple Newsroom **2026-05-11**: „begins rolling out today in beta for iPhone users running **iOS 26.5** with **supported carriers** and Android users on the latest version of Google Messages"; zámek v chatu; Universal Profile 3.0 (MLS). Ke 2026-10-31 jsem **nenašel ani zprávu, že beta skončila, ani že pořád běží** — v listopadu 2026 už může být „still in beta" zastaralé (iOS 27 vyšel v září) | ZMÍRNIT |
| S83 | cesta mezi nimi je konečně vydlážděná | rétorika; s výhradou operátorů a bety přijatelná | OK 💬 |

**Návrh S75:**
```
Apple didn't say why now.
```

**Návrh S82** (platí, ať beta skončila, nebo ne):
```
In 2026, Apple and Google
began rolling out encryption
for those messages,
first as a beta,
and only with some operators.
```

## S84–S90 Odpověď na titul

| | tvrzení | ověření | závěr |
|---|---|---|---|
| S86 | RCS není iMessage | Apple 2023-11-16: RCS „will work alongside iMessage, which will continue to be the best and most secure messaging experience for Apple users" | OK |
| S87 | je to novější lepší cesta, ale pořád cesta, kterou dává mobilní síť | RCS na iPhonu jde jen u operátorů, kteří ho podporují (Apple Newsroom „supported carriers"); že ho často provozuje Google jménem operátora, říká už S72 — nekoliduje to | OK 💬 |
| S88 | modrá je vyhrazená zprávám, které nese Apple | Apple Support 105087: zelená = „RCS or MMS/SMS instead of iMessage" | OK |
| S86–S90 | RCS zprávy na iPhonu jsou opravdu zelené (ne jiný odstín) | Apple Support 105087 je řadí do zelené spolu s SMS/MMS; jinou barvu ani odstín Apple nezavedl — RCS konverzace se liší jen popiskem „RCS" v poli pro psaní a od iOS 26.5 zámkem u šifrovaných | OK |
| S89–S90 | barva nikdy neznamenala „tenhle telefon je horší", znamenala „tahle zpráva není naše" | interpretace; s faktem (barva = transport) souhlasí | OK 💬 |

## S91–S96 Pointa

| | tvrzení | ověření | závěr |
|---|---|---|---|
| S92 | SMS patřila operátorům, a proto fungovala se všemi | DOJ ¶ 83: „all mobile phones can receive SMS messages" | OK |
| S93 | messengery, které ji nahradily, patří firmám, co dělají telefony a aplikace | iMessage (Apple), WhatsApp (Meta), Google Messages (Google). RCS je sice otevřený standard, ale S93 mluví o messengerech | OK 💬 |
| S94 | firma, která vlastní cestu, rozhoduje, kdo na ni smí | u iMessage doloženo činem (Beeper Mini, S79) i e-maily (S61 a Schillerův e-mail ze škrtnuté S63 v0.3). Obecně: v EU od 2024 musí WhatsApp a Messenger podle DMA nabízet interoperabilitu, takže „gets to decide" neplatí bez výjimky — iMessage ale označen nebyl, takže na příkladu videa věta platí. Fér | OK |
| S95 | a jakou máš barvu, když na ni smíš | barvu volí Apple pro vše, co nenese sám (S88) | OK 💬 |
| S96 | otázka do komentářů | není tvrzení | — |

---

## Shrnutí

**76 ověřených tvrzení** (řádky tabulek bez S96 a bez souhrnného řádku
S86–S90), z toho:

| závěr | počet | scény |
|---|---|---|
| OK | 65 | |
| ZMÍRNIT | 9 | S09 (volitelné), S21, S24, S40, S46, S48, S49, S63, S82 |
| OPRAVIT | 2 | **S56** (iPhone neměl v USA většinu, dokud se zelená bublina stávala problémem — až od 2021/22), **S75** (Apple důvod uvedl, neřekl jen „proč teď") |

**Nedoloženo zůstává** přímá příčinná vazba „drahá SMS → WhatsApp"
(S48–S49): podporují ji nepřímo objemy SMS a tarify, studii jsem nenašel.
Proto ZMÍRNIT, ne škrtat. Bez primárního zdroje jsou taky domácí ceny SMS
v Evropě po zemích a jedna drobnost z paměti (S09: přijaté bubliny v iPhone
OS 1 šedé).

Nosná teze bloku S45–S57 **stojí**, ale ne na jediné příčině: zelená
bublina potřebovala **levnou SMS a zároveň hodně iPhonů v okolí**. V USA
platilo obojí (teenageři 87 %), v Evropě ani jedno, v Indii zvlášť to druhé.
Navržená znění S48, S49 a S56 to drží bez přepsání oblouku.

## Dodatek: změny ve v0.3 (zpětná vazba `zpetna vazba 0.2.txt`, 2026-10-31)

Nové nebo přeformulované věty, ověřené proti zdrojům výš:

| | nové znění | ověření | závěr |
|---|---|---|---|
| S19 | „practically every phone… they belong to the mobile network" | DOJ ¶ 83 „all mobile phones can receive SMS"; „practically" pokryje MMS (první iPhone do 2009) | OK |
| S27–S28 | minulý čas „couldn't… fell back" | od iOS 18 jde iPhone → Android přes RCS, pokud ho operátor podporuje; přítomný čas tvrdil, že to platí dodnes | OK |
| S30 | „Green means someone else did." | Apple Support 105087: zelená = „RCS or MMS/SMS instead of iMessage". Původní „the mobile network did" kolidovalo s S72 (RCS často provozuje Google) | OK |
| S35–S36 | minulý čas „dropped… arrived" | smíšená skupina jde od iOS 18 přes RCS; MMS byl stav před 2024 | OK |
| S57 | „took hold where texting was cheap and iPhones were common" | dvě podmínky z S54 a S56 (viz 💬 u S57 výš) | OK |
| S87 | „a newer, better road, but it isn't Apple's road" | Apple 2023-11-16: RCS „alongside iMessage"; standard GSMA, ne Applu | OK |

**Nepřevzato:** S21 (číslo ~1 MB je doložené Telnyxem a do 1:10 se má
platit konkrétním číslem), S47 (už opatrné „may get a blank look"; návrh
by zopakoval S46), S82 („both carriers" je nepřesné, protože Apple
podmiňuje šifrování operátorem jen na straně iPhonu, u Androidu verzí Google
Messages; „still in beta" může ke 2026-11 být zastaralé), S76–S79 (už
formulováno opatrně, Beeper je chronologicky až po ohlášení).

## Dodatek: škrty ve v0.4 (zpětná vazba `zpetna vazba 0.3.txt`, 2026-10-31)

- Škrtnuta S61 v0.3 *„And they show the worry."* (přechod) a S63 v0.3
  (Schiller 2016). Doklad S63 v tabulce zůstává, ve videu už není.
- S61 (dříve S62) začíná *„But one executive argued"*. Je to obrat bez
  nového tvrzení.
- S70 (dříve S72) zkrácena na *„A standard designed by the mobile industry
  in the late 2000s."*, doklad beze změny.
- Zpětná vazba připisuje *„Buy your mom an iPhone"* Federighimu. Řekl to
  **Tim Cook** (DOJ ¶ 92), scénář má správně „Apple's CEO".

## Poznámka k S19 a S92 (třetí zpětná vazba, 2026-10-31)

| | tvrzení | ověření | závěr |
|---|---|---|---|
| S19 | SMS/MMS „belong to the mobile network, not to the phone makers" | Standardy SMS/MMS vlastní standardizační orgány (ETSI/3GPP, MMS také OMA), operátoři je nevlastní. Operátoři ale **provozují** SMSC/MMSC a za zprávy účtují (DOJ ¶ 83). Věta je zkratka pro kontrast s platformami, které vlastní jedna firma (S93–S94). Výrobce telefonu na SMS opravdu nemá vliv. | OK 💬 |
| S92 | „SMS belonged to the operators, and so it worked with everyone" | Je to tatáž zkratka, kterou nese pointa. Interoperabilitu zajišťuje otevřený standard a propojení operátorů. | OK 💬 |
