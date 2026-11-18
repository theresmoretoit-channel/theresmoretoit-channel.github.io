# Lokalizované názvy a popisy — 076

Čte `tools/lokalizace.py` a nahrává přes `videos.update(part="localizations")`.
Anglický titul a popis jsou v `youtube.md` a posílají se zpátky beze změny.

**Pořadí sekcí je podle YouTube Studia** (bajtově podle ČESKÉHO názvu jazyka).

## Co se NEPŘEKLÁDÁ

- řádky s atribucí snímků (názvy souborů a autoři: SRI International, Michael Hicks,
  The wub, Al Lemos, Marcin Wichary, Timothy Colegrove, Sailko, Wikimedia Commons)
  a řádek `Licences: …`
- **věta „Used with permission from Microsoft."** — podmínka Microsoftu pro
  screenshoty (`art/PUVOD.md`), doslova v každém jazyce, protože lokalizovaný
  popis nahrazuje anglický
- časy kapitol na vteřinu (stejné jako v `youtube.md`; **po dalším běhu
  `tts.py` přepočítat v obou souborech**)
- tagy (YouTube je per-jazyk nemá)

## Kontrola čísel

Čísla v popisu: 1985 (první Windows), 1968 (Engelbart), 1970s (Alto), 1981 (Star),
spor šest let, patnáct kapitol se stejnými časy jako v `youtube.md`. Popis
nikoho přímo neoslovuje, takže registr nerozhoduje. **Windows je v jednotném
čísle** tam, kde jazyk má volbu (jako titulky). Věta o titulcích a americké
stopě je kanonické znění z `docs/zverejneni.md`.

**Codex 2026-10-01:** zapracováno 21 nálezů — průkopníci místo jejich počítačů
na stolech (cs, pl, vi; opraveno i v angličtině na „none of their machines“
a ve všech jazycích), it „quasi tutti“ místo „většina“, id „Para klon“ (osoby),
„kruh/smyčka se roztočí“ (fr, pl, pt-BR, uk, sv, vi). **Nepřijato:** cs
„smyčka … roztočí“ — drží znění schválených titulků (S80, kapitola „Smyčka“).


## suomi (`fi`)

```
Miten Windows voitti, vaikka se ei keksinyt graafista käyttöliittymää?
```

```
Ikkunat, kuvakkeet, valikot, hiiri. Useimmille ihmisille tietokone yksinkertaisesti näyttää tältä, ja useimmat heistä tutustuivat siihen Microsoftin kautta. Mutta kun ensimmäinen Windows ilmestyi vuonna 1985, lähes mikään siitä ei ollut uutta.

Douglas Engelbart esitteli hiirellä ohjattavaa tietokonetta vuonna 1968. Xerox PARC rakensi Alton 1970-luvulla ja toi Starin myyntiin vuonna 1981. Apple toi markkinoille Lisan ja sitten Macintoshin. Kaikki ne ehtivät ennen Microsoftia, eikä yksikään niiden koneista päätynyt useimmille maailman työpöydille.

Tämä video seuraa, mitä siinä välissä tapahtui: sopimus IBM:n kanssa, yhteensopivien PC:iden aalto, kuusi vuotta kestänyt oikeusjuttu ja kierre, jota on hyvin vaikea katkaista, kun se on kerran päässyt vauhtiin.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/how-did-windows-win-without-inventing-the-gui/

LUVUT
00:00 Mitä Windows ei keksinyt
00:36 Engelbartin esittely
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: Lisa ja Mac
04:01 Koukku
04:22 IBM tarvitsee käyttöjärjestelmän
04:56 Sopimuksen yksityiskohta
05:17 Kloonit
06:21 Windows 1.0 ja 2.0
06:50 Apple vastaan Microsoft
07:25 Windows 3.0
08:08 Kierre
08:35 Windows 95
08:57 Miten Windows voitti

KUVALÄHTEET
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Kaikki muut arkistokuvat ovat public domainia.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

WINDOWS-KUVAKAAPPAUKSET
Windows 1.01, Windows/386 2.01, Windows 3.0 ja Windows 95, tallennettu PCjs-emulaattorissa (pcjs.org).
Used with permission from Microsoft.
```

## français (`fr`)

```
Comment Windows a-t-il gagné sans inventer l'interface graphique ?
```

