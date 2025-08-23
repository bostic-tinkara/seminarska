# pobere podatke: seznam vseh znamenitosti, kriterijev, kontinentalnih in
# državnih kratic, lastnosti posameznih znamenitosti

import os
import time
import requests

def poberi_osnovno():
    """
    Pobere vsebino spletne strani s seznamom dediščine (po državah)
    ter jo zapiše v datoteko HTML.
    """
    odgovor = requests.get("https://whc.unesco.org/en/list/")

    if odgovor.status_code != 200:
        print("Napaka pri pobiranju osnovnih podatkov.")

    with open(os.path.join("podatki", "glavna.html"), "w", encoding="utf8") as dat:
        dat.write(odgovor.text)

def poberi_kriterije():
    """
    Pobere vsebino spletne strani s kriteriji, po katerih je ocenjena dediščina, 
    ter jo zapiše v datoteko HTML.
    """
    odgovor = requests.get("https://whc.unesco.org/en/criteria/")
    
    if odgovor.status_code != 200:
        print("Napaka pri pobiranju kriterijev.")

    with open(os.path.join("podatki", "kriteriji.html"), "w", encoding="utf8") as dat:
        dat.write(odgovor.text)

def poberi_kontinente():
    """
    Pobere vsebino spletne strani s tabelo kontinentalnih in državnih kratic
    ter jo zapiše v datoteko HTML.
    """
    odgovor = requests.get("https://en.wikipedia.org/wiki/List_of_sovereign"
                        "_states_and_dependent_territories_by_continent_(data_file)")
    
    if odgovor.status_code != 200:
        print("Napaka pri pobiranju kontinentov.")

    with open(os.path.join("podatki", "kontinenti.html"), "w", encoding="utf8") as dat:
        dat.write(odgovor.text)

def poberi_znamenitosti(znamenitosti):
    """
    Pobere vsebino spletnih strani vseh posameznih znamenitosti
    ter jo zapiše v datoteke HTML.
    """
    for znamenitost in znamenitosti:
        sifra = znamenitost[0]
        odgovor = requests.get(f"https://whc.unesco.org/en/list/{sifra}")
        
        if odgovor.status_code != 200:
            print("napaka", sifra)
            continue

        with open(
            os.path.join("podatki", f"znamenitost{sifra}.html"),
            "w",
            encoding="utf8"
        ) as dat:
            dat.write(odgovor.text)

        time.sleep(1)
