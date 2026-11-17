<!-- S01 -->
Představ si, že zapneš počítač s Windows
a nenajdeš žádný hlavní panel, žádné tlačítko Start
a na ploše ani jednu ikonu.

<!-- S02 -->
Místo toho je nahoře tenká lišta,
nabídka, která vyskočí, kamkoli klikneš,
a čtyři virtuální plochy vedle sebe.

<!-- S03 -->
Vypadá to jako Linux.
Jenže tvoje programy, ovladače a soubory
jsou přesně tam, kde jsi je nechal.
Pořád je to Windows.

<!-- S04 -->
Změnila se jen plocha.
A přepínač, který ji mění,
je jediné nastavení.

<!-- S05 -->
Windows ho má v registru,
v hodnotě jménem Shell.
Skoro na každém počítači s Windows
v ní stojí explorer.exe.

<!-- S06 -->
Napiš tam jméno jiného programu,
odhlas se a znovu přihlas,
a Windows místo explorer.exe spustí ten tvůj.
Cokoli nakreslí, to je tvoje plocha.

<!-- S07 -->
A není to trik, na který někdo přišel loni.
Už Windows 3.0 z roku 1990 měl stejný přepínač
v obyčejném textovém souboru system.ini.
Jeden řádek: shell=progman.exe.

<!-- S08 -->
Stačilo to jméno změnit
a Správce programů, okno plné skupin ikon,
se vůbec neobjevil.

<!-- S09 -->
Otázka tedy nezní, jestli Windows
může mít jinou plochu.
Mohl vždycky.
Otázka je, proč ji skoro nikdo neviděl.

<!-- S10 -->
Začněme tím, na co ten řádek vlastně ukazuje.
Hlavní panel, ikony na ploše,
oznamovací oblast u hodin:
to všechno je jeden program, explorer.exe.

<!-- S11 -->
Ano, tentýž explorer.exe,
ve kterém si v Průzkumníku procházíš soubory.
Dělá dvě práce
a většina lidí si všimne jen jedné.

<!-- S12 -->
Ta druhá práce má jméno: shell.
Je to vrstva, přes kterou počítač ovládáš.
Pod ní je jádro, ovladače
a služby, které udržují Windows v chodu.

<!-- S13 -->
Nic z toho hlavní panel nepotřebuje.
Ukonči explorer.exe ve Správci úloh
a hlavní panel i ikony zmizí...
ale Poznámkový blok, prohlížeč
a všechna ostatní okna fungují dál.

<!-- S14 -->
Spusť ho znovu a plocha je zpátky.
Jasnější důkaz snad ani neexistuje,
že plocha je prostě další program.

<!-- S14b -->
Jestli sis někdy změnil spouštěč
na telefonu s Androidem,
znáš podobný princip.
Na Androidu je to běžné nastavení.
Windows ten mechanismus má taky,
jen běžným uživatelům nikdy nedal
jednoduché tlačítko.

<!-- S15 -->
Tři pojmy se tu pletou.
Shell je to, odkud věci spouštíš:
hlavní panel, nabídky, plocha.
Správce oken řídí, kde okna leží,
co je nahoře a které má fokus.
Desktopové prostředí
to všechno spojí do jednoho celku.

<!-- S16 -->
Na Linuxu jdou ty kusy
kombinovat mnoha různými způsoby.
Ve Windows výměna shellu
nenahradí systémovou správu oken
ani to, jak aplikace kreslí rámy svých oken.

<!-- S17 -->
Lidi to přesto zkoušeli.
Na začátku devadesátých let sis mohl zajít do obchodu
a koupit náhradu za Správce programů.

<!-- S18 -->
Norton Desktop for Windows
ti dal vlastní plochu,
vlastní nástroje pro práci se soubory a vlastní spouštěč,
a pod tím pořád tentýž Windows.

<!-- S19 -->
Někteří výrobci počítačů ho vyměnili
dřív, než zákazník počítač vůbec zapnul.
Navigator od Packard Bell vítal kupující
domem, kterým se dalo projít místnost po místnosti.

<!-- S20 -->
Pak Windows 95 tu práci předal programu explorer.exe
a řádek v system.ini
se prostě změnil na explorer.exe.
Přepínač zůstal přesně tam, kde byl.

<!-- S21 -->
Koncem devadesátých let
kolem toho přepínače vyrostla celá komunita.
Nejznámějším projektem byl LiteStep.

<!-- S22 -->
Vzhled si půjčil z AfterStepu,
unixového správce oken podle vzoru NeXTSTEPu
od firmy, kterou Steve Jobs založil po odchodu z Applu.

<!-- S23 -->
LiteStep neměl nabídku Start, dokud sis ji nepostavil.
Všechno byl modul:
tady dok, tam hodiny,
nabídka, která se otevřela, kdekoli jsi klikl pravým.

<!-- S24 -->
Motivy se sdílely jako tapety.
Některé vypadaly futuristicky.
Některé jako unixová pracovní stanice.
Některé na obrazovce nenechaly skoro nic.

<!-- S25 -->
Blackbox for Windows šel opačnou cestou.
Kopíroval Blackbox, minimalistického unixového správce oken,
až po jedinou prostou nabídku
a úzký panel nástrojů.