```
Des fenêtres, des icônes, des menus, une souris. Pour la plupart des gens, c'est tout simplement à ça que ressemble un ordinateur, et la plupart l'ont découvert grâce à Microsoft. Pourtant, quand le premier Windows est sorti en 1985, presque rien de tout cela n'était nouveau.

Douglas Engelbart a présenté un ordinateur piloté à la souris en 1968. Xerox PARC a construit l'Alto dans les années 1970 et commercialisé le Star en 1981. Apple a lancé le Lisa, puis le Macintosh. Tous sont arrivés avant Microsoft, et aucune de leurs machines n'a fini sur la plupart des bureaux du monde.

Cette vidéo raconte ce qui s'est passé entre-temps : un contrat avec IBM, une vague de PC compatibles, un procès de six ans et une dynamique qui, une fois enclenchée, est très difficile à briser.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/how-did-windows-win-without-inventing-the-gui/

CHAPITRES
00:00 Ce que Windows n'a pas inventé
00:36 La démo d'Engelbart
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple : le Lisa et le Mac
04:01 Le hic
04:22 IBM cherche un système d'exploitation
04:56 Le détail du contrat
05:17 Les clones
06:21 Windows 1.0 et 2.0
06:50 Apple contre Microsoft
07:25 Windows 3.0
08:08 La dynamique
08:35 Windows 95
08:57 Comment Windows a gagné

CRÉDITS DES IMAGES
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Toutes les autres images d'archives sont dans le domaine public.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

CAPTURES D'ÉCRAN DE WINDOWS
Windows 1.01, Windows/386 2.01, Windows 3.0 et Windows 95, capturés dans l'émulateur PCjs (pcjs.org).
Used with permission from Microsoft.
```

## Bahasa Indonesia (`id`)

```
Bagaimana Windows Menang Tanpa Menciptakan Antarmuka Grafis?
```

```
Jendela, ikon, menu, mouse. Bagi kebanyakan orang, seperti inilah tampilan komputer, dan sebagian besar dari mereka mengenalnya lewat Microsoft. Namun, ketika Windows pertama muncul pada tahun 1985, hampir tidak ada yang baru dari semua itu.

Douglas Engelbart memperagakan komputer yang dikendalikan dengan mouse pada tahun 1968. Xerox PARC membangun Alto pada 1970-an dan mulai menjual Star pada tahun 1981. Apple meluncurkan Lisa, lalu Macintosh. Semuanya lebih dulu daripada Microsoft, tetapi tidak satu pun komputer mereka yang akhirnya ada di sebagian besar meja di dunia.

Video ini menelusuri apa yang terjadi di antaranya: kontrak dengan IBM, gelombang PC yang kompatibel, proses hukum yang berlangsung selama enam tahun, dan sebuah lingkaran yang sangat sulit diputus begitu sudah berjalan.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/how-did-windows-win-without-inventing-the-gui/

BAB
00:00 Yang tidak diciptakan Windows
00:36 Demo Engelbart
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: Lisa dan Mac
04:01 Satu kendala
04:22 IBM butuh sistem operasi
04:56 Detail dalam kontrak
05:17 Komputer klon
06:21 Windows 1.0 dan 2.0
06:50 Apple melawan Microsoft
07:25 Windows 3.0
08:08 Lingkaran itu
08:35 Windows 95
08:57 Bagaimana Windows menang

KREDIT GAMBAR
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Semua gambar arsip lainnya berada dalam domain publik.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

TANGKAPAN LAYAR WINDOWS
Windows 1.01, Windows/386 2.01, Windows 3.0, dan Windows 95, diambil di emulator PCjs (pcjs.org).
Used with permission from Microsoft.
```

## italiano (`it`)

```
Come ha vinto Windows senza inventare l'interfaccia grafica?
```

