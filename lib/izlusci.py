# izlušči podatke o znamenitostih: šifra, ime, kategorija, države, leto vpisa,
# površina, izpolnjeni kriteriji, kontinenti, opisi kriterijev

import os
import re
from lib.pomozni_funkciji import opis_kriterija, z_besedo

def izlusci_osnovno():
    """
    Izlušči podatke o kategoriji, šifri in imenu znamenitosti
    ter jih vrne kot seznam naborov.
    """
    with open(os.path.join("podatki", "glavna.html"), encoding="utf8") as dat:
        besedilo = dat.read()

    vzorec = re.compile(
        r'<li class="\s*(?P<kategorija>\w+)\s*"> <a href="/en/list/(?P<sifra>\d+)" '
        r'>(?P<ime>.+?)</a>'
    )

    znamenitosti = []
    for zadetek in vzorec.finditer(besedilo):
        podatki = (zadetek["sifra"], zadetek["ime"], zadetek["kategorija"])
        # da se ne ponavljajo, ker so nekatere znamenitosti v več državah
        if podatki not in znamenitosti:
            znamenitosti.append(podatki)

    return znamenitosti

def izlusci_opise_kriterijev():
    """
    Izlušči kriterije (rimska števila) in njihove opise
    ter jih vrne kot slovar.
    """
    with open(os.path.join("podatki", "kriteriji.html"), encoding="utf8") as dat:
        besedilo = dat.read()

    vzorec = re.compile(
        r'<h3>\(([ivx]+)\)</h3>.*?'
        r'<p>(.+?)[;.]</p>',
        flags=re.DOTALL
    )

    slovar_kriterijev = {}
    for zadetek in vzorec.finditer(besedilo):
        kriterij = zadetek.group(1)
        opis = zadetek.group(2)
        slovar_kriterijev[kriterij] = opis

    return slovar_kriterijev

def izlusci_kontinente():
    """
    Izlušči kratice in imena kontinentov
    ter jih vrne kot slovar.
    """
    with open(os.path.join("podatki", "kontinenti.html"), encoding="utf8") as dat:
        tabela_kontinenti = dat.read()

    vzorec = re.compile(
        r'<li>(\w+?) - <a href="/wiki/.+?" title=".+?">(.+?)</a></li>'
    )

    slovar_kontinentov = {}
    for zadetek in vzorec.finditer(tabela_kontinenti):
        kratica = zadetek.group(1)
        kontinent = zadetek.group(2)
        slovar_kontinentov[kratica] = kontinent

    return slovar_kontinentov

def izlusci_znamenitosti(znamenitosti, slovar_kont, slovar_krit):
    """
    Izlušči nadaljnje podatke o znamenitostih (države, leto vpisa, površina in izpolnjeni
    kriteriji), s pomožnima funkcijama doda kontinent(e) in opise kriterijev
    ter jih vrne kot seznam slovarjev.
    """
    podatki = []

    # pred zanko preberemo tabelo kontinentov za poznejše dodajanje kontinentov
    with open(os.path.join("podatki", "kontinenti.html"), encoding="utf8") as dat:
            tabela_kontinenti = dat.read()

    for znamenitost in znamenitosti:
        sifra = znamenitost[0]
        ime = znamenitost[1]
        kategorija = znamenitost[2]
        drzave = []
        kontinenti = []
        leto_vpisa = ""
        povrsina = ""
        kriteriji = []

        with open(
            os.path.join("podatki", f"znamenitost{sifra}.html"), 
            encoding="utf8"
        ) as dat:
            besedilo = dat.read()

        # izluščenje držav in državnih kod
        drzava_re = re.compile(
            r'<a href="/en/statesparties/(?P<koda>.+?)" class="d-block">'
            r'<strong>(?P<drzava>.+?)</strong>'
        )

        for zadetek in drzava_re.finditer(besedilo):
            drzava = zadetek["drzava"]
            if drzava not in drzave:
                drzave.append(drzava)

            # prek državne kode najde kratico kontinenta v tabeli kontinentov
            koda = zadetek["koda"].upper()
            koda_re = re.compile(
                fr'<tr>.<td>(?P<kont>\w+?)</td>.<td>{koda}</td>',
                flags=re.DOTALL
            )

            najdba = koda_re.search(tabela_kontinenti)
            kontinent = najdba["kont"]
            if kontinent not in kontinenti:
                kontinenti.append(kontinent)

        if not drzave:
            drzave = ["ni podatka"]

        # izluščenje leta vpisa
        leto_re = re.compile(
            r'Date of Inscription:</strong>\s*(\d+?)\s*</div>'
        )

        zadetek = leto_re.search(besedilo)
        if zadetek:
            leto_vpisa = zadetek.group(1)
        else:
            print("Napaka: leto vpisa", sifra)

        # izluščenje površine
        povrsina_re = re.compile(r'Property\s*:</strong>\s*([0-9,\.]+)\s*ha')

        zadetek = povrsina_re.search(besedilo)
        if zadetek:
            povrsina = zadetek.group(1).replace(",", "")     # če je za tisočicami vejica
        else:
            povrsina = "ni podatka"

        # izluščenje kriterijev
        kriterij_re = re.compile(r'<a href="/en/criteria/">(\([ivx\(\)]+?\))</a>')

        zadetek = kriterij_re.search(besedilo)
        if zadetek:
            niz = zadetek.group(1)
            kriteriji = niz.strip('()').split(')(')       # ločimo števila brez oklepajev
        else:
            print("Napaka: kriteriji", sifra)

        podatki.append(
            {
                "id": sifra,
                "znamenitost": ime,
                "kategorija": kategorija,
                "drzave": drzave,
                "kontinenti": z_besedo(kontinenti, slovar_kont),
                "leto vpisa": leto_vpisa,
                "povrsina": povrsina,
                "kriteriji": opis_kriterija(kriteriji, slovar_krit)
            }
        )

    return podatki
