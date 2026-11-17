# Fact check — 101 What Is the Internet Really Optimizing For?

Ověřeno 2026-10-11 proti scénáři v0.3 (ID scén v0.3, platí i pro v0.4).
Opravy jsou ve v0.4: **dvě**, obě zpřesňují míru jistoty, žádná neobrací
tvrzení.

**Hlavní past tématu:** nepřisoudit platformám ani algoritmu víc, než
doklady dovolují. Proto se drží tři hranice: YouTube kvalitu **nevidí
přímo, ale snaží se ji odhadnout** (S53); polský případ je **odhad strany**,
ne měření (S38); Goodhartův zákon je ve scénáři **v populární formulaci**,
ne Goodhartovými slovy (S32).

## Úvod (S01–S07)

- **S01–S03 OK, hypotetické.** „Imagine…" — nic netvrdí o kanálu. Kanál
  na TikToku není (`docs/shorty.md`), proto musí zůstat v podmiňovacím
  rámci; **nepřepisovat do první osoby**.
- **S04–S07 OK.** Úvaha, ne tvrzení.

## Co systém vidí (S08–S11)

- **S08–S10 OK.** Goodrow (VP Engineering YouTube), *On YouTube's
  recommendation system*, 15. 9. 2021: jako signály uvádí kliky, dobu
  sledování, odpovědi z průzkumů, sdílení, lajky a dislajky.
  https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/
  „Skip" tam výslovně není; ve scénáři je jako obecný příklad chování
  napříč platformami (TikTok, Shorts) — přijatelné.
  S08 „can't see what a video is worth" je formulace **„nevidí"**, ne
  „nesnaží se odhadnout" — revize v0.1 správně namítla, že YouTube to
  odhadovat zkouší; to je v S53.

## YouTube: kliky → doba sledování (S12–S15)

- **S12 OK.** YouTube Creator Blog, *Changes to Related and Recommended
  Videos*, 12. 3. 2012: dosavadní systém se silně opíral o kliky (*„relied
  heavily on clicks"* v souhrnu), nově *„we'll be focusing more prominently
  on time watched"*, *„engagement will become the leading indicator"*.
  https://youtubecreator-uk.googleblog.com/2012/03/changes-to-related-and-recommended.html
- **S13 OK.** Goodrow 2021: *„we learned back in 2011 that clicking on
  a video doesn't mean you actually watched it."* Září 2012 (*YouTube now:
  why we focus on watch time*): *„This rewarded videos that were successful
  at attracting clicks, rather than the videos that actually kept viewers
  engaged."* https://youtubecreator-uk.googleblog.com/2012/09/youtube-now-why-we-focus-on-watch-time.html
