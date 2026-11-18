# YouTube — 156 „Why Can't One Program Take Over Your Computer?“: lokalizace

Lokalizované názvy a popisy pro třináct jazyků (bez `en`, ten je
v `youtube.md`). Pořadí podle YouTube Studia. Nahrává
`python tools/lokalizace.py videos/156-why-cant-one-program-take-over-your-computer`.

**Co se NEPŘEKLÁDÁ:**

- vlastní jména a časy kapitol, ty jsou na vteřinu shodné s angličtinou (CrowdStrike, Intel, Microsoft, Windows, Multics, Meltdown, Spectre, Riot, Vanguard, Valorant, strace),
- řádek zdrojů, přeložené je jen úvodní slovo „Sources:“. Názvy dokumentů zůstávají anglicky, jsou to doklady. Věta o vlastním měření strace přeložená je, není to název dokumentu,
- jméno autora a název snímku v kreditech, „via Wikimedia Commons“, licence a řádek „Licences:“ s adresami,
- tagy — YouTube je pro jednotlivé jazyky nemá.

Pointa videa (do ringu 0 pouštějí lidé, pokaždé když instalují ovladač, S85) se v popisu neprozrazuje.
Odstavec o titulcích a americké stopě je doslova z kanonické tabulky v `docs/zverejneni.md`.
Úvod popisu přebírá znění S01–S09 daného jazyka (`script.<kód>.md`), termíny (ring/anillo/anneau/anel/pierścień/кільце/rengas, kernel/noyau/jądro/ядро/çekirdek/ydin/kärnan) taky.
Pevné obraty (Zdroje, Kapitoly, kredity) jsou ze 155. Registr podle překladů scénáře: neformální všude (cs tykání, de *du*, fi *sinä*, vi *bạn*, pt-BR *você*, tr *sen*, uk *ти*, id *kamu*).

## suomi (`fi`)

```
Miksi yksi ohjelma ei voi kaapata tietokonettasi?
```

```
19. heinäkuuta 2024 tietoturvayhtiö CrowdStrike lähetti tavallisen päivityksen. Ei uusi ohjelma, vain pieni asetustiedosto. Muutamassa tunnissa 8,5 miljoonaa Windows-tietokonetta oli pysähtynyt siniseen ruutuun. Lentoyhtiöt peruivat lentoja ja sairaalat leikkauksia. Ja virhe kaiken takana oli ihan tavallinen: ohjelma odotti 20 tietokenttää, ja päivitys antoi sille 21. Pelisi tekevät tuollaisia virheitä koko ajan ja yksinkertaisesti sulkeutuvat. Miksi siis yksi ohjelma ei voi kaapata tietokonettasi, ja miksi tämä pystyi?

Videolla käydään läpi suojausrenkaat, neljä käyttöoikeustasoa, jotka Intel toi 80286-suorittimen mukana vuonna 1982, miksi numerointi kulkee takaperin, miten suoritin tarkistaa käskyt ja muistin jokaisella käyttökerralla, mikä järjestelmäkutsu on ja kuinka monta niitä selain tekee, mitä tapahtui renkaille 1 ja 2, miten Meltdown löysi reitin muurin läpi, mitä korjaus maksoi, miksi tietoturvaohjelmat ja pelien huijauksenestot ovat silti renkaassa 0, ja kenen pitäisi päättää, mitä sisään päästetään.

Lähteet: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Järjestelmäkutsujen määrät mittasimme itse strace-työkalulla.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/why-cant-one-program-take-over-your-computer/

LUVUT
00:00 8,5 miljoonaa sinistä ruutua
01:01 Kun mikään ei pysäyttänyt ohjelmaa
01:36 Neljä rengasta, numeroitu takaperin
02:29 Suoritin tarkistaa
03:28 Takaisin CrowdStrikeen
03:58 Miten selain tallentaa tiedoston?
04:48 Laskimme järjestelmäkutsut
05:09 Mitä tapahtui renkaille 1 ja 2?
06:58 Meltdown: reitti muurin läpi
08:34 Korjaus ja sen hinta
09:12 Miksi se oli renkaassa 0?
09:54 Huijauksenesto ytimessä
10:26 Miksi siis yksi ohjelma ei voi kaapata konetta?

KUVALÄHTEET
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

## français (`fr`)

```
Pourquoi un programme ne peut-il pas prendre le contrôle de ton ordinateur ?
```

```
Le 19 juillet 2024, une entreprise de sécurité nommée CrowdStrike a envoyé une mise à jour de routine. Pas un nouveau programme, juste un petit fichier de configuration. En quelques heures, 8,5 millions d'ordinateurs sous Windows s'étaient bloqués sur un écran bleu. Des compagnies aériennes ont cloué leurs avions au sol et des hôpitaux ont annulé des opérations. Et l'erreur derrière tout ça était tout à fait banale : le programme attendait 20 données et la mise à jour lui en a donné 21. Tes jeux font ce genre d'erreur tout le temps, et ils se ferment simplement. Alors pourquoi un programme ne peut-il pas prendre le contrôle de ton ordinateur, et pourquoi celui-ci a pu le faire ?

