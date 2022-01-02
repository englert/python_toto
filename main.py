''' toto.txt http://www.infojegyzet.hu/erettsegi/informatika-ismeretek/kozep-prog-2020okt/
Év;Hét;Forduló;T13p1;Ny13p1;Eredmények
2020;18;1;0;0;2X22211X1X11X1
• Év : A fogadási forduló éve (1998-2020)
• Hét : A fogadási forduló hete (1-53)
• Forduló : Forduló sorszáma (1 vagy 2)
• T13p1 : 13+1 találatos (telitalálatos) szelvények darabszáma
• Ny13p1 : Egy darab 13+1 találatos szelvény után fizetett nyeremény [Ft]
• Eredmények : A forduló 14 mérkőzésének kimenetelei
'''

class Toto:
    def __init__(self, sor):
        s = sor.strip().split(';');
        self.ev         = int( s[0] );
        self.het        = int( s[1] );
        self.fordulo    = int( s[2] );
        self.t13p1      = int( s[3] );
        self.ny13p1     = int( s[4] );
        self.eredmenyek = s[5];

def dontetlen_nelkuli(txt):
    return not ('X' in txt)

# 2. Olvassa be a toto.txt állományban lévő adatokat

with open("toto.txt") as sr:
    elsosor = sr.readline();
    lista = [ Toto(sor) for sor in sr ]
        
# 3. Határozza meg és írja ki a képernyőre, hány forduló adatai találhatók a forrásállományban!
# 3. feladat: Fordulók száma: {}

print(f"3. feladat: Fordulók száma: {len(lista)}");

# 4. Számolja meg és írja ki a képernyőre a telitalálatos szelvények számát!

telitalalat = sum( [ sor.t13p1 for sor in lista ] )
print(f"4. feladat: Telitalálatos szelvények száma: {telitalalat}");

# 5. Számítsa ki, mekkora volt a „telitalálatos” ( T13p1>0 vagy Ny13p1>0 ) fordulók során a telitalálatos szelvényekre kifizetett nyereményösszegek átlaga! Egy fordulóban a nyereményösszeget a T13p1 * Ny13p1 kifejezéssel számolja! Ügyeljen rá, hogy a telitalálatos fordulók során a telitalálatos szelvényekre kifizetett nyereményösszegek összege nem fér el egy 32  bites egész változóban. Az átlagot egész számra kerekítve jelenítse meg!
  
darab_szorozva_nyeremeny = [ sor.ny13p1 * sor.t13p1 for sor in lista if sor.ny13p1 > 0 ]
print(f"5. feladat: Átlag: {( sum(darab_szorozva_nyeremeny) / len(lista) ):.0f} Ft");
    
# 6. Írja ki annak a két fordulónak az adatait a minta szerint, ahol a legnagyobb és a legkisebb volt az egy telitalálatos szelvény után fizetett nyeremény! Feltételezheti, hogy nem alakult ki holtverseny a két szélsőértéknél és nem fordult olyan elő, hogy a telitalálatos szelvény után ne fizettek volna nyereményt!
      
nyeremeny = sorted( [ sor for sor in lista if  sor.ny13p1 > 0 ], key=lambda x: x.ny13p1 )
  
maxi = nyeremeny[-1]
mini = nyeremeny[0]

print(f"6. feladat:");
print(f"        Legnagyobb:");
print(f"        Év: {maxi.ev}");
print(f"        Hét: {maxi.het}.");
print(f"        Forduló: {maxi.fordulo}.");
print(f"        Telitalálat: {maxi.t13p1} db");
print(f"        Nyeremény: {maxi.ny13p1} Ft");
print(f"        Eredmények: {maxi.eredmenyek}");
print();
print(f"        Legkisebb:");
print(f"        Év: {mini.ev}");
print(f"        Hét: {mini.het}.");
print(f"        Forduló: {mini.fordulo}.");
print(f"        Telitalálat: {mini.t13p1} db");
print(f"        Nyeremény: {mini.ny13p1} Ft");
print(f"        Eredmények: {mini.eredmenyek}");

# 7. Forráskódjába tegye elérhetővé a java.txt vagy a csharp.txt állományból az EredmenyElemzo osztályt definiáló kódrészletet!         Az osztály felhasználható arra, hogy megállapítsa egy forduló eredményeiről (pl.: „2X22211X1X11X1” ), hogy egyetlen érkőzés sem végződött döntetlen eredménnyel ( NemvoltDontetlenMerkozes ).    

dontetlen_nelkul = [ dontetlen_nelkuli( sor.eredmenyek) for sor in lista]
if True in dontetlen_nelkul:
    print( "8. feladat: Volt döntetlen nélküli forduló!" );
else:
    print( "8. feladat: Nem volt döntetlen nélküli forduló!" );
