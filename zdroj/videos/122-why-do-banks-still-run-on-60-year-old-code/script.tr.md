<!-- S01 -->
999 sterlin
ve 99 peni.
Bir peni ekle.

<!-- S02 -->
Sonuç sıfır.

<!-- S03 -->
Hata mesajı yok. Çökme yok.
Sadece sıfır, sessizce hesaba yazılmış.

<!-- S04 -->
COBOL'da, sonuç için ayrılan alan
sonucun sığmayacağı kadar küçükse,
fazladan basamak düpedüz kaybolabilir.
Program uyarılmak istemedikçe
hesaplama devam eder.

<!-- S05 -->
Yuvarlama da yapmaz.
2 sterlin 34,5 peni,
peni hassasiyetinde saklanınca,
2,34 olur.

<!-- S06 -->
Fazladan tek bir kelime yaz, ROUNDED,
ve sonuç 2,35 olur.

<!-- S07 -->
Bunların hiçbiri hata değil.
Bunlar kural.
Ve dünyadaki pek çok banka
hâlâ bu tür kurallarla çalışıyor.

<!-- S08 -->
COBOL, bir programlama dili,
1959'dan kalma.
Onunla yazılan her program o kadar eski değil.
Ama dilin kendisi öyle,
alışkanlıkları da.

<!-- S09 -->
Peki bankalar neden onu değiştirmedi?
Paraları var.
Mühendisleri var.

<!-- S10 -->
Bunu anlamak için üç gerçek vakaya bakacağız.
Eski sisteminden ayrılmaya çalışan bir banka,
bunu başaran bir banka,
ve herkesin COBOL'u suçladığı bir kriz.

<!-- S11 -->
Ama önce, şu kayıp yarım peni.

<!-- S12 -->
Diyelim ki o bankacılık programını
modern bir dilde yeniden yazdın.
Muhtemelen o kuralları düzeltirdin.
Taşma bir hataya dönüşür.
Yarım peni yukarı yuvarlanır.

<!-- S13 -->
Daha temiz. Daha güvenli.
Ama artık yarım peni çıkan her yerde
programın eskisinden farklı sonuç veriyor.

<!-- S14 -->
Modern diller kesin ondalık hesap yapabilir.
Java'nın bunun için özel bir tipi var.
Ama orada bile
yuvarlama kuralı bir tercih.

<!-- S15 -->
Yaygın bir ayar yarımı yukarı yuvarlar:
2,35.
Bir diğeri en yakın çift rakama yuvarlar:
2,34.
İkisi de doğru. Yalnızca biri eşleşiyor.

<!-- S16 -->
Sıradan kayan noktalı sayılarla ise,
çoğu kodun varsayılan olarak kullandığı türle,
iş daha da tuhaflaşıyor.
Sıfır virgül bir artı sıfır virgül iki
sıfır virgül üç etmiyor.

<!-- S17 -->
Yani COBOL'u değiştirmek çeviri değil.
Bunun gibi her kuralı bulmak demek,
milyonlarca satırın içinde,
ve her birini aynen korumak.

<!-- S18 -->
Peki oraya en başta nasıl geldi?

<!-- S19 -->
Mayıs 1959'da
ABD Savunma Bakanlığı
Pentagon'da bir toplantı düzenledi.
Bilgisayar üreticileri, devlet kurumları
ve büyük şirketler geldi,
hepsi aynı sorunla.

<!-- S20 -->
Her bilgisayarın kendi dili vardı.
Bir makine için yazılan bordro programı
başka bir makinede işe yaramıyordu.

<!-- S21 -->
Bir komite ortak bir dil tasarladı,
iş dünyası için.
En çok FLOW-MATIC'ten esinlendi,
Grace Hopper'ın Remington Rand'deki ekibinden.

<!-- S22 -->
Ve Aralık 1960'ta
özünde aynı COBOL programı
rakip üreticilerin
iki bilgisayarında çalıştı.
Bütün mesele buydu.

<!-- S23 -->
İnsanlar anlayabilsin diye tasarlanmıştı.
ADD PAYMENT TO ACCOUNT-BALANCE.
Bunun ne yaptığını muhtemelen tahmin edersin.

<!-- S24 -->
Ve parayı insanların yazdığı gibi saklıyordu:
ondalık basamaklar olarak.
Ondalık ayırıcının
saklanmasına bile gerek yok.
Nereye geleceğini alanın tanımı söyler:
son iki basamak penidir.

<!-- S25 -->
1964'te IBM, System/360'ı piyasaya sürdü.
Tasarımı, ondalık aritmetik için
komutlar içeriyordu.

<!-- S26 -->
Ve IBM o zamandan beri ana bilgisayarlarını
uyumlu kalacak şekilde tasarlıyor.
Pek çok eski program hâlâ
bugünün makinelerinde
yeniden yazılmadan çalışabiliyor.