<!-- S26 -->
Jeho nástupce bbLean
tu myšlenku držel naživu na Windows 2000 a XP.

<!-- S27 -->
Emerge Desktop rozložil shell na samostatné části:
spouštěč, oznamovací oblast, seznam úloh,
každá z nich malý program, který sis mohl nechat, nebo zahodit.

<!-- S28 -->
Proč se s tím tolik dřít?
Zčásti proto, že vzhled XP
se dal snadno poznat a těžko změnit.
Motivy měnily barvy a tlačítka.
Rozložení zůstávalo.

<!-- S29 -->
Zčásti kvůli paměti.
Na stroji se 128 megabajty
sliboval lehčí shell víc místa
pro všechno ostatní.

<!-- S30 -->
A zčásti kvůli Linuxu.
Tam byl výběr plochy normální věc
a někteří uživatelé Windows chtěli
stejnou volbu.

<!-- S31 -->
Většina těch projektů už neexistuje.
Poslední vydání LiteStepu byla testovací verze
z roku 2014, pořád označená jako alfa.
Emerge Desktop a SharpEnviro taky skončily.

<!-- S32 -->
Zčásti za to mohly malé dobrovolnické týmy.
Jenže změnil se i Windows.
Postupně se z jeho plochy stalo mnohem víc
než jeden spustitelný soubor.

<!-- S33 -->
Prostředí plochy je dnes rozložené
do několika procesů,
systémových komponent a balíčkovaných aplikací.
I nabídka Start běží jako samostatný program.

<!-- S34 -->
Nahradit explorer.exe neznamená nahradit
všechno, z čeho se skládá dnešní rozhraní Windows.
A to je jeden z důvodů, proč je dnes
úplnou alternativní plochu
postavit těžší než dřív.

<!-- S35 -->
A přesto to pořád jde.
Cairo Desktop, open-source projekt,
dnes běží na Windows 11.

<!-- S36 -->
Přináší vlastní lištu s nabídkami nahoře,
vlastní hlavní panel
a složky, které si můžeš připnout na lištu jako stohy.

<!-- S37 -->
Umí běžet vedle explorer.exe,
nebo převzít roli shellu.
V tom druhém režimu
můžou části Windows 11 zlobit,
mezi nimi Nastavení a Zabezpečení Windows.

<!-- S38 -->
Seelen UI na to jde jinak.
Nenahrazuje explorer.exe.
Skryje hlavní panel a přidá vlastní prvky:
dok, lištu, widgety
a správce oken, který ti okna rovná vedle sebe.

<!-- S39 -->
Výsledek nemusí Windows vůbec připomínat.
Ale pod ním pořád běží explorer.exe.
Je to nová tvář, ne nový shell.

<!-- S40 -->
A Microsoft?
Ten na to dokonce má oficiální funkci.
Jmenuje se Shell Launcher
a je určená pro zařízení, jako jsou kiosky.

<!-- S41 -->
Nejspíš jsi něco takového už použil,
aniž bys o tom věděl.
Automat na jízdenky na nádraží.
Samoobslužná pokladna. Bankomat.

<!-- S42 -->
Spousta z nich jsou počítače s Windows,
jejichž celý shell je jediná aplikace.
Správce určí program
a po přihlášení je ten program celá plocha.

<!-- S43 -->
Je ale k dispozici jen
v edicích Enterprise, Education
a IoT Enterprise.

<!-- S44 -->
A starší mechanismus v registru
je pořád součástí Windows.
Microsoft z něj jen nikdy neudělal
běžné nastavení plochy
pro obyčejné uživatele.

<!-- S45 -->
Proč to tedy vypadá, že Windows má jen jednu plochu?
Ne proto, že by jinou mít nemohl.
Protože plocha je produkt.

<!-- S46 -->
Na Linuxu je plocha volba.
Některé distribuce tě nechají vybrat
ještě během instalace.
KDE Plasma, GNOME, Xfce, Cinnamon...

<!-- S47 -->
Ve Windows je plocha to, co Microsoft ukazuje
v každé reklamě, na každém snímku obrazovky
a na každé stránce podpory.
Jedna plocha znamená jeden návod
pro víc než miliardu počítačů.

<!-- S48 -->
To je skutečná výhoda.
Když se něco rozbije,
obrazovka v návodu vypadá jako ta tvoje.
Cenou je, že se většina lidí nikdy nedozví,
že měla na výběr.

<!-- S49 -->
Lidi vyměňovali plochu Windows
ještě dřív, než vůbec existoval Windows 95.
Stavěli doky, holé nabídky
a plochy, které se ničemu jinému nepodobaly.

<!-- S50 -->
Většina těch projektů zmizela.
Myšlenka ne.
Pod každým hlavním panelem, na který jsi kdy klikl,
pořád leží to jedno nastavení a čeká na jiné jméno.

<!-- S51 -->
Plocha je jen další software.
A software se dá vyměnit.

<!-- S52 -->
Takže otázka pro tebe:
kdyby ti Windows nechal vybrat plochu
při instalaci, jako některé linuxové distribuce,
přešel bys, nebo si nechal tu, kterou znáš?
Napiš mi to do komentářů.
