<!-- S01 -->
Zkusíš smazat soubor.
Počítač oznámí, že je otevřený
v jiném programu.
Ale neřekne, ve kterém.

<!-- S02 -->
Ta hláška je viditelný konec
mnohem podivnější otázky.
Co vlastně znamená
otevřít soubor?

<!-- S03 -->
Protože na jiném počítači
se týž soubor, otevřený stejně,
smaže bez jediné námitky.

<!-- S04 -->
Týž soubor.
Týž úkon.
Dvě úplně jiné odpovědi.

<!-- S05 -->
Začněme tím,
co štve každého.
Který program?

<!-- S06 -->
Windows to ví.
Má pro ten otevřený soubor
objekt v jádře
a ví, kterému procesu patří.
Mohl by ho pojmenovat.

<!-- S07 -->
Tak zavíráš věci nazdařbůh.
Otevřeš Správce úloh.
Zíráš na seznam procesů
a skoro žádný nepoznáváš.

<!-- S08 -->
A dlouhá léta
byla odpověď opravdu ta,
že sis stáhl zvláštní nástroj.
Unlocker vyšel v roce 2005
a na Windows XP to byla odpověď.

<!-- S09 -->
Pak Windows 7 přinesl
Sledování prostředků.
Záložku Procesor.
Seznam Přidružené popisovače.

<!-- S10 -->
Napíšeš jméno souboru.
Vrátí ti program
i číslo procesu.
Nic se neinstaluje.
Je to tam od roku 2009.

<!-- S10b -->
Cizí nástroje toho ale
uměly víc než jen poradit.
Uměly ten handle zavřít
a soubor uvolnit.

<!-- S11 -->
Čímž se vracíme
k té otázce.
Co ten program vlastně dostal,
když soubor otevřel?

<!-- S12 -->
Řekněme, že přehrávač otevře
soubor movie.mp4.
Ve Windows znamená otevřít soubor
vyplnit dvě věci.

<!-- S13 -->
První je zřejmá.
Co s ním chci dělat já?
Číst ho. Zapisovat do něj.

<!-- S14 -->
Ta druhá je ta zajímavá.
Co s ním smějí dělat ostatní,
dokud ho mám otevřený?

<!-- S15 -->
Je to skutečné nastavení.
Řekneš v něm, co smějí
ostatní programy, dokud ho držíš.

<!-- S16 -->
Smějí ho číst.
Smějí do něj i zapisovat.
Smějí ho smazat nebo přejmenovat.

<!-- S16b -->
Nebo vůbec nic.
Dokud ho používám já,
nikdo na něj nesáhne.

<!-- S17 -->
Příznak, který povoluje mazání,
se jmenuje FILE_SHARE_DELETE.
A dokumentace Microsoftu
hned pod ním uvádí jednu větu.

<!-- S18 -->
Právo mazat zahrnuje
i přejmenování.

<!-- S19 -->
Takže program, který odmítne
sdílení pro mazání,
zablokoval i přejmenování.

<!-- S20 -->
A pokud ho program, který soubor
otevřel, nepovolil,
nikdo jiný si ho nevezme.

<!-- S21 -->
Proto se ta chyba
nejmenuje soubor se používá.
Jmenuje se porušení sdílení.

<!-- S22 -->
Odpověď byla celou dobu
schovaná
v názvu té chyby.

<!-- S23 -->
Teď totéž
na linuxovém stroji.
Přehrávač otevře video.

<!-- S24 -->
A ty napíšeš
rm movie.mp4.

<!-- S24b -->
Projde to.
Video hraje dál.

<!-- S25 -->
Co tedy ten program dostal,
když ne to, že ten soubor drží?

<!-- S26 -->
Tohle je hlavní myšlenka
celého videa.
Jméno není soubor.

<!-- S27 -->
movie.mp4 je řádek
v adresáři.
Ten řádek ukazuje na objekt,
ve kterém jsou vlastní data.

<!-- S28 -->
Když program otevře soubor,
dostane odkaz
na ten objekt.
Ne na ten řádek.

<!-- S29 -->
Smazání souboru
tedy smaže řádek.
Objektu se nedotkne.

<!-- S30 -->
Manuálová stránka to říká
jedinou větou.
Soubor zůstane existovat,
dokud se nezavře poslední
deskriptor, který na něj odkazuje.

<!-- S31 -->
Zní to abstraktně,
dokud to člověk neuvidí.
Udělal jsem tedy protokol
o velikosti pět set megabajtů
a nechal jeden proces, ať ho drží.

<!-- S31b -->
Pak jsem ho smazal.

<!-- S32 -->
Výpis adresáře
neukáže vůbec nic.
Nástroj, který měří
velikost složky, hlásí nulu.

<!-- S33 -->
A nástroj, který měří
volné místo na disku,
hlásí, že pět set megabajtů
pořád chybí.

<!-- S33b -->
Prázdná složka.
Půl gigabajtu pryč.

<!-- S34 -->
Stává se to tak často,
že na hledání takových souborů
existuje zvláštní příkaz.
Smazané, neviditelné, pořád na disku.

<!-- S35 -->
A místo se vrátí
v okamžiku, kdy ten jeden proces
soubor pustí.

<!-- S36 -->
Totéž platí o přejmenování.
Přesuň soubor, dokud je otevřený,
a program si toho ani nevšimne.

<!-- S37 -->
Manuál to říká taky bez obalu.
Otevřených deskriptorů staré cesty
se to nijak nedotkne.

<!-- S37b -->
To jméno nikdy nepoužíval.