- **S14 OK, a „shifted its weight" je přesné.** Kliky zůstaly signálem
  (*„while we'll still be looking at clicks"*), takže **„switched" by bylo
  přehnané** — ve v0.1 tak stálo, od v0.2 už ne. Goodrow: *„That's why we
  added in watchtime in 2012."* Doporučování březen 2012, vyhledávání
  říjen 2012.
- **S14b OPRAVENO: + „often".** Covington, Adams, Sargin, *Deep Neural
  Networks for YouTube Recommendations*, RecSys '16, Boston, 15.–19. 9. 2016,
  s. 5: *„Ranking by click-through rate often promotes deceptive videos
  that the user does not complete (“clickbait”) whereas watch time better
  captures engagement."* (ověřeno v PDF přes `pdftotext`)
  https://research.google/pubs/pub45530/
  Autoři jsou z Googlu (YouTube), „its own engineers" sedí; 2016 − 2012
  = „four years later" sedí. Revize ChatGPT studii nazvala „údajnou" —
  **je skutečná a citát je doslovný**.
- **S15 OK jako úsudek.** „Harder to fake" — doba sledování je dražší na
  podvržení než klik; Covington ji staví právě proti clickbaitu.

## Meloun a feed (S16–S27)

- Úvaha a ilustrace, žádné ověřitelné tvrzení. S25 „short videos can be
  brilliant, and long ones terrible" je výhrada, ne fakt.

## Reklama a dvacet minut (S28–S31)

- **S28 OK.** „Most of them are paid by advertisers": Meta má z reklamy
  přes 97 % tržeb, TikTok a X převážně z reklamy; YouTube má i předplatné,
  ale reklama převažuje. **Z paměti, ne ze zdroje dohledaného v tomto
  průchodu** — kdyby se scéna měnila na konkrétní číslo, dohledat 10-K. „Most" je přesné,
  „all" by nebylo.

## Goodhart (S32–S35)

- **S32 OK, s vědomím formulace.** Charles Goodhart (britský ekonom,
  Bank of England), 1975: *„Any observed statistical regularity will tend
  to collapse once pressure is placed upon it for control purposes."*
  Známá věta *„When a measure becomes a target, it ceases to be a good
  measure"* je **parafráze Marilyn Strathernové (1997)** podle Hoskina;
  Goodhart sám ji v hesle o svém zákoně (2015) přijímá.
  https://en.wikipedia.org/wiki/Goodhart%27s_law
  Scénář říká „Economists have a name for this. Goodhart's law." a pak
  formulaci — **nepřisuzuje citát Goodhartovi**, proto beze změny.
  **Nepřidávat „as Goodhart put it".**
- **S33–S35 OK.** Aplikace zákona; S33 opírá S12–S14b.

## Facebook 2018 a Polsko (S36–S40)

- **S36 OK.** Leden 2018, změna News Feedu na *„meaningful social
  interactions"* — bodový systém, kde komentáře, sdílení a reakce váží
  víc než lajk. WSJ, Hagey a Horwitz, *Facebook Tried to Make Its Platform
  a Healthier Place. It Got Angrier Instead.*, 15. 9. 2021 (Facebook Files).
- **S37 OK.** Tamtéž: tým datových analytiků interně psal *„Our approach
  has had unhealthy side effects on important slices of public content,
  such as politics and news"*; výzkumníci zjistili, že vydavatelé
  a strany přeorientovali příspěvky na pobouření a senzaci. Podtitul
  článku: změna z roku 2018 **„rewarded outrage"**.
  **Vydavatelé:** Jonah Peretti (BuzzFeed) Facebooku psal, že virálně se
  šíří nejvíc rozdělující obsah, který vydavatelé vyrábějí — tamtéž.
  https://electionlawblog.org/2021/facebook-tried-to-make-its-platform-a-healthier-place-it-got-angrier-instead/
- **S38 OPRAVENO: + „by its own estimate".** Interní zpráva Facebooku
  z dubna 2019 (Facebook Papers): sociální tým **jedné nejmenované**
  strany *„estimates that they have shifted the proportion of their posts
  from 50/50 positive/negative to 80% negative"*. OKO.press cituje polsky
  (*„jednej z partii… szacuje… z 50/50… na 80 proc. negatywnych…
  bezpośrednio w następstwie modyfikacji algorytmu"*).
  https://oko.press/wina-zuckerberga-nie-tylko-facebook-podsyca-podzialy
  > **Výhrada, kvůli které je oprava nutná:** Dominik Batorski (Varšavská
  > univerzita) analyzoval oficiální stránky polských stran a **takový
  > posun 50/50 → 80 % nenašel**. Zároveň pro Washington Post zjistil, že
  > negativní příspěvky se **po roce 2018 sdílely výrazně víc** — takže
  > mechanismus (S37) data podporují, konkrétní číslo (S38) je jen tvrzení
  > strany. Proto „by its own estimate"; bez toho by divák číslo četl jako
  > změřené.
- **S39 OK.** „And it said why. Because of the change to the feed." —
  připisuje příčinu **straně** (*„as a function of the change to the
  algorithm"*), ne nám. Neměnit na „because of the algorithm".
- **S40 OK jako závěr.** „It changed what they posted" — doklad je
  tvrzení strany (S38) a Batorského nález o sdílení; formulace je
  o motivaci, ne o měřeném podílu.

## Jsou lidé hloupější? (S41–S47)

- **S42 OK.** Gladiátorské hry (Řím), davy u veřejných poprav (např.
  Tyburn do 1783), senzační tisk (penny press, yellow journalism) —
  obecně známé.
- **S42b–S42c OK.** Microsoft Canada, Consumer Insights, *Attention Spans*
  (2015): pokles „z 12 na 8 sekund", zlatá rybka 9 s. Zpráva čísla
  připisuje webu **Statistic Brain**; BBC (Simon Maybin, More or Less,
  2017) obešel jeho zdroje a **žádný výzkum za číslem nenašel**; podle
  BBC není doklad ani o tom, že by ryby měly krátkou pozornost.
  https://www.warc.com/newsandopinion/opinion/the_goldfish_myth/2806
  „Nobody has found the study behind it. Or the goldfish." sedí na obojí.
  Pozor: jeden zdroj tvrdí, že samotná zpráva o rybce nemluví — WSJ i BBC
  ji tam uvádějí; „appeared in a 2015 report from Microsoft" je proto
  formulace, která obstojí.
- **S43–S47 OK.** Úvaha.

## Řešení (S48–S57)

- **S53 OK.** Goodrow 2021: *„We measure valued watchtime through user
  surveys that ask you to rate the video you watched from one to five
  stars"*; počítají se jen hodnocení 4–5. „Tries to reward time people say
  was well spent" sedí.
- **S54 OK.** „Still a guess about you" — Goodrow: *„we've trained
  a machine learning model to predict potential survey responses for
  everyone"*, protože průzkum vyplní málokdo. Doklad přesně pro „guess".
- Ostatní úvaha.

## Fermi (S58–S68)

- **S58 OK.** Stáří vesmíru 13,787 ± 0,020 mld. let (Planck 2018) →
  „thirteen point eight billion". Mléčná dráha **100–400 mld. hvězd**
  (NASA, ESA) — „hundreds of billions" je běžná formulace, při dolním
  odhadu je to hraniční; nechávám, protože většina odhadů leží nad 200.
- **S59 OK.** Žádný potvrzený technosignál ani biosignatura.
- **S61–S63 OK** — vtip, výslovně hypotetický; S64 to říká nahlas
  („no evidence that this explains the silence").
- **S66 OK jako hodnocení** („greatest knowledge-sharing machine").

## Co z toho plyne pro další fáze

- **Obrázky:** S14b ukazuje článek — titulní stranu RecSys '16 lze
  citovat textem v diagramu (ne snímkem PDF). S37 Peretti/BuzzFeed bez
  loga. S42b–c rybka nesmí dostat „9 s" jako fakt — v obraze jen jako
  citovaný mýtus (přeškrtnutý zdroj, otazník).
- **Popis videa:** odkazy výš (Goodrow 2021, Covington 2016, WSJ 2021,
  OKO.press) jsou podklad pro „Sources" v `youtube.md`.