<!-- S27 -->
Yani kimseyi taşınmaya zorlayan bir an
nadiren oldu.
Kod her yıl çalışmaya devam etti,
ve her yıl daha fazla kural biriktirdi.
Yeni ürünler, yeni vergiler, yeni düzenlemeler,
yeni istisnalar.

<!-- S28 -->
Dünyada hâlâ ne kadar COBOL'un
çalıştığını kimse saymadı.
Ama IBM'e göre dünyanın
en büyük 50 bankasından 45'i
hâlâ onun ana bilgisayarlarını kullanıyor.

<!-- S29 -->
Bazı sahipleri ise saymış.
2017'de ABD Sosyal Güvenlik İdaresi,
sistemlerinde 60 milyonu aşkın
satır COBOL bulunduğunu söyledi.

<!-- S30 -->
2025'te ABD hükümetinin denetçileri
değiştirilmeye en çok ihtiyaç duyan
11 federal sistemi listeledi.

<!-- S31 -->
Bu sistemler 23 ile
60 yaş arasındaydı
ve işletilmeleri yılda yaklaşık
750 milyon dolara mal oluyordu.

<!-- S32 -->
Yani kod eski, her yerde,
ve kimsenin yazıya dökmediği kurallarla dolu.
Herhalde asıl tehlike onu tutmakta.

<!-- S33 -->
Bakalım bir banka ayrılınca
ne oluyor.

<!-- S34 -->
2018'de TSB adlı bir İngiliz bankasının
yaklaşık beş milyon müşterisi
ve bir sorunu vardı.

<!-- S35 -->
Sistemlerini kiralıyordu,
Lloyds Banking Group'tan,
yani bir rakipten,
ve ücretler sert biçimde artacaktı.

<!-- S36 -->
Bu yüzden TSB her şeyi
yeni bir platforma taşımaya karar verdi;
platformu yeni sahibi kurmuştu:
İspanyol bankası Sabadell.

<!-- S37 -->
Nisan'da bir hafta sonu.
Pazar akşamı
yeni sistem devreye alındı.

<!-- S38 -->
Pazartesi günü yaklaşık
900 bin giriş denemesi oldu.
İnternet bankacılığı girişlerinin
ancak onda biri kadarı başarılı oldu.

<!-- S39 -->
Ödemeler başarısız oldu.
Bazı müşteriler giriş yaptı
ve başkalarının hesaplarını gördü.

<!-- S40 -->
En kötüsü yaklaşık bir hafta sürdü.
TSB olağan işleyişine
ancak Aralık'ta dönebildi.

<!-- S41 -->
Faturası yaklaşık
330 milyon sterlini buldu,
yalnızca 2018'de.
Düzenleyiciler sonradan
49 milyona yakın ceza ekledi.

<!-- S42 -->
Ve işin tuhaf yanı şu.
Müşteri verileri sağlam ulaştı.
İki resmî rapor da bunu söylüyor.

<!-- S43 -->
Çöken, verileri çevreleyen yeni platformdu.
İki veri merkezi, farklı kurulmuş.
Performans yalnızca birinde test edilmiş,
hedefler de düşürülmüş,
testler geçilemeyince.

<!-- S44 -->
Ve geri dönüş yoktu.
Veriler bir kez taşındıktan sonra,
eski sisteme dönmek,
düzenleyicinin ifadesiyle,
"esasen imkânsız"dı.

<!-- S45 -->
TSB bozuk bir sistemden kaçmıyordu.
Çalışan bir sistemden ayrılıyordu,
sahibinin kim olduğu
ve maliyeti yüzünden.
Tehlikeli olan, ayrılmanın kendisiydi.

<!-- S46 -->
Peki ayrılmak her zaman felaket mi?

<!-- S47 -->
2008'de Avustralya'nın Commonwealth Bank'i,
45 yılı aşkın süredir
kendisine hizmet eden
çekirdek sistemlerini değiştirmeye girişti.

<!-- S48 -->
Plan: yaklaşık 580
milyon Avustralya doları
ve dört yıl.

<!-- S49 -->
Beş yıl sürdü.
Basın haberlerine göre toplam
sonunda yaklaşık 1,1 milyarı buldu,
proje büyüdükçe.

<!-- S50 -->
Ama her şeyi
tek bir hafta sonunda taşımadı.
Önce, 2010'da mevduat hesapları geçti.
2011'de ticari hesaplar izledi,
2012'de de krediler.

<!-- S51 -->
Banka her adımı
izleyip kontrol edebiliyor, ondan ders çıkarabiliyordu,
bir sonrakini göze almadan önce.