<!-- S38 -->
Což má jedno omezení,
o kterém stojí za to vědět.
Běžící program
nejde přepsat na místě.

<!-- S38b -->
Linux to odmítne.
Text file busy.

<!-- S39 -->
Co ale udělat jde,
je odpojit jméno
a dát tam nový soubor.

<!-- S40 -->
Starý proces běží dál
z objektu,
který už žádné jméno nemá.
Co spustíš potom, dostane nový soubor.

<!-- S41 -->
Ta samá myšlenka znovu,
a sama se potvrzuje.
Spoustu věcí jde vyměnit,
aniž bys sáhl na samotný objekt.

<!-- S41b -->
Proto Linux umí aktualizovat
program i za běhu.
Novou verzi ale dostaneš,
až ho ukončíš a spustíš znovu.

<!-- S42 -->
Je tedy Windows
prostě horší návrh?

<!-- S42b -->
Ne.
A tohle je ta část,
kterou skoro nikdo nezná.

<!-- S43 -->
Windows má způsob,
jak udělat přesně totéž.

<!-- S43b -->
Na NTFS si Windows umí
říct o mazání ve stylu POSIX.

<!-- S44 -->
Microsoft popisuje,
co se při tom stane.
Jméno zmizí
z viditelného jmenného prostoru.

<!-- S45 -->
A aplikace, které už soubor
otevřený měly, ho smějí používat dál,
přestože jméno,
kterým ho otevřely, je pryč.

<!-- S46 -->
To je unixové chování.
Na NTFS.
Zdokumentované Microsoftem.

<!-- S47 -->
Oba systémy umějí obojí.
Liší se výchozí nastavení.
To, co dostaneš, když soubor otevřeš
a vůbec o tom nepřemýšlíš.

<!-- S48 -->
Ve Windows dostaneš smlouvu.
V Unixu dostaneš odkaz
na objekt.

<!-- S49 -->
Což zní jako otázka
pro programátory,
dokud člověk neuvidí
zrovna tuhle hlášku.

<!-- S50 -->
Restartujte počítač,
aby se aktualizace dokončily.

<!-- S51 -->
Řekněme, že Windows má vyměnit
knihovnu, kterou běžící proces
drží otevřenou podle přísné smlouvy.

<!-- S52 -->
Nemůže ten soubor vyměnit,
dokud ho ten proces drží otevřený.
Takže ho něco musí pustit.

<!-- S53 -->
Ukončit aplikaci.
Zastavit službu.
Nebo předat celou věc
Správci restartů.

<!-- S54 -->
Což je skutečná součást systému.
Vypíná věci v pořadí.
Aplikace s grafickým rozhraním,
pak konzolové programy,

<!-- S55 -->
pak služby
a Průzkumníka až nakonec.
Potom je zase spustí.

<!-- S56 -->
A existuje z jediného důvodu,
který Microsoft říká natvrdo
ve vlastní dokumentaci.

<!-- S57 -->
Hlavní důvod,
proč instalace softwaru
a aktualizace vyžadují
restart systému...

<!-- S58 -->
je ten, že některé aktualizované
soubory zrovna používá
běžící aplikace
nebo služba.

<!-- S59 -->
Bylo by příliš úhledné tady skončit.
Pravidla sdílení nejsou jediný důvod,
proč si počítač říká o restart.

<!-- S60 -->
Aktualizace jádra je něco jiného.
Jádro pod sebou samým
vyměnit nejde.

<!-- S61 -->
Linux má týž problém,
i když záplatování za běhu
se restartu občas vyhne.

<!-- S62 -->
Poctivá verze tedy
tvrdí míň než ta,
která se lépe poslouchá.

<!-- S63 -->
Tím, jak Windows zachází
s používanými soubory, šly některé
součásti za běhu měnit hůř.
A to k tomu přispělo.

<!-- S64 -->
Protože každé rozhodnutí v návrhu
má někde svůj důsledek.

<!-- S65 -->
Windows nechává program,
který soubor otevře, rozhodnout,
co s ním smějí ostatní.

<!-- S66 -->
Cena je, že někdy
nesmažeš vlastní soubor,
protože ti to jiný program
nedovolil.

<!-- S67 -->
Unix drží jméno
a objekt odděleně,
takže spoustu věcí jde vyměnit
za chodu systému.

<!-- S68 -->
Cena je půl gigabajtu,
který zmizel z disku
a nepatří vůbec žádnému souboru.

<!-- S69 -->
A všimni si, jak se každá
z těch dvou věcí řeší.
Ve Windows je jedna cesta ven
ukončit program,
který ten soubor drží.

<!-- S70 -->
V Linuxu je jedna cesta,
jak to místo dostat zpátky,
restartovat službu,
která ho pořád drží.

<!-- S71 -->
Jiné příčiny.
Někdy tentýž lék.

<!-- S71b -->
Mimochodem, jestli chceš vidět,
kam nás zavede příští otázka,
zvaž odběr.
Kanálu to hodně pomůže.

<!-- S72 -->
Takže. Ta otázka ze začátku.
Co znamená
otevřít soubor?

<!-- S73 -->
Znamená to, že něco držíš.
Ty dva systémy ti prostě
dávají do ruky něco jiného.

<!-- S74 -->
Proto ta hláška ve skutečnosti
nikdy neřekla,
že ten soubor nejde smazat.

<!-- S75 -->
Řekla, že program,
který ho otevřel,
ti to nedovolil.

<!-- S75b -->
A ví, který program to je.
Jen se o tom nezmínil.