```
Finestre, icone, menu, un mouse. Per la maggior parte delle persone un computer è semplicemente così, e la maggior parte di loro l'ha conosciuto grazie a Microsoft. Eppure, quando nel 1985 uscì il primo Windows, quasi niente di tutto questo era nuovo.

Douglas Engelbart mostrò un computer controllato con un mouse nel 1968. Lo Xerox PARC costruì l'Alto negli anni '70 e mise in vendita lo Star nel 1981. Apple lanciò il Lisa e poi il Macintosh. Arrivarono tutti prima di Microsoft, e nessuna delle loro macchine finì sulla maggior parte delle scrivanie del mondo.

Questo video racconta cosa è successo nel mezzo: un contratto con IBM, un'ondata di PC compatibili, una causa durata sei anni e un circolo molto difficile da spezzare una volta avviato.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/how-did-windows-win-without-inventing-the-gui/

CAPITOLI
00:00 Cosa Windows non ha inventato
00:36 La demo di Engelbart
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: il Lisa e il Mac
04:01 Il problema
04:22 IBM cerca un sistema operativo
04:56 Il dettaglio nel contratto
05:17 I cloni
06:21 Windows 1.0 e 2.0
06:50 Apple contro Microsoft
07:25 Windows 3.0
08:08 Il circolo
08:35 Windows 95
08:57 Come ha vinto Windows

CREDITI DELLE IMMAGINI
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Tutte le altre immagini d'archivio sono di pubblico dominio.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

SCREENSHOT DI WINDOWS
Windows 1.01, Windows/386 2.01, Windows 3.0 e Windows 95, catturati nell'emulatore PCjs (pcjs.org).
Used with permission from Microsoft.
```

## Deutsch (`de`)

```
Wie hat Windows gewonnen, ohne die grafische Oberfläche zu erfinden?
```

```
Fenster, Symbole, Menüs, eine Maus. Für die meisten Menschen sieht ein Computer einfach so aus, und die meisten haben das über Microsoft kennengelernt. Doch als 1985 das erste Windows erschien, war fast nichts davon neu.

Douglas Engelbart führte 1968 einen Computer vor, der mit einer Maus gesteuert wurde. Xerox PARC baute in den 1970ern den Alto und brachte 1981 den Star auf den Markt. Apple brachte die Lisa und dann den Macintosh heraus. Alle waren vor Microsoft da, aber keiner ihrer Rechner landete auf den meisten Schreibtischen der Welt.

Dieses Video zeigt, was dazwischen geschah: ein Vertrag mit IBM, eine Welle kompatibler PCs, ein sechs Jahre langer Rechtsstreit und ein Kreislauf, der sich kaum noch durchbrechen lässt, wenn er einmal läuft.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/how-did-windows-win-without-inventing-the-gui/

KAPITEL
00:00 Was Windows nicht erfunden hat
00:36 Engelbarts Vorführung
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: die Lisa und der Mac
04:01 Der Haken
04:22 IBM braucht ein Betriebssystem
04:56 Das Detail im Vertrag
05:17 Die Klone
06:21 Windows 1.0 und 2.0
06:50 Apple gegen Microsoft
07:25 Windows 3.0
08:08 Der Kreislauf
08:35 Windows 95
08:57 Wie Windows gewann

BILDNACHWEISE
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Alle übrigen Archivbilder sind gemeinfrei.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

WINDOWS-SCREENSHOTS
Windows 1.01, Windows/386 2.01, Windows 3.0 und Windows 95, aufgenommen im Emulator PCjs (pcjs.org).
Used with permission from Microsoft.
```

## polski (`pl`)

```
Jak Windows wygrał, choć nie wymyślił interfejsu graficznego?
```

```
Okna, ikony, menu, mysz. Dla większości ludzi tak po prostu wygląda komputer, a większość z nich poznała go dzięki Microsoftowi. Jednak kiedy w 1985 roku pojawił się pierwszy Windows, prawie nic z tego nie było nowe.

Douglas Engelbart pokazał w 1968 roku komputer sterowany myszą. Xerox PARC zbudował Alto w latach 70., a w 1981 roku wprowadził do sprzedaży Star. Apple wypuściło Lisę, a potem Macintosha. Wszyscy wyprzedzili Microsoft, ale żaden z ich komputerów nie trafił na większość biurek na świecie.

Ten film opowiada, co wydarzyło się pomiędzy: umowa z IBM, fala kompatybilnych pecetów, sześcioletni proces i pętla, którą bardzo trudno przerwać, gdy już zacznie działać.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/how-did-windows-win-without-inventing-the-gui/

ROZDZIAŁY
00:00 Czego Windows nie wymyślił
00:36 Pokaz Engelbarta
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: Lisa i Mac
04:01 Haczyk
04:22 IBM potrzebuje systemu operacyjnego
04:56 Szczegół w umowie
05:17 Klony
06:21 Windows 1.0 i 2.0
06:50 Apple kontra Microsoft
07:25 Windows 3.0
08:08 Pętla
08:35 Windows 95
08:57 Jak Windows wygrał

ŹRÓDŁA ZDJĘĆ
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Pozostałe zdjęcia archiwalne są w domenie publicznej.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

ZRZUTY EKRANU WINDOWS
Windows 1.01, Windows/386 2.01, Windows 3.0 i Windows 95, przechwycone w emulatorze PCjs (pcjs.org).
Used with permission from Microsoft.
```

