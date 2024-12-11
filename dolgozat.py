"""
Olvassunk be billentyűzetről egész számokat, és tároljuk őket egy listában! A bevitel végét a 0 jelezze.  Majd oldjuk meg a következő feladatokat!Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e -10 és -15 közé eső szám a beírtak között?
2. Írjuk ki az utolsó 2-vel és 5-tel osztható szám indexét!
3. Hány darab 20-nál nagyobb számot írtak be?
4. Melyik és hányadik volt a legkisebb beírt pozitív egész szám?
5. Mennyi a negatív számok számok átlaga?
"""

szamlista = []


def elsofeladat():
    for szam in szamlista:
        if -15 <= szam <= -10:
            return szam
        else:
            return None


def masodikfeladat():
    for i in range(len(szamlista) - 1, -1, -1):
        if szamlista[i] % 2 == 0 and szamlista[i] % 5 == 0:
            return i
        else:
            return None


def harmadikfeladat():
    husznalnagyobb = 0
    for szam in szamlista:
        if szam > 20:
            husznalnagyobb += 1
    return husznalnagyobb


def negyedikfeladat():
    index_ = None
    legkisebb_pozitiv_szam = None
    for i, szam in enumerate(szamlista):
        if szam > 0:
            index_ = i
            legkisebb_pozitiv_szam = szam
    return index_, legkisebb_pozitiv_szam



def otodikfeladat():
    negativak = None
    negativosszeg = None
    for szam in szamlista:
        if szam < 0:
            negativak = negativak + 1
            negativosszeg = negativosszeg + szam
    atlag = negativosszeg / negativak
    return atlag



def feladatok():
    print("Az általad megadott számok: ", szamlista)
    print("1. ", elsofeladat())
    print("2. ", masodikfeladat())
    print("3. ", harmadikfeladat())
    print("4. ", negyedikfeladat())
    print("5. ", otodikfeladat())


def bevitel():
    print("Adj meg számokat, ha elég számot megadtál írj egy nullát! (0)")
    hozzaadas = int(input("Szám: "))
    if hozzaadas == 0:
        feladatok()
    else:
        szamlista.append(hozzaadas)
        bevitel()


bevitel()