Cette vidéo explique les anneaux de protection, les quatre niveaux de privilège qu'Intel a introduits avec le 80286 en 1982, pourquoi la numérotation va à l'envers, comment le processeur vérifie les instructions et la mémoire à chaque accès, ce qu'est un appel système et combien en fait un navigateur, ce que sont devenus les anneaux 1 et 2, comment Meltdown a trouvé un moyen de traverser le mur, ce qu'a coûté le correctif, pourquoi les logiciels de sécurité et les anti-triche des jeux se trouvent quand même dans l'anneau 0, et qui devrait décider de ce qui entre.

Sources : CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Le nombre d'appels système, nous l'avons mesuré nous-mêmes avec strace.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/why-cant-one-program-take-over-your-computer/

CHAPITRES
00:00 8,5 millions d'écrans bleus
01:01 Quand rien n'arrêtait un programme
01:36 Quatre anneaux, numérotés à l'envers
02:29 Le processeur vérifie
03:28 Retour à CrowdStrike
03:58 Comment un navigateur enregistre-t-il un fichier ?
04:48 On a compté les appels système
05:09 Que sont devenus les anneaux 1 et 2 ?
06:58 Meltdown : un passage à travers le mur
08:34 Le correctif et ce qu'il a coûté
09:12 Pourquoi était-il dans l'anneau 0 ?
09:54 L'anti-triche dans le noyau
10:26 Alors pourquoi un programme ne peut-il pas tout contrôler ?

CRÉDITS IMAGES
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

## Bahasa Indonesia (`id`)

```
Kenapa satu program tidak bisa mengambil alih komputermu?
```

```
Pada 19 Juli 2024, sebuah perusahaan keamanan bernama CrowdStrike mengirim pembaruan rutin. Bukan program baru, hanya file konfigurasi kecil. Dalam hitungan jam, 8,5 juta komputer Windows berhenti di layar biru. Maskapai menghentikan penerbangan dan rumah sakit membatalkan operasi. Dan kesalahan di baliknya sangat biasa: programnya mengharapkan 20 data, tapi pembaruannya memberinya 21. Game-mu membuat kesalahan seperti itu terus-menerus, lalu game-nya tertutup begitu saja. Jadi kenapa satu program tidak bisa mengambil alih komputermu, dan kenapa yang satu ini bisa?

Video ini membahas ring proteksi, empat tingkat hak akses yang diperkenalkan Intel lewat 80286 pada tahun 1982, kenapa penomorannya terbalik, bagaimana prosesor memeriksa instruksi dan memori di setiap akses, apa itu system call dan berapa banyak yang dibuat sebuah browser, apa yang terjadi dengan ring 1 dan 2, bagaimana Meltdown menemukan cara menembus tembok, berapa harga perbaikannya, kenapa software keamanan dan anti-cheat game tetap berada di ring 0, dan siapa yang seharusnya memutuskan apa yang boleh masuk.

Sumber: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Jumlah system call kami ukur sendiri dengan strace.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/why-cant-one-program-take-over-your-computer/

BAB
00:00 8,5 juta layar biru
01:01 Saat tidak ada yang menghentikan program
01:36 Empat ring, bernomor terbalik
02:29 Prosesor memeriksa
03:28 Kembali ke CrowdStrike
03:58 Bagaimana browser menyimpan file?
04:48 Kami menghitung system call
05:09 Apa yang terjadi dengan ring 1 dan 2?
06:58 Meltdown: jalan menembus tembok
08:34 Perbaikan dan harganya
09:12 Kenapa ia ada di ring 0?
09:54 Anti-cheat di kernel
10:26 Jadi kenapa satu program tidak bisa mengambil alih?

KREDIT GAMBAR
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

## italiano (`it`)

```
Perché un programma non può prendere il controllo del tuo computer?
```

```
Il 19 luglio 2024, un'azienda di sicurezza chiamata CrowdStrike ha inviato un aggiornamento di routine. Non un nuovo programma, solo un piccolo file di configurazione. Nel giro di poche ore, 8,5 milioni di computer Windows si erano fermati su una schermata blu. Le compagnie aeree hanno bloccato i voli e gli ospedali hanno annullato interventi. E l'errore dietro a tutto questo era del tutto banale: il programma si aspettava 20 dati e l'aggiornamento gliene ha dati 21. I tuoi giochi fanno errori così di continuo, e semplicemente si chiudono. Allora perché un programma non può prendere il controllo del tuo computer, e perché questo invece ci è riuscito?