## português (Brasil) (`pt-BR`)

```
Como o Windows venceu sem inventar a interface gráfica?
```

```
Janelas, ícones, menus, um mouse. Para a maioria das pessoas, um computador é simplesmente assim, e a maioria o conheceu pela Microsoft. Mas, quando o primeiro Windows saiu, em 1985, quase nada disso era novo.

Douglas Engelbart demonstrou um computador controlado por mouse em 1968. O Xerox PARC construiu o Alto nos anos 1970 e lançou o Star em 1981. A Apple lançou o Lisa e depois o Macintosh. Todos chegaram antes da Microsoft, e nenhuma de suas máquinas foi parar na maioria das mesas do mundo.

Este vídeo acompanha o que aconteceu nesse meio-tempo: um contrato com a IBM, uma onda de PCs compatíveis, um processo de seis anos e um ciclo muito difícil de quebrar depois que se inicia.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/how-did-windows-win-without-inventing-the-gui/

CAPÍTULOS
00:00 O que o Windows não inventou
00:36 A demonstração de Engelbart
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: o Lisa e o Mac
04:01 O porém
04:22 A IBM precisa de um sistema operacional
04:56 O detalhe no contrato
05:17 Os clones
06:21 Windows 1.0 e 2.0
06:50 Apple contra Microsoft
07:25 Windows 3.0
08:08 O ciclo
08:35 Windows 95
08:57 Como o Windows venceu

CRÉDITOS DAS IMAGENS
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Todas as outras imagens de arquivo estão em domínio público.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

CAPTURAS DE TELA DO WINDOWS
Windows 1.01, Windows/386 2.01, Windows 3.0 e Windows 95, capturados no emulador PCjs (pcjs.org).
Used with permission from Microsoft.
```

## Türkçe (`tr`)

```
Windows, Grafik Arayüzü İcat Etmeden Nasıl Kazandı?
```

```
Pencereler, simgeler, menüler, bir fare. Çoğu insan için bilgisayar zaten böyle görünür ve çoğu bununla Microsoft sayesinde tanıştı. Ama ilk Windows 1985'te çıktığında bunların neredeyse hiçbiri yeni değildi.

Douglas Engelbart 1968'de fareyle kontrol edilen bir bilgisayarı tanıttı. Xerox PARC 1970'lerde Alto'yu yaptı ve 1981'de Star'ı satışa sundu. Apple önce Lisa'yı, ardından Macintosh'u piyasaya çıkardı. Hepsi Microsoft'tan önce oradaydı ama hiçbirinin bilgisayarları dünyadaki masaların çoğuna ulaşamadı.

Bu video aradaki dönemde neler olduğunu anlatıyor: IBM ile bir sözleşme, uyumlu PC'lerden oluşan bir dalga, altı yıl süren bir dava ve bir kez dönmeye başladığında kırılması çok zor bir döngü.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/how-did-windows-win-without-inventing-the-gui/

BÖLÜMLER
00:00 Windows'un icat etmedikleri
00:36 Engelbart'ın gösterisi
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: Lisa ve Mac
04:01 Tek bir sorun
04:22 IBM'in işletim sistemine ihtiyacı var
04:56 Sözleşmedeki ayrıntı
05:17 Klonlar
06:21 Windows 1.0 ve 2.0
06:50 Apple, Microsoft'a karşı
07:25 Windows 3.0
08:08 Döngü
08:35 Windows 95
08:57 Windows nasıl kazandı

GÖRSEL KAYNAKLARI
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Diğer tüm arşiv görselleri kamu malıdır.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

WINDOWS EKRAN GÖRÜNTÜLERİ
Windows 1.01, Windows/386 2.01, Windows 3.0 ve Windows 95, PCjs emülatöründe alındı (pcjs.org).
Used with permission from Microsoft.
```

## українська (`uk`)

```
Як Windows переміг, не винайшовши графічний інтерфейс?
```

