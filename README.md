# Analiza podatkov o Unescovi svetovni dediščini
Ta seminarska naloga analizira podatke o Unescovi svetovni dediščini. Program (python) zajame podatke s spletnih strani Unesca in Wikipedie, jih shrani v datoteke HTML, obdela in na koncu izbrane podatke shrani v datoteko CSV. Analiza teh podatkov s pandas je nato predstavljena z Jupyter Notebook.

Med zajetimi podatki so šifre in imena Unescovih znamenitosti, njihova kategorija, lokacija po državah in kontinentih, leto vpisa, površina in Unescovi kriteriji, ki jih izpolnjujejo. Analiza s pandas pa jih (statistično) obdela in grafično predstavi.

## Struktura repozitorija
V mapi `lib/` so .py-datoteke, ki vsebujejo funkcije za pobiranje, izluščenje in shranitev podatkov ter pomožni funkciji.

V mapi `podatki/` so datoteke, ki jih ustvari program: datoteke HTML (ne vse; med zagonom programa pa se ustvarijo vse) in datoteka `podatki.csv`.

Datoteka `main.py` požene celoten program.

Datoteka `analiza.ipynb` vsebuje analizo podatkov s pandas.

## Navodila za zagon programa
Za zagon programa potrebuje uporabnik naslednje knjižnice:
- os: za dostopanje datotek,
- time: za odmore med zajemom podatkov s spletnih strani,
- requests: za zajem podatkov s spletnih strani,
- re: za iskanje z regularnimi izrazi,
- csv: za pisanje datotek CSV,
- pandas: za analizo podatkov,
- ast: za pravilno interpretacijo podatkovnih struktur (kot python).

Uporabnik lahko program klonira v ukazni vrstici z ukazom `git clone https://github.com/bostic-tinkara/seminarska.git`.

Celoten program požene datoteka `main.py` (v ukazni vrstici z ukazom `python main.py`), in sicer se mora pognati iz korenskega direktorija repozitorija: `seminarska/` (kjer se nahaja `main.py`), saj program uporablja relativne poti datotek. Program se izvaja dlje časa - okoli pol ure, saj zajem podatkov traja precej dolgo.

V datoteki `analiza.ipynb` so že predstavljeni rezultati analize s pandas, sicer pa se celice ponovno zažene z uporabo primernega python jedra (s knjižnicama pandas in ast) in ukaza `Run All`.