Questo video racconta i ring di protezione, i quattro livelli di privilegio che Intel introdusse con l'80286 nel 1982, perché la numerazione va al contrario, come il processore controlla istruzioni e memoria a ogni accesso, cos'è una chiamata di sistema e quante ne fa un browser, che fine hanno fatto i ring 1 e 2, come Meltdown trovò un modo per attraversare il muro, quanto è costata la correzione, perché i software di sicurezza e gli anti-cheat dei giochi stanno comunque nel ring 0, e chi dovrebbe decidere cosa entra.

Fonti: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Il numero di chiamate di sistema l'abbiamo misurato noi con strace.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/why-cant-one-program-take-over-your-computer/

CAPITOLI
00:00 8,5 milioni di schermate blu
01:01 Quando niente fermava un programma
01:36 Quattro ring, numerati al contrario
02:29 Il processore controlla
03:28 Ritorno a CrowdStrike
03:58 Come fa un browser a salvare un file?
04:48 Abbiamo contato le chiamate di sistema
05:09 Che fine hanno fatto i ring 1 e 2?
06:58 Meltdown: un varco nel muro
08:34 La correzione e quanto è costata
09:12 Perché era nel ring 0?
09:54 Anti-cheat nel kernel
10:26 Allora perché un programma non può prendere il controllo?

CREDITI DELLE IMMAGINI
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

## Deutsch (`de`)

```
Warum kann ein einzelnes Programm nicht deinen Computer übernehmen?
```

```
Am 19. Juli 2024 verschickte die Sicherheitsfirma CrowdStrike ein routinemäßiges Update. Kein neues Programm, nur eine kleine Konfigurationsdatei. Innerhalb weniger Stunden hingen 8,5 Millionen Windows-Rechner auf einem Bluescreen fest. Fluglinien strichen Flüge, Krankenhäuser sagten Operationen ab. Und der Fehler dahinter war ganz gewöhnlich: Das Programm erwartete 20 Werte, das Update lieferte ihm 21. Deine Spiele machen ständig solche Fehler und schließen sich einfach. Warum kann also ein einzelnes Programm nicht deinen Computer übernehmen, und warum konnte es dieses hier?

Das Video erklärt die Schutzringe, die vier Berechtigungsstufen, die Intel 1982 mit dem 80286 eingeführt hat, warum die Zählung rückwärts läuft, wie der Prozessor Befehle und Speicher bei jedem Zugriff prüft, was ein Systemaufruf ist und wie viele davon ein Browser macht, was aus Ring 1 und 2 geworden ist, wie Meltdown einen Weg durch die Wand fand, was die Lösung gekostet hat, warum Sicherheitssoftware und Anti-Cheat in Spielen trotzdem in Ring 0 sitzen, und wer entscheiden sollte, was hinein darf.

Quellen: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Die Zahlen der Systemaufrufe haben wir selbst mit strace gemessen.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/why-cant-one-program-take-over-your-computer/

KAPITEL
00:00 8,5 Millionen Bluescreens
01:01 Als nichts ein Programm aufhielt
01:36 Vier Ringe, rückwärts nummeriert
02:29 Der Prozessor prüft
03:28 Zurück zu CrowdStrike
03:58 Wie speichert ein Browser eine Datei?
04:48 Wir haben die Systemaufrufe gezählt
05:09 Was ist aus Ring 1 und 2 geworden?
06:58 Meltdown: ein Weg durch die Wand
08:34 Die Lösung und ihr Preis
09:12 Warum lief es in Ring 0?
09:54 Anti-Cheat im Kernel
10:26 Warum kann also ein einzelnes Programm nicht übernehmen?

BILDNACHWEISE
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

## polski (`pl`)

```
Dlaczego jeden program nie może przejąć twojego komputera?
```

```
19 lipca 2024 roku firma CrowdStrike, zajmująca się bezpieczeństwem, rozesłała rutynową aktualizację. Nie nowy program, tylko mały plik konfiguracyjny. W ciągu kilku godzin 8,5 miliona komputerów z Windowsem zatrzymało się na niebieskim ekranie. Linie lotnicze odwołały loty, a szpitale operacje. A błąd, który za tym stał, był całkiem zwyczajny: program spodziewał się 20 wartości, a aktualizacja dała mu 21. Twoje gry robią takie błędy cały czas i po prostu się zamykają. Więc dlaczego jeden program nie może przejąć twojego komputera i dlaczego ten mógł?

