#!/urs/bin/python3
# -*- coding:utf-8 -*-
"""2013.majus.13 Informatikaerettsegi megoldas Python programozasi nyelven. """
"""1.feladat szavazatokat beimportalni. """
"""beiimportalom a szavazatokat egy szotarba ami a kovetkezo keppen nezne ki
szavazat={
hanyadik{
"valasztokerulet":8
"szavazat":149
"Vezetek nev":Zeller
"Uto nev":Zelma
"Nev":Zeller Zelma
"Part":ZEP
}
hanyadik{
"valasztokerulet":6
"szavazat":63
"Vezetek nev":Zsoldos
"Uto nev":Zolt
"Nev":Zsoldos Zolt
"Part":-
}
}

"""

szavazat = {}
n = 0
with open("szavazatok.txt","rt+",encoding="utf-8") as f:
    for s in f:
        n+=1
        sor = s.replace("\n","").split(" ")
        szavazat[n] = {}
        szavazat[n]["valasztokerulet"] = int(sor[0])
        szavazat[n]["szavazat"] = int(sor[1])
        szavazat[n]["Vezetek nev"] = str(sor[2])
        szavazat[n]["Uto nev"] = str(sor[3])
        szavazat[n]["nev"] = [str(sor[2]), str(sor[3])]
        
        if str(sor[4]) == "-":
            szavazat[n]["Part"] = 'fuggetlen'
        else:
            szavazat[n]["Part"] = str(sor[4])
        
        
#print(szavazat)
"""
Javitast segiti
with open("sem.txt", "wt", encoding="utf-8") as g:
    for k, v in szavazat.items():
        g.write("{0}:{1} \n".format(k,v))
"""        
print("2. feladat")
"""Ki kell irni hogy hany kepviselo indult a valasztason. """
print("A helyhatosagi valasztason {} kepviselojelolt indult.".format(len(szavazat)))

print("3. feladat")
"""Be kell kerni a felhasznalotol egy vezetek nevet es egy uto nevet es meg kell nezni hogy benne van-e a szotarban. """
vezeteknev = str(input("Kerem adja meg a keresendo vezetek nevet.: "))
utonev = str(input("Kerem adja meg a keresendo uto nevet/vezetek nevet.:  "))
szerepel = False
for a in szavazat.values():
    if a["Vezetek nev"] == vezeteknev and a['Uto nev'] == utonev:
        print("{0} kepviselojelolt {1} szavazatot kapott.".format(" ".join(a['nev']), a["szavazat"]))
        szerepel = True

if szerepel == False:
    print("Ilyen nevu kepviselojelolt nem szerepel a nyilvantartasban!")

print("4. feladat")
"""Meg kell hatarozni hogy hanyan adtak le a szavazataikat vagyis hogy mennyi volt a reszveteli arany. """
szavazatleadas = 0
osszes = 12345
for a in szavazat.values():
    szavazatleadas += int(a["szavazat"])    
szazalek = ((szavazatleadas/osszes)*100)
print("A valasztason {0} allampolgar , a jogosultak {1}%-a vett reszt.".format(szavazatleadas, round(szazalek, 2)))

print("5. feladat")
"""Partokra leadott szavcazatok aranyat ki kell szamolni es ki kell irni a kepernyore."""
GYEP = 0
HEP = 0
TISZ = 0
ZEP = 0
Fuggetlen = 0

for a in szavazat.values():
    if a["Part"] == "GYEP":
        GYEP+=a["szavazat"]
    elif a["Part"] == "HEP":
        HEP+=a["szavazat"]
    elif a["Part"] == "TISZ":
        TISZ+=a["szavazat"]
    elif a["Part"] == "ZEP":
        ZEP+=a["szavazat"]
    elif a["Part"] == "fuggetlen":
        Fuggetlen+=a["szavazat"]

print("Gyumolcsevok Partja= {}%".format(round(((GYEP/szavazatleadas)*100), 2)))
print("Husevok Partja= {}%".format(round(((HEP/szavazatleadas)*100), 2)))
print("Tejivok Partja= {}%".format(round(((TISZ/szavazatleadas)*100), 2)))
print("Zoldsegevok Partja= {}%".format(round(((ZEP/szavazatleadas)*100), 2)))
print("Fuggetlenek Partja= {}%".format(round(((Fuggetlen/szavazatleadas)*100), 2)))

print("6. feladat")
"""Legtobb szavazato gyujto kepviselo nevet es partjat ki kell iratni a kepernyore. """
szavaz = []
for a in szavazat.values():
    szavaz.append(a["szavazat"])

for d in szavazat.values():
    if d["szavazat"] == max(szavaz):
        print("Indulo neve: {0}, ot tamogato part roviditese: {1}".format(" ".join(d["nev"]), d["Part"]))


print("7. feladat")
"""Egye valasztokeruletekben kik lettek a nyertesek """
egyes = []
kettes = []
harmas = []
negyes = []
otos = []
hatos = []
hetes = []
nyolcas = []

for a in szavazat.values():
    if a['valasztokerulet'] == 1:
        egyes.append(a["szavazat"])
    elif a['valasztokerulet'] == 2:
        kettes.append(a["szavazat"])
    elif a['valasztokerulet'] == 3:
        harmas.append(a["szavazat"])
    elif a['valasztokerulet'] == 4:
        negyes.append(a["szavazat"])
    elif a['valasztokerulet'] == 5:
        otos.append(a["szavazat"])
    elif a['valasztokerulet'] == 6:
        hatos.append(a["szavazat"])
    elif a['valasztokerulet'] == 7:
        hetes.append(a["szavazat"])
    elif a['valasztokerulet'] == 8:
        nyolcas.append(a["szavazat"])
kepviselok = {}
listam = [egyes, kettes, harmas, negyes, otos, hatos, hetes, nyolcas]
g = [1,2,3,4,5,6,7,8]

for n in szavazat.values():
        for gf in g:
            if max(listam[int(gf-1)]) == int(n["szavazat"]):
                kepviselok[gf] = {}
                kepviselok[gf]["nev"] = n["nev"]
                kepviselok[gf]["part"] = n["Part"]
        
#print(kepviselok)
with open("kepviselok.txt","wt",encoding="utf-8") as d:
    for n in sorted(kepviselok.keys()):
        d.write("{0} {1} {2} \n".format(n, " ".join(kepviselok[n]['nev']), kepviselok[n]['part']))