<!-- S52 -->
Sonunda, bankanın dediğine göre,
gerçek zamanlı bankacılığı
günün her saati sunan
ilk büyük Avustralya bankası oldu.

<!-- S53 -->
Yani yapılabiliyor.
Ama neye mal olduğuna bak.
Beş yıl, çok daha büyük bir fatura
ve sabır.

<!-- S54 -->
Modernizasyon bir satın alma değil.
Kendi riskleri olan
bir proje.

<!-- S55 -->
Şimdi de herkesin COBOL'u
suçladığı krize gelelim.

<!-- S56 -->
Mart 2020.
Pandemi New Jersey'yi kapatırken,
yeni işsizlik ödeneği başvuruları
haftada 10 binin altından
155 binin üzerine fırladı.

<!-- S57 -->
On altı kat,
yedi günde.
İşsizlik ofisi yetişemedi.

<!-- S58 -->
Nisan başında vali
gönüllü çağrısı yaptı.
Sadece sağlık çalışanları değil,
COBOL bilen insanlar da aranıyordu.
Valiye göre eyaletin sistemleri
40 yıldan eskiydi.

<!-- S59 -->
Hikâye hızla yayıldı.
Antika kod
pandeminin yükü altında çökmüştü.

<!-- S60 -->
Ama eyalet denetçisi
konuyu sonradan incelediğinde,
gecikmelerin
bilgisayar sistemlerinden kaynaklandığına
dair hiçbir kanıt bulamadı.

<!-- S61 -->
Bundan bağımsız olarak, insanların gördüğü
hata mesajlarını inceleyen muhabirler
bunların çoğunu öndeki web sitesine bağladı;
site çok daha yeni bir dilde, Java'da yazılmıştı.
Arkadaki eski kod çalışmaya devam etti.

<!-- S62 -->
Eyalet neden COBOL programcısı aradı peki?
Çünkü Kongre kuralları değiştiriyordu.
Yeni yardımlar, yeni tutarlar,
hak kazanan yeni insanlar,
ve her değişikliğin
hızla koda girmesi gerekiyordu.

<!-- S63 -->
Sorun kodun eski olması değildi.
Sorun, onu değiştirebilen az kişi olmasıydı,
ve telefon hatlarıyla personelin
de aşırı yük altında kalmasıydı.

<!-- S64 -->
Üç vaka.
Hâlâ çalışan bir sistemden ayrılan
ve geçişi başarısız olan bir banka.
Dikkatle ayrılan
ve başaran bir banka.
Ve eski kodun suçlandığı,
ama kimsenin bunu kanıtlayamadığı bir kriz.

<!-- S65 -->
Bu, eski sistemlerin hiç arızalanmadığı anlamına gelmez.
Arızalanırlar.
Pahalılaşırlar,
onları anlayan insanlar emekli olur,
ve beklemenin de kendi bedeli vardır.

<!-- S66 -->
Ama yaş kolayca görülür,
gerçek riskler ise görülmez.
Kimsenin yazıya dökmediği kurallar.
Birkaç kişinin kafasındaki bilgi.
Ve geçiş anı.

<!-- S67 -->
Bu yüzden pek çok banka eski çekirdeği
tek seferde değiştirmez.
Onu sarmalar.
Telefonundaki uygulama yeni,
ama çok daha eski bir şeyle
konuşuyor olabilir.

<!-- S68 -->
Ve onu parça parça değiştirirler.
2004'te yazılım yazarı Martin Fowler
buna boğucu inciri örnek alarak ad verdi:
bir ağacı sararak büyüyen bir yağmur ormanı bitkisi,
ta ki kendi başına ayakta durabilene dek.

<!-- S69 -->
Eski sistem çalışmaya devam eder,
yenisi ise onun çevresinde büyür,
görevleri tek tek devralarak,
ta ki eskisine hiçbir şey bağlı kalmayana dek.

<!-- S70 -->
Bu da bizi o yarım peniye geri getiriyor.
Bir yerlerde bir program onu hâlâ atıyor olabilir,
çünkü biri öyle olması gerektiğine karar vermiş,
onlarca yıl önce.
O programı değiştirmek bunu bilmek demek,
ve buna benzer her şeyi.

<!-- S71 -->
Eski sistem her zaman
çöken taraf değildir.
Bazen çöken, onun yerine geçendir.

<!-- S72 -->
Çünkü teknolojiyi değiştirmek
riski ortadan kaldırmakla aynı şey değil.
Bazen riski yalnızca taşır,
Nisan'daki tek bir hafta sonuna.

<!-- S73 -->
O zaman sana bir sorum var.
Bir sistem kırk yıldır çalışıyorsa,
onu değiştirmenin doğru zamanı ne zaman?
Sen de hiç birini değiştirmek zorunda kaldın mı?
Yorumlarda anlat.