Film omawia pierścienie ochrony, cztery poziomy uprawnień, które Intel wprowadził w 1982 roku razem z procesorem 80286, dlaczego numeracja idzie od tyłu, jak procesor sprawdza instrukcje i pamięć przy każdym dostępie, czym jest wywołanie systemowe i ile ich robi przeglądarka, co się stało z pierścieniami 1 i 2, jak Meltdown znalazł drogę przez mur, ile kosztowała poprawka, dlaczego oprogramowanie zabezpieczające i anty-cheaty w grach i tak siedzą w pierścieniu 0, i kto powinien decydować, co trafia do środka.

Źródła: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Liczbę wywołań systemowych zmierzyliśmy sami narzędziem strace.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/why-cant-one-program-take-over-your-computer/

ROZDZIAŁY
00:00 8,5 miliona niebieskich ekranów
01:01 Kiedy nic nie zatrzymywało programu
01:36 Cztery pierścienie, numerowane od tyłu
02:29 Procesor sprawdza
03:28 Z powrotem do CrowdStrike
03:58 Jak przeglądarka zapisuje plik?
04:48 Policzyliśmy wywołania systemowe
05:09 Co się stało z pierścieniami 1 i 2?
06:58 Meltdown: droga przez mur
08:34 Poprawka i jej koszt
09:12 Dlaczego był w pierścieniu 0?
09:54 Anty-cheat w jądrze
10:26 Więc dlaczego jeden program nie może przejąć komputera?

ŹRÓDŁA ZDJĘĆ
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

## português (Brasil) (`pt-BR`)

```
Por que um programa não consegue tomar conta do seu computador?
```

```
Em 19 de julho de 2024, uma empresa de segurança chamada CrowdStrike enviou uma atualização de rotina. Não era um programa novo, só um pequeno arquivo de configuração. Em poucas horas, 8,5 milhões de computadores com Windows tinham travado numa tela azul. Companhias aéreas suspenderam voos e hospitais cancelaram cirurgias. E o erro por trás disso era bem comum: o programa esperava 20 dados e a atualização entregou 21. Seus jogos cometem erros assim o tempo todo e simplesmente fecham. Então por que um programa não consegue tomar conta do seu computador, e por que este conseguiu?

Este vídeo explica os anéis de proteção, os quatro níveis de privilégio que a Intel introduziu com o 80286 em 1982, por que a numeração vai ao contrário, como o processador confere instruções e memória a cada acesso, o que é uma chamada de sistema e quantas um navegador faz, o que aconteceu com os anéis 1 e 2, como o Meltdown achou um jeito de atravessar o muro, quanto custou a correção, por que softwares de segurança e anti-cheats de jogos ficam no anel 0 mesmo assim, e quem deveria decidir o que entra.

Fontes: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Os números de chamadas de sistema foram medidos por nós com strace.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/why-cant-one-program-take-over-your-computer/

CAPÍTULOS
00:00 8,5 milhões de telas azuis
01:01 Quando nada impedia um programa
01:36 Quatro anéis, numerados ao contrário
02:29 O processador confere
03:28 De volta à CrowdStrike
03:58 Como um navegador salva um arquivo?
04:48 Contamos as chamadas de sistema
05:09 O que aconteceu com os anéis 1 e 2?
06:58 Meltdown: um jeito de atravessar o muro
08:34 A correção e quanto custou
09:12 Por que estava no anel 0?
09:54 Anti-cheat no kernel
10:26 Então por que um programa não consegue tomar conta?

CRÉDITOS DAS IMAGENS
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

## Türkçe (`tr`)

```
Neden tek bir program bilgisayarını ele geçiremez?
```

```
19 Temmuz 2024'te CrowdStrike adlı bir güvenlik şirketi sıradan bir güncelleme gönderdi. Yeni bir program değil, sadece küçük bir yapılandırma dosyası. Birkaç saat içinde 8,5 milyon Windows bilgisayar mavi ekranda durmuştu. Havayolları uçuşları durdurdu, hastaneler ameliyatları iptal etti. Ve bunun arkasındaki hata gayet sıradandı: program 20 veri bekliyordu, güncelleme ona 21 tane verdi. Oyunların böyle hataları sürekli yapar ve sadece kapanır. Peki neden tek bir program bilgisayarını ele geçiremez ve bu neden geçirebildi?