```
Вікна, значки, меню, миша. Для більшості людей комп'ютер просто так і виглядає, і більшість із них познайомилася з ним завдяки Microsoft. Але коли 1985 року вийшов перший Windows, майже нічого з цього не було новим.

Дуглас Енгельбарт 1968 року показав комп'ютер, яким керували мишею. Xerox PARC у 1970-х збудувала Alto, а 1981 року почала продавати Star. Apple випустила Lisa, а потім Macintosh. Усі вони встигли раніше за Microsoft, але жоден з їхніх комп'ютерів не опинився на більшості столів світу.

Це відео розповідає, що сталося в проміжку: контракт з IBM, хвиля сумісних ПК, шестирічний судовий спір і замкнене коло, яке дуже важко розірвати, коли воно вже запрацювало.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/how-did-windows-win-without-inventing-the-gui/

РОЗДІЛИ
00:00 Чого Windows не винайшов
00:36 Демонстрація Енгельбарта
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: Lisa і Mac
04:01 Заковика
04:22 IBM потрібна операційна система
04:56 Деталь у контракті
05:17 Клони
06:21 Windows 1.0 і 2.0
06:50 Apple проти Microsoft
07:25 Windows 3.0
08:08 Замкнене коло
08:35 Windows 95
08:57 Як Windows переміг

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Усі інші архівні зображення є суспільним надбанням.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

ЗНІМКИ ЕКРАНА WINDOWS
Windows 1.01, Windows/386 2.01, Windows 3.0 і Windows 95, зроблені в емуляторі PCjs (pcjs.org).
Used with permission from Microsoft.
```

## Tiếng Việt (`vi`)

```
Windows đã thắng thế nào dù không phát minh ra giao diện đồ họa?
```

```
Cửa sổ, biểu tượng, menu, con chuột. Với hầu hết mọi người, máy tính đơn giản là trông như vậy, và phần lớn họ biết đến nó qua Microsoft. Nhưng khi Windows đầu tiên ra mắt vào năm 1985, gần như chẳng có gì trong số đó là mới.

Douglas Engelbart đã trình diễn một chiếc máy tính điều khiển bằng chuột vào năm 1968. Xerox PARC chế tạo Alto vào thập niên 1970 và đưa Star ra thị trường năm 1981. Apple ra mắt Lisa rồi Macintosh. Tất cả đều đi trước Microsoft, nhưng không mẫu máy nào trong số đó xuất hiện trên phần lớn bàn làm việc trên thế giới.

Video này kể lại những gì đã diễn ra trong khoảng thời gian đó: một hợp đồng với IBM, một làn sóng máy PC tương thích, một vụ kiện kéo dài sáu năm và một vòng lặp rất khó phá vỡ một khi nó đã chạy.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/how-did-windows-win-without-inventing-the-gui/

CHƯƠNG
00:00 Những gì Windows không phát minh
00:36 Buổi trình diễn của Engelbart
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: Lisa và Mac
04:01 Điểm vướng
04:22 IBM cần một hệ điều hành
04:56 Chi tiết trong hợp đồng
05:17 Các máy nhái
06:21 Windows 1.0 và 2.0
06:50 Apple kiện Microsoft
07:25 Windows 3.0
08:08 Vòng lặp
08:35 Windows 95
08:57 Windows đã thắng thế nào

NGUỒN HÌNH ẢNH
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Tất cả hình ảnh lưu trữ khác thuộc phạm vi công cộng.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

ẢNH CHỤP MÀN HÌNH WINDOWS
Windows 1.01, Windows/386 2.01, Windows 3.0 và Windows 95, chụp trong trình giả lập PCjs (pcjs.org).
Used with permission from Microsoft.
```

## čeština (`cs`)

```
Jak Windows vyhrál, když nevynalezl grafické rozhraní?
```

