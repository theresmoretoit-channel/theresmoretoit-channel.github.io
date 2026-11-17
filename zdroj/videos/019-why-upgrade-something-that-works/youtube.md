# Podklady pro nahrání na YouTube

## Titul

```
It Still Works. So Why Upgrade It?
```

## Popis

```
"But it works."

It's the most popular argument in IT, and it isn't wrong. Windows XP
worked. A phone from 2008 still works. So why replace anything?

Because "it works" was never a property of your software. It's a property
of your software and everything around it — today. This video follows that
idea from a 2G device on a wall, through a water company switching to
Water 2.0, to a chair manufacturer that will happily sell you Enterprise
Extended Chair Support.

And then it stops being a joke: when Windows XP ran out of support in
2014, Microsoft sold exactly that contract. Around two hundred dollars per
machine for the first year, double for the second. The British public
sector signed for five and a half million pounds — and a year later
decided not to renew, while the old machines were still there.

Old technology rarely fails by crashing. It fails when the security audit
comes back with a finding, when a partner's interface needs something your
platform cannot speak, when the hosting provider retires your image, or
when nobody wants the job. Nothing is broken. The world simply stopped
waiting for you.

Not everything needs upgrading — a system that gets switched off next year
can stay exactly as it is, and "there is a newer version" is not an
argument on its own. The question was never "is this the latest?" The
question is: when this breaks, will anyone still be able to fix it?

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

CHAPTERS
0:00 They already know
0:26 "But it works"
0:45 It's a property of everything around it
1:09 A real example: 2G
1:30 Water 2.0
2:15 Chair 6
2:59 Enterprise Extended Chair Support
3:19 Except this part is not a joke
3:59 What will the upgrade give us?
4:25 Old technology rarely fails by crashing
4:58 Changing the oil
5:21 Five years later: archaeology
5:48 Technical debt is also fear
5:59 The blacksmith's horse
6:32 "We don't have time right now"
6:47 The trap
7:10 Two costs, two budgets
7:50 When not to upgrade
8:10 The healthy version is boring
8:34 Remember 2G, Water 2.0 and Chair 6

―――

Sources for the Windows XP figures:
Government Technology blog (gov.uk), 22 May 2015 — the support agreement
was not extended
https://governmenttechnology.blog.gov.uk/2015/05/22/update-on-the-customer-support-agreement-for-windows-xp/

Department of Health and Crown Commercial Services letter, 8 April 2014
https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/314721/DHandCabinetOfficeMicrosoftXPupdate8April14.pdf

Computer Weekly — Government signs £5.5m Microsoft deal
https://www.computerweekly.com/news/2240217389/Government-signs-55m-Microsoft-deal-to-extend-Windows-XP-support

Computerworld — Microsoft to double the price of XP's post-retirement support
https://www.computerworld.com/article/1640632/microsoft-to-double-price-of-xps-post-retirement-support.html

―――

Music is generated procedurally, not taken from a library.

IMAGE CREDITS
Pouring engine oil to motor — Santeri Viinamäki, CC BY-SA 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0
All other archive images are in the public domain.
```

## Kapitoly

**Jsou už uvnitř bloku popisu** (doplněno 2026-09-05). Do té doby ležely
jen tady, tedy MIMO blok — a popis přitom sliboval „Chapters below", takže
slíbil něco, co v něm nebylo. Ten slib je teď nahrazený skutečnými kapitolami.
Ověřeno proti `work/timing.json`: první je na `00:00`, je jich dvacet
a nejkratší trvá 10,4 s — YouTube uzná minimum tři kapitoly a 10 s.

```
0:00 They already know
0:26 "But it works"
0:45 It's a property of everything around it
1:09 A real example: 2G
1:30 Water 2.0
2:15 Chair 6
2:59 Enterprise Extended Chair Support
3:19 Except this part is not a joke
3:59 What will the upgrade give us?
4:25 Old technology rarely fails by crashing
4:58 Changing the oil
5:21 Five years later: archaeology
5:48 Technical debt is also fear
5:59 The blacksmith's horse
6:32 "We don't have time right now"
6:47 The trap
7:10 Two costs, two budgets
7:50 When not to upgrade
8:10 The healthy version is boring
8:34 Remember 2G, Water 2.0 and Chair 6
```

## Co nahrát

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 551,40 s, 1920×1080/25p, −14,0 LUFS / −1,2 dBTP, 64 MB |
| náhled | `render/thumbnail.jpg` — 1280×720, 80 kB (limit je 2 MB) |
| titulky | `subtitles/*.srt` — devět jazyků |
| atribuce do popisu | `CREDITS.md` |

## Nastavení

| položka | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — hlas je `bf_emma`. **Nastavit PRVNÍ**, jinak zůstane dlaždice „Titulky" zašedlá |
| byla použita AI? | **ne** — 55 diagramů kreslených kódem, 6 malovaných SDXL scén (ne fotorealismus), 2 archivní snímky upravené jen barevně, hudba procedurální |
| kategorie | Věda a technika |
| pro děti | ne |

## Tagy

```
technical debt, legacy software, software maintenance, why upgrade,
end of support, windows xp, custom support agreement, 2g shutdown,
legacy systems, software architecture, it management, technology obsolescence
```

## Test & Compare

YouTube umí testovat až tři náhledy. Zbylé dva jsou hotové:
`render/thumb-c2-museum.jpg` a `render/thumb-c3-still-barefoot.jpg`.

## Odkaz na sesterské video

Scéna S09 používá jako první reálný příklad vypínání 2G, tedy téma videa
**„2G Is Ancient. So Why Are Lifts, Cars and Alarms Still Using It?"**.
Až budou obě venku, patří odkaz do popisu obou.

## Před nahráním zkontrolovat

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/019-why-upgrade-something-that-works/render/final-en.mp4
ffmpeg -v error -i .../final-en.mp4 -f null -      # musí projít BEZE SLOVA
```

A hlavně: **nahrát jako neveřejné a podívat se na to v přehrávači.**
YouTube video překóduje a jak vyjdou tmavé diagramy po jejich kompresi
se dopředu posoudit nedá. Je to jediný krok, který nejde udělat na disku.