Bu video koruma halkalarını anlatıyor: Intel'in 1982'de 80286 ile getirdiği dört yetki seviyesi, numaraların neden tersten gittiği, işlemcinin komutları ve belleği her erişimde nasıl kontrol ettiği, sistem çağrısının ne olduğu ve bir tarayıcının kaç tane yaptığı, Ring 1 ve 2'ye ne olduğu, Meltdown'ın duvardan geçmenin yolunu nasıl bulduğu, düzeltmenin neye mal olduğu, güvenlik yazılımlarının ve oyunlardaki hile önleyicilerin yine de neden Ring 0'da durduğu ve içeri neyin gireceğine kimin karar vermesi gerektiği.

Kaynaklar: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Sistem çağrısı sayılarını strace ile kendimiz ölçtük.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/why-cant-one-program-take-over-your-computer/

BÖLÜMLER
00:00 8,5 milyon mavi ekran
01:01 Hiçbir şeyin programı durdurmadığı zamanlar
01:36 Dört ring, tersten numaralı
02:29 İşlemci kontrol ediyor
03:28 CrowdStrike'a geri dönüş
03:58 Bir tarayıcı dosyayı nasıl kaydeder?
04:48 Sistem çağrılarını saydık
05:09 Ring 1 ve 2'ye ne oldu?
06:58 Meltdown: duvardan geçen bir yol
08:34 Düzeltme ve bedeli
09:12 Neden Ring 0'daydı?
09:54 Çekirdekte hile önleyici
10:26 Peki neden tek bir program ele geçiremez?

GÖRSEL KAYNAKLARI
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

## українська (`uk`)

```
Чому одна програма не може захопити твій комп'ютер?
```

```
19 липня 2024 року компанія з кібербезпеки CrowdStrike розіслала звичайне оновлення. Не нову програму, лише маленький файл конфігурації. За кілька годин 8,5 мільйона комп'ютерів з Windows зупинилися на синьому екрані. Авіакомпанії скасовували рейси, а лікарні — операції. А помилка, що за цим стояла, була цілком звичайною: програма чекала 20 значень, а оновлення дало їй 21. Твої ігри роблять такі помилки постійно й просто закриваються. То чому одна програма не може захопити твій комп'ютер і чому ця змогла?

Відео пояснює кільця захисту — чотири рівні привілеїв, які Intel запровадила 1982 року разом із процесором 80286, — чому нумерація йде навпаки, як процесор перевіряє інструкції та пам'ять під час кожного доступу, що таке системний виклик і скільки їх робить браузер, що сталося з кільцями 1 і 2, як Meltdown знайшов шлях крізь стіну, чого коштувало виправлення, чому програми безпеки та античити в іграх однаково сидять у кільці 0, і хто має вирішувати, що потрапляє всередину.

Джерела: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Кількість системних викликів ми виміряли самі за допомогою strace.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/why-cant-one-program-take-over-your-computer/

РОЗДІЛИ
00:00 8,5 мільйона синіх екранів
01:01 Коли ніщо не зупиняло програму
01:36 Чотири кільця, пронумеровані навпаки
02:29 Процесор перевіряє
03:28 Знову про CrowdStrike
03:58 Як браузер зберігає файл?
04:48 Ми порахували системні виклики
05:09 Що сталося з кільцями 1 і 2?
06:58 Meltdown: шлях крізь стіну
08:34 Виправлення і його ціна
09:12 Чому він був у кільці 0?
09:54 Античит у ядрі
10:26 То чому одна програма не може захопити комп'ютер?

ДЖЕРЕЛА ЗОБРАЖЕНЬ
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

## Tiếng Việt (`vi`)

```
Tại sao một chương trình không thể chiếm quyền máy tính của bạn?
```

```
Ngày 19 tháng 7 năm 2024, một công ty bảo mật tên là CrowdStrike đã gửi đi một bản cập nhật thường lệ. Không phải một chương trình mới, chỉ là một tệp cấu hình nhỏ. Chỉ trong vài giờ, 8,5 triệu máy tính Windows đã dừng lại ở màn hình xanh. Các hãng hàng không phải dừng chuyến bay, bệnh viện hủy các ca phẫu thuật. Và lỗi đằng sau chuyện đó lại rất bình thường: chương trình chờ 20 mục dữ liệu, còn bản cập nhật đưa cho nó 21. Game của bạn mắc những lỗi như thế suốt, và chúng chỉ đơn giản là tắt đi. Vậy tại sao một chương trình không thể chiếm quyền máy tính của bạn, và tại sao chương trình này lại làm được?

