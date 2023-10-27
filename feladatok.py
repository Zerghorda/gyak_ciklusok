import math
import statistics


def fel1():
    print("Írjuk ki 0-tól 150-ig a páros számokat!")
    i = 0
    while i <= 150:
        if i == 150:
            print(i, end="")
        elif i % 2 == 0:
            print(i, end=",")
        i += 1


def fel2():
    print("Számold meg 10 bekért szám esetében a 3-mal osztható számokat!")
    i = 0
    while i < 10:
        szam: int = int(input("Adjon meg egy számot!"))
        if szam % 3 == 0:
            print(f"{szam} oszthato 3-mal!")
        else:
            print(f"{szam} nem oszthato 3-mal!")
        i += 1


def fel3():
    print("Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!*")
    szam: int = int(input("Adjon meg egy 10-zel oszthato számot!"))
    while szam % 10 != 0:
        print("Nem jó!")
        szam: int = int(input("Adjon meg egy 10-zel oszthato számot!"))
    print("10-zel oszthato!")


def fel4():
    print("Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*")
    szam: int = int(input("Adjon meg egy számot ,ami 2 jegyü és páros!"))
    while szam < 10 or szam % 2 != 0 or szam < 0 or szam >= 100:
        print("NEM JÓ!")
        szam: int = int(input("Adjon meg egy számot ,ami 2 jegyü és páros!"))
    print("Jó a szám!")


def fel5():
    print("Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.*")
    szam: int = int(input("Adjon meg egy számot ,ami pozitiv jegyü és páratlan!"))
    while szam < 0 or szam % 2 != 1:
        print("NEM JÓ!")
        szam: int = int(input("Adjon meg egy számot ,ami pozitiv jegyü és páratlan!"))
    print("Jó a szám!")


def fel6():
    print("Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.*")
    szam: int = int(input("Adjon meg egy számot ,ami 3-mal oszthato vagy négyzetszám!"))
    while not (szam % 3 == 0 or ((szam ** 0.5).is_integer())):
        print("NEM JÓ!")
        szam: int = int(input("Adjon meg egy számot ,ami 3-mal oszthato vagy négyzetszám!"))
    print("Jó a szám!")


def fel7():
    print("Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!")
    szam1: int = int(input("Adjon meg egy számot!"))
    szam2: int = int(input("Adjon meg egy számot!"))
    szam3: int = int(input("Adjon meg egy számot!"))
    aOlda = pow(szam1, 2) > pow(szam3, 2) + pow(szam2, 2)
    bOldal = pow(szam2, 2) > pow(szam1, 2) + pow(szam3, 2)
    cOldal = pow(szam3, 2) > pow(szam1, 2) + pow(szam2, 2)
    while not (aOlda or bOldal or cOldal):
        print("Nem jó!")
        szam1: int = int(input("Adjon meg egy számot!"))
        szam2: int = int(input("Adjon meg egy számot!"))
        szam3: int = int(input("Adjon meg egy számot!"))
    print("Jó a szám")


def fel8():
    print("Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be.Majd írjuk ki a szót csupa nagy betűvel!*")
    szoveg: str = str(input("Adjon egy szöveget!"))
    while len(szoveg) < 3:
        print("Adjpn 3 betűnél többet!")
        szoveg: str = str(input("Adjon egy szöveget!"))
    print(szoveg.upper())


def fel9():
    print("Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!*")
    szoveg: str = str(input("Adjon egy szöveget!"))
    kicsik: bool = szoveg.islower()
    #while len(szoveg) != 4 or kicsik != False:
    while not (len(szoveg) == 4 and kicsik == True):
        print("Nem jó!")
        szoveg: str = str(input("Adjon egy szöveget!"))
        kicsik: bool = szoveg.islower()
    print("Jó a szöveg!")


def fel10():
    print("Kérj a felhasználótól bizonyos számú egész számot (0-tól eltérő értékeket), és írasd ki az átlagukat 2 tizedes jegy pontossággal (a felhasználó úgy jelzi, hogy többet nem kíván beírni, hogy azt írja: 0)!")
    szam: int = int(input("Adjon egy számot(írjon 0-át ,ha le akarja állítani)!"))
    db: int = 1
    osszeg: int = 0
    while szam != 0:
        osszeg += szam
        print(f"{osszeg / db:.2f}")
        db += 1
        szam: int = int(input("Adjon egy számot(írjon 0-át ,ha le akarja állítani)!"))
    print("Vége!")


def fel11():
    print("A fenti feladatot írd meg úgy, hogy csak pozitív számot fogadjon el (ha negatív, addig kérjen új számot, ameddig pozitív nem lesz), illetve ha 0-t ír, akkor legyen vége a bemeneteknek!")
    szam: int = int(input("Adjon egy számot(írjon 0-át ,ha le akarja állítani)!"))
    db: int = 1
    osszeg: int = 0
    while szam != 0:
        while szam < 0:
            print("Nem lehet kissebb mint 0!")
            szam: int = int(input("Adjon egy számot(írjon 0-át ,ha le akarja állítani)!"))
        osszeg += szam
        print(f"{osszeg / db:.2f}")
        db += 1
        szam: int = int(input("Adjon egy számot(írjon 0-át ,ha le akarja állítani)!"))
    print("Nyert  egy Gucci táskát!")


def fel12():
    print("Egy olimpián a részt vevők elért eredményeit kaphatjuk meg tört alakban (legyenek pl. futók, idő másodpercben;a számok is bekérés eredményei). ")
    letszam: int = int(input("Adja meg alétszámot!"))
    i = 1
    beert = 0
    osszeg = 0
    while i < letszam:
        ido: int = int(input("Adja meg a tag idejét!(0 ha lesérült ,de jelen volt)"))
        if ido < 0:
            print("HIBA: érvénytelen adat!")
            return
        if ido == 0:
            osszeg += ido
        else:
            osszeg += ido
            beert += 1
        i += 1
    print(f"")