```
Okna, ikony, nabídky, myš. Pro většinu lidí takhle prostě vypadá počítač a většina z nich se s tím seznámila díky Microsoftu. Jenže když v roce 1985 vyšel první Windows, skoro nic z toho nebylo nové.

Douglas Engelbart předvedl v roce 1968 počítač ovládaný myší. Xerox PARC postavil v 70. letech Alto a v roce 1981 začal prodávat Star. Apple uvedl Lisu a pak Macintosh. Všichni předběhli Microsoft, ale žádný z jejich počítačů se nerozšířil na většinu stolů na světě.

Video sleduje, co se stalo mezitím: smlouvu s IBM, vlnu kompatibilních PC, spor, který se táhl šest let, a smyčku, kterou je velmi těžké přerušit, jakmile se jednou roztočí.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/how-did-windows-win-without-inventing-the-gui/

KAPITOLY
00:00 Co Windows nevynalezl
00:36 Engelbartova ukázka
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: Lisa a Mac
04:01 Háček
04:22 IBM potřebuje operační systém
04:56 Detail ve smlouvě
05:17 Klony
06:21 Windows 1.0 a 2.0
06:50 Apple proti Microsoftu
07:25 Windows 3.0
08:08 Smyčka
08:35 Windows 95
08:57 Jak Windows vyhrál

ZDROJE OBRÁZKŮ
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Ostatní archivní snímky jsou volné dílo.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

SNÍMKY OBRAZOVKY WINDOWS
Windows 1.01, Windows/386 2.01, Windows 3.0 a Windows 95, pořízené v emulátoru PCjs (pcjs.org).
Used with permission from Microsoft.
```

## español (`es`)

```
¿Cómo ganó Windows sin inventar la interfaz gráfica?
```

```
Ventanas, iconos, menús, un ratón. Para la mayoría de la gente, un ordenador es simplemente así, y la mayoría lo conoció gracias a Microsoft. Pero cuando salió el primer Windows, en 1985, casi nada de eso era nuevo.

Douglas Engelbart presentó un ordenador controlado con un ratón en 1968. Xerox PARC construyó el Alto en los años setenta y puso a la venta el Star en 1981. Apple lanzó el Lisa y después el Macintosh. Todos llegaron antes que Microsoft, y ninguna de sus máquinas acabó en la mayoría de los escritorios del mundo.

Este vídeo sigue lo que pasó entre medias: un contrato con IBM, una oleada de PC compatibles, un pleito de seis años y un círculo muy difícil de romper una vez que se pone en marcha.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/how-did-windows-win-without-inventing-the-gui/

CAPÍTULOS
00:00 Lo que Windows no inventó
00:36 La demostración de Engelbart
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: el Lisa y el Mac
04:01 El inconveniente
04:22 IBM necesita un sistema operativo
04:56 El detalle del contrato
05:17 Los clones
06:21 Windows 1.0 y 2.0
06:50 Apple contra Microsoft
07:25 Windows 3.0
08:08 El círculo
08:35 Windows 95
08:57 Cómo ganó Windows

CRÉDITOS DE LAS IMÁGENES
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Todas las demás imágenes de archivo son de dominio público.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

CAPTURAS DE PANTALLA DE WINDOWS
Windows 1.01, Windows/386 2.01, Windows 3.0 y Windows 95, capturadas en el emulador PCjs (pcjs.org).
Used with permission from Microsoft.
```

## svenska (`sv`)

```
Hur vann Windows utan att uppfinna det grafiska gränssnittet?
```

```
Fönster, ikoner, menyer, en mus. För de flesta ser en dator helt enkelt ut så, och de flesta kom i kontakt med det via Microsoft. Men när det första Windows kom 1985 var nästan inget av det nytt.

Douglas Engelbart visade 1968 en dator som styrdes med en mus. Xerox PARC byggde Alto på 1970-talet och började sälja Star 1981. Apple lanserade Lisa och sedan Macintosh. Alla var där före Microsoft, men ingen av deras datorer hamnade på de flesta skrivborden i världen.

Den här videon följer vad som hände däremellan: ett avtal med IBM, en våg av kompatibla pc-datorer, en rättstvist som pågick i sex år och en självförstärkande process som är mycket svår att stoppa när den väl har kommit igång.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/how-did-windows-win-without-inventing-the-gui/

KAPITEL
00:00 Det Windows inte uppfann
00:36 Engelbarts demo
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: Lisa och Mac
04:01 Haken
04:22 IBM behöver ett operativsystem
04:56 Detaljen i avtalet
05:17 Klonerna
06:21 Windows 1.0 och 2.0
06:50 Apple mot Microsoft
07:25 Windows 3.0
08:08 Den självförstärkande processen
08:35 Windows 95
08:57 Hur Windows vann

BILDKÄLLOR
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
Alla övriga arkivbilder är fria från upphovsrätt (public domain).
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

SKÄRMBILDER FRÅN WINDOWS
Windows 1.01, Windows/386 2.01, Windows 3.0 och Windows 95, tagna i emulatorn PCjs (pcjs.org).
Used with permission from Microsoft.
```