Video này giải thích các ring bảo vệ, bốn cấp đặc quyền mà Intel giới thiệu cùng bộ xử lý 80286 năm 1982, vì sao cách đánh số lại ngược, bộ xử lý kiểm tra lệnh và bộ nhớ ở mỗi lần truy cập như thế nào, lời gọi hệ thống là gì và một trình duyệt thực hiện bao nhiêu lần, chuyện gì đã xảy ra với ring 1 và 2, Meltdown đã tìm ra cách xuyên qua bức tường ra sao, bản vá tốn kém thế nào, vì sao phần mềm bảo mật và hệ thống chống gian lận trong game vẫn nằm ở ring 0, và ai nên quyết định thứ gì được vào bên trong.

Nguồn: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Số lời gọi hệ thống do chúng tôi tự đo bằng strace.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/why-cant-one-program-take-over-your-computer/

CHƯƠNG
00:00 8,5 triệu màn hình xanh
01:01 Khi không gì ngăn được một chương trình
01:36 Bốn ring, đánh số ngược
02:29 Bộ xử lý kiểm tra
03:28 Quay lại CrowdStrike
03:58 Trình duyệt lưu tệp bằng cách nào?
04:48 Chúng tôi đã đếm các lời gọi hệ thống
05:09 Ring 1 và 2 đã đi đâu?
06:58 Meltdown: một lối xuyên qua bức tường
08:34 Bản vá và cái giá của nó
09:12 Tại sao nó nằm ở ring 0?
09:54 Chống gian lận trong kernel
10:26 Vậy tại sao một chương trình không thể chiếm quyền?

NGUỒN HÌNH ẢNH
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

## čeština (`cs`)

```
Proč nemůže jeden program ovládnout tvůj počítač?
```

```
19. července 2024 rozeslala bezpečnostní firma CrowdStrike běžnou aktualizaci. Žádný nový program, jen malý konfigurační soubor. Během pár hodin se 8,5 milionu počítačů s Windows zastavilo na modré obrazovce. Aerolinky rušily lety a nemocnice operace. A chyba, která za tím stála, byla úplně obyčejná: program čekal 20 údajů a aktualizace mu jich dala 21. Tvoje hry dělají takové chyby pořád a prostě se zavřou. Tak proč nemůže jeden program ovládnout tvůj počítač a proč tenhle mohl?

Video prochází ochranné ringy, čtyři úrovně oprávnění, které Intel zavedl v roce 1982 s procesorem 80286, proč se číslují pozpátku, jak procesor kontroluje instrukce a paměť při každém přístupu, co je systémové volání a kolik jich udělá prohlížeč, co se stalo s ringy 1 a 2, jak Meltdown našel cestu skrz zeď, co stála oprava, proč bezpečnostní software i anti-cheaty ve hrách stejně sedí v ringu 0, a kdo má rozhodovat, co se dostane dovnitř.

Zdroje: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Počty systémových volání jsme změřili sami nástrojem strace.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/why-cant-one-program-take-over-your-computer/

KAPITOLY
00:00 8,5 milionu modrých obrazovek
01:01 Když program nic nezastavilo
01:36 Čtyři ringy, číslované pozpátku
02:29 Procesor kontroluje
03:28 Zpátky u CrowdStriku
03:58 Jak prohlížeč uloží soubor?
04:48 Spočítali jsme systémová volání
05:09 Co se stalo s ringy 1 a 2?
06:58 Meltdown: cesta skrz zeď
08:34 Oprava a co stála
09:12 Proč byl v ringu 0?
09:54 Anti-cheat v kernelu
10:26 Tak proč nemůže jeden program ovládnout počítač?

ZDROJE OBRÁZKŮ
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

## español (`es`)

```
¿Por qué un programa no puede apoderarse de tu ordenador?
```

```
El 19 de julio de 2024, una empresa de seguridad llamada CrowdStrike envió una actualización rutinaria. No era un programa nuevo, solo un pequeño archivo de configuración. En pocas horas, 8,5 millones de ordenadores con Windows se habían quedado bloqueados en una pantalla azul. Las aerolíneas suspendieron vuelos y los hospitales cancelaron operaciones. Y el error que había detrás era de lo más corriente: el programa esperaba 20 datos y la actualización le dio 21. Tus juegos cometen errores así todo el tiempo y simplemente se cierran. Entonces, ¿por qué un programa no puede apoderarse de tu ordenador, y por qué este sí pudo?

Este vídeo recorre los anillos de protección, los cuatro niveles de privilegio que Intel introdujo con el 80286 en 1982, por qué la numeración va al revés, cómo el procesador comprueba las instrucciones y la memoria en cada acceso, qué es una llamada al sistema y cuántas hace un navegador, qué pasó con los anillos 1 y 2, cómo Meltdown encontró una forma de atravesar el muro, cuánto costó el arreglo, por qué el software de seguridad y los anticheats de los juegos están igualmente en el anillo 0, y quién debería decidir qué entra.

Fuentes: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Las cifras de llamadas al sistema las medimos nosotros con strace.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/why-cant-one-program-take-over-your-computer/

CAPÍTULOS
00:00 8,5 millones de pantallas azules
01:01 Cuando nada detenía a un programa
01:36 Cuatro anillos, numerados al revés
02:29 El procesador comprueba
03:28 De vuelta a CrowdStrike
03:58 ¿Cómo guarda un archivo un navegador?
04:48 Contamos las llamadas al sistema
05:09 ¿Qué pasó con los anillos 1 y 2?
06:58 Meltdown: una forma de atravesar el muro
08:34 El arreglo y lo que costó
09:12 ¿Por qué estaba en el anillo 0?
09:54 Anticheat en el kernel
10:26 Entonces, ¿por qué un programa no puede apoderarse de todo?

CRÉDITOS DE LAS IMÁGENES
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

## svenska (`sv`)

```
Varför kan inte ett program ta över din dator?
```

```
Den 19 juli 2024 skickade säkerhetsföretaget CrowdStrike ut en rutinuppdatering. Inte ett nytt program, bara en liten konfigurationsfil. Inom några timmar hade 8,5 miljoner Windowsdatorer stannat på en blå skärm. Flygbolag ställde in flyg och sjukhus ställde in operationer. Och misstaget bakom det var helt vanligt: programmet väntade sig 20 värden och uppdateringen gav det 21. Dina spel gör sådana misstag hela tiden och stängs bara. Så varför kan inte ett program ta över din dator, och varför kunde det här?

Videon går igenom skyddsringarna, de fyra behörighetsnivåer som Intel införde med 80286 år 1982, varför numreringen går baklänges, hur processorn kontrollerar instruktioner och minne vid varje åtkomst, vad ett systemanrop är och hur många en webbläsare gör, vad som hände med ring 1 och 2, hur Meltdown hittade en väg genom väggen, vad lösningen kostade, varför säkerhetsprogram och anti-cheat i spel ändå ligger i ring 0, och vem som ska få bestämma vad som släpps in.

Källor: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). Antalet systemanrop har vi själva mätt med strace.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/why-cant-one-program-take-over-your-computer/

KAPITEL
00:00 8,5 miljoner blå skärmar
01:01 När ingenting stoppade ett program
01:36 Fyra ringar, numrerade baklänges
02:29 Processorn kontrollerar
03:28 Tillbaka till CrowdStrike
03:58 Hur sparar en webbläsare en fil?
04:48 Vi räknade systemanropen
05:09 Vad hände med ring 1 och 2?
06:58 Meltdown: en väg genom väggen
08:34 Lösningen och vad den kostade
09:12 Varför låg det i ring 0?
09:54 Anti-cheat i kärnan
10:26 Så varför kan inte ett program ta över?

BILDKÄLLOR
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